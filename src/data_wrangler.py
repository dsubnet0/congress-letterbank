import requests 
from typing import List, Dict
import yaml
import csv

def _get_historical_legislators() -> List:
    response = requests.get('https://github.com/unitedstates/congress-legislators/raw/main/legislators-historical.yaml')
    print('parsing yaml')
    return yaml.safe_load(response.text)

def _get_current_legislators() -> List:
    response = requests.get('https://github.com/unitedstates/congress-legislators/raw/main/legislators-current.yaml')
    print('parsing yaml')
    return yaml.safe_load(response.text)

def get_all_legislators() -> List:
    return _get_current_legislators() + _get_historical_legislators()

def _get_all_capitals() -> List:
    response = requests.get('http://goodcsv.com/wp-content/uploads/2020/08/us-states-territories.csv')
    decoded_response = response = response.content.decode('utf-8')
    csv_reader = csv.reader(decoded_response.splitlines(), delimiter=',')
    return list(csv_reader)

def _are_letterbanked(string1: str, string2: str):
    for s in string1:
        if s not in string2:
            return False
    for s in string2:
        if s not in string1:
            return False
    return True

#def find_letterbanked_capital(name:str) -> str:
#    for state in _get_all_capitals():
#        if _are_letterbanked(name, state[1]):
#            return f'state[0], state[1]'
#    return None

def _get_term_states(legislator: Dict) -> List:
    state_list = []
    for term in legislator['terms']:
        state_list.append(term['state'])
    return state_list

if __name__ == '__main__':
#    d = get_all_legislators()
#    print(f'{len(d)} total legislators')
#    print('Checking for Cheney...')
#    for i in d:
#        if i['name']['last'] == 'Cheney':
#            print(i)
    state_capitols = _get_all_capitals() 
    for legislator in get_all_legislators():
        name = legislator['name']['last']
        state_list = _get_term_states(legislator)
        print(f'Checking {name}...')