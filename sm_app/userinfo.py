from flask import jsonify

def get_user_info(user, refresh=False):
    if refresh is False:
        result = jsonify({'id': user.ID, 'name': user.NAME, 'lang': user.LANG,
                          'age': user.AGE, 'surname': user.SURNAME, 'email': user.EMAIL,
                          'creation': user.CREATION_DATE, 'avatar': user.AVATAR,
                          'pass': user.PASS, 'fail': user.FAIL, 'belt': user.BELT})
    else:
        result = jsonify({'id': user.ID, 'name': user.NAME, 'lang': user.LANG,
                          'age': user.AGE, 'surname': user.SURNAME, 'email': user.EMAIL,
                          'creation': user.CREATION_DATE, 'avatar': user.AVATAR,
                          'pass': user.PASS, 'fail': user.FAIL, 'belt': user.BELT,
                          'refresh': True})
    return result

def extract_top_info(users):
    result = {}
    item = 1
    for user in users:
        result[str(item)] = user.get_userinfo()
        item += 1
    return jsonify(result)
