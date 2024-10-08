﻿import time
import traceback
from datetime import datetime

from sqlalchemy import desc
from sqlalchemy import func
from sqlalchemy import extract

from sqlalchemy.exc import SQLAlchemyError

from flask import request, jsonify
from flask import render_template

from sm_app import sm_app, sm_db
from sm_app.user import User
from sm_app.result import Result
from sm_app.friends import Friends
from sm_app.scores import Scores
from sm_app.tasks import Tasks

from sm_app.emailer import send_selfemail
from sm_app.emailer import send_forget_email
from sm_app.emailer import send_registration_email

from sm_app.userinfo import get_user_info

@sm_app.route('/')
def hello():
    # send_forget_email(name, surname, password, lang, recipient)
    # send_forget_email('Sergei', 'Voloktin', 'psswds', 'ru', 'yuri.volokitin@gmail.com')
    return 'Hello User'

@sm_app.route('/register')
def registration_html():
    # send_registration_email(name, surname, lang, recipient)
    send_registration_email('Yura', 'Volokitin', 'ru', 'yuri.volokitin@gmail.com')
    return 'Registration email were Email Sent'

@sm_app.route('/showreg')
def show_registration_html():
    arguments = {
        'subject': 'Welcome to SuperMathSuperMath.xyz',
        'name': 'Yura',
        'surname': 'Volokitin',
        'title': 'Welcome to Arithmetical world',
        'description': 'SuperMath is a collection of free math activities to practice straightforward arithmetic problems that adapt as they learn.',
        'text': 'Kids can keep results, trade points, select avatars and track the progress using fluency reports and dashboards.',
    }
    return render_template('index.html', **arguments)

@sm_app.route('/api/email', methods = ['POST'])
def selfemail():
    # send_email({'name': name, 'email': email, 'lang': props.lang, 'message': message});
    name = request.json.get('name')
    email = request.json.get('email')
    lang = request.json.get('lang')
    message = request.json.get('message')
    if name is None or email is None or lang is None or message is None:
        result = jsonify({'error': 'Api Email: missing arguments'})
    else:
        send_selfemail(name, email, lang, message)
        result = jsonify({'email': email})

    return (result, 200)

@sm_app.route('/api/scores', methods = ['POST'])
def getscores():
    amount = request.json.get('amount')
    if amount is None:
        result = jsonify({'error': 'Topusers Call: missing arguments'})
    else:
        # select scores.SCORE, users.ID, users.NAME, users.SURNAME, users.FAILED, users.PASSED from users, scores where users.ID=scores.USERID order by scores.SCORE DESC;
        users = sm_db.session.query(User, Scores).filter(User.ID == Scores.USERID).order_by(desc(Scores.SCORE)).limit(int(amount)).all()
        data = []
        for user in users:
            data.append({'id': user.User.ID,
                    'name': user.User.NAME,
                    'surname': user.User.SURNAME,
                    'avatar': user.User.AVATAR,
                    'passed': user.User.PASSED,
                    'failed': user.User.FAILED,
                    'level': user.User.LEVEL,
                    'score': user.Scores.SCORE,
            })

        result = jsonify(data)

    return (result, 200)

@sm_app.route('/api/poopthrow', methods = ['POST'])
def poopthrow():
    user_id = request.json.get('user_id')
    pswdhash = request.json.get('pswdhash')
    target_id = request.json.get('target_id')

    if user_id is None:
        result = jsonify({'error': 'PoopThrow Call: missing arguments, no user id received'})
    elif pswdhash is None:
        result = jsonify({'error': 'PoopThrow Call: no authorization method provided'})
    elif target_id is None:
        result = jsonify({'error': 'PoopThrow Call: no target provided'})
    else:
        user = None
        try:
            user = User.query.filter_by(ID=user_id, PSWDHASH=pswdhash).first()
            target = User.query.filter_by(ID=target_id).first()
        except Exception as e:
            print(traceback.format_exc())
            result = jsonify({'error': 'PoopThrow Call: exception raised during sql query ' + str(e)})
        else:
            if user is None:
                result = jsonify({'error': 'PoopThrow Call: no registered user with user ID: ' + str(user_id)})
            elif target is None:
                result = jsonify({'error': 'PoopThrow Call: no registered target user with user ID: ' + str(target_id)})
            else:
                if user.PSWDHASH != pswdhash:
                    result = jsonify({'error': 'PoopThrow Call: incorrect password used \'' + str(email) + '\' account'})
                else:
                    if int(user.PASSED) < 20:
                        result = jsonify({'error': 'PoopThrow Call: user does not have enough points to throw poops'})
                    else:
                        new_passed = int(user.PASSED) - 20
                        user.PASSED = new_passed

                        new_failed = int(target.FAILED) + 1
                        target.FAILED = new_failed
                        sm_db.session.commit()

                        score = Scores.query.filter_by(USERID=user_id).first()
                        current_score = new_passed - (int(user.FAILED) *30);
                        if score is None:
                            score = Scores(USERID=user_id, SCORE=current_score)
                            sm_db.session.add(score)
                        else:
                            score.SCORE = current_score;

                        score = Scores.query.filter_by(USERID=target_id).first()
                        current_score = int(target.PASSED) - (new_failed * 30);
                        if score is None:
                            score = Scores(USERID=user_id, SCORE=current_score)
                            sm_db.session.add(score)
                        else:
                            score.SCORE = current_score;

                        sm_db.session.commit()
                        result = jsonify({
                            'operation': 'poopthrow',
                            'id': user.ID,
                            'passed': new_passed,
                        })

    return (result, 200)

