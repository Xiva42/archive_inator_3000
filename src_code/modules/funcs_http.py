#################################################### Standard Imports ###########################################################
import httplib2 as hlib
import json
#################################################### Module Imports #############################################################
from modules.enums import LinkAdress


#################################################################################################################################
#################################################### HTTP Functions #############################################################
#################################################################################################################################
# This modifies the link to go through the imdb api, makes the request to the given link and return it as a python dictionary.
def http_get_request(http:hlib.Http, link:str) -> dict | str:
    """Returns a string if an error occurred, otherwise returns a dictionary"""

    # extracts the imdb id in the given link.
    id_start = len(LinkAdress.ROOT_IMDB_MOVIES.value)
    id = link[id_start:id_start+9]
    link = LinkAdress.ROOT_IMDB_API_TITLE.value + id

    # This makes the http request and gets the data as json
    (resp, content) = http.request(link, "GET")
    # If the response status is not 200 (which means successful) it returns only the status.
    if resp["status"] != "200":
        error = f"HTTP status {resp["status"]}"
        return error
    
    # Converts the bytes recived into a python dictionary and returns it.
    data = json.loads(content)
    return data
