#################################################### Standard Imports ###########################################################
import httplib2 as hlib
import json
#################################################### Module Imports #############################################################
from ..enums import LinkAdress


#################################################################################################################################
#################################################### HTTP Functions #############################################################
#################################################################################################################################
# This modifies the link to go through the imdb api, makes the request to the given link and return it as a python dictionary.
def http_get_request(http:hlib.Http, link:str) -> dict | str:
    """Returns a string if an error occurred, otherwise returns a dictionary"""

    # extracts the imdb id in the given link.
        # id_start finds where "/tt" occurrs in the link, which is only at the start of the id.
        # +1 to avoid the first "/" when we search for the id_end and extract the final id.
    id_start = link.find("/tt")+1
        # id_end finds the first "/" after id_start index.
    id_end = link.find("/",id_start)

    id = link[id_start:id_end]
    link = LinkAdress.ROOT_IMDB_API_TITLE.value + id

    print("IMDb http - [REQUESTING IMDB DATA]")
    # This makes the http request and gets the data as json
    (resp, content) = http.request(link, "GET")
    print(f"IMDb http - [RESPONSE RECIVED] - status: {resp["status"]}")
    # If the response status is not 200 (which means successful) it returns only the status.
    if resp["status"] != "200":
        error = f"HTTP status {resp["status"]}"
        return error
    
    # Converts the bytes recived into a python dictionary and returns it.
    data = json.loads(content)
    return data