@sm_app.route('/api/results', methods = ['POST'])
def results():
    user_id = request.json.get('user_id')
    pswdhash = request.json.get('pswdhash')
    month = request.json.get('month')

    if user_id is None:
        result = jsonify({'error': 'Results Call: missing arguments, no user id received'})
    elif pswdhash is None:
        result = jsonify({'error': 'Results Call: no authorization method provided'})
    elif month is None:
        result = jsonify({'error': 'Results Call: no query information'})
    else:
        result = None
        try:
            results = Result.query.filter(extract('month', Result.EXECUTION_DATE)==month).filter_by(USERID=user_id).all()
        except Exception as e:
            print(traceback.format_exc())
            result = jsonify({'error': 'Results Call: exception raised during sql query ' + str(e)})
        else:
            if results is None:
                result = jsonify({'error': 'Results Call: no registered user with user ID: ' + str(user_id)})
            else:
                data = []
                for res in results:
                    data.append(res.get_result())

                result = jsonify(data)

    return (result, 200)

@sm_app.route('/api/refresh', methods = ['POST'])
def refresh():
    user_id = request.json.get('user_id')
    pswdhash = request.json.get('pswdhash')
    refresh = request.json.get('refresh')
    if user_id is None:
        result = jsonify({'error': 'Refresh Call: missing arguments, no user id received'})
    elif pswdhash is None:
        result = jsonify({'error': 'Refresh Call: no authorization method provided'})
    elif refresh is None:
        result = jsonify({'error': 'Refresh Call: no refresh option'})
    else:
        user = None
        try:
            user = User.query.filter_by(ID=user_id, PSWDHASH=pswdhash).first()
        except Exception as e:
            print(traceback.format_exc())
            result = jsonify({'error': 'Refresh Call: exception raised during sql query ' + str(e)})
        else:
            if user is None:
                result = jsonify({'error': 'Refresh Call: no registered user with user ID: ' + str(user_id)})
            else:
                if refresh is True:
                    result = get_user_info(user, True)
                else:
                    result = get_user_info(user, False)

    return (result, 200)

@sm_app.route('/api/login', methods = ['POST'])
def login():
    email = request.json.get('email')
    pswdhash = request.json.get('pswdhash')
    if email is None or pswdhash is None:
        result = jsonify({'error': 'Login Call: missing arguments, no email or password provided'})
    else:
        user = None
        try:
            user = User.query.filter_by(EMAIL=email, PSWDHASH=pswdhash).first()

        except SQLAlchemyError as error:
            result = jsonify({'error': 'Login Call: sql error ' + str(error)})

        except Exception as e:
            print(traceback.format_exc())
            result = jsonify({'error': 'Login Call: exception raised ' + str(e)})

        else:
            if user is None:
                result = jsonify({'error': 'Login Call: no user found with \'' + str(email) + '\' email address'})
            else:
                if user.PSWDHASH != pswdhash:
                    result = jsonify({'error': 'Login Call: incorrect password used \'' + str(email) + '\' account'})
                else:
                    result = get_user_info(user)

    return (result, 200)

