from pypresence import Presence #Library Importing
import time
import time
from time import mktime
import psutil    
import win32gui
w=win32gui #Initializing win32gui

client_id = 'yeah this is not going on github sorry...'  #Client ID for HitFilm Express
RPC = Presence(client_id) #Setting up RPC connection

RPC.connect() #Connecting to RPC

while True: #Main Loop
    print("its working")
    if ("HitFilmExpress.exe" in (p.name() for p in psutil.process_iter())): #Checks if the program is runing
        start_time = mktime(time.localtime()) #Sets start time
        while ("HitFilmExpress.exe" in (p.name() for p in psutil.process_iter())): #While the user is still in HitFilm Express
            status = ""
            state = ""
            if (".hfp" in w.GetWindowText (w.GetForegroundWindow())): ##If the user is in the HitFilm window
                state = "In a File" 
                status = w.GetWindowText (w.GetForegroundWindow()).split("-",1)[0]
            elif ( w.GetWindowText (w.GetForegroundWindow()) == "HitFilm Express"): ##If the user is on the homescreen
                state = "Idling"
                status = "Homescreen"
            elif ("Untitled Project" in w.GetWindowText (w.GetForegroundWindow())): #If the user is in an untitled project
                state = "In a File" 
                status = "Untitled Project"
            else: ##If the user isn't even in the app in the first place
                state = "Idling"
                status = "Not even in the app lmao"
            (RPC.update(state=status, details=state, large_image="hitfilm", small_image="fxhome", small_text = "FXHome", large_text="HitFilm", start=start_time)) #Sending data
    RPC.clear() #If the while loop above does not (Meaning the user isn't in the app) run, clear the RPC (therefore removing the discord rich status)
