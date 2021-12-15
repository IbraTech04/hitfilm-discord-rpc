from pypresence import Presence #Library Importing
import time
import time
from time import mktime
import psutil    
import win32gui

w=win32gui #Initializing win32gui
client_id = '860354715886682112'  #Client ID for HitFilm Express
clientIDPro = '860354715886682112' #Client ID for HitFilm Pro
RPC = Presence(client_id) #Setting up RPC connection
RPCPro = Presence(clientIDPro) #Setting up RPC connection
counter = 0
RPC.connect() #Connecting to RPC
RPCPro.connect() #Connecting to RPC
mouse = win32gui.GetCursorPos()
print(mktime(time.localtime()))
while True: #Main Loop
    if ("HitFilmExpress.exe" in (p.name() for p in psutil.process_iter())): #Checks if the program is runing
        start_time = mktime(time.localtime()) #Sets start time
        #start_time = 1535857560.0 #Sets start time
        while ("HitFilmExpress.exe" in (p.name() for p in psutil.process_iter())): #While the user is still in HitFilm Express
            prevMouse = mouse
            mouse = win32gui.GetCursorPos()
            if (prevMouse == mouse):
                counter = counter + 1
            else:
                counter = 0
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
            elif ("Open Project" in w.GetWindowText (w.GetForegroundWindow())): #If the user is in an untitled project
                state = "Opening a Project"
                status = "Loading files"
            elif ("Relink Files" in w.GetWindowText (w.GetForegroundWindow())): #If the user is in an untitled project
                state = "Relinking files"
                status = "Probably deleted something"
            else: ##If the user isn't even in the app in the first place
                state = "Idling"
                status = "Not even in the app lmao"
            if (counter >= 100):
                status = "Idling"
            (RPC.update(state=status, details=state, large_image="hitfilmexpress", small_image="fxhome", small_text = "FXHome", large_text="HitFilm", start=start_time)) #Sending data
    if ("HitFilmPro.exe" in (p.name() for p in psutil.process_iter())): #Checks if the program is runing
        start_time = mktime(time.localtime()) #Sets start time
        #start_time = 1535857560.0 #Sets start time
        while ("HitFilmPro.exe" in (p.name() for p in psutil.process_iter())): #While the user is still in HitFilm Express
            prevMouse = mouse
            mouse = win32gui.GetCursorPos()
            if (prevMouse == mouse):
                counter = counter + 1
            else:
                counter = 0
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
            elif ("Open Project" in w.GetWindowText (w.GetForegroundWindow())): #If the user is in an untitled project
                state = "Opening a Project"
                status = "Loading files"
            elif ("Relink Files" in w.GetWindowText (w.GetForegroundWindow())): #If the user is in an untitled project
                state = "Relinking files"
                status = "Probably deleted something"
            else: ##If the user isn't even in the app in the first place
                state = "Idling"
                status = "Not even in the app lmao"
            if (counter >= 100):
                status = "Idling"
            (RPCPro.update(state=status, details=state, large_image="hitfilmpro", small_image="fxhome", small_text = "FXHome", large_text="HitFilm", start=start_time)) #Sending data
   
    RPCPro.clear()
    RPC.clear() #If the while loop above does not (Meaning the user isn't in the app) run, clear the RPC (therefore removing the discord rich status)
    time.sleep(15) #Sleep for 5 seconds so the users PC doesn't blow up
