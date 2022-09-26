import requests


def return_from_common_table(payload):
    response_common_table = requests.get(
        'https://api.airtable.com/v0/appfS4qdnNRuKf7Nj/Common?api_key=keymymTDarJxGrQJC')
    for x in range(len(response_common_table.json()['records'])):
        if payload in response_common_table.json()['records'][x]['fields']['Phone']:
            if 'BLZ' in response_common_table.json()['records'][x]['fields']:
                return response_common_table.json()['records'][x]['fields']['BLZ']


def return_from_blz_manipula_table(apprat_num):
    response_blz_manipula_table = requests.get('https://api.airtable.com/v0/appfS4qdnNRuKf7Nj/blz_manipula?'
                                               'api_key=keymymTDarJxGrQJC')
    for x in range(len(response_blz_manipula_table.json()['records'])):
        if apprat_num in response_blz_manipula_table.json()['records'][x]['fields']['BLZ']:
            return response_blz_manipula_table.json()['records'][x]['fields']['Manipules']


def user_data_from_db(payload):
    temp_dict = {}
    user_data = {}
    if return_from_common_table(payload) is not None:
        for i in list(return_from_common_table(payload).split('\n')):
            temp_dict[i] = list(return_from_blz_manipula_table(i).split('\n'))
    user_data['BLZ'] = temp_dict
    return user_data


print(user_data_from_db('+79017045424'))