import json
import requests

api_k = "bb71d9cd"

def get_movie_data(string):
    baseurl = "http://www.omdbapi.com/"
    d_params = {}
    d_params['apikey'] = api_k
    d_params['t'] = string
    d_params['r'] = "json"
    ombd_resp = requests.get(baseurl, params=d_params)
    print(ombd_resp.url)
    return ombd_resp.json()

def get_movie_rating(diction):
    for critic in diction['Ratings']:
        if  critic['Source'] == "Rotten Tomatoes":
            val= critic['Value'].replace('%', '')
            return int(val)
    return 0

print(get_movie_rating(get_movie_data("Black Panther")))