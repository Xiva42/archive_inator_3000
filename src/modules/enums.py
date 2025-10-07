#################################################### Standard Imports ###########################################################
from enum import Enum


#################################################################################################################################
#################################################### Enums ######################################################################
#################################################################################################################################
# Different web addresses.
class LinkAdress(Enum):
    # Root web addresses
    ROOT_IMDB_MEDIAS     = "https://www.imdb.com/title/"
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
    MOVIE        = "Movie"
    ANIMATION    = "Animation"
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

    MEDIA_COMMON        = 4
    MEDIA_OTHER         = 5

    LOCATION_COMMON     = 7
    LOCATION_OTHER      = 8

    CONFIRM             = 9

    GENERAL_ERROR_MSG   = 10

    SUCCESS_FRAME       = 11
    SUBJECT_MEDIA       = 12
    ARCHIVE_SIZE        = 13
    ARCHIVE_LINK        = 14

    # Extra Keys.
    ENTER_KEY           = 15


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
    MEDIA = 1