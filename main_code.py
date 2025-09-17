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

#################################################### Variables ####################################################
output = []

#################################################### Tuples ####################################################
keys_in_order = ("primaryTitle", "runtimeSeconds", "interests", "link", "location")

#################################################### Functions ####################################################
def extract_and_append_to_output(dict_key = str, from_dict = dict) -> None:
    key_value = from_dict[dict_key]
    output.append(key_value)


#################################################### HTTP Getter ##################################################
# This makes the request to a imdb api that allows us to GET data with the imdb ID.
# imdb api link: "https://imdbapi.dev/"
h = hlib.Http(".cache")
(resp, content) = h.request("https://api.imdbapi.dev/titles/tt0172495", "GET")

# Converts the bytes recived into a python dictionary 
data_dict = json.loads(content)







#robably is not gonna be used because it will write directly into the google sheets
str_output = "\t".join(output)
print(str_output)
#pyclp.copy(str_output)