# In this application there is a lot of genre chaos... so to set things straight:
    # super_genre   ->  The genres wanted and is to be used in the google sheets document.
    # sub_genre     ->  The genres that IMDb have, these will all have a relative super_genres which it will translated to.
    # interest      ->  The genres the application recives with the given movie (thats what they are called in the HTTP response).
#################################################### Standard Imports #############################################
import httplib2 as hlib
import FreeSimpleGUI as sg
import pyperclip as pyclp
#################################################### Module Imports ###############################################
from modules import functions as f
from modules import data_fields as d


###################################################################################################################
#################################################### Application Loop #############################################
###################################################################################################################
# Initiates the http class.
h = hlib.Http(".cache")


#Initates the window with the gui_layout list.
window = sg.Window("The Archive Inator 3000", d.window_layout, finalize=True)

while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED:
        break

    elif event == "-location-":
        if values["-location-"] == "Other":
            window["-other_location-"].update(visible=True)
            
        elif window["-other_location-"].visible:
            window["-other_location-"].update(visible=False)            

    elif event == "-confirm-":
        try:
            ######################################## HTTP Getter ##################################################
            # This makes the request to a imdb api that allows us to GET data with the user given imdb ID.
            given_link = values["-link-"]
            data_dict = f.http_get_request(h, given_link)
            
            ######################################## Data extraction and formatting ###############################
            # This inserts the user given "location" for the movie into the data_dict.
            data_dict["storageLocation"] = {"location": values["-location-"], "other_location": values["-other_location-"]}

            # This runs all the extraction functions which extracts the wanted data and appends it in the given extraction_order.
            for i in d.extracton_order:
                d.extracton_order[i](data_dict)

            ######################################## Data String Export ###########################################
            # Joins the output list with tab as separator so it can be pasted easily into google sheet.
            str_output = "\t".join(d.output)
            pyclp.copy(str_output)

            ######################################## Success reset ###############################################
            # Hides the Error message if it was there.
            window["-error_msg-"].update(visible=False)
            # Removes the link from the input box.
            window["-link-"].update(value="")
            # shows the retrieved Movie's name in the success_frame.
            window["-subject_movie-"].update(value=d.output[0])
            # Displays the success_frame and _separator.
            #window["-success_frame-"].update(visible=True)
            window["-success_column-"].update(visible=True)
        
        # If the link given didnt work or wasn't a link this makes sure the program doesn't crash.
        except Exception as e:
            print(e)
            window["-error_msg-"].update(visible=True)

window.close()