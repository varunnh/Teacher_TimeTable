import customtkinter as w
from PIL import Image
from PIL import Image
from PIL import ImageTk
import os
import tkinter as tk
import mysql.connector
from tkinter.ttk import *
import random
from show_pass import show_pass
#from show_pass import show_pass
mydb= mysql.connector.connect( host="127.0.0.1", user= "root", password = "Varun123$", database="python_project1")
print(mydb)
my_database= mydb.cursor(buffered=True)



#####PAGE-1####
def admin():
    """
    The "admin" function destroys the login window and opens the admin.py file.
    """
    login.destroy()
    os.system(r"C:\Users\pg401\Programs\Python_Project2\admin.py")
    #admin.mainloop()
def show_teacher():
    """
    The function "show_teacher" displays the teacher page and calls the "teacher_table" function.
    """
    l3.configure(text="Hi")
    student_page.forget()
    login_page.forget()
    teacher_page.pack()
    print("Hi")
    teacher_table()
def show_student():
    """
    The function "show_student" updates the text of a label, hides the login and teacher pages, and
    displays the student page and section table.
    """
    l3.configure(text="Wsg")
    login_page.forget()
    teacher_page.forget()
    student_page.pack()
    section_table()

def restart_app():
    """
    The function restart_app() destroys the current login window and restarts the application by running
    a Python script.
    """
    login.destroy()
    os.system(r"C:\Users\pg401\Programs\Python_Project2\Custom_Tkinter_trial.py")

def save():
    """
    The function "save" checks if the PRN and password fields are empty, and if not, it queries the
    database to check the user's role and redirects them accordingly.
    """
    prn=a1.get()
    passw=a2.get()
    num=a3.get()
    if prn=="" or passw=="":
        l3.configure(text="Enter all fields")
    else:
        my_database.execute("Select User_Role from login_info where PRN='{}' and PassWord='{}'".format(prn,passw))
        role=my_database.fetchall()
        print(role)
        if len(role)>0:
            if role[0][0]=="Admin":
                admin()
            elif role[0][0]=="Teacher":
                show_teacher()
            elif role[0][0]=="Student":
                show_student()
        else:
            l3.configure(text="Wrong PRN or Password")

w.set_appearance_mode('dark')
w.set_default_color_theme('green')




title="Login"
login=w.CTk(fg_color='#0b3444')
login.geometry('1920x1080')
login.title(title)
s=login.winfo_screenwidth()
t=login.winfo_screenheight()
# The above code is creating a login window using the Tkinter library in Python. It sets the title of
# the window to "Login" and sets the foreground color of the window to '#0b3444'. The window size is
# set to 1920x1080 pixels. The code then gets the screen width and height using the
# `winfo_screenwidth()` and `winfo_screenheight()` methods.



#Background Image Frame




        
        













# The below code is creating a login page using the Tkinter library in Python. It creates a frame with
# a specified height and width, and sets the foreground color to transparent and the background color
# to '#0b3444'. The frame is then packed and displayed on the screen.
login_page=w.CTkFrame(login, height = 1920, width = 1080,fg_color='transparent',bg_color='#0b3444')
login_page.pack(fill="both",expand=True,anchor="nw")

# The below code is creating a Tkinter image object called `image1` by opening an image file called
# "blue_bg.png" located at the specified file path. It then creates a Tkinter label object called
# `bg_img` and sets its image attribute to `image1`. Finally, it places the `bg_img` label on a
# Tkinter frame called `login_page` and sets its position and size using relative coordinates.
image1=w.CTkImage(dark_image=Image.open(r"C:\Users\pg401\Downloads\image files\blue_bg.png"),size=(t,s))
bg_img=w.CTkLabel(login_page,text="",image=image1)
bg_img.place(relx=0,rely=0,relheight=1,relwidth=1)


