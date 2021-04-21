from tkinter import *
import time
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)


##hardware
ledGreen=14


##GUI DEFINITIONS##
win=Tk()
win.title("MorseCode LED light")
win.geometry('400x300')
win['bg'] = 'gray'



MORSE_CODE = {'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..'
        
       }

RPi.GPIO.setup(ledGreen,RPi.GPIO.OUT)      


def close():
    RPi.GPIO.cleanup()
    win.destroy()


name_var=tkinter.StringVar()
name_var.set("")


name_entry= tkinter.Entry(win,textvariable=name_var)
    
name_entry.grid(row = 1,column = 1)

   



##EVENT FUNCTION##
def ledToggleGreen():
            name=name_var.get()[:12]
             
            while True:
                
                for character in name:
                      for sign in MORSE_CODE[character.upper()]:
                                
                                
                                if sign=='-':
                                     RPi.GPIO.output(ledGreen,True)
                                     time.sleep(3)
                                     RPi.GPIO.output(ledGreen,False)
                                     time.sleep(1)
                                     
                                   
                                elif sign == '.':
                                    RPi.GPIO.output(ledGreen,True)
                                    time.sleep(1)
                                    RPi.GPIO.output(ledGreen,False)
                                    time.sleep(1)
                                    print(sign)
                       
                time.sleep(10)               
                           
                        


ledButton=Button(win,text='Submit',command=ledToggleGreen,bg='bisque2',height=1,width=24)
ledButton.grid(row=2,column=1)

exitButton=Button(win,text='Exit',command=close,bg='red',height=1,width=6)
exitButton.grid(row=3,column=1)

win.protocol("WM_DELETE_WINDOW",close)#exit clean

win.mainloop() #loop forever


