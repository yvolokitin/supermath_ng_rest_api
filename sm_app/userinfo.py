from flask import jsonify

def get_user_info(user, refresh=False):
    if refresh is False:
        result = jsonify({'id': user.ID, 'name': user.NAME, 'lang': user.LANG,
                          'birthday': user.BIRTHDAY, 'surname': user.SURNAME,
                          'email': user.EMAIL, 'creation': user.CREATION_DATE,
                          'avatar': user.AVATAR, 'passed': user.PASSED,
                          'failed': user.FAILED, 'belt': user.BELT,
                          'solved': user.SOLVED, 'subscr': user.SUBSCR})
    else:
        result = jsonify({'id': user.ID, 'name': user.NAME, 'lang': user.LANG,
                          'birthday': user.BIRTHDAY, 'surname': user.SURNAME,
                          'email': user.EMAIL, 'creation': user.CREATION_DATE,
                          'avatar': user.AVATAR, 'passed': user.PASSED,
                          'failed': user.FAILED, 'belt': user.BELT,
                          'solved': user.SOLVED, 'subscr': user.SUBSCR, 'refresh': True})
    return result

def extract_top_info(users):
    result = {}
    item = 1
    for user in users:
        result[str(item)] = user.get_userinfo()
        item += 1
    return jsonify(result)
