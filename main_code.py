# #Debugs########
# print("From Cache:", resp.fromcache)
#
# print("\n respons:")
# for d in resp:
#     print("part of response: ",d ," -->> ", resp[d])
#
# print("\nData length:", len(content))
# print("first part of data", content[:70])
# ##########


#################################################### Imports ######################################################
import httplib2 as hlib
import json
import pyperclip as pyclp
from math import floor as flr


#################################################### Variables ####################################################
output = []


#################################################### Tuples, lists & Dictionaries #################################
# Tuples
    # This tuple contains the different information titles in the order that it is stored in the google sheets document
keys_in_order = ("primaryTitle", "runtimeSeconds", "interests", "link", "location")

# Dictionaries
    # This dictionary contains all the imdb interestes (genres and subgenres) and what genre counterpart it has in the google sheets document
Interests_relation = {"Action"      : ("Action", "Action Epic", "B-Action", "Car Action", "Martial Arts", "One-Person Army Action", "Superhero", "Sword & Sandal", "War", "War Epic", "Gun Fu", "Kung Fu", "Samurai", "Wuxia"),
                      "Thriller"    : (),
                      "Comedy"      : (),
                      "Adventure"   : ("Adventure", "Desert Adventure", "Dinosaur Adventure", "Adventure Epic", "Globetrotting Adventure", "Jungle Adventure", "Mountain Adventure", "Quest", "Road Trip", "Sea Adventure", "Swashbuckler", "Teen Adventure", "Urban Adventure"),
                      "Sci-Fi"      : (),
                      "Fantasy"     : (),
                      "War"         : (),
                      "Mystery"     : (),
                      "Crime"       : (),
                      "Drama"       : (),
                      "Agent"       : (),
                      "Dystopia"    : (),
                      "Vampire"     : (),
                      "Western"     : (),
                      "One-Man-Army": ("One-Person Army Action", ),
                      "Christmas"   : (),
                      "Romance"     : (),
                      "Epic"        : (),
                      "Superhero"   : (),
                      "Disaster"    : (),
                      "Gangster"    : (),
                      "Pirate"      : ("Swashbuckler", )
                     }

#################################################### Functions ####################################################



#################################################### HTTP Getter ##################################################
# This makes the request to a imdb api that allows us to GET data with the imdb ID.
    # imdb api link: "https://imdbapi.dev/"
h = hlib.Http(".cache")
(resp, content) = h.request("https://api.imdbapi.dev/titles/tt0172495", "GET")

# Converts the bytes recived into a python dictionary 
data_dict = json.loads(content)


#################################################### Data extraction and formatting ###############################
#Extracts and appends the title
title = data_dict[keys_in_order[0]]
output.append(title)

#Extracts and appends the length in hours and minutes
length_in_seconds = data_dict[keys_in_order[1]]
minutes = int(flr(length_in_seconds/60))
hours = int(flr(minutes/60))
extra_minutes = minutes - hours*60

lenght_str = str(hours) + "h " + str(extra_minutes) + "m"
output.append(lenght_str)

# Extracts and appends relvent genres & subgenres





#################################################### Data String Export ###########################################

#robably is not gonna be used because it will write directly into the google sheets
str_output = "\t".join(output)
print(str_output)
#pyclp.copy(str_output)