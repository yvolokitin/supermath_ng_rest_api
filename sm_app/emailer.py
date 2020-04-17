from flask_mail import Message
from sm_app import sm_app, mail

def send_forget_email(name, surname, password, lang, recipient):
    msg = Message('Password from SuperMath.xyz',
                  sender=sm_app.config.get('MAIL_USERNAME'),
                  recipients=[recipient])

    msg.body = 'SuperMath.xyz Password ' + password

    msg.html = '<!DOCTYPE html><html lang=\"en\"><head><title>SuperMath Password</title>'
    msg.html += '<meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">'
    msg.html += '<style>body {font-family: Arial; margin: 0;} .header { padding: 30px; text-align: center; background: #1abc9c; color: white; font-size: 30px;}'
    msg.html += '.content {padding:20px;}</style></head>'
    msg.html += '<body><div class=\"header\"><h2>SuperMath.xyz</h2></div><div class=\"content\">'

    if lang is 'ru':
        msg.html += '<h2>Добрый День ' + name + ' ' + surname + '</h2>'
    else :
        msg.html += '<h2>Dear ' + name + ' ' + surname + '</h2>'

    if lang is 'ru':
        msg.html += '<p>Мы очень сожалеем, что у вас возникли проблемы со входов в нашу систему.'
        msg.html += 'Пожалуйста, используйте информацию, которую вы запросили :-)</p> <p>' + password + '</p></div></body></html>'
    else:
        msg.html += '<p>We are sorry that you are having a problem with login. Please look in the below information, '
        msg.html += 'this is probably exactly what you need :-)</p> <p>' + password + '</p></div></body></html>'

    mail.send(msg)

def send_registration_email(recipient):
    return 'not implemented yet'
