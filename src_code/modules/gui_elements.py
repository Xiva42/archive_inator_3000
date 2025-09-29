#################################################### Standard Imports ###########################################################
import FreeSimpleGUI as sg

#################################################### Module Imports #############################################################
from modules.enums import GuiColor, GuiKey, Location, MediaType

#################################################################################################################################
#################################################### GUI Functions ##############################################################
#################################################################################################################################
# This disables and clears a target checkbox if the active checkbox is checked, else it enables the target checkbox.
    #1 If there is given two active_checkboxes in a tuple it checks if the first is checked and passes that one as the active_checkbox.
    #2 Else it just passes the second because it will be checked in the next if statement.
def checkbox_availability(window: sg.Window, values:dict[GuiKey,any], active_checkbox_ids: GuiKey, target_checkbox_id: GuiKey) -> None:
    if type(active_checkbox_ids) == tuple: #1
        if values[active_checkbox_ids[0]]:
            active_checkbox_ids = active_checkbox_ids[0] 
        else: #2
            active_checkbox_ids = active_checkbox_ids[1]

    if values[active_checkbox_ids]:
        window[target_checkbox_id].update(disabled=True)
        window[target_checkbox_id].update(value=False)
    else:
        window[target_checkbox_id].update(disabled=False)


#################################################################################################################################
#################################################### GUI Elements ###############################################################
#################################################################################################################################
#Sets the GUI theme
sg.theme(GuiColor.THEME.value)
    # This defines what the intro column contains and is called in the window_layout.
intro_column_layout = [
                [sg.Text("WELCOME", font=("Impact", "20"))],
                [sg.Text("to", font=("Helvetica", "10")), sg.Text("Xiva's", font=("Helvetica", "10", "underline"), enable_events=True, tooltip="Link to Xiva's Website :)", key=GuiKey.XIVA_LINK)],
                [sg.Text("ARCHIVE INATOR 3000", font=("Impact", "40"), background_color=GuiColor.DARK_RED.value, border_width=10)]
                      ]

    # This defines what the success frame contains and is called in the window_layout.
success_frame_layout = [
                [sg.Text("The wanted data on:", text_color=GuiColor.LIGHT_GREEN.value, ), sg.Text("", text_color=GuiColor.GOLD.value, key=GuiKey.SUBJECT_MEDIA,)],
                [sg.Text("Is now in:", text_color=GuiColor.LIGHT_GREEN.value), sg.Text("The Movie Archive", font=("Helvetica", "10", "underline"), enable_events=True, tooltip="Link to \"The Movie Archive\" Google Sheets", text_color=GuiColor.LIGHT_BLUE.value, key=GuiKey.ARCHIVE_LINK)],
                [sg.Text("With a total of:", text_color=GuiColor.LIGHT_GREEN.value), sg.Text("", text_color=GuiColor.GOLD.value, key=GuiKey.ARCHIVE_SIZE,), sg.Text("archived media", text_color=GuiColor.LIGHT_GREEN.value)],
                [sg.Text("You can repeat the process if needed :)")]
                       ]

    # Defines all the elements in the window_layout (main window).
window_layout = [
                [sg.Push(), sg.Column(intro_column_layout, element_justification="Center"), sg.Push()],
                [sg.HorizontalSeparator()],
                [sg.Text("Insert the IMDb link into the box below:")],
                [sg.Input(key=GuiKey.IMDB_LINK, expand_x=True)],
                [sg.pin(sg.Text("Error: Not a valid link. It should look something like: \"https://www.imdb.com/title/tt...\"", text_color=GuiColor.RED.value, visible=False, key=GuiKey.HTTP_ERROR_MSG))],
                [sg.pin(sg.Text("", text_color=GuiColor.RED.value, visible=False, key=GuiKey.HTTP_ERROR_TYPE_MSG))],

                [sg.HorizontalSeparator()],
                [sg.Text("Select the media:")],
                [sg.Checkbox(MediaType.INDEP_MOVIE.value, default=True, enable_events=True, key=GuiKey.MEDIA_INDEP_MOVIE)],
                [sg.Checkbox(MediaType.MOVIE_SERIES.value, enable_events=True, key=GuiKey.MEDIA_MOVIE_SERIES)],
                [sg.Checkbox(MediaType.SERIES.value, disabled=True, enable_events=True, key=GuiKey.MEDIA_SERIES)],
                [sg.Checkbox(MediaType.OTHER.value, enable_events=True, key=GuiKey.MEDIA_OTHER), sg.Input("", size=(15,1), visible=False, key=GuiKey.MEDIA_OTHER_INPUT, expand_x=True)],
                
                [sg.HorizontalSeparator()],
                [sg.Text(f"Select the media \"storage location\":", key=GuiKey.LOCATION_TXT)],
                [sg.Combo([Location.DVD.value, Location.BLU_RAY.value, Location.SERVER.value, Location.OTHER.value], default_value=Location.DVD.value, readonly=True, enable_events=True, key=GuiKey.LOCATION_COMMON),
                 sg.Input("", size=(15,1), visible=False, key=GuiKey.LOCATION_OTHER, expand_x=True)],
                
                [sg.HorizontalSeparator()],
                [sg.Push(), sg.Button("Comfirm", enable_events=True, key=GuiKey.CONFIRM), sg.Push()],
                [sg.HorizontalSeparator()],

                [sg.pin(sg.Text("", text_color=GuiColor.RED.value, visible=False, key=GuiKey.GENERAL_ERROR_MSG))],
                [sg.Push(), sg.pin(sg.Frame("Success!", success_frame_layout, title_color=GuiColor.LIGHT_GREEN.value, element_justification="Center", visible=False, key=GuiKey.SUCCESS_FRAME)), sg.Push()]
                ]
