#!flask/bin/python
import os
from flask import Flask, abort, request, jsonify, g, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello YuraV'

@app.route('/api/login', methods = ['POST'])
def user_login():
    user = request.json.get('user')
    pswd = request.json.get('pswd')

    print (user)
    print (pswd)

    if user is None or pswd is None:
        abort(400) # missing arguments

    # fake behaviour and reply with HTTP OK, 200
    return jsonify({'id': 13, 'name': user, 'age': 6, 'pass': 767, 'fail': 13}), 200

@app.route('/api/reg', methods = ['POST'])
def user_registration():
    user = request.json.get('user')
    last = request.json.get('lastname')
    mail = request.json.get('email')
    pswd = request.json.get('pswd')
    age = request.json.get('age')

    print (user)
    print (pswd)

    if user is None or pswd is None:
        abort(400) # missing arguments

    # fake behaviour and reply with HTTP OK, 200
    return jsonify({'id': 13, 'name': user, 'age': 6, 'pass': 0, 'fail': 0}), 200

# curl -i -X POST -H "Content-Type: application/json" -d "{"""user""":"""miguel""","""pswd""":"""python"""}" http://127.0.0.1:5000/api/login
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 443
    port = int(os.environ.get('PORT', 443))
    app.run(host='0.0.0.0', port=port)