title=w.CTkFrame(login_page,width=0.5*s,height=0.5*t,fg_color='#0b3444')
title.place(relx=0.5,rely=0.3,anchor='center')
title_label=w.CTkLabel(title,text="Login Page",pady=10,height=10,font=("Product Sans",35))
title_label.place(relx=0.35,rely=0.4)

# The above code is creating a graphical user interface (GUI) using the Tkinter library in Python. It
# creates a frame called "page1" with a specific width and height, and sets its foreground color. It
# also creates three StringVar variables to store user input.
page1=w.CTkFrame(login_page,width=0.5*s,height=0.5*t,fg_color='#0b3444')
page1.place(relx=0.5,rely=0.45,anchor='center')
page1.grid_rowconfigure(3, weight= 1)
a1=tk.StringVar()
a2=tk.StringVar()
a3=tk.StringVar()
#Input Name
e0=w.CTkEntry(page1,textvariable=a1,width=100)
l0=w.CTkLabel(page1,text="Enter PRN",font=("Arial",14))
l0.grid(row = 0, column = 0, sticky = 'nsew', padx = 20, pady = 2)
e0.grid(row = 0, column = 1, sticky = 'nsew', padx = 20, pady = 2)
#Input password
e1=w.CTkEntry(page1,show='*',textvariable=a2,width=100)

e1.grid(row = 1, column = 1, sticky = 'nsew', padx = 20, pady = 2)
l1=w.CTkLabel(page1,text="Enter Password",font=("Arial",14))
l1.grid(row = 1, column = 0, sticky = 'nsew', padx = 20, pady = 2)
show_button=w.CTkButton(login_page,width=10,text='Show',font=("Arial Rounded MT",18),command=lambda:show_pass(e1,show_button),fg_color='#0b3444')
show_button.place(relx=0.60,rely=0.43)
e2=w.CTkEntry(page1,textvariable=a3,width=100)
e2.grid(row = 2, column = 1, sticky = 'nsew', padx = 20, pady = 2)
l2=w.CTkLabel(page1,text="Enter Number")
l2.grid(row = 2, column = 0, sticky = 'nsew', padx = 20, pady = 2)
#Save Button
save_frame=w.CTkFrame(login_page,width=0.1*page1.winfo_width(),height=0.2*page1.winfo_height(),fg_color='transparent')
save_frame.place(relx=0.49,rely=0.59,anchor='center')
save_frame.grid_rowconfigure(2,weight=1)
b0=w.CTkButton(save_frame,text="Save",fg_color='#0b3444',command=lambda:save())
b0.grid(row = 0, column = 0, columnspan = 1, sticky = 'nsew')
l3=w.CTkLabel(save_frame,text="",fg_color='#0b3444')
l3.grid(row = 1, column = 0, columnspan = 1, sticky = 'nsew')






####PAGE-2####

student_page=w.CTkFrame(login, height = 1100, width = 1920,fg_color='transparent')
student_page.pack()
image1=w.CTkImage(dark_image=Image.open(r"C:\Users\pg401\Downloads\image files\blue_bg.png"),size=(t,s))
bg_img=w.CTkLabel(student_page,text="",image=image1)
bg_img.place(relx=0,rely=0,relheight=1,relwidth=1)

button_frame=w.CTkFrame(student_page,width=1400,height=s/22,fg_color='#0b3444')
button_frame.grid(row=0,column=0,sticky='nsew',padx=10,pady=0)
b0=w.CTkButton(button_frame,text="Go Back",command=lambda:restart_app())
b0.place(relx=0.052,rely=0.38,anchor='center')


page3=w.CTkFrame(student_page,height=3800,width=1400,fg_color='transparent')
page3.grid(row=3,column=0,sticky='nsew',padx=0,pady=150)
page3.grid_rowconfigure(5, weight= 1)
page3.grid_columnconfigure(9,weight=1)

