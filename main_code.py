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
Interests_relation = {"Action"      : ("Action", "Action Epic", "B-Action", "Car Action", "Disaster", "Martial Arts", "One-Person Army Action", "Superhero", "Sword & Sandal", "War", "War Epic", "Gun Fu", "Kung Fu", "Samurai", "Wuxia"),
                      "Adventure"   : ("Adventure", "Desert Adventure", "Dinosaur Adventure", "Adventure Epic", "Globetrotting Adventure", "Jungle Adventure", "Mountain Adventure", "Quest", "Road Trip", "Sea Adventure", "Swashbuckler", "Teen Adventure", "Urban Adventure"),
                      "Spy"         : ("Spy"),
                      "Animation"   : ("Animation", "Adult Animation", "Computer Animation", "Hand-Drawn Animation", "Stop Motion Animation"),
                      "Anime"       : ("Anime", "Isekai", "Iyashikei", "Josei", "Mecha", "Seinen", "Shōnen", "Shōjo", "Slice of Life"),
                      "Comedy"      : ("Comedy", "Buddy Comedy", "Buddy Cop", "Dark Comedy", "Farce", "High-Concept Comedy", "Mockumentary", "Parody", "Quirky Comedy", "Raunchy Comedy", "Satire", "Screwball Comedy", "Sitcom", "Sketch Comedy", "Slapstick", "Stand-Up", "Stoner Comedy", "Teen Comedy"),
                      "Con"         : ("Caper", "Heist"),
                      "Crime"       : ("Crime", "Caper", "Cop Drama", "Drug Crime", "Film Noir", "Gangster", "Heist", "Police Procedural", "True Crime"),
                      "Disaster"    : ("Disaster"),
                      "Documentary" : ("Documentary", "Crime Documentary", "Docuseries", "Faith & Spirituality Documentary", "Food Documentary", "History Documentary", "Military Documentary", "Music Documentary", "Nature Documentary", "Political Documentary", "Science & Technology Documentary", "Sports Documentary", "Travel Documentary"),
                      "Drama"       : ("Drama", "Biography", "Coming-of-Age", "Costume Drama", "Docudrama", "Epic", "Financial Drama", "History", "Legal Drama", "Medical Drama", "Period Drama", "Political Drama", "Prison Drama", "Psychological Drama", "Showbiz Drama", "Soap Opera", "Teen Drama", "Tragedy", "Workplace Drama", "Korean Drama", "Telenovela", "Cop Drama"),
                      "Dystopia"    : ("Dystopian Sci-Fi", "Cyberpunk"),
                      "Epic"        : ("Epic", "Action Epic", "War Epic", "Historical Epic", "Fantasy Epic", "Romantic Epic", "Sci-Fi Epic", "Western Epic"),
                      "Fantasy"     : ("Fantasy", "Dark Fantasy", "Fantasy Epic", "Fairy Tale", "Supernatural Fantasy", "Sword & Sorcery", "Teen Fantasy"),
                      "Gangster"    : ("Gangster"),
                      "Holiday"     : ("Holiday", "Holiday Animation", "Holiday Comedy", "Holiday Family", "Holiday Romance"),
                      "Horror"      : ("Horror", "B-Horror", "Body Horror", "Folk Horror", "Found Footage Horror", "Monster Horror", "Psychological Horror", "Slasher Horror", "Splatter Horror", "Supernatural Horror", "Teen Horror", "Vampire Horror", "Werewolf Horror", "Witch Horror", "Zombie Horror"),
                      "Music"       : ("Music", "Concert"),
                      "Musical"     : ("Musical", "Classic Musical", "Jukebox Musical", "Pop Musical", "Rock Musical"),
                      "Mystery"     : ("Mystery", "Bumbling Detective", "Cozy Mystery", "Hard-boiled Detective", "Suspense Mystery", "Whodunnit"),
                      "One-Man-Army": ("One-Person Army Action"),
                      "Romance"     : ("Romance", "Dark Romance", "Romantic Epic", "Feel-Good Romance", "Romantic Comedy", "Steamy Romance", "Teen Romance", "Tragic Romance"),
                      "Sci-Fi"      : ("Sci-Fi", "Alien Invasion", "Artificial Intelligence", "Cyberpunk", "Kaiju", "Space Sci-Fi", "Steampunk", "Time Travel"),
                      "Superhero"   : ("Superhero"),
                      "Sport"       : ("Sport", "Baseball", "Basketball", "Boxing", "Extreme Sport", "Football", "Motorsport", "Soccer", "Water Sport"),
                      "Swashbuckler": ("Swashbuckler"),
                      "Time Travel" : ("Time Travel"),
                      "Thriller"    : ("Thriller", "Conspiracy Thriller", "Cyber Thriller", "Erotic Thriller", "Giallo", "Legal Thriller", "Political Thriller", "Psychological Thriller", "Serial Killer", "Spy", "Survival"),
                      "Vampire"     : ("Vampire Horror"),
                      "War"         : ("War", "War Epic"),
                      "Western"     : ("Western", "Classical Western", "Contemporary Western", "Western Epic", "Spaghetti Western")
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