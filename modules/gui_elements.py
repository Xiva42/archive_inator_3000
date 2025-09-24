#################################################### Standard Imports #############################################
import FreeSimpleGUI as sg
#################################################### Module Imports ###############################################
from modules import data_fields as d


###################################################################################################################
#################################################### GUI Elements #################################################
###################################################################################################################
#Sets the GUI theme
sg.theme(d.APPLICATION_THEME)
    # This defines what the intro column contains and is called in the window_layout.
intro_column_layout = [
                [sg.Text("WELCOME", font=("Impact", "20"))],
                [sg.Text("to", font=("Helvetica", "10")), sg.Text("Xiva's", font=("Helvetica", "10", "underline"), enable_events=True, tooltip="Link to Xiva's Website :)", key="-xiva_link-")],
                [sg.Text("ARCHIVE INATOR 3000", font=("Impact", "40"), background_color="DarkRed", border_width=10)]
                      ]
    # This defines what the error column contains and is called in the window_layout.
error_column_layout = [
                
                      ]    

    # This defines what the success frame contains and is called in the window_layout.
success_frame_layout = [
                [sg.Text("The wanted data on:", text_color=d.COLOR_LIGHT_GREEN), sg.Text("", key="-subject_movie-", text_color=d.COLOR_GOLD)],
                [sg.Text("is now in your clipboard", text_color=d.COLOR_LIGHT_GREEN)],
                [sg.Text("You can repeat the process if needed :)")]
                       ]

    # Defines all the elements in the window_layout (main window).
window_layout = [
                [sg.Push(), sg.Column(intro_column_layout, element_justification="Center"), sg.Push()],
                [sg.HorizontalSeparator()],
                [sg.Text("Insert the IMDb link into the box below")],
                [sg.Input(key="-link-", expand_x=True)],
                [sg.Text("Error: Not a valid link. It should look something like: 'https://www.imdb.com/title/tt...'", text_color=d.COLOR_RED, visible=False, key="-error_msg-")],

                [sg.HorizontalSeparator()],
                [sg.Text("Choose what we have this movie \"stored\" on :)")],
                [sg.Combo(["DVD", "Blu-ray", "Server", "Other"], default_value="DVD", readonly=True, enable_events=True, key="-location-"),
                sg.Input("", size=(15,1), visible=False, key="-other_location-", expand_x=True)],
                [sg.HorizontalSeparator()],
                
                [sg.Push(), sg.Button("Comfirm", enable_events=True, key="-confirm-"), sg.Push()],
                [sg.HorizontalSeparator()],
                [sg.Push(), sg.pin(sg.Frame("Success!", success_frame_layout, title_color=d.COLOR_LIGHT_GREEN, element_justification="Center", visible=False, key="-success_frame-")), sg.Push()]
                ]