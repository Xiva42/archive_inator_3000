#################################################### Standard Imports ###########################################################
import httplib2 as hlib
import json
from math import floor as flr
# (Module import is at the bottom of the file)


#################################################################################################################################
#################################################### Functions ##################################################################
#################################################################################################################################

#################################################### Other Functions ############################################################
# This modifies the link to go through the imdb api, makes the request to the given link and return it as a python dictionary.
def http_get_request(http:hlib.Http, link:str) -> dict:
    # Finds the imdb id in the given link.
    id_start = len(RootAdress.IMDB_MOVIES.value)
    id = link[id_start:id_start+9]
    link = RootAdress.IMDB_API_TITLE.value + id

    # This makes the http request and gets the data as json.
    (resp, content) = http.request(link, "GET")
    # Converts the bytes recived into a python dictionary.
    data = json.loads(content)
    return data

    

# This function finds the super_genre that corrosponds with the given interest and returns it.
def find_reletive_super_genre(interest:str) -> str:
    for super_genre in d.super_and_sub_genre_relation:
        # This checks if the super_genre already have been added to the final_super_genre list so it doesn't add duplicate genres.
        if d.already_added_super_genre[super_genre]:
            pass
        else:
            # Gets the relative sub_genres (in a tuple) for the current super_genre.
            relative_sub_genres = d.super_and_sub_genre_relation[super_genre]

            # This means that there is more than one relative sub_genre, which means we need to iterate them.
            if type(relative_sub_genres) == tuple:
                # This compares all the sub_genres from the current super_genre with the current interest and returns the super_genre if it matches.
                for sub_genre in relative_sub_genres:
                    if interest == sub_genre:
                        return super_genre

            # This means there is only one sub_genre, and therefore the sub_genre and super_genre is the same (sub_genre = super_genre).
            elif type(relative_sub_genres) == str:
                # This compares the sub_genre from the current super_genre with the current interest and returns the super_genre if it matches.
                if interest == relative_sub_genres:
                        return super_genre

#################################################### Extraction Functions #######################################################
    #This function extracts and appends the title to output.
def extract_title(src:dict) -> None:
    title = src[DataKey.TITLE.value]
    d.output.append(title)

    #This function extracts and appends the length in hours and minutes to output.
def extract_runtime(src:dict) -> None:
    length_in_seconds = src[DataKey.RUNTIME.value]
    minutes = int(flr(length_in_seconds/60))
    hours = int(flr(minutes/60))
    extra_minutes = minutes - hours*60

    # Concatenates the hours and minutes with letters in between and appends the movie length to output.
    lenght_str = str(hours) + "h " + str(extra_minutes) + "m"
    d.output.append(lenght_str)

    # Extracts and appends relevant super_genres to output.
def extract_super_genres(src:dict) -> None:
    for interest_dict in src[DataKey.INTERESTS.value]:
        interest_name = interest_dict["name"]

        # This functions finds and returns the relative super_genre to the current interest.
        relative_super_genre = find_reletive_super_genre(interest_name)
        if relative_super_genre != None:
            # this sets the found super_genres relative value in the already_added_super_genre list to True.
            d.already_added_super_genre[relative_super_genre] = True
            # This appends the relative super_genre to the final_super_genres.
            d.final_super_genres.append(relative_super_genre)

    # This formats and appends the list of super_genres to the output list.
    genre_str = ", ".join(d.final_super_genres)
    d.output.append(genre_str)

    # Extracts and appends the chosen location of the movie.
def extract_location(src:dict) -> None:
    loc = src[DataKey.LOCATION][DataKey.LOCATION_COMMON]
    # if the selected location was other, it takes the other_location value instead.
    if loc == Location.OTHER.value:
        loc = src[DataKey.LOCATION][DataKey.LOCATION_OTHER]
    d.output.append(loc)

    # Extracts and appends the media it is in.
def extract_media(src:dict) -> None:
    media = src[DataKey.MEDIA][DataKey.MEDIA_COMMON]
    # If the selected media is other, it takes the other_type value instead.
    if media == MediaType.OTHER.value:
        media = src[DataKey.MEDIA][DataKey.MEDIA_OTHER]
    d.output.append(media)

    # Extracts and appends the link for this movies imdb site.
def extract_link(src:dict) -> None:
    movie_id = src["id"]
    imdb_link = RootAdress.IMDB_MOVIES.value + movie_id
    d.output.append(imdb_link)

#################################################### Module Imports ###############################################
from modules import data_fields as d
from modules.enums import *