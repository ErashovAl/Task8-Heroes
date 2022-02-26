import requests
from pprint import pprint

def hero_features(name):
    
    url = 'http://superheroapi.com/api/2619421814940190/'
    dict_id = {}
    
    for hero in name:
        stats_hero = requests.get(url + '/search/' + hero).json()['results'][0]
        int_hero = stats_hero['powerstats']['intelligence']   
        dict_id[hero] = int_hero
    
    total, hero_intel = sort_int_hero(dict_id)
    
    return f'Список героев {total}, intelligence = {hero_intel}'

def sort_int_hero(dict1):
    
    smartest = []
    intell = sorted(dict1.values())
    max_intell = intell[0]
    
    for k,v in dict1.items():
        if v == max_intell:
            smartest += [k]
    return smartest, max_intell    
     
pprint(hero_features(['Hulk','Captain America','Thanos']))