# image1=w.CTkImage(dark_image=Image.open(r"C:\Users\pg401\Downloads\image files\blue_bg.png"),size=(1200,1800))
# bg_img=w.CTkLabel(page2,text="HELLO",image=image1)
# bg_img.place(relx=0,rely=0,relheight=1,relwidth=1)
print("Placed")
#LABELS 
# day_label=w.CTkLabel(page2,text="Day",font=("Georgia",25),width=150,height=100,fg_color='yellow',corner_radius=1)
# day_label.place(relx=0.05,rely=0.1,anchor='center')
# period1_label=w.CTkLabel(page2,text="Period1",font=("Georgia",25),width=150,height=100,fg_color='transparent')
# period1_label.place(relx=0.12,rely=0.1,anchor='center')
# period2_label=w.CTkLabel(page2,text="Period2",font=("Georgia",25),width=150,height=100,fg_color='transparent')
# period2_label.place(relx=0.21,rely=0.1,anchor='center')
# period3_label=w.CTkLabel(page2,text="Period3",font=("Georgia",25),width=150,height=100,fg_color='transparent')
# period3_label.place(relx=0.30,rely=0.1,anchor='center')
# period4_label=w.CTkLabel(page2,text="Period4",font=("Georgia",25),width=150,height=100,fg_color='transparent')
# period4_label.place(relx=0.39,rely=0.1,anchor='center')
# period5_label=w.CTkLabel(page2,text="Period5",font=("Georgia",25),width=150,height=100,fg_color='transparent')
# period5_label.place(relx=0.48,rely=0.1,anchor='center')
# period6_label=w.CTkLabel(page2,text="Period6",font=("Georgia",25),width=150,height=100,fg_color='transparent')
# period6_label.place(relx=0.57,rely=0.1,anchor='center')
# period7_label=w.CTkLabel(page2,text="Period7",font=("Georgia",25),width=150,height=100,fg_color='transparent')
# period7_label.place(relx=0.66,rely=0.1,anchor='center')
# period8_label=w.CTkLabel(page2,text="Period8",font=("Georgia",25),width=150,height=100,fg_color='transparent')
# period8_label.place(relx=0.75,rely=0.1,anchor='center')
# period9_label=w.CTkLabel(page2,text="Period9",font=("Georgia",25),width=150,height=100,fg_color='transparent')
# period9_label.place(relx=0.84,rely=0.1,anchor='center')
#Data adding
# free_day=w.CTkLabel(page2,text="",font=("Georgia",25),width=120,height=0,fg_color='transparent')
# free_day.grid(row=0,column=2,sticky='nsew',padx=0,pady=0)
# free_label=w.CTkLabel(page2,text=" ",font=("Georgia",25),width=120,height=50,fg_color='yellow')
# free_label.grid(row=1,column=5,columnspan=10,sticky='nsew',padx=0,pady=0)
title_label=w.CTkLabel(page3,text="Hi",height=2,width=90,font=("Georgia",16),fg_color='transparent')
title_label.grid(row=0,column=5,sticky='nsew',padx=0,pady=0)
def section_table():
    """
    The function `section_table` generates a timetable for a specific section based on the PRN (Personal
    Registration Number) provided.
    """
    for i in range(5):
        prn=a1.get()
        my_database.execute("Select Section from login_info where PRN='{}'".format(prn))
        Section_Name=my_database.fetchall()[0][0]
        weekday=['Monday','Tuesday','Wednesday','Thursday','Friday']
        per=["Period 1","Period 2","Period 3","Period 4","Period 5","Period 6","Period 7","Period 8","Period 9"]
        days=[["Day","Period1","Period2","Period3","Period4","Period5","Period6","Period7","Period8","Period9"],["","","","","","","","","",""],["","","","","","","","","",""],["","","","","","","","","",""],["","","","","","","","","",""],["","","","","","","","","",""]]
        for k in range(len(weekday)):
            for l in range(len(per)):
                #print(weekday[k],period,Teacher_Name)
                my_database.execute("Select Sub from student_table where WeekDay='{}'and Section='{}' and Period='{}'".format(weekday[k],Section_Name,per[l]))
                infant_data=my_database.fetchall()
                unocc_tuple=('Unoccupied',)
                if len(infant_data)<1:
                    infant_data.insert(0,unocc_tuple)
                print(infant_data)
                days[k+1][l]=infant_data[0][0]
            days[k+1].insert(0,weekday[k])
            print(days[k+1])
        #days[k+1].insert(0,weekday[k])
        #print(days[k+1])             
        print("Day Done!")
        for j in range(10):
            
            record_s=w.CTkFrame(page3,fg_color='transparent')
            record_s.grid(row=i+2,column=j,sticky='nsew',padx=0,pady=0)
            days_label_s=w.CTkLabel(record_s,text="Hello",height=50,width=120,font=("Georgia",16),fg_color='transparent')
            days_label_s.grid(row=0,column=0,sticky='nsew',padx=0,pady=0)
            color=random.randint(0,1)
            if i+1 ==1:
                #record.configure(highlightbackground='red',highlightcolor='red'
                pass
            if color==1:
                days_label_s.configure(fg_color='#075665')
            else:
                days_label_s.configure(fg_color='#045374')
            days_label_s.configure(text=days[i][j])
    title_label.configure(text=Section_Name+" TimeTable")

