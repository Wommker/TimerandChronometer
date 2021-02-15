"""
Created : 15:02:2021

@author: Woomker
"""

from tkinter import *
from tkinter.font import Font
import pygame

#Control variables

run = False 
toc = False

#Class Interface where everything happens

class interface:

    #Start stopwatch or timer as the case may be

    def start(self,cot):
        global run
        global toc
        if run == False:
            run = True
            toc = cot
            
            if cot:
                self.btnchoro.config(text = "Stop")
                self.tick(cot)
            elif cot == False and self.millisecond != 0 or self.second != 0  or self.minute != 0 or self.hour != 0:
                    self.tick(cot)
                    self.btntimer.config(text = "Stop")
            else:
                run = False
        else: 
            if toc == cot:
                self.stop()
                if toc == True:
                    self.btnchoro.config(text = "Chronometer")
                else:
                    self.btntimer.config(text = "Timer")
            else:
                self.stop()
                self.btnchoro.config(text = "Chronometer")
                self.btntimer.config(text = "Timer")

    #Stop the stopwatch or timer as the case may be

    def stop(self):
        global run
        run = False

    #Restart the stopwatch or timer as the case may be

    def reset(self):
        self.stop()
        global run
        run= False
        self.hour=0
        self.minute=0
        self.second=0
        self.millisecond=0
        self.text.set("00:00:00:000")
        self.btnchoro.config(text = "Chronometer")
        self.btntimer.config(text = "Timer")

    #Call the same function every millisecond to be exact in the passage of time

    def tick(self,cot):
        if cot:
            self.passofthetime(cot,"millisecond")
        else:
            self.passofthetime(cot,"millisecond")
        if run:
            self.root.after(1,lambda:self.tick(cot))

                    
    def  __init__(self):
        #Time variables
        self.hour=0
        self.minute=0
        self.second=0
        self.millisecond=0
        self.toc = False
        self.tempo=[self.hour,self.minute,self.second,self.millisecond]
        #Interface variables
        self.root=Tk()
        self.root.title("stopwatch")    
        self.root.resizable(False,False)
        self.root.config(bg = "#063956")
        self.text = StringVar()
        self.text.set("00:00:00:000")
        self.myFont =Font(family="Times New Roman", size=18)
        #
        self.label = Label(self.root,textvariable=self.text)
        self.label.grid(row = 0,column = 1)
        self.label.configure(font=self.myFont, bg = "#063956", fg = "#cb0c59")
        #----------------1-First column----------------#
        #Button to decrease one hour
        self.BHD = Button(self.root,text = "-",command = lambda:self.passofthetime(False,"hour"))
        self.BHD.grid(row = 1,column = 0)
        self.BHD.config(font = 64, bg = "#0c4383", fg = "#cb0c59")
        #Button to decrease one minute
        self.BMD = Button(self.root,text = "-",command = lambda:self.passofthetime(False,"minute"))
        self.BMD.grid(row = 2,column = 0)
        self.BMD.config(font = 64, bg = "#0c4383", fg = "#cb0c59")
        #Button to decrease one second
        self.BSD = Button(self.root,text = "-",command = lambda:self.passofthetime(False,"second"))
        self.BSD.grid(row = 3,column = 0)
        self.BSD.config(font = 64, bg = "#0c4383", fg = "#cb0c59")
        #----------------2-Second column----------------#
        #Hours text box
        self.HL = Label(self.root,text="Hours",font = 64, bg = "#063956", fg = "#cb0c59")
        self.HL.grid(row = 1,column = 1)
        #Minutes text box
        self.ML = Label(self.root,text="Minutes",font = 64, bg = "#063956", fg = "#cb0c59")
        self.ML.grid(row = 2,column = 1)
        #Seconds text box
        self.SL = Label(self.root,text="Seconds",font = 64, bg = "#063956", fg = "#cb0c59")
        self.SL.grid(row = 3,column = 1)
        #----------------3-Third column----------------#
        #Button to Increase one hour
        self.BHI = Button(self.root,text = "+",command = lambda:self.passofthetime(True,"hour"))
        self.BHI.grid(row = 1,column = 2)
        self.BHI.config(font = 64, bg = "#0c4383", fg = "#cb0c59")
        #Button to Increase one minute
        self.BMI = Button(self.root,text = "+",command = lambda:self.passofthetime(True,"minute"))
        self.BMI.grid(row = 2,column = 2)
        self.BMI.config(font = 64, bg = "#0c4383", fg = "#cb0c59")
        #Button to Increase one second
        self.BSI = Button(self.root,text = "+",command = lambda:self.passofthetime(True,"second"))
        self.BSI.grid(row = 3,column = 2)
        self.BSI.config(font = 64, bg = "#0c4383", fg = "#cb0c59")
        #Reset time
        self.btnreset = Button(self.root,text="Reset",fg="Blue",command= self.reset)
        self.btnreset.grid(row = 5,column = 1)
        self.btnreset.config( bg = "#0c4383", fg = "#cb0c59")
        #Start to turn back time
        self.btntimer = Button(self.root, text="Timer" ,fg="Green",command = lambda:self.start(False))
        self.btntimer.grid(row = 4,column = 0)
        self.btntimer.config( bg = "#0c4383", fg = "#cb0c59")
        #Start the passage of time
        self.btnchoro = Button(self.root,text="Chronometer",fg="red",command = lambda:self.start(True))
        self.btnchoro.grid(row = 4,column = 2)
        self.btnchoro.config( bg = "#0c4383", fg = "#cb0c59") 

    #All time control operation

    def passofthetime(self,cot,value):
        if cot:
            if value == "millisecond" and run:
                self.millisecond +=1
                if(self.millisecond > 999):
                    self.second += 1 
                    self.millisecond = 0
                if(self.second > 59):
                    self.minute += 1
                    self.second = 0
                elif(self.minute > 59):
                    self.hour += 1
                    self.minute = 0
            if value == "second" and run == False:
                self.second +=1
                if self.second > 59:
                    self.minute += 1
                    self.second = 0
                if self.minute > 59:
                    self.hour +=1
                    self.minute = 0
            elif value == "minute" and run == False:
                self.minute +=1
                if self.minute > 59:
                    self.hour +=1
                    self.minute = 0
            elif value == "hour" and run == False:
                    self.hour +=1
        else:
            if value == "millisecond":
                if(self.millisecond > 0):
                    self.millisecond -=1 
                elif(self.second > 0):
                    self.second -=1
                    self.millisecond = 999
                elif(self.minute > 0):
                    self.minute -= 1
                    self.second = 59
                    self.millisecond = 999
                elif(self.hour > 0):
                    self.hour -=1
                    self.minute = 59
                    self.second = 59
                    self.millisecond = 999
                elif run:
                    self.stop()
                    self.btntimer.config(text = "Timer")
                    pygame.init()
                    pygame.mixer.music.load('sound.mp3')
                    pygame.mixer.music.play()
            if value == "second" and run == False:
                if self.second > 0:
                    self.second -=1
                elif self.minute > 0:
                    self.minute -=1
                    self.second = 59
                elif self.hour > 0:
                    self.hour -=1
                    self.minute = 59
                    self.second = 59
            elif value == "minute" and run == False:
                if self.minute > 0:
                    self.minute -=1
                elif self.hour > 0:
                    self.hour -=1
                    self.minute = 59
            elif value == "hour" and self.hour > 0 and run == False:
                    self.hour -=1

        result=self.getvalue(self.hour,False)+":"+self.getvalue(self.minute,False)+":"+self.getvalue(self.second,False)+":"+self.getvalue(self.millisecond,True)
        self.text.set(result)
        
    #Take values to show a clean time bar

    def getvalue(self,value,zeros):
        if zeros:
            if value < 10:
                return ("00" + str(value))
            elif value < 100 and value >= 10:
                return ("0" + str(value))
            else:
                return str(value)
        if zeros == False:
            if value <10:
                return ("0" + str(value))
            else:
                return str(value)

App=interface()
App.root.mainloop()
