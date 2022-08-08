import requests 
from typing import List, Dict
import yaml
import csv

def _get_historical_legislators() -> List:
    print(f'Getting historical legislators...')
    response = requests.get('https://github.com/unitedstates/congress-legislators/raw/main/legislators-historical.yaml')
    print('parsing...')
    return yaml.safe_load(response.text)

def _get_current_legislators() -> List:
    print(f'Getting current legislators...')
    response = requests.get('https://github.com/unitedstates/congress-legislators/raw/main/legislators-current.yaml')
    print('parsing...')
    return yaml.safe_load(response.text)

def get_all_legislators() -> List:
    return _get_current_legislators() + _get_historical_legislators()

def _get_all_capitals() -> List:
    print(f'Getting state capitals...')
    response = requests.get('http://goodcsv.com/wp-content/uploads/2020/08/us-states-territories.csv')
    print('parsing csv')
    decoded_response = response.text
    csv_reader = csv.reader(decoded_response.splitlines(), delimiter=',')
    return list(csv_reader)

def _are_letterbanked(string1: str, string2: str):
    if string1 is None or string2 is None:
        return False
    string1 = string1.upper()
    string2 = string2.upper()
    for s in string1:
        if s not in string2:
            return False
    for s in string2:
        if s not in string1:
            return False
    return True

def is_letterbanked_with_capital(name: str, state_abbrev: str) -> bool:
    capital = get_capital_from_abbrev(state_abbrev)
    return _are_letterbanked(name, capital)

def get_capital_from_abbrev(abbrev: str) ->str:
    for state in STATE_CAPITALS:
        if abbrev == state[2].strip():
            return state[3].strip()
    return None

def get_term_states(legislator: Dict) -> List:
    """
    Returns a list of unique state abbrevs for all of
    the legislators terms
    """
    state_list = []
    for term in legislator['terms']:
        state_list.append(term['state'])
    return set(state_list)


STATE_CAPITALS = _get_all_capitals() 

if __name__ == '__main__':
    all_legislators = get_all_legislators()
    print(f'Iterating over all {len(all_legislators)} past and present legislators...')
    for legislator in all_legislators:
        name = legislator['name']['last']
        print(f'Checking {name}...')
        state_list = get_term_states(legislator)
        for state in state_list:
            print(f'Checking against capital of {state}...')
            if is_letterbanked_with_capital(name, state):
                print('MATCH!\n\n')