import time
import traceback
from datetime import datetime

from flask import request, jsonify

from sm_app import sm_app, sm_db
from sm_app.user import User

def get_user_info(user, email):
    if user is None:
        result = jsonify({'error': 'User with Email address ' + email + ' does not exist OR password does not match registration records.'})
    else:
        result = jsonify({'id': user.ID,
                          'name': user.NAME,
                          'age': user.AGE,
                          'surname': user.SURNAME,
                          'email': user.EMAIL,
                          'creation': user.CREATION_DATE,
                          'pass': user.PASS,
                          'fail': user.FAIL,
                          'ava': user.AVATAR})
    return result

@sm_app.route('/')
def hello():
    return 'Hello YuraV'

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
                result = jsonify({'error': 'No user found with ' + email + ' email address'})
            elif user.PSWD != pswd:
                result = jsonify({'error': 'Incorrect password'})
            else:
                result = get_user_info(user, email)

    return (result, 200)

@sm_app.route('/api/update', methods = ['POST'])
def update_user():
    user_id = request.json.get('user_id')
    operation = request.json.get('operation')

    if user_id is None or operation is None:
        result = jsonify({'error': 'Missing arguments, no user id \'' + user_id + '\' or no operation \'' + operation + '\' received'})
    else:
        user = None
        try:
            user = User.query.filter_by(ID=user_id).first()
        except Exception as e:
            print(traceback.format_exc())
            result = jsonify({'error': 'Exception raised during sql query ' + e})
        else:
            if user is None:
                result = jsonify({'error': 'No registered user with user ID: ' + user_id})
            else:
                if operation == 'results':
                    passed = request.json.get('passed')
                    failed = request.json.get('failed')
                    if passed is None or failed is None:
                        result = jsonify({'error': 'Received wrong passed/failed counters, passed: ' + str(passed) + '/failed: ' + str(failed)})
                    else:
                        user.PASS = int(user.PASS) + int(passed)
                        user.FAIL = int(user.FAIL) + int(failed)
                        sm_db.session.commit()
                        result = jsonify({'id': user.ID, 'pass': user.PASS, 'fail': user.FAIL})
                elif operation == 'avatar':
                    image = request.json.get('image')
                    if image is None:
                        result = jsonify({'error': 'Received wrong or no image for avatar: ' + str(image)})
                    else:
                        user.AVATAR = image
                        sm_db.session.commit()
                        result = jsonify({'id': user.ID, 'ava': user.AVATAR})

    return (result, 200)

@sm_app.route('/api/reg', methods = ['POST'])
def registration():
    user = request.json.get('user')
    age = request.json.get('age')
    last = request.json.get('lastname')
    email = request.json.get('email')
    pswd = request.json.get('pswd')

    if user is None or age is None or email is None or pswd is None:
        result = jsonify({'error': 'Missing arguments, no user/age/email/password provided'})
    else:
        user = User(NAME=user, AGE=age, SURNAME=last, EMAIL=email, PSWD=pswd, PSWDHASH=pswdhash, CREATION_DATE=datetime.now())
        sm_db.session.add(user)
        sm_db.session.commit()
        # sleep 1 second for DB operation
        time.sleep(1)
        user = User.query.filter_by(EMAIL=email).first()
        result = get_user_info(user, email)

    return (result, 200)