###PAGE3"Teacher's Page

teacher_page=w.CTkFrame(login, height = 1100, width = 1920,fg_color='transparent')
teacher_page.pack()
image1=w.CTkImage(dark_image=Image.open(r"C:\Users\pg401\Downloads\image files\blue_bg.png"),size=(t,s))
bg_img=w.CTkLabel(teacher_page,text="",image=image1)
bg_img.place(relx=0,rely=0,relheight=1,relwidth=1)

button_frame=w.CTkFrame(teacher_page,width=1400,height=s/22,fg_color='#0b3444')
button_frame.grid(row=0,column=0,sticky='nsew',padx=10,pady=0)
b0=w.CTkButton(button_frame,text="Go Back",command=lambda:restart_app())
b0.place(relx=0.052,rely=0.38,anchor='center')


page2=w.CTkFrame(teacher_page,height=1800,width=1200,fg_color='transparent')
page2.grid(row=3,column=0,sticky='nsew',padx=40,pady=150)
page2.grid_rowconfigure(1, weight= 1)
page2.grid_columnconfigure(0,weight=1)

# image1=w.CTkImage(dark_image=Image.open(r"C:\Users\pg401\Downloads\image files\blue_bg.png"),size=(1200,1800))
# bg_img=w.CTkLabel(page2,text="HELLO",image=image1)
# bg_img.place(relx=0,rely=0,relheight=1,relwidth=1)
print("Placed")
#LABELS 
# day_label=w.CTkLabel(page2,text="Day",font=("Georgia",25),width=150,height=100,fg_color='yellow',corner_radius=1)
# day_label.place(relx=0.05,rely=0.1,anchor='center')
# period1_label=w.CTkLabel(page2,text="Period1",font=("Georgia",25),width=150,height=100,fg_color='transparent')
# period1_label.place(relx=0.12,rely=0.1,anchor='center')
# period2_label=w.CTkLabel(page2,text="Period2",font=("Georgia",25),width=150,height=100,fg_color='transparent')
# period2_label.place(relx=0.21,rely=0.1,anchor='center')
# period3_label=w.CTkLabel(page2,text="Period3",font=("Georgia",25),width=150,height=100,fg_color='transparent')
# period3_label.place(relx=0.30,rely=0.1,anchor='center')
# period4_label=w.CTkLabel(page2,text="Period4",font=("Georgia",25),width=150,height=100,fg_color='transparent')
# period4_label.place(relx=0.39,rely=0.1,anchor='center')
# period5_label=w.CTkLabel(page2,text="Period5",font=("Georgia",25),width=150,height=100,fg_color='transparent')
# period5_label.place(relx=0.48,rely=0.1,anchor='center')
# period6_label=w.CTkLabel(page2,text="Period6",font=("Georgia",25),width=150,height=100,fg_color='transparent')
# period6_label.place(relx=0.57,rely=0.1,anchor='center')
# period7_label=w.CTkLabel(page2,text="Period7",font=("Georgia",25),width=150,height=100,fg_color='transparent')
# period7_label.place(relx=0.66,rely=0.1,anchor='center')
# period8_label=w.CTkLabel(page2,text="Period8",font=("Georgia",25),width=150,height=100,fg_color='transparent')
# period8_label.place(relx=0.75,rely=0.1,anchor='center')
# period9_label=w.CTkLabel(page2,text="Period9",font=("Georgia",25),width=150,height=100,fg_color='transparent')
# period9_label.place(relx=0.84,rely=0.1,anchor='center')
#Data adding
# free_day=w.CTkLabel(page2,text="",font=("Georgia",25),width=120,height=0,fg_color='transparent')
# free_day.grid(row=0,column=2,sticky='nsew',padx=0,pady=0)
# free_label=w.CTkLabel(page2,text=" ",font=("Georgia",25),width=120,height=50,fg_color='transparent')
# free_label.grid(row=1,column=5,columnspan=10,sticky='nsew',padx=0,pady=0)
title_label=w.CTkLabel(page2,text="",height=2,width=90,font=("Product Sans",36),fg_color='transparent')
title_label.grid(row=0,column=0,sticky='nsew',padx=0,pady=0)
table_frame = w.CTkFrame(master=page2,fg_color='transparent')
table_frame.rowconfigure(5, weight=1)
table_frame.columnconfigure(9, weight=1)
table_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
def teacher_table():
    """
    The function `teacher_table()` generates a timetable for a teacher based on their PRN (Personal
    Registration Number) and displays it in a graphical user interface.
    """
    for i in range(5):
        prn=a1.get()
        my_database.execute("Select User_Name from login_info where PRN='{}'".format(prn))
        Teacher_Name=my_database.fetchall()[0][0]
        weekday=['Monday','Tuesday','Wednesday','Thursday','Friday']
        per=["Period 1","Period 2","Period 3","Period 4","Period 5","Period 6","Period 7","Period 8","Period 9"]
        days=[["Day","Period1","Period2","Period3","Period4","Period5","Period6","Period7","Period8","Period9"],["","","","","","","","","",""],["","","","","","","","","",""],["","","","","","","","","",""],["","","","","","","","","",""],["","","","","","","","","",""]]
        for k in range(len(weekday)):
            for l in range(len(per)):
                #print(weekday[k],period,Teacher_Name)
                my_database.execute("Select Sub from student_table where WeekDay='{}'and Teacher_Name='{}' and Period='{}'".format(weekday[k],Teacher_Name,per[l]))
                infant_data=my_database.fetchall()
                unocc_tuple=('Unoccupied',)
                if len(infant_data)<1:
                    infant_data.insert(0,unocc_tuple)
                print(infant_data)
                days[k+1][l]=infant_data[0][0]
            days[k+1].insert(0,weekday[k])
            #print(days[k+1])
        #days[k+1].insert(0,weekday[k])
        #print(days[k+1])             
        print("Day Done!")
        for j in range(10):
            
            record=w.CTkFrame(table_frame,height=50,width=90,fg_color='transparent')
            record.grid(row=i+2,column=j,sticky='nsew',padx=0,pady=0)
            days_label=w.CTkLabel(record,text="Hello",height=50,width=120,font=("Roboto",16),fg_color='transparent')
            days_label.grid(row=0,column=0,sticky='nsew',padx=0,pady=0)
            color=random.randint(0,1)
            if i==0:
                days_label.configure(fg_color='#6600cc')
                print("eeyeh")
            elif j==0:
                days_label.configure(fg_color='#6600cc')
            elif color==1:
                days_label.configure(fg_color='#075665')
            else:
                days_label.configure(fg_color='#045374')
            days_label.configure(text=days[i][j])
    title_label.configure(text=Teacher_Name+" TimeTable            ")
login.mainloop()