@sm_app.route('/api/getfailtask', methods = ['POST'])
def get_fail_task():
    lang = request.json.get('lang')
    level = request.json.get('level')
    user_id = request.json.get('user_id')
    task_id = request.json.get('task_id')
    if lang is None:
        result = jsonify({'error': 'Get Task: missing arguments, no language'})
    elif level is None:
        result = jsonify({'error': 'Get Task: missing arguments, no level'})
    elif user_id is None:
        result = jsonify({'error': 'Get Task: missing arguments, no user'})
    elif task_id is None:
        result = jsonify({'error': 'Get Task: missing arguments, no fail task id'})
    else:
        try:
            # SELECT * FROM tasks ORDER BY RAND() LIMIT 1;
            # task = Tasks.query.order_by(func.random()).first()
            task = Tasks.query.filter_by(ID=task_id, LEVEL=level).first()

        except Exception as e:
            print(traceback.format_exc())
            result = jsonify({'error': 'Get Task: exception raised' + str(e)})
        else:
            if task is None:
                result = jsonify({'error': 'Get Task: no more tasks found in database per ' + level})
            else:
                if lang == 'ru' and len(task.RU)>0:
                    language = lang
                    description = task.RU
                elif lang == 'nl' and len(task.NL)>0:
                    language = lang
                    description = task.NL
                elif lang == 'de' and len(task.DE)>0:
                    language = lang
                    description = task.DE
                elif lang == 'fr' and len(task.FR)>0:
                    language = lang
                    description = task.FR
                elif lang == 'ES' and len(task.ES)>0:
                    language = lang
                    description = task.ES
                elif lang == 'it' and len(task.IT)>0:
                    language = lang
                    description = task.IT
                else:
                    language = 'en'
                    description = task.EN

                result = jsonify({
                    'task_id': task_id,
                    'lang': language,
                    'description': description,
                    'result': task.RESULT,
                    'image': task.IMAGE,})

    return (result, 200)

@sm_app.route('/api/getnexttask', methods = ['POST'])
def get_next_task():
    lang = request.json.get('lang')
    level = request.json.get('level')
    user_id = request.json.get('user_id')
    current = request.json.get('task_id')

    if lang is None:
        result = jsonify({'error': 'Get Task: missing arguments, no language'})
    elif level is None:
        result = jsonify({'error': 'Get Task: missing arguments, no level'})
    elif user_id is None:
        result = jsonify({'error': 'Get Task: missing arguments, no user'})
    elif current is None:
        result = jsonify({'error': 'Get Task: missing arguments, no current task count'})
    else:
        task_id = int(current) + 1;
        task = None
        try:
            # SELECT * FROM tasks ORDER BY RAND() LIMIT 1;
            # task = Tasks.query.order_by(func.random()).first()
            task = Tasks.query.filter_by(ID=task_id, LEVEL=level).first()

            if task is None:
                task_id = 1
                task = Tasks.query.filter_by(ID=task_id, LEVEL=level).first()

        except Exception as e:
            print(traceback.format_exc())
            result = jsonify({'error': 'Get Task: exception raised' + str(e)})

        else:
            if task is None:
                result = jsonify({'error': 'Get Task: no more tasks found in database per ' + level})

            else:
                if lang == 'ru' and len(task.RU)>0:
                    language = lang
                    description = task.RU
                elif lang == 'nl' and len(task.NL)>0:
                    language = lang
                    description = task.NL
                elif lang == 'de' and len(task.DE)>0:
                    language = lang
                    description = task.DE
                elif lang == 'fr' and len(task.FR)>0:
                    language = lang
                    description = task.FR
                elif lang == 'ES' and len(task.ES)>0:
                    language = lang
                    description = task.ES
                elif lang == 'it' and len(task.IT)>0:
                    language = lang
                    description = task.IT
                else:
                    language = 'en'
                    description = task.EN

                result = jsonify({
                    'task_id': task_id,
                    'lang': language,
                    'description': description,
                    'result': task.RESULT,
                    'image': task.IMAGE,})

    return (result, 200)

