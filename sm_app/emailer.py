from flask import render_template
from flask_mail import Message
from sm_app import sm_app, mail

# self send email message
def send_selfemail(name, sender, lang, message):
    msg = Message('SuperMath.xyz Question',
                  body = 'SuperMath.xyz Question',
                  sender=sm_app.config.get('MAIL_USERNAME'),
                  recipients=[sm_app.config.get('MAIL_USERNAME')])

    msg.html = '<!DOCTYPE html><html lang=\"en\"><head><title>SuperMath Question</title>'
    msg.html += '<meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">'
    msg.html += '<style>body {font-family: Arial; margin: 0;} .header { padding: 30px; text-align: center; background: #1abc9c; color: white; font-size: 30px;}'
    msg.html += '.content {padding:20px;}</style></head>'
    msg.html += '<body><div class=\"header\"><h2>SuperMath.xyz</h2></div><div class=\"content\">'

    if lang == 'ru':
        msg.html += '<h2>Пользователь ' + name + ', (' + sender + ')</h2>'
        msg.html += '<p>Оставил сообщение</p> <p>' + message + '</p></div></body></html>'
    else:
        msg.html += '<h2>User ' + name + ', (' + sender + ')</h2>'
        msg.html += '<p>Sent a message</p> <p>' + message + '</p></div></body></html>'

    mail.send(msg)

def send_forget_email(name, surname, password, lang, recipient):
    msg = Message('SuperMath.xyz password',
                  body = 'SuperMath.xyz password ' + password,
                  sender=sm_app.config.get('MAIL_USERNAME'),
                  recipients=[recipient])

    msg.html = '<!DOCTYPE html><html lang=\"en\"><head><title>SuperMath Password</title>'
    msg.html += '<meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">'
    msg.html += '<style>body {font-family: Arial; margin: 0;} .header { padding: 30px; text-align: center; background: #1abc9c; color: white; font-size: 30px;}'
    msg.html += '.content {padding:20px;}</style></head>'
    msg.html += '<body><div class=\"header\"><h2>SuperMath.xyz</h2></div><div class=\"content\">'

    if lang == 'ru':
        msg.html += '<h2>Добрый День ' + name + ' ' + surname + '</h2>'
        msg.html += '<p>Мы очень сожалеем, что у вас возникли проблемы со входов в нашу систему.'
        msg.html += 'Пожалуйста, используйте информацию, которую вы запросили :-)</p> <p>' + password + '</p></div></body></html>'
    else:
        msg.html += '<h2>Dear ' + name + ' ' + surname + '</h2>'
        msg.html += '<p>We are sorry that you are having a problem with login. Please look in the below information, '
        msg.html += 'this is probably exactly what you need :-)</p> <p>' + password + '</p></div></body></html>'

    mail.send(msg)

def send_registration_email(name, surname, lang, recipient):
    if lang == 'ru':
        subject = 'Добро пожаловавть на SuperMath.xyz'
        title = 'Добро пожаловавть в Мир Арифметики SuperMath.xyz'
        description = 'SuperMath - это набор бесплатных математических упражнений для практики простых и сложных арифметических действий.'
        text = 'Дети могут сохранять результаты, обмениваться баллами, выбирать аватары и отслеживать прогресс, используя отчеты и информационные панели.'
    else:
        subject = 'Welcome to SuperMathSuperMath.xyz'
        title = 'Welcome to Arithmetical world'
        description = 'SuperMath is a collection of free math activities to practice straightforward arithmetic problems that adapt as they learn.'
        text = 'Kids can keep results, trade points, select avatars and track the progress using fluency reports and dashboards.'

    arguments = {
        'subject': subject,
        'name': name,
        'surname': surname,
        'title': title,
        'description': description,
        'text': text,
    }

    msg = Message(subject, body=subject, sender=sm_app.config.get('MAIL_USERNAME'), recipients=[recipient])
    msg.html = render_template('index.html', **arguments)
    mail.send(msg)

