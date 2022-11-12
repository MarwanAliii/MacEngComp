from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime

time = datetime.now()
window = Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=1)

def send_msg():
    global text 
    msg = (text.get())
    sensors = get_sensor_data()

    if sensors[0] > 100 and sensors[0] < 600:
        log.insert(END,"**Temperature is abnormally high**\n")
    elif sensors[0] >= 600:
        log.insert(END,"**FIRE DETECTED**\n")
        emergency()
    elif sensors[1]== "True":
        log.insert(END,"**WATER DETECTED**\n")
        emergency()
    
    #Log the transmission sent
    log.insert(END,"\tSENT: "+msg+"\nTime: "+
                str(time)+
                "\nTemp: "+str(sensors[0])+"°C"
                ", Water detected: "+str(sensors[1])+
                '\n\n') 
    log.see(tk.END) #Automatically scroll

    output = received(msg) #Data returned from the server

    if output == "weather_stats":
        log.insert(END,"\tReceived: "+
                    "25° and Sunny\n"+
                    "Time: "+str(time)+
                    "\nServer Location: "+"Greece\n\n")
    elif output == None:
        log.insert(END,"\tReceived: "+
                    "**NO RESPONSE**\n")


def received(msg):
    input = msg.lower()
    if input == "help":
        emergency()
        return "help"
    elif input == "weather":
        #Access local weather data using an API
        return "weather_stats"
    else:
        return None

def get_sensor_data():
    temperature = int(input("Temperature: "))
    water_detected = input("Water detected (True/False): ")
    return temperature,water_detected

def emergency():
    log.insert(END,"Emergency Responders have been dispatched"+'\n')
    #Use FM/AM radio to broadcast to nearby ships aswell

text = tk.StringVar() 
ttk.Label(window, text="Send Message: ").grid(row=0,column=0)
user_msg = ttk.Entry(window, width=20,textvariable=text).grid(row=0,column=1)
send = ttk.Button(window,text="SEND",command = send_msg).grid(row=0,column=2)

log = Text(window,width=45) #All saves all sent/received messages and system notices.
log.grid(row=0,column=5)

window.mainloop()
