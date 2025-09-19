# In this application there is a lot of genre chaos... so to set things straight:
    # super_genre   ->  The genres wanted and is to be used in the google sheets document
    # sub_genre     ->  The genres that IMDb have, these will all have a relative super_g which it will translated to
    # interest      ->  The genres the application recives with the given movie (thats what they are called in the HTTP response).

#################################################### Imports ######################################################
import httplib2 as hlib
import json
import pyperclip as pyclp
from math import floor as flr


#################################################### Variables ####################################################
debug = 0


#################################################### Tuples, lists & Dictionaries #################################
# Tuples
    # This tuple contains the different information titles in the order that it is stored in the google sheets document
keys_in_order = ("primaryTitle", "runtimeSeconds", "interests", "link", "location")

# Lists
    # This list will contain the output message and will be joined with \t in the end.
output = []
    # This list contains all the super_genres that will be added to the output list.
final_super_genres = []

# Dictionaries
    # This dictionary contains all the super_genres as the key and its sub_genre relatives as its values.
                                # Super Genres      # Sub Genres
super_and_sub_genre_relation =  {"Action"           : ("Action", "Action Epic", "B-Action", "Car Action", "Disaster", "Martial Arts", "One-Person Army Action", "Superhero", "Sword & Sandal", "War", "War Epic", "Gun Fu", "Kung Fu", "Samurai", "Wuxia"),
                                "Adventure"         : ("Adventure", "Desert Adventure", "Dinosaur Adventure", "Adventure Epic", "Globetrotting Adventure", "Jungle Adventure", "Mountain Adventure", "Quest", "Road Trip", "Sea Adventure", "Swashbuckler", "Teen Adventure", "Urban Adventure"),
                                "Spy"               : ("Spy"),
                                "Animation"         : ("Animation", "Adult Animation", "Computer Animation", "Hand-Drawn Animation", "Stop Motion Animation"),
                                "Anime"             : ("Anime", "Isekai", "Iyashikei", "Josei", "Mecha", "Seinen", "Shōnen", "Shōjo", "Slice of Life"),
                                "Comedy"            : ("Comedy", "Buddy Comedy", "Buddy Cop", "Dark Comedy", "Farce", "High-Concept Comedy", "Mockumentary", "Parody", "Quirky Comedy", "Raunchy Comedy", "Satire", "Screwball Comedy", "Sitcom", "Sketch Comedy", "Slapstick", "Stand-Up", "Stoner Comedy", "Teen Comedy"),
                                "Con"               : ("Caper", "Heist"),
                                "Crime"             : ("Crime", "Caper", "Cop Drama", "Drug Crime", "Film Noir", "Gangster", "Heist", "Police Procedural", "True Crime"),
                                "Disaster"          : ("Disaster"),
                                "Documentary"       : ("Documentary", "Crime Documentary", "Docuseries", "Faith & Spirituality Documentary", "Food Documentary", "History Documentary", "Military Documentary", "Music Documentary", "Nature Documentary", "Political Documentary", "Science & Technology Documentary", "Sports Documentary", "Travel Documentary"),
                                "Drama"             : ("Drama", "Biography", "Coming-of-Age", "Costume Drama", "Docudrama", "Epic", "Financial Drama", "History", "Legal Drama", "Medical Drama", "Period Drama", "Political Drama", "Prison Drama", "Psychological Drama", "Showbiz Drama", "Soap Opera", "Teen Drama", "Tragedy", "Workplace Drama", "Korean Drama", "Telenovela", "Cop Drama"),
                                "Dystopia"          : ("Dystopian Sci-Fi", "Cyberpunk"),
                                "Epic"              : ("Epic", "Action Epic", "War Epic", "Historical Epic", "Fantasy Epic", "Romantic Epic", "Sci-Fi Epic", "Western Epic"),
                                "Fantasy"           : ("Fantasy", "Dark Fantasy", "Fantasy Epic", "Fairy Tale", "Supernatural Fantasy", "Sword & Sorcery", "Teen Fantasy"),
                                "Gangster"          : ("Gangster"),
                                "Holiday"           : ("Holiday", "Holiday Animation", "Holiday Comedy", "Holiday Family", "Holiday Romance"),
                                "Horror"            : ("Horror", "B-Horror", "Body Horror", "Folk Horror", "Found Footage Horror", "Monster Horror", "Psychological Horror", "Slasher Horror", "Splatter Horror", "Supernatural Horror", "Teen Horror", "Vampire Horror", "Werewolf Horror", "Witch Horror", "Zombie Horror"),
                                "Music"             : ("Music", "Concert"),
                                "Musical"           : ("Musical", "Classic Musical", "Jukebox Musical", "Pop Musical", "Rock Musical"),
                                "Mystery"           : ("Mystery", "Bumbling Detective", "Cozy Mystery", "Hard-boiled Detective", "Suspense Mystery", "Whodunnit"),
                                "One-Man-Army"      : ("One-Person Army Action"),
                                "Romance"           : ("Romance", "Dark Romance", "Romantic Epic", "Feel-Good Romance", "Romantic Comedy", "Steamy Romance", "Teen Romance", "Tragic Romance"),
                                "Sci-Fi"            : ("Sci-Fi", "Alien Invasion", "Artificial Intelligence", "Cyberpunk", "Kaiju", "Space Sci-Fi", "Steampunk", "Time Travel"),
                                "Superhero"         : ("Superhero"),
                                "Sport"             : ("Sport", "Baseball", "Basketball", "Boxing", "Extreme Sport", "Football", "Motorsport", "Soccer", "Water Sport"),
                                "Swashbuckler"      : ("Swashbuckler"),
                                "Time Travel"       : ("Time Travel"),
                                "Thriller"          : ("Thriller", "Conspiracy Thriller", "Cyber Thriller", "Erotic Thriller", "Giallo", "Legal Thriller", "Political Thriller", "Psychological Thriller", "Serial Killer", "Spy", "Survival"),
                                "Vampire"           : ("Vampire Horror"),
                                "War"               : ("War", "War Epic"),
                                "Western"           : ("Western", "Classical Western", "Contemporary Western", "Western Epic", "Spaghetti Western")
                                }
    # This dictionary keeps track of which super_genres already has been added to the final_genres list, to avoid duplicates.
