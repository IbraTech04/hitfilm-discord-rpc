from pypresence import Presence
import time
import time
from time import mktime
import psutil    
import win32gui
w=win32gui

client_id = '860354715886682112'  
RPC = Presence(client_id) 
print("RPC connection successful.")

RPC.connect()

while True:
    if ("HitFilmExpress.exe" in (p.name() for p in psutil.process_iter())):
        start_time = mktime(time.localtime())
        while ("HitFilmExpress.exe" in (p.name() for p in psutil.process_iter())):
            status = ""
            state = ""
            if (".hfp" in w.GetWindowText (w.GetForegroundWindow())):
                state = "In a File" 
                status = w.GetWindowText (w.GetForegroundWindow()).split("-",1)[0]
            elif ( w.GetWindowText (w.GetForegroundWindow()) == "HitFilm Express"):
                state = "Idling"
                status = "Homescreen"
            elif ("Untitled Project" in w.GetWindowText (w.GetForegroundWindow())):
                state = "In a File" 
                status = "Untitled Project"
            else:
                state = "Idling"
                status = "Not even in the app lmao"
            (RPC.update(state=status, details=state, large_image="hitfilm", small_image="fxhome", small_text = "FXHome", large_text="HitFilm", start=start_time))
    RPC.clear()