#################################################### Standard Imports ###########################################################
from enum import Enum
from functools import partial
#################################################### Module Imports #############################################################
from modules.functions import extract_link, extract_location, extract_media, extract_runtime, extract_super_genres, extract_title


#################################################################################################################################
#################################################### Enums ######################################################################
#################################################################################################################################
# Different web address roots.
class RootAdress(Enum):
    IMDB_MOVIES     = "https://www.imdb.com/title/"
    IMDB_API_TITLE  = "https://api.imdbapi.dev/titles/"

# The Different Storage location types.
class Location(Enum):
    DVD     = "DVD"
    BLU_RAY = "Blu-ray"
    SERVER  = "Server"
    OTHER   = "Other"

# The Different media types possible.
class MediaType(Enum):
    MOVIE        = "Movie"
    SERIES       = "Series"
    MOVIE_SERIES = "Movie Series"
    OTHER        = "Other"

# All color related constants for the GUI.
class GuiColor(Enum):
    # Theme
    THEME = "DarkGrey9"
    # Colors
    RED         = "Red"
    DARK_RED    = "DarkRed"
    LIGHT_GREEN = "LightGreen"
    GOLD        = "Gold"

# All keys for GUI elements, they are sortet as they are separated in the GUI.
class GuiKey(Enum):
    XIVA_LINK = 0

    IMDB_LINK = 1
    ERROR_MSG = 2

    MEDIA = 3
    MEDIA_OTHER = 4

    LOCATION_TXT = 5
    LOCATION = 6
    LOCATION_OTHER = 7

    CONFIRM = 8

    SUCCESS_FRAME = 9
    SUBJECT_MEDIA = 10

    # Extra Keys.
    ENTER_KEY = 11

# This contains the dictionary keys for the relevant data sections from the requested data_dict. (including self inserted keys.)
class DataKey(Enum):
    # Name specific keys from the IMDb request.
    TITLE      = "primaryTitle"
    RUNTIME    = "runtimeSeconds"
    INTERESTS  = "interests"
    IMDB_MEDIA = "type"

    # Self added keys to the data_dict.
        # For the location.
    LOCATION =  0
    LOCATION_COMMON = 1
    LOCATION_OTHER = 2
        # For the Media Type.
    MEDIA = 3
    MEDIA_COMMON = 4
    MEDIA_OTHER = 5


# This contains the order of data in the output as keys and the relative extract function as the value.
class Extraction(Enum):
    TITLE        = partial(extract_title)
    RUNTIME      = partial(extract_runtime)
    SUPER_GENRES = partial(extract_super_genres)
    LOCATION     = partial(extract_location)
    MEDIA        = partial(extract_media)
    IMDB_LINK    = partial(extract_link)