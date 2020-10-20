from flask import jsonify

def get_user_info(user, refresh=False, user_name=''):
    if refresh is False:
        result = jsonify({'id': user.ID, 'name': user.NAME, 'lang': user.LANG,
                          'birthday': user.BIRTHDAY, 'surname': user.SURNAME,
                          'email': user.EMAIL, 'creation': user.CREATION_DATE,
                          'avatar': user.AVATAR, 'passed': user.PASSED,
                          'failed': user.FAILED, 'cards': user.CARDS,
                          'belt': user.BELT, 'level': user.LEVEL,
                          'solved': user.SOLVED, 'subscr': user.SUBSCR,
                          'refferal': user_name})
    else:
        result = jsonify({'id': user.ID, 'name': user.NAME, 'lang': user.LANG,
                          'birthday': user.BIRTHDAY, 'surname': user.SURNAME,
                          'email': user.EMAIL, 'creation': user.CREATION_DATE,
                          'avatar': user.AVATAR, 'passed': user.PASSED,
                          'failed': user.FAILED, 'cards': user.CARDS,
                          'belt': user.BELT, 'level': user.LEVEL,
                          'solved': user.SOLVED, 'subscr': user.SUBSCR,
                          'refferal': user_name, 'refresh': True})
    return result
