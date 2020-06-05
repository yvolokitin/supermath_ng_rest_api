'''
    Functions, which were a part of API, but not valid @current moment
'''

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