@sm_app.route('/api/counter', methods = ['POST'])
def update_counter():
    user_id = request.json.get('user_id')
    pswdhash = request.json.get('pswdhash')
    belt = request.json.get('belt')
    passed = request.json.get('passed')
    failed = request.json.get('failed')
    cards = request.json.get('cards')

    if user_id is None:
        result = jsonify({'error': 'Counter Call: missing arguments, no user id received'})
    elif pswdhash is None:
        result = jsonify({'error': 'Counter Call: no authorization method provided'})
    elif passed is None or failed is None or belt is None or cards is None:
        result = jsonify({'error': 'Counter Call: missing arguments, no user info and results'})
    else:
        user = None
        try:
            user = User.query.filter_by(ID=user_id, PSWDHASH=pswdhash).first()
        except Exception as e:
            print(traceback.format_exc())
            result = jsonify({'error': 'Counter Call: exception raised during sql query ' + str(e)})
        else:
            if user is None:
                result = jsonify({'error': 'Counter Call: no registered user with user ID: ' + str(user_id)})
            else:
                pass_dec = int(passed, 2)
                fail_dec = int(failed, 2)
                card_dec = int(cards, 2)

                pass_value =  int(pass_dec / user_id)
                fail_value =  int(fail_dec / user_id)
                card_value =  int(card_dec / user_id)

                user.PASSED = pass_value
                user.FAILED = fail_value
                user.CARDS = card_value
                user.BELT = belt
                sm_db.session.commit()

                score = Scores.query.filter_by(USERID=user_id).first()
                current_score = pass_value - fail_value*30;
                if score is None:
                    score = Scores(USERID=user_id, SCORE=current_score)
                    sm_db.session.add(score)
                else:
                    score.SCORE = current_score;

                sm_db.session.commit()
                result = jsonify({
                    'operation': 'exchanged',
                    'id': user.ID,
                    'belt': user.BELT,
                    'passed': user.PASSED,
                    'failed': user.FAILED,
                    'cards': user.CARDS
                })

    return (result, 200)

