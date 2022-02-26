# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 20:45:11 2022

@author: shn99
"""

from tkinter import *
import random

root=Tk()
root.title("list")
root.geometry("400x400")

random_number_list = Label(root)
random_number_sorted_list = Label(root)

def randomlist():
    
    randomlist2 = "Juice", "Bread","Water"
    randomlist = random.sample(range(0,3),1)
    random_number_list["text"] = "Put item no " + str(randomlist) + "In Bag"
    randomlist.sort()
    random_number_sorted_list["text"] = "Take item 1 " + str(randomlist2)

btn=Button(root,text="generate random list ", command=randomlist)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)  

random_number_list.place(relx=0.5, rely=0.5, anchor=CENTER)   
random_number_sorted_list.place(relx=0.5, rely=0.6, anchor=CENTER)   

root.mainloop()