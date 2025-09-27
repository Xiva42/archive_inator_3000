# In this application there is a lot of genre chaos... so to set things straight:
    # super_genre   ->  The genres wanted and is to be used in the google sheets document.
    # sub_genre     ->  The genres that IMDb have, these will all have a relative super_genres which it will translated to.
    # interest      ->  The genres the application recives with the given movie (thats what they are called in the HTTP response).
#################################################### Standard Imports ###########################################################
import httplib2 as hlib
import FreeSimpleGUI as sg
import webbrowser as webb

#################################################### Module Imports #############################################################
# Functions:
from modules import funcs_extract as f_ext
from modules import funcs_http as f_htt
from modules import funcs_sheets_comm as f_shc
# Enums for constants:
from modules.enums import GuiKey, Location, MediaType, DataKey, LinkAdress
# Variables, lists, and dictionaries:
from modules import data_fields as d
# window layout and theme configurations for the GUI:
from modules import gui_elements as gui


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
        webb.open(LinkAdress.XIVA_WEBSITE_LINK.value, 2)

    elif event == GuiKey.ARCHIVE_LINK:
        webb.open(LinkAdress.ARCHIVE_SPREADSHEET_LINK.value, 2)

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
        try:
            ######################################## HTTP Getter ################################################################
            # This makes the request to a imdb api that allows us to GET data with the user given imdb ID.
            given_link = values[GuiKey.IMDB_LINK]
            data_dict = f_htt.http_get_request(h, given_link)
            
            ######################################## Data extraction and formatting #############################################
            # This inserts the user given "location" for the media into the data_dict.
            data_dict[DataKey.LOCATION] = {DataKey.LOCATION_COMMON: values[GuiKey.LOCATION], DataKey.LOCATION_OTHER: values[GuiKey.LOCATION_OTHER]}
            # This inserts the user given "media" into the data_dict.
            data_dict[DataKey.MEDIA] = {DataKey.MEDIA_COMMON: values[GuiKey.MEDIA], DataKey.MEDIA_OTHER: values[GuiKey.MEDIA_OTHER]}
    
            # This runs all the extraction functions which extracts the wanted data from the given data_dict and appends it in the given extraction_order.
            for func in f_ext.Extraction:
                func.value(data_dict)

            ######################################## Data Export To Sheets Document #############################################
            # This connects to the google spreadsheet which is the archive inators storage.
            archive_spreadsheet = f_shc.connect_to_sheet()
            # This writes the output data to the connected spreadsheet, and returns the new archive size.
            archive_size = f_shc.write_to_sheet(archive_spreadsheet, [d.output])
            

            ######################################## Success reset ##############################################################
            # Hides the Error message if it was there.
            window[GuiKey.ERROR_MSG].update(visible=False)
            # Removes the link from the input box.
            window[GuiKey.IMDB_LINK].update(value="")
            # Shows the retrieved Movie's name in the success_frame.
            window[GuiKey.SUBJECT_MEDIA].update(value=d.output[0])
            # Shows the current amount of archived media in the archive spreadsheet.
            window[GuiKey.ARCHIVE_SIZE].update(value=str(archive_size))
            # Displays the success_frame.
            window[GuiKey.SUCCESS_FRAME].update(visible=True)
            # Empties the output list.
            d.output = []
        
        # If the link given didnt work or wasn't a link this makes sure the program doesn't crash.
        except Exception as e:
            print("Error: ", e)
            window[GuiKey.ERROR_MSG].update(visible=True)

window.close()