@sm_app.route('/api/update', methods = ['POST'])
def update_user():
    user_id = request.json.get('user_id')
    operation = request.json.get('operation')
    pswdhash = request.json.get('pswdhash')

    if user_id is None:
        result = jsonify({'error': 'Missing arguments, no user id received'})
    elif operation is None:
        result = jsonify({'error': 'Missing arguments, no operation received'})
    elif pswdhash is None:
        result = jsonify({'error': 'No authorization method provided'})
    else:
        user = None
        try:
            user = User.query.filter_by(ID=user_id, PSWDHASH=pswdhash).first()
        except Exception as e:
            print(traceback.format_exc())
            result = jsonify({'error': 'Exception raised during sql query ' + str(e)})
        else:
            if user is None:
                result = jsonify({'error': 'No registered user with user ID: ' + str(user_id)})
            else:
                if operation == 'results':
                    passed = request.json.get('passed')
                    failed = request.json.get('failed')
                    game_uid = request.json.get('game_uid')
                    # needed for separate results table
                    duration = request.json.get('duration')
                    percent = request.json.get('percent')
                    rate = request.json.get('rate')
                    belt = request.json.get('belt')
                    task = request.json.get('task')

                    if passed is None or failed is None:
                        result = jsonify({'error': 'Received wrong passed/failed counters, passed: '
                                        + str(passed) + '/failed: ' + str(failed)})
                    elif game_uid is None or duration is None or percent is None or rate is None or belt is None or task is None:
                        result = jsonify({'error': 'Received wrong game_uid/duration/percent/rate/belt/task parameters'})

                    else:
                        passed_counter = int(user.PASSED)
                        failed_counter = int(user.FAILED)
                        user_level_str = str(user.LEVEL)
                        game_uid_str = str(game_uid)

                        if (int(failed) == 0) and (int(passed) > 0):
                            if 'task_' in game_uid_str:
                                passed_counter = passed_counter + int(passed)

                            elif game_uid_str == 'blackT':
                                passed_counter = passed_counter + int(passed)
                                cards = int(user.CARDS) + 1
                                user.LEVEL = 'black'
                                user.SOLVED = ''
                                user.CARDS = cards

                            elif game_uid_str == 'brownT':
                                passed_counter = passed_counter + int(passed)
                                if user_level_str not in ['black', 'brown']:
                                    cards = int(user.CARDS) + 1
                                    user.LEVEL = 'brown'
                                    user.SOLVED = ''
                                    user.CARDS = cards

                            elif game_uid_str == 'navyT':
                                passed_counter = passed_counter + int(passed)
                                if user_level_str not in ['black', 'brown', 'navy']:
                                    cards = int(user.CARDS) + 1
                                    user.LEVEL = 'navy'
                                    user.CARDS = cards
                                    # updating solved programms list
                                    user_solved = user.SOLVED.split(',')
                                    new_solved = ''
                                    for sol in user_solved:
                                        if 'brown' in sol:
                                            new_solved = new_solved + sol + ','
                                    user.SOLVED = new_solved

                            elif game_uid_str == 'greenT':
                                passed_counter = passed_counter + int(passed)
                                if user_level_str not in ['black', 'brown', 'navy', 'green']:
                                    cards = int(user.CARDS) + 1
                                    user.LEVEL = 'green'
                                    user.CARDS = cards
                                    # updating solved programms list
                                    user_solved = user.SOLVED.split(',')
                                    new_solved = ''
                                    for sol in user_solved:
                                        if (('brown' in sol) or ('navy' in sol)):
                                            new_solved = new_solved + sol + ','
                                    user.SOLVED = new_solved

                            elif game_uid_str == 'orangeT':
                                passed_counter = passed_counter + int(passed)
                                if user_level_str not in ['black', 'brown', 'navy', 'green', 'orange']:
                                    cards = int(user.CARDS) + 1
                                    user.LEVEL = 'orange'
                                    user.CARDS = cards
                                    # updating solved programms list
                                    user_solved = user.SOLVED.split(',')
                                    new_solved = ''
                                    for sol in user_solved:
                                        if (('white' not in sol) and ('orange' not in sol) and (len(sol)>0)):
                                            new_solved = new_solved + sol + ','
                                    user.SOLVED = new_solved

                            elif game_uid_str == 'whiteT':
                                passed_counter = passed_counter + int(passed)
                                if user_level_str not in ['black', 'brown', 'navy', 'green', 'orange', 'white']:
                                    cards = int(user.CARDS) + 1
                                    user.LEVEL = 'white'
                                    user.CARDS = cards
                                    # updating solved programms list
                                    user_solved = user.SOLVED.split(',')
                                    new_solved = ''
                                    for sol in user_solved:
                                        if 'white' not in sol:
                                            new_solved = new_solved + sol + ','
                                    user.SOLVED = new_solved

                            elif game_uid_str not in str(user.SOLVED):
                                if 'white' in game_uid_str:
                                    if user_level_str not in ['black', 'brown', 'navy', 'green', 'orange', 'white']:
                                        passed_counter = passed_counter + int(passed)
                                        cards = int(user.CARDS) + 1
                                        user.SOLVED += game_uid + ','
                                        user.CARDS = cards
                                elif 'orange' in game_uid_str:
                                    if user_level_str not in ['black', 'brown', 'navy', 'green', 'orange']:
                                        passed_counter = passed_counter + int(passed)
                                        cards = int(user.CARDS) + 1
                                        user.SOLVED += game_uid + ','
                                        user.CARDS = cards
                                elif 'green' in game_uid_str:
                                    if user_level_str not in ['black', 'brown', 'navy', 'green']:
                                        passed_counter = passed_counter + int(passed)
                                        cards = int(user.CARDS) + 1
                                        user.SOLVED += game_uid + ','
                                        user.CARDS = cards
                                elif 'navy' in game_uid_str:
                                    if user_level_str not in ['black', 'brown', 'navy']:
                                        passed_counter = passed_counter + int(passed)
                                        cards = int(user.CARDS) + 1
                                        user.SOLVED += game_uid + ','
                                        user.CARDS = cards
                                elif 'brown' in game_uid_str:
                                    if user_level_str not in ['black', 'brown']:
                                        passed_counter = passed_counter + int(passed)
                                        cards = int(user.CARDS) + 1
                                        user.SOLVED += game_uid + ','
                                        user.CARDS = cards
                                elif 'black' in game_uid_str:
                                    passed_counter = passed_counter + int(passed)
                                    cards = int(user.CARDS) + 1
                                    user.CARDS = cards

                        else:
                            passed_counter = passed_counter + int(passed)
                            failed_counter = failed_counter + int(failed)

                        user.PASSED = passed_counter
                        user.FAILED = failed_counter
                        user.BELT = belt
                        sm_db.session.commit()

                        result = Result(USERID=user_id, EXECUTION_DATE=datetime.now(), PASSED=passed, FAILED=failed, DURATION=duration, PERCENT=percent, RATE=rate, BELT=belt, TASK=task)
                        sm_db.session.add(result)
                        sm_db.session.commit()

                        score = Scores.query.filter_by(USERID=user_id).first()
                        if score is None:
                            current_score = passed_counter - failed_counter*30;
                            score = Scores(USERID=user_id, SCORE=current_score)
                            sm_db.session.add(score)
                            sm_db.session.commit()
                        else:
                            score.SCORE = passed_counter - failed_counter*30;
                            sm_db.session.commit()

                        result = jsonify({'id': user.ID, 'passed': user.PASSED, 'failed': user.FAILED, 'solved': user.SOLVED})

                elif operation == 'name':
                    name = request.json.get('name')
                    if name is None:
                        result = jsonify({'error': 'Missing arguments, no user name'})
                    else:
                        user.NAME = name
                        sm_db.session.commit()
                        result = jsonify({'id': user.ID})

                elif operation == 'surname':
                    surname = request.json.get('surname')
                    if surname is None:
                        result = jsonify({'error': 'Missing arguments, no surname'})
                    else:
                        user.SURNAME = surname
                        sm_db.session.commit()
                        result = jsonify({'id': user.ID})

                elif operation == 'email':
                    email = request.json.get('email')
                    if email is None:
                        result = jsonify({'error': 'Missing arguments, no email'})
                    else:
                        user.EMAIL = email
                        sm_db.session.commit()
                        result = jsonify({'id': user.ID, 'email': user.EMAIL})

                elif operation == 'birthday':
                    birthday = request.json.get('birthday')
                    if birthday is None:
                        result = jsonify({'error': 'Missing arguments, no birthday'})
                    else:
                        user.BIRTHDAY = birthday
                        sm_db.session.commit()
                        result = jsonify({'id': user.ID, 'birthday': user.BIRTHDAY})

                elif operation == 'avatar':
                    avatar = request.json.get('avatar')
                    if avatar is None:
                        result = jsonify({'error': 'Received no avatar'})
                    else:
                        user.AVATAR = avatar
                        sm_db.session.commit()
                        result = jsonify({'id': user.ID, 'avatar': user.AVATAR})

                elif operation == 'lang':
                    lang = request.json.get('lang')
                    if lang is None:
                        result = jsonify({'error': 'Received no language code received'})
                    else:
                        user.LANG = lang
                        sm_db.session.commit()
                        result = jsonify({'id': user.ID, 'lang': user.LANG})
                else:
                    result = jsonify({'error': 'Unknown operation received \'' + operation + '\''})

    return (result, 200)

