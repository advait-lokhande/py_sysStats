import sys
import os
import psutil
import tkinter as tk
import socket
from tkinter.constants import BOTTOM, LEFT, RIGHT, W
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(ip_address)

_bg = 'black' #bg color variable
_fg = 'white' #fg color variable
intrvl = 1 #refresh speed /time interval

mw = tk.Tk()
mw.overrideredirect(True)
mw.geometry("300x350-20+20")
mw.configure(bg='black')
mw.attributes('-alpha',0.4)

def update():

    ipvaL.configure(text=socket.gethostbyname(hostname))
    cpuvaL.configure(text=psutil.cpu_percent(intrvl))
    ramvaL.configure(text=psutil.virtual_memory()[2])
    ramvaL.after(1000,update)

    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
ipL = tk.Label(mw,text="My IP addr: ", bg=_bg, fg= _fg)
ipvaL = tk.Label(mw,text=socket.gethostbyname(hostname), bg=_bg, fg= _fg)
ipL.grid(row=0, column=0, padx=4, pady=4, ipadx=4, ipady=4)
ipvaL.grid(row=0, column=1, padx=4, pady=4, ipadx=4, ipady=4)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
cpuL = tk.Label(mw,text="CPU usage: ", bg=_bg, fg= _fg)
cpuvaL = tk.Label(mw,text=psutil.cpu_percent(intrvl), bg=_bg, fg= _fg)
cpuL.grid(row=1, column=0, padx=4, pady=4, ipadx=4, ipady=4)
cpuvaL.grid(row=1, column=1, padx=4, pady=4, ipadx=4, ipady=4)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
ramL = tk.Label(mw,text="RAM usage: ", bg=_bg, fg= _fg)
ramvaL = tk.Label(mw,text=psutil.virtual_memory()[2], bg=_bg, fg= _fg)
ramL.grid(row=2, column=0, padx=4, pady=4, ipadx=4, ipady=4)
ramvaL.grid(row=2, column=1, padx=4, pady=4, ipadx=4, ipady=4)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
bt = tk.Button(mw, text="Exit", command=mw.destroy, bg=_bg, fg=_fg, width=10)
bt.grid(row=3, column=0, columnspan=2, padx=4, pady=4, ipadx=2, ipady=2)

update()
mw.mainloop()
