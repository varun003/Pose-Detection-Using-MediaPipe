import cv2
import mediapipe as mp
from tkinter import *
import math as m
from helper import *


def first():
    face()

def second():
    squat()

def third():
    back()



root = Tk()
root.geometry('500x500')
root.resizable(0,0)
root.title('Tkinter GUI')

Label(root,text='Tkinter GUI for MediaPipe',font='comicsansms 14 bold').pack(pady=50)
b1 = Button(root,text='face',bg='black',fg='white',height=1,width=5,command=first).pack(side=LEFT,padx=60,pady=50)  # ,command=face
b2 = Button(root,text='squat',bg='black',fg='white',height=1,width=5,command=second).pack(side=LEFT,padx=60,pady=50)  # ,command=squat
b3 = Button(root,text='back',bg='black',fg='white',height=1,width=5,command=third).pack(side=LEFT,padx=60,pady=50)  # ,command=back


root.mainloop()