#!flask/bin/python
import os
from sm_app import sm_app

# curl -i -X POST -H "Content-Type: application/json" -d "{"""user""":"""miguel""","""pswd""":"""python"""}" http://127.0.0.1:5000/api/login
# curl -i -X POST -H "Content-Type: application/json" -d "{"""user""":"""miguel""","""pswd""":"""python"""}" http://145.14.158.94:3000/api/login
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 443
    port = int(os.environ.get('PORT', 3000))
    # app.run(host='0.0.0.0', port=port)
    sm_app.run(host='0.0.0.0', port=port)
