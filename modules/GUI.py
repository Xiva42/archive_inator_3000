import FreeSimpleGUI as sg

sg.theme("DarkGrey5")

link_promt = [

    [sg.Titlebar("The Archive Inator 3000")],
    [sg.Text("Insert the IMDb link into the box below")],
    [sg.Input(key="-link-")],
    [sg.Text("Error: Not a valid link", visible=False, text_color="red", key="-error_msg-")],

    [sg.HorizontalSeparator()],
    [sg.Text("")],

    [sg.Text("Choose what we have this movie \"stored\" on :)")],
    [sg.Combo(["DVD", "Blu-ray", "Server", "Other"], default_value="DVD", readonly=True, enable_events=True, key="-location-"),
     sg.Input(size=(15,1), visible=False, key="-other_location-")],
    
    [sg.Text("")],
    [sg.Push(), sg.Button("Comfirm", enable_events=True, key="-confirm-"),  sg.Push()],
    [sg.Frame("Success!",
            [[sg.Text("The wanted data on:", text_color="LightGreen"),
             sg.Text("", text_color="Gold", key="-subject_movie-")],
             [sg.Text("is now in your clipboard", text_color="Green")],
             [sg.Text("You can repeat the process if needed :)")]
            ], title_color="LightGreen", visible=False, key="-success_frame-")]
]

window = sg.Window("The Archive Inator 3000", link_promt)

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
        # Go get the data and copy it into the clipboard



        # Removes the link from the input box
        window["-link-"].update(value="")
        #
        window["-subject_movie-"].update(value="THE MOVIE")
        # Displays the success_frame.
        window["-success_frame-"].update(visible=True)

window.close()