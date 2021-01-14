from tkinter import *
from math import floor
import pygame

#Increase the hours with the button

def Mohours(incordec):
    global run
    if(run == False):
        if(incordec):
            if(int(tempo[0]) > 0):
                tempo[0] = (str(int(tempo[0]) - 1))
            update(True)
        else:
            tempo[0] = (str(int(tempo[0]) + 1))
            update(False)

#Increase the minutes with the button

def Mominutes(incordec):
    global run
    if(run == False):
        if(incordec):
            if(int(tempo[1]) > 0 ):
                tempo[1] = (str(int(tempo[1]) - 1))
            elif(int(tempo[0]) > 0):
                tempo[0] = (str(int(tempo[0]) - 1))
                tempo[1] = (str(59))
            update(True)
        else:
            tempo[1] = (str(int(tempo[1]) + 1))
            update(False)

#Increase the seconds with the button

def Moseconds(incordec):
    global run
    if(run == False):
        if(incordec):
            if(int(tempo[2]) > 0 ):
                tempo[2] = (str(int(tempo[2]) - 1))
            elif(int(tempo[1]) > 0):
                tempo[1] = (str(int(tempo[1]) - 1))
                tempo[2] = (str(59))
            elif(int(tempo[0]) > 0):
                tempo[0] = (str(int(tempo[0]) - 1))
                tempo[1] = (str(59))
                tempo[2] = (str(59))
            update(True)            
        else:
            tempo[2] = (str(int(tempo[2]) + 1))
            update(False)

#Update and show time bar and error prevention
def update(incordec):            
    if(incordec):
        pass
    else:
            #Seconds
        if((int(tempo[2])) >= 60):
            tempo[1] = str(int(tempo[1]) + floor(int(tempo[2])/60))
            tempo[2] = str(int(tempo[2]) - (floor(int(tempo[2])/60)*60))
            #Minutes
        if((int(tempo[1])) >= 60):
            tempo[0] = str(int(tempo[0]) + floor(int(tempo[1])/60))
            tempo[1] = str(int(tempo[1]) - (floor(int(tempo[1])/60)*60))
    #Update and show time bar
    clo.set(tempo[0]+":"+tempo[1]+":"+tempo[2])

#Pass of the time

def passtime(Sot):
    global ms
    ms+=1
    if ms >=1000:
        if(Sot):
            if(int(tempo[2]) > 0 ):
                tempo[2] = (str(int(tempo[2]) - 1))
            elif(int(tempo[1]) > 0):
                tempo[1] = (str(int(tempo[1]) - 1))
                tempo[2] = (str(59))
            elif(int(tempo[0]) > 0):
                tempo[0] = (str(int(tempo[0]) - 1))
                tempo[1] = (str(59))
                tempo[2] = (str(59))
            update(True)
            ms = 0
        else:
            if(int(tempo[2]) < 59 ):
                tempo[2] = (str(int(tempo[2]) + 1))
            elif(int(tempo[1]) < 59):
                tempo[1] = (str(int(tempo[1]) + 1))
                tempo[2] = (str(0))
            else:
                tempo[0] = (str(int(tempo[0]) + 1))
                tempo[1] = (str(0))
                tempo[2] = (str(0))
            update(False)
            ms = 0

#Call the same function every millisecond to be exact in the passage of time

def sechan():
    global aod
    global run
    if(run):
        if(aod):    
                if(int(tempo[0]) > 0 or int(tempo[1]) > 0 or int(tempo[2]) > 0):
                    root.after(1,sechan)
                    passtime(aod)
                else:
                    pygame.init()
                    pygame.mixer.music.load('sound.mp3')
                    pygame.mixer.music.play()
        else:
            root.after(1,sechan)
            passtime(aod)

#Start stopwatch or timer as the case may be

def start(SoT):
    global aod
    aod = SoT
    global run
    if(SoT):
        if((int(tempo[0]) > 0 or int(tempo[1]) > 0 or int(tempo[2]) > 0) and (run == False)):
            run = True
            sechan()
            BT.config(text = "Stop")
        elif((int(tempo[0]) > 0 or int(tempo[1]) > 0 or int(tempo[2]) > 0) and (run == True)):
            run = False
            BT.config(text = "Timer")
            BC.config(text = "Chronometer")
    elif(SoT == False and run == False):
        run = True
        sechan()
        BC.config(text = "Stop")
    elif(SoT == False and run == True):
        run = False
        BC.config(text = "Chronometer")
        BT.config(text = "Timer")
   
