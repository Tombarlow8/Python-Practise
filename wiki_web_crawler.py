# connect to a API (hopefully wiki)
# https://en.wikipedia.org/w/api.php?
# add this on to the end of the url to say we want to search 'action=opensearch'
# add this on the ed to recieve the request in joson format '&format=json'
# and ad this on the end to enter the searcg info '&search='
# can always enter the url into the address bar of the browser to test
# https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search=Radcliffe
# a link on the wikipedia API - https://www.mediawiki.org/wiki/API:FAQ
import requests
import random


def get_json_request_dict(random_wiki_word):
    url = "https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search="
    my_request = requests.get(url + random_wiki_word)     
    response_dict = my_request.json()      
    return response_dict


def get_random_wiki_word(response_dict):   
    rand_index = random.randrange(0,len(response_dict[1])-1)
    print("Search Term: " + response_dict[1][rand_index] + " --- " + response_dict[2][rand_index] )
    response_words = response_dict[2][rand_index]
    words = str(response_words).split()
    random_wiki_word = words[random.randrange(0,len(words)-1)]
    return random_wiki_word


search_terms = []

while len(search_terms) < 10:
    if len(search_terms) <= 0:
        start_wiki_word = input("type to start the search: ")
        search_terms.append(get_random_wiki_word(get_json_request_dict(start_wiki_word)))
    else:
        search_terms.append(get_random_wiki_word(get_json_request_dict(search_terms[len(search_terms)-1])))