def update_refferal(user_id, bonus):
    user = User.query.filter_by(ID=user_id).first()
    if user is not None:
        new_passed = int(user.PASSED) + bonus
        user.PASSED = new_passed
        sm_db.session.commit()
        return user.NAME + ' ' + user.SURNAME

    return ''

@sm_app.route('/api/reg', methods = ['POST'])
def registration():
    name = request.json.get('name')
    lang = request.json.get('lang')
    birthday = request.json.get('birthday')
    last = request.json.get('lastname')
    email = request.json.get('email')
    subcsr = request.json.get('subcsr')
    pswdhash = request.json.get('pswdhash')
    passed = request.json.get('passed')
    failed = request.json.get('failed')
    bonus = request.json.get('bonus')

    if name is None:
        result = jsonify({'error': 'Missing arguments, no user name'})
    elif lang is None:
        result = jsonify({'error': 'Missing arguments, no language'})
    elif birthday is None:
        result = jsonify({'error': 'Missing arguments, no birthday'})
    elif email is None:
        result = jsonify({'error': 'Missing arguments, no email address'})
    elif subcsr is None:
        result = jsonify({'error': 'Missing arguments, no subscription'})
    elif pswdhash is None:
        result = jsonify({'error': 'Missing arguments, no password hash'})
    else:
        if bonus is None:
            code = 100
            refferal = ''
        else:
            code = 200
            refferal = update_refferal(user_id=bonus.lstrip('0'), bonus=code)

        # search by email for existed user
        user = User.query.filter_by(EMAIL=email).first()
        if user is not None:
            result = jsonify({'error': 'User with such email address \'' + str(email) + '\' has already registered/existed. Please, use another email address if you want to create a new account.'})
        else:
            try:
                birth = datetime.strptime(birthday,'%Y-%m-%d')
            except Exception as err:
                result = jsonify({'error': 'User birthdate does not match expected format YYYY-MM-DD: ' + str(birthday)})
            else:
                if passed is None:
                    passed = code
                else:
                    passed = int(passed) + code

                # added 100 point as signup bonus
                user = User(NAME=name, LANG=lang, BIRTHDAY=birthday, SURNAME=last, EMAIL=email, PSWDHASH=pswdhash, CREATION_DATE=datetime.now(), PASSED=passed, SUBSCR=subcsr)
                sm_db.session.add(user)
                sm_db.session.commit()
                # sleep 1 second for DB operation
                time.sleep(1)
                user = User.query.filter_by(EMAIL=email).first()
                result = get_user_info(user, refresh=False, user_name=refferal)
                send_registration_email(name, last, lang, email)

    return (result, 200)
