import json
import requests

# Tastedive part
td_api_key = "384601-project-ITUMD59T"

# Getting a dictionary with information on the movies related to the input movie
def get_movies_from_tastedive(string):
    baseurl = "https://tastedive.com/api/similar"
    d_params = {}
    d_params['q'] = string
    d_params['limit'] = 5
    d_params['type'] = "movies"
    #d_params['callback'] = 1
    #d_params['k'] = td_api_key
    dive_resp = requests.get(baseurl, params=d_params)
    print(dive_resp.url)
    return dive_resp.json()

# Extracting only the title names for the related movies
def extract_movie_titles(diction):
    return ([i['Name'] for i in diction["Similar"]['Results']])
    
# Getting a single list of related movies
def get_related_titles(lst):
    new_lst = []
    fin_lst = []
    for item in lst:
        new_lst+=(extract_movie_titles(get_movies_from_tastedive(item)))

    for movie in new_lst:
        if movie not in fin_lst:
            fin_lst.append(movie)
    
    return(fin_lst)

#OMDB part
om_api_k = "bb71d9cd"

# Getting information on a movie
def get_movie_data(string):
    baseurl = "http://www.omdbapi.com/"
    d_params = {}
    d_params['apikey'] = om_api_k
    d_params['t'] = string
    d_params['r'] = "json"
    ombd_resp = requests.get(baseurl, params=d_params)
    print(ombd_resp.url)
    return ombd_resp.json()

# Extracting movie rating from Rotten Tomatoes
def get_movie_rating(diction):
    for critic in diction['Ratings']:
        if critic['Source'] == "IMDb":
           return int(critic['Value'][:-1])
    return 0

def get_sorted_recommendations(m_lst):
    related_movies = get_related_titles(m_lst)
    
    sorted_lst = sorted(related_movies, key=lambda movie_name: get_movie_rating(get_movie_data(movie_name)),
                                    reverse=True )
    return sorted_lst

print(get_sorted_recommendations(["Pulp Fiction", "Reservoir Dogs"]))