import time
import traceback
from datetime import datetime

from sqlalchemy import desc

from flask import request, jsonify
from flask import render_template

from sm_app import sm_app, sm_db
from sm_app.user import User
from sm_app.result import Result
from sm_app.friends import Friends
from sm_app.scores import Scores

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
        users = sm_db.session.query(User, Scores).filter(User.ID == Scores.USERID).order_by(desc(Scores.SCORE)).limit(10).all()
        data = []
        for user in users:
            data.append({'id': user.User.ID, 'name': user.User.NAME, 'surname': user.User.SURNAME, 'passed': user.User.PASSED, 'failed': user.User.FAILED, 'score': user.Scores.SCORE})
        result = jsonify(data)

    return (result, 200)

@sm_app.route('/api/forget', methods = ['POST'])
def forget():
    email = request.json.get('email')
    if email is None:
        result = jsonify({'error': 'Forget Call: missing arguments, no email received'})
    else:
        user = None
        try:
            user = User.query.filter_by(EMAIL=email).first()
        except Exception as e:
            print(traceback.format_exc())
            result = jsonify({'error': 'Forget Call: exception raised ' + e})
        else:
            if user is None:
                result = jsonify({'error': 'Forget Call: No user found with \'' + str(email) + '\' email address'})
            else:
                send_forget_email(user.NAME, user.SURNAME, user.PSWD, user.LANG, email)
                result = jsonify({'email': email})

    return (result, 200)

@sm_app.route('/api/refresh', methods = ['POST'])
def refresh():
    user_id = request.json.get('user_id')
    pswdhash = request.json.get('pswdhash')
    if user_id is None:
        result = jsonify({'error': 'Refresh Call: missing arguments, no user id received'})
    elif pswdhash is None:
        result = jsonify({'error': 'Refresh Call: no authorization method provided'})
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
                result = get_user_info(user, True)

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
        except Exception as e:
            print(traceback.format_exc())
            result = jsonify({'error': 'Login Call: exception raised' + e})
        else:
            if user is None:
                result = jsonify({'error': 'Login Call: no user found with \'' + str(email) + '\' email address'})
            else:
                if user.PSWDHASH != pswdhash:
                    result = jsonify({'error': 'Login Call: incorrect password used \'' + str(email) + '\' account'})
                else:
                    result = get_user_info(user)

    return (result, 200)

@sm_app.route('/api/counter', methods = ['POST'])
def update_counter():
    user_id = request.json.get('user_id')
    pswdhash = request.json.get('pswdhash')
    passed = request.json.get('passed')
    failed = request.json.get('failed')
    belt = request.json.get('belt')

    if user_id is None:
        result = jsonify({'error': 'Counter Call: missing arguments, no user id received'})
    elif pswdhash is None:
        result = jsonify({'error': 'Counter Call: no authorization method provided'})
    elif passed is None or failed is None or belt is None:
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
                pass_value =  int(pass_dec / user_id)
                fail_value =  int(fail_dec / user_id)
                user.PASS = pass_value
                user.FAIL = fail_value
                user.BELT = belt
                sm_db.session.commit()
                result = jsonify({'id': user.ID, 'pass': user.PASS, 'fail': user.FAIL, 'belt': user.BELT})

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
                        if (int(failed) == 0) and (int(passed) > 0):
                            if game_uid not in user.SOLVED:
                                user.SOLVED += game_uid + ','
                                cards = int(user.CARDS) + 1
                                user.CARDS = cards

                        passed_counter = int(user.PASSED) + int(passed)
                        failed_counter = int(user.FAILED) + int(failed)
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
                    passed = 100
                else:
                    passed = int(passed) + 100

                # added 100 point as signup bonus
                user = User(NAME=name, LANG=lang, BIRTHDAY=birthday, SURNAME=last, EMAIL=email, PSWDHASH=pswdhash, CREATION_DATE=datetime.now(), PASSED=passed, SUBSCR=subcsr)
                sm_db.session.add(user)
                sm_db.session.commit()
                # sleep 1 second for DB operation
                time.sleep(1)
                user = User.query.filter_by(EMAIL=email).first()
                result = get_user_info(user)
                send_registration_email(name, last, lang, email)

    return (result, 200)
