import tkinter as w
import os 
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import mysql.connector
mydb= mysql.connector.connect( host="127.0.0.1", user= "root", password = "Varun123$", database="python_project1")
print(mydb)
my_database= mydb.cursor(buffered=True)
import random

def _from_rgb(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'


section=input("Enter section")
title=section+" "+"TimeTable"
student=w.Tk()
student.geometry('800x500')
student.title(title)
student.resizable(0,0)
student['bg'] = '#AC99F2'


game_frame = Frame(student,width=800)
head_text=Text(game_frame,width=15,height=1,font=('arial',20,'bold'),bg='#AC99F2',fg='black')
head_text.pack(padx=10,pady=10,side=w.TOP)
head_text.insert(w.END,title)
game_frame.pack(padx=100,pady=94,side=w.BOTTOM)
game_scroll = Scrollbar(game_frame)
game_scroll.pack(side=RIGHT, fill=Y)
game_scroll = Scrollbar(game_frame,orient='horizontal')
game_scroll.pack(side= BOTTOM,fill=X)
my_tt = ttk.Treeview(game_frame,yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set)
my_tt.pack(padx=10,pady=10,side=w.BOTTOM)
game_scroll.config(command=my_tt.yview)
game_scroll.config(command=my_tt.xview)

my_tt['columns'] = ('WeekDay','1st Slot','2nd Slot','3rd Slot', '4th Slot','5th Slot','6th Slot','7th Slot','8th Slot','9th Slot')
my_tt.column('#0',width=0,stretch=NO)
my_tt.column('WeekDay',anchor=CENTER,width=80)
my_tt.column('1st Slot',anchor=CENTER,width=80)
my_tt.column('2nd Slot',anchor=CENTER,width=80)
my_tt.column('3rd Slot',anchor=CENTER,width=80)
my_tt.column('4th Slot',anchor=CENTER,width=80)
my_tt.column('5th Slot',anchor=CENTER,width=80)
my_tt.column('6th Slot',anchor=CENTER,width=80)
my_tt.column('7th Slot',anchor=CENTER,width=80)
my_tt.column('8th Slot',anchor=CENTER,width=80)
my_tt.column('9th Slot',anchor=CENTER,width=80)

my_tt.heading('#0',text="")
my_tt.heading('WeekDay',text='Day')
my_tt.heading('1st Slot',text='Period 1')
my_tt.heading('2nd Slot',text='Period 2')
my_tt.heading('3rd Slot',text='Period 3')
my_tt.heading('4th Slot',text='Period 4')
my_tt.heading('5th Slot',text='Period 5')
my_tt.heading('6th Slot',text='Period 6')
my_tt.heading('7th Slot',text='Period 7')
my_tt.heading('8th Slot',text='Period 8')
my_tt.heading('9th Slot',text='Period 9')

big_list=[]
days=['Monday','Tuesday','Wednesday','Thursday','Friday']
my_database.execute("Select * from student_table where Section='{}'".format(section))
all_data=my_database.fetchall()
for day in days:
    in_day=day
    my_database.execute("Select Sub from student_table where WeekDay='{}' and Section='{}'".format(in_day,section))
    baby_data=my_database.fetchall()
    day_tup=(in_day,)
    baby_data.insert(0,day_tup)
    my_tt.insert(parent='',index='end',text='',
    values=(baby_data))
    print(baby_data)
student.mainloop()

