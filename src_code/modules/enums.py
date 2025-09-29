#################################################### Standard Imports ###########################################################
from enum import Enum


#################################################################################################################################
#################################################### Enums ######################################################################
#################################################################################################################################
# Different web addresses.
class LinkAdress(Enum):
    # Root web addresses
    ROOT_IMDB_MOVIES     = "https://www.imdb.com/title/"
    ROOT_IMDB_API_TITLE  = "https://api.imdbapi.dev/titles/"

    # Other link adresses
    XIVA_WEBSITE_LINK = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    ARCHIVE_SPREADSHEET_LINK = "https://docs.google.com/spreadsheets/d/12CpXUYHlsGttUsxaArsBuJx0K_oXVFNgvtWUv_g48Nk"

# The Different Storage location types.
class Location(Enum):
    DVD     = "DVD"
    BLU_RAY = "Blu-ray"
    SERVER  = "Server"
    OTHER   = "Other"

# The Different media types possible.
class MediaType(Enum):
    INDEP_MOVIE  = "Indep. Movie"
    MOVIE_SERIES = "Movie-Series"
    SERIES       = "Series"
    OTHER        = "Other"

# All color related constants for the GUI.
class GuiColor(Enum):
    # Theme
    THEME = "DarkGrey9"
    # Colors
    RED         = "Red"
    DARK_RED    = "DarkRed"
    LIGHT_GREEN = "LightGreen"
    LIGHT_BLUE  = "LightBlue"
    GOLD        = "Gold"

# All keys for GUI elements, they are sortet as they are separated in the GUI.
class GuiKey(Enum):
    XIVA_LINK = 0

    IMDB_LINK = 1
    HTTP_ERROR_MSG = 2
    HTTP_ERROR_TYPE_MSG = 3

    MEDIA_INDEP_MOVIE   = MediaType.INDEP_MOVIE.value
    MEDIA_MOVIE_SERIES  = MediaType.MOVIE_SERIES.value
    MEDIA_SERIES        = MediaType.SERIES.value
    MEDIA_OTHER         = MediaType.OTHER.value
    MEDIA_OTHER_INPUT   = 8

    LOCATION_TXT        = 9
    LOCATION_COMMON     = 10
    LOCATION_OTHER      = 11

    CONFIRM             = 12

    GENERAL_ERROR_MSG   = 13

    SUCCESS_FRAME       = 14
    SUBJECT_MEDIA       = 15
    ARCHIVE_SIZE        = 16
    ARCHIVE_LINK        = 17

    # Extra Keys.
    ENTER_KEY           = 18


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
        # For the Media Type.
    MEDIA = 3