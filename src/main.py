# In this application there is a lot of genre chaos... so to set things straight:
    # super_genre   ->  The genres format wanted and is to be used in the google sheets document.
    # sub_genre     ->  The genres that IMDb have, these will all have a relative super_genres which it will translated to.
    # interest      ->  The genres the application recives with the given movie (thats what they are called in the HTTP response).
#################################################### Standard Imports ###########################################################
import httplib2 as hlib
import FreeSimpleGUI as sg
import webbrowser as webb

#################################################### Module Imports #############################################################
# Functions:
from modules import all_funcs as f
# Variables, lists, and dictionaries:
from modules import data_fields as d
# window layout and theme configurations for the GUI:
from modules import gui_elements as gui
# Enums for constants:
from modules.enums import GuiKey, Location, MediaType, DataKey, LinkAdress


#################################################################################################################################
#################################################### Application Loop ###########################################################
#################################################################################################################################
# Initiates the http class.
h = hlib.Http(".cache")

# This connects to the google spreadsheet which is the archive inators storage.
archive_spreadsheet = f.sheet.connect_to_sheet()

#Initates the window with the gui_layout list.
window = sg.Window("The Archive Inator 3000", gui.window_layout, keep_on_top=True, finalize=True)
# Enables the enter key to act as a "confirm" button.
window.bind("<Return>", GuiKey.ENTER_KEY)

# The main application loop which reads events and inputs into the GUI and makes operations with the input.
while True:
    event, values = window.read()
    print(event, values)
    # If the window is closed, break out of the loop.
    if event == sg.WIN_CLOSED:
        break

    # If the xiva text is pressed, open the XIVA_WEBSITE_LINK.
    elif event == GuiKey.XIVA_LINK:
        webb.open(LinkAdress.XIVA_WEBSITE_LINK.value, 2)
    # If the "Movie Archive" text in the success message is pressed open the Archive Spreadsheet.
    elif event == GuiKey.ARCHIVE_LINK:
        webb.open(LinkAdress.ARCHIVE_SPREADSHEET_LINK.value, 2)

    # If a different media is selected in the media dropdown menu, hide/unhide the "other" text input box.
        #1 If the selected media is "other", unhide the text inputbox.
        #2 If the the selected media is anything else than "other" and the "other" text input is visible, hide it.
    elif event == GuiKey.MEDIA_COMMON:
        if values[GuiKey.MEDIA_COMMON] == MediaType.OTHER.value: #1
            window[GuiKey.MEDIA_OTHER].update(visible=True)

        elif window[GuiKey.MEDIA_OTHER].visible: #2
            window[GuiKey.MEDIA_OTHER].update(visible=False)

    # If a different location is selected in the location dropdown menu, hide/unhide the "other" text input box.
        #1 If the selected location is "other", unhide the text inputbox.
        #2 If the the selected location is anything else than "other" and the "other" text input is visible, hide it.   
    elif event == GuiKey.LOCATION_COMMON:
        if values[GuiKey.LOCATION_COMMON] == Location.OTHER.value: #1
            window[GuiKey.LOCATION_OTHER].update(visible=True)

        elif window[GuiKey.LOCATION_OTHER].visible: #2
            window[GuiKey.LOCATION_OTHER].update(visible=False)            

    # If the confirm button or the enter key is pressed:
        #1 Initiate the HTTP data getter.
        #2 Extract the wanted data.
        #3 Connect to the google spreadsheet and write it to the first empty row.
        #4 Reset the application so it is ready for the next promt.
    elif event == GuiKey.CONFIRM or event == GuiKey.ENTER_KEY:
        # try:
            for super_genre in range(1):
                ######################################## >1< HTTP Getter ########################################################
                # This makes the request to a imdb api that allows us to GET data with the user given imdb ID.
                given_link = values[GuiKey.IMDB_LINK]
                data = f.http.http_get_request(h, given_link)
                
                # This checks if the data is a string and therefor an error msg and displays it.
                if type(data) == str:
                    error = f"Error Type: {data}"
                    print(error)
                    window[GuiKey.HTTP_ERROR_MSG].update(visible=True)
                    window[GuiKey.HTTP_ERROR_TYPE_MSG].update(visible=True)
                    window[GuiKey.HTTP_ERROR_TYPE_MSG].update(value=error)
                    break
                
                # Calls the data for data_dict, because we now know its a dictionary.
                data_dict = data

                ######################################## >2< Data extraction and formatting #####################################
                # This inserts the user given "media" into the data_dict.
                data_dict[DataKey.MEDIA] = {GuiKey.MEDIA_COMMON: values[GuiKey.MEDIA_COMMON],
                                            GuiKey.MEDIA_OTHER: values[GuiKey.MEDIA_OTHER]
                                           }
                # This inserts the user given "location" for the media into the data_dict.
                data_dict[DataKey.LOCATION] = {GuiKey.LOCATION_COMMON: values[GuiKey.LOCATION_COMMON],
                                               GuiKey.LOCATION_OTHER: values[GuiKey.LOCATION_OTHER]
                                              }
        
                # This runs all the extraction functions which extracts the wanted data from the given data_dict and appends it in the given extraction_order.
                for func in f.ex.Extraction:
                    func.value(data_dict)

                ######################################## >3< Data Export To Sheets Document #####################################
                # This writes the output data to the connected spreadsheet, and returns the new archive size.
                archive_size = f.sheet.write_to_sheet(archive_spreadsheet, [d.output])
                

                ######################################## >4< Success reset ######################################################
                # Hides all error messages if they were there.
                window[GuiKey.HTTP_ERROR_MSG].update(visible=False)
                window[GuiKey.HTTP_ERROR_TYPE_MSG].update(visible=False)
                window[GuiKey.GENERAL_ERROR_MSG].update(visible=False)
                # Removes the link from the input box.
                window[GuiKey.IMDB_LINK].update(value="")
                # Shows the retrieved Movie's name in the success_frame.
                window[GuiKey.SUBJECT_MEDIA].update(value=d.output[0])
                # Shows the current amount of archived media in the archive spreadsheet.
                window[GuiKey.ARCHIVE_SIZE].update(value=str(archive_size))
                # Displays the success_frame.
                window[GuiKey.SUCCESS_FRAME].update(visible=True)
                # Empties the output and final genres lists.
                d.output = []
                # Resets the already added super genres dictionary.
                for super_genre in d.already_added_super_genre:
                    d.already_added_super_genre[super_genre] = False
        
        # # If the link given didnt work or wasn't a link this makes sure the program doesn't crash.
        # except Exception as e:
        #     error = f"An error occurred: {e}"
        #     print(error)
        #     window[GuiKey.GENERAL_ERROR_MSG].update(visible=True)
        #     window[GuiKey.GENERAL_ERROR_MSG].update(value=error)

window.close()