already_added_super_genre =     {
                                "Action"            : False,
                                "Adventure"         : False,
                                "Spy"               : False,
                                "Animation"         : False,
                                "Anime"             : False,
                                "Comedy"            : False,
                                "Con"               : False,
                                "Crime"             : False,
                                "Disaster"          : False,
                                "Documentary"       : False,
                                "Drama"             : False,
                                "Dystopia"          : False,
                                "Epic"              : False,
                                "Fantasy"           : False,
                                "Gangster"          : False,
                                "Holiday"           : False,
                                "Horror"            : False,
                                "Music"             : False,
                                "Musical"           : False,
                                "Mystery"           : False,
                                "One-Man-Army"      : False,
                                "Romance"           : False,
                                "Sci-Fi"            : False,
                                "Superhero"         : False,
                                "Sport"             : False,
                                "Swashbuckler"      : False,
                                "Time Travel"       : False,
                                "Thriller"          : False,
                                "Vampire"           : False,
                                "War"               : False,
                                "Western"           : False
                                }


#################################################### Functions ####################################################




# This function finds the super_genre that corrosponds with the given interest and returns it.
def find_reletive_super_genre(interest:str) -> str:
    for super_genre in super_and_sub_genre_relation:
        # This checks if the super_genre already have been added to the final_super_genre list so it doesn't add duplicate genres.
        if already_added_super_genre[super_genre]:
            pass
        else:
            # Gets the relative sub_genres (in a tuple) for the current super_genre.
            relative_sub_genres = super_and_sub_genre_relation[super_genre]

            # This means that there is more than one relative sub_genre, which means we need to iterate them.
            if type(relative_sub_genres) == tuple:
                # This compares all the sub_genres from the current super_genre with the current interest and returns the super_genre if it matches.
                for sub_genre in relative_sub_genres:
                    if interest == sub_genre:
                        print(interest, "==", sub_genre, "->", super_genre)
                        print(final_super_genres)
                        return super_genre

            # This means there is only one sub_genre, and therefore the sub_genre and super_genre is the same (sub_genre = super_genre).
            elif type(relative_sub_genres) == str:
                # This compares the sub_genre from the current super_genre with the current interest and returns the super_genre if it matches.
                if interest == relative_sub_genres:
                        print(interest, "==", sub_genre, "->", super_genre)
                        print(final_super_genres)
                        return super_genre

#################################################### HTTP Getter ##################################################
# This makes the request to a imdb api that allows us to GET data with the imdb ID.
    # imdb api link: "https://imdbapi.dev/"
h = hlib.Http(".cache")
(resp, content) = h.request("https://api.imdbapi.dev/titles/tt0172495", "GET")

# Converts the bytes recived into a python dictionary.
data_dict = json.loads(content)


#################################################### Data extraction and formatting ###############################
#Extracts and appends the title to output.
title = data_dict[keys_in_order[0]] # keys_in_order[0] = "primaryTitle"
output.append(title)

#Extracts and appends the length in hours and minutes to output.
length_in_seconds = data_dict[keys_in_order[1]] # keys_in_order[1] = "runtimeSeconds"
minutes = int(flr(length_in_seconds/60))
hours = int(flr(minutes/60))
extra_minutes = minutes - hours*60

# Concatenates the hours and minutes with letters in between and appends the movie length to output.
lenght_str = str(hours) + "h " + str(extra_minutes) + "m"
output.append(lenght_str)

# Extracts and appends relevant super_genres to output.
for interest_dict in data_dict[keys_in_order[2]]: # keys_in_order[2] = "interets"
    interest_name = interest_dict["name"]

    # This functions finds and returns the relative super_genre to the current interest.
    relative_super_genre = find_reletive_super_genre(interest_name)
    # This appends the relative super_genre to the final_super_genres.
    final_super_genres.append(relative_super_genre)
    # this sets the found super_genres relative value in the already_added_super_genre list to True.
    already_added_super_genre[relative_super_genre] = True




#################################################### Data String Export ###########################################

#robably is not gonna be used because it will write directly into the google sheets
str_output = "\t".join(output)
print(str_output)
#pyclp.copy(str_output)