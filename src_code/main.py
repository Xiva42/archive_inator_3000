# In this application there is a lot of genre chaos... so to set things straight:
    # super_genre   ->  The genres wanted and is to be used in the google sheets document.
    # sub_genre     ->  The genres that IMDb have, these will all have a relative super_genres which it will translated to.
    # interest      ->  The genres the application recives with the given movie (thats what they are called in the HTTP response).
#################################################### Standard Imports ###########################################################
import httplib2 as hlib
import FreeSimpleGUI as sg
import pyperclip as pyclp
import webbrowser as webb
#################################################### Module Imports #############################################################
from modules import functions as f
from modules import data_fields as d
from modules import gui_elements as gui
from modules.enums import *


#################################################################################################################################
#################################################### Application Loop ###########################################################
#################################################################################################################################
# Initiates the http class.
h = hlib.Http(".cache")

#Initates the window with the gui_layout list.
window = sg.Window("The Archive Inator 3000", gui.window_layout, keep_on_top=True, finalize=True)
# Enables the enter key to act as a "confirm" button.
window.bind("<Return>", GuiKey.ENTER_KEY)

# The main application loop which reads events and inputs into the GUI and makes operations with the input.
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break


    elif event == GuiKey.XIVA_LINK:
        webb.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ",2)


    elif event == GuiKey.MEDIA:
        d.media_type = values[GuiKey.MEDIA]
        window[GuiKey.LOCATION_TXT].update(f"Select the {d.media_type} \"storage location\":")

        if values[GuiKey.MEDIA] == MediaType.OTHER.value:
            window[GuiKey.MEDIA_OTHER].update(visible=True)
            
        elif window[GuiKey.MEDIA_OTHER].visible:
            window[GuiKey.MEDIA_OTHER].update(visible=False)


    elif event == GuiKey.LOCATION:
        if values[GuiKey.LOCATION] == Location.OTHER.value:
            window[GuiKey.LOCATION_OTHER].update(visible=True)
            
        elif window[GuiKey.LOCATION_OTHER].visible:
            window[GuiKey.LOCATION_OTHER].update(visible=False)            


    elif event == GuiKey.CONFIRM or event == GuiKey.ENTER_KEY:
        # try:
            ######################################## HTTP Getter ################################################################
            # This makes the request to a imdb api that allows us to GET data with the user given imdb ID.
            given_link = values[GuiKey.IMDB_LINK]
            data_dict = f.http_get_request(h, given_link)
            
            ######################################## Data extraction and formatting #############################################
            
            # This runs all the extraction functions which extracts the wanted data and appends it in the given extraction_order.
            for func in Extraction:

                if func == Extraction.LOCATION:
                    # This inserts the user given "location" for the media into the data_dict.
                    data_dict[DataKey.LOCATION] = {DataKey.LOCATION_COMMON: values[GuiKey.LOCATION], DataKey.LOCATION_OTHER: values[GuiKey.LOCATION_OTHER]}
                elif func == Extraction.MEDIA:
                    # This inserts the user given "media" into the data_dict.
                    data_dict[DataKey.MEDIA] = {DataKey.MEDIA_COMMON: values[GuiKey.MEDIA], DataKey.MEDIA_OTHER: values[GuiKey.MEDIA_OTHER]}

                func.value(data_dict)

            ######################################## Data String Export #########################################################
            # Joins the output list with tab as separator so it can be pasted easily into google sheet.
            str_output = "\t".join(d.output)
            pyclp.copy(str_output)

            ######################################## Success reset ##############################################################
            # Hides the Error message if it was there.
            window[GuiKey.ERROR_MSG].update(visible=False)
            # Removes the link from the input box.
            window[GuiKey.IMDB_LINK].update(value="")
            # shows the retrieved Movie's name in the success_frame.
            window[GuiKey.SUBJECT_MEDIA].update(value=d.output[0])
            # Displays the success_frame.
            window[GuiKey.SUCCESS_FRAME].update(visible=True)
            # Empties the output list.
            d.output = []
        
        # If the link given didnt work or wasn't a link this makes sure the program doesn't crash.
        # except Exception as e:
        #     print("Error: ", e)
        #     window[GuiKey.ERROR_MSG].update(visible=True)

window.close()