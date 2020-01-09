#!flask/bin/python
import os
from flask import Flask, abort, request, jsonify, g, url_for

app = Flask(__name__)

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
    return jsonify({ 'username': user }), 200, {'user_id': '13'}

# curl -i -X POST -H "Content-Type: application/json" -d "{"""user""":"""miguel""","""pswd""":"""python"""}" http://127.0.0.1:5000/api/login
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 443
    port = int(os.environ.get('PORT', 443))
    app.run(host='0.0.0.0', port=port)