#Reset the timer
        
def restart():
    global run
    run = False
    tempo[0] = str(int(0))
    tempo[1] = str(int(0))
    tempo[2] = str(int(0))
    clo.set(tempo[0]+":"+tempo[1]+":"+tempo[2])
    BT.config(text = "Timer")
    BC.config(text = "Chronometer")

#Interface

#Root
root = Tk()
root.title("Timer and Chronometer")
root.resizable(False,False)
root.geometry("400x300")
root.config(bg = "#063956")

#Frame
frame = Frame(root,width = 500,height = 400)
frame.pack()
frame.config(bg = "#063956")

#Time variables
tempo=['0','0','0']
ms = 0
clo=StringVar()
clo.set(tempo[0]+":"+tempo[1]+":"+tempo[2])

#Timer bar
clock = Label(frame, textvariable = clo)
clock.grid(row = 0,column = 0,columnspan = 4)
clock.config(font = 64, bg = "#063956", fg = "#cb0c59")

#Controlling variables
run = False
aod = False

#----------------1-First column----------------#

#Button to decrease one hour
BHD = Button(frame,text = "-", command = lambda:Mohours(True))
BHD.grid(row = 1,column = 0)
BHD.config(font = 64, bg = "#0c4383", fg = "#cb0c59")
#Button to decrease one minute
BMD = Button(frame,text = "-", command = lambda:Mominutes(True))
BMD.grid(row = 2,column = 0)
BMD.config(font = 64, bg = "#0c4383", fg = "#cb0c59")
#Button to decrease one second
BSD = Button(frame,text = "-", command = lambda:Moseconds(True))
BSD.grid(row = 3,column = 0)
BSD.config(font = 64, bg = "#0c4383", fg = "#cb0c59")
#Start the passage of time
BT = Button(frame,text = "Timer", command = lambda:start(True), padx = 30)
BT.grid(row = 4,column = 0,columnspan = 2)
BT.config(font = 64, bg = "#0c4383", fg = "#cb0c59")

#----------------2-Second column----------------#

#Seconds text box
HL = Label(frame, text = 'Hours')
HL.grid(row = 1,column = 1,columnspan = 2)
HL.config(font = 64, bg = "#063956", fg = "#cb0c59")
#Minutes text box
ML = Label(frame, text = 'Minutes')
ML.grid(row = 2,column = 1,columnspan = 2)
ML.config(font = 64, bg = "#063956", fg = "#cb0c59")
#Hours text box
SL = Label(frame, text = 'Seconds')
SL.grid(row = 3,column = 1,columnspan = 2)
SL.config(font = 64, bg = "#063956", fg = "#cb0c59")
#Reset time
BR = Button(frame,text = "Restart", command = restart, padx = 30)
BR.grid(row = 5,column = 1,columnspan = 2)
BR.config(font = 64, bg = "#0c4383", fg = "#cb0c59")
#Start to turn back time
BC = Button(frame,text = "Chronometer", command = lambda:start(False), padx = 30)
BC.grid(row = 4,column = 2,columnspan = 2)
BC.config(font = 64, bg = "#0c4383", fg = "#cb0c59")

#----------------3-Third column----------------#
#Button to Increase one hour
BHI = Button(frame,text = "+", command = lambda:Mohours(False))
BHI.grid(row = 1,column = 3)
BHI.config(font = 64, bg = "#0c4383", fg = "#cb0c59")
#Button to Increase one minute
BMI = Button(frame,text = "+", command = lambda:Mominutes(False))
BMI.grid(row = 2,column = 3)
BMI.config(font = 64, bg = "#0c4383", fg = "#cb0c59")
#Button to Increase one second
BSI = Button(frame,text = "+", command = lambda:Moseconds(False))
BSI.grid(row = 3,column = 3)
BSI.config(font = 64, bg = "#0c4383", fg = "#cb0c59")

#Stop Timer and Terminate Root

root.mainloop()
