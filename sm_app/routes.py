﻿import time
import traceback
from datetime import datetime

from flask import request, jsonify, abort

from sm_app import sm_app, sm_db
from sm_app.user import User
from sm_app.result import Result

def get_user_info(user, refresh=False):
    if user is None:
        result = jsonify({'error': 'User with Email address ' + str(email)
                        + ' does not exist OR password does not match registration records.'})
    else:
        result = jsonify({'id': user.ID,
                          'name': user.NAME,
                          'lang': user.LANG,
                          'age': user.AGE,
                          'surname': user.SURNAME,
                          'email': user.EMAIL,
                          'creation': user.CREATION_DATE,
                          'pass': user.PASS,
                          'fail': user.FAIL,
                          'belt': user.BELT,
                          'avatar': user.AVATAR})
    return result

@sm_app.route('/')
def hello():
    return 'Hello User'

@sm_app.route('/api/refresh', methods = ['POST'])
def refresh():
    result = jsonify({'error': 'Unimplementer'})
    return (result, 200)

@sm_app.route('/api/login', methods = ['POST'])
def login():
    email = request.json.get('email')
    pswd = request.json.get('pswd')

    if email is None or pswd is None:
        result = jsonify({'error': 'Missing arguments, no email or password provided'})
    else:
        user = None
        try:
            user = User.query.filter_by(EMAIL=email).first()
        except Exception as e:
            print(traceback.format_exc())
            result = jsonify({'error': e})
        else:
            if user is None:
                result = jsonify({'error': 'No user found with \'' + str(email) + '\' email address'})
            elif user.PSWD != pswd:
                result = jsonify({'error': 'Incorrect password used \'' + str(pswd) + '\' for login'})
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
                    # needed for separate results table
                    duration = request.json.get('duration')
                    percent = request.json.get('percent')
                    rate = request.json.get('rate')
                    belt = request.json.get('belt')
                    task = request.json.get('task')

                    if passed is None or failed is None:
                        result = jsonify({'error': 'Received wrong passed/failed counters, passed: '
                                        + str(passed) + '/failed: ' + str(failed)})
                    elif duration is None or percent is None or rate is None or belt is None or task is None:
                        result = jsonify({'error': 'Received wrong duration/percent/rate/belt/task parameters'})
                    else:
                        user.PASS = int(user.PASS) + int(passed)
                        user.FAIL = int(user.FAIL) + int(failed)
                        user.BELT = belt
                        sm_db.session.commit()

                        result = Result(USERID=user_id, EXECUTION_DATE=datetime.now(), PASSED=passed, FAILED=failed, DURATION=duration, PERCENT=percent, RATE=rate, BELT=belt, TASK=task)
                        sm_db.session.add(result)
                        sm_db.session.commit()

                        result = jsonify({'id': user.ID, 'pass': user.PASS, 'fail': user.FAIL})

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
                        result = jsonify({'id': user.ID})

                elif operation == 'password':
                    pswd = request.json.get('pswd')
                    newhash = request.json.get('newhash')
                    if pswd is None:
                        result = jsonify({'error': 'No NEW password received'})
                    elif newhash is None:
                        result = jsonify({'error': 'No NEW password Hash received'})
                    else:
                        user.PSWD = pswd
                        user.PSWDHASH = newhash
                        sm_db.session.commit()
                        result = jsonify({'id': user.ID})

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
                    result = jsonify({'error': 'Unknown operatino received \'' + operation + '\''})

    return (result, 200)

@sm_app.route('/api/reg', methods = ['POST'])
def registration():
    name = request.json.get('name')
    lang = request.json.get('lang')
    age = request.json.get('age')
    last = request.json.get('lastname')
    email = request.json.get('email')
    subcsr = request.json.get('subcsr')
    pswd = request.json.get('pswd')
    pswdhash = request.json.get('pswdhash')

    if name is None:
        result = jsonify({'error': 'Missing arguments, no user name'})
    elif lang is None:
        result = jsonify({'error': 'Missing arguments, no language'})
    elif age is None:
        result = jsonify({'error': 'Missing arguments, no birth date'})
    elif email is None:
        result = jsonify({'error': 'Missing arguments, no email address'})
    elif pswd is None:
        result = jsonify({'error': 'Missing arguments, no password'})
    elif subcsr is None:
        result = jsonify({'error': 'Missing arguments, no subscription'})
    elif pswdhash is None:
        result = jsonify({'error': 'Missing arguments, no password hash'})
    else:
        # search by email for existed user
        user = User.query.filter_by(EMAIL=email).first()
        if user is not None:
            result = jsonify({'error': 'User with such email address \'' + str(email) + '\' has already registered. Please, use another email address if you want to create a new account.'})
        else:
            try:
                birth = datetime.strptime(age,'%Y-%m-%d')
            except Exception as err:
                result = jsonify({'error': 'User birthdate does not match expected format YYYY-MM-DD: ' + str(age)})
            else:
                user = User(NAME=name, LANG=lang, AGE=birth, SURNAME=last, EMAIL=email, PSWD=pswd, PSWDHASH=pswdhash, CREATION_DATE=datetime.now())
                sm_db.session.add(user)
                sm_db.session.commit()
                # sleep 1 second for DB operation
                time.sleep(1)
                user = User.query.filter_by(EMAIL=email).first()
                result = get_user_info(user)

    return (result, 200)
