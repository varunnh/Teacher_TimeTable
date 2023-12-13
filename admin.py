import customtkinter as w
from PIL import Image,ImageTk
from PIL.Image import *
from PIL.ImageTk import *
import tkinter as tk
from tkinter import *
import mysql.connector
import random
import os
#import WhatsApp_Selenium
#from WhatsApp_Selenium import *
#import Custom_Tkinter trial.py as trial
mydb= mysql.connector.connect( host="127.0.0.1", user= "root", password = "Varun123$", database="python_project1")
print(mydb)
my_database= mydb.cursor(buffered=True)




w.set_appearance_mode('dark')
w.set_default_color_theme('green')

admin=w.CTk(fg_color="#0b3444")
admin.geometry('1920x1080')
admin.title("Admin")
s=admin.winfo_screenheight()
t=admin.winfo_screenwidth()

#PAGE 1

def focus_next_window(event):
    event.widget.tk_focus().focus()
    
    return("break")

def show_user():

    teacher_page.forget()
    section1_page.forget()
    section2_page.forget()
    teacher1_page.forget()
    teacher2_page.forget()
    delete_page.forget()
    update_page.forget()
    user_page.pack()
def show_teacher():
    section1_page.forget()
    section2_page.forget()
    teacher1_page.forget()
    user_page.forget()
    teacher2_page.forget()
    delete_page.forget()
    update_page.forget()
    teacher_page.pack()
def show_section1():
    teacher_page.forget()
    section1_page.forget()
    section2_page.pack_forget()
    teacher1_page.forget()
    teacher2_page.forget()
    user_page.forget()
    delete_page.forget()
    update_page.forget()
    section1_page.pack()
    

def show_section2():
    teacher_page.forget()
    section1_page.forget()
    teacher1_page.forget()
    user_page.forget()
    teacher2_page.forget()
    delete_page.forget()
    update_page.forget()
    section2_page.forget()
    section2_page.pack()
    section_table()

def show_teacher1():
    teacher_page.forget()
    section1_page.forget()
    section2_page.forget()
    user_page.forget()
    teacher2_page.forget()
    delete_page.forget()
    update_page.forget()
    teacher1_page.pack()


def show_teacher2():
    teacher_page.pack_forget()
    section1_page.pack_forget()
    section2_page.pack_forget()
    teacher1_page.pack_forget()
    user_page.pack_forget()
    delete_page.pack_forget()
    update_page.pack_forget()
    teacher2_page.pack()
    teacher_table()

def show_deletion():
    teacher_page.forget()
    section1_page.forget()
    section2_page.forget()
    teacher1_page.forget()
    teacher2_page.forget()
    user_page.forget()
    update_page.forget()
    delete_page.pack()

def show_update():
    teacher_page.forget()
    section1_page.forget()
    section2_page.forget()
    teacher1_page.forget()
    teacher2_page.forget()
    user_page.forget()
    delete_page.forget()
    update_page.pack()


def restart_app():
    """
    The function restart_app() restarts the admin.py application.
    """
    admin.destroy()
    os.system(r"C:\Users\pg401\Downloads\admin.py")

def focus_previous_widget(event):
    event.widget.tk_focusPrev().focus()
    return("break")





def addition_of_section(sec):
    """
    The function `addition_of_section` checks if a section is empty and if so, populates it with default
    values, and then proceeds to perform subject allotment and teacher update.
    
    :param sec: The parameter "sec" represents the section for which the addition of sections is being
    performed. It is used to identify and manipulate the data related to that particular section in the
    student_table
    """
    days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    periods=['Period 1','Period 2','Period 3','Period 4','Period 5','Period 6','Period 7','Period 8','Period 9']
    unocc="unoccupied"
    default_val='Mr.X'
    my_database.execute("Select count(0) from student_table where Section='{}'".format(sec))
    section_count=my_database.fetchall()
    print(section_count)
    if section_count[0][0]==0 or len(section_count)==0:
        for day in days:
            for period in periods:
                my_database.execute('Insert into student_table values("%s","%s","%s","%s","%s")'%(sec,day,period,unocc,default_val))
                mydb.commit()
        subject_allotment(sec)
    else:
        subject_allotment(sec)
        teacher_update(sec)
            
def teacher_update(sec):
    """
    The function `teacher_update` updates the teacher names in the student_table based on the subjects
    and section provided.
    
    :param sec: The parameter "sec" represents the section for which the teacher update is being
    performed. It is used to filter the data from the "master_teacher" table and update the
    "student_table" with the corresponding teacher names for each subject in the given section
    """
    days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    periods=['Period 1','Period 2','Period 3','Period 4','Period 5','Period 6','Period 7','Period 8','Period 9']
    phy_subjects={}
    phy_teachers={}
    my_database.execute("Select Sub,Credits from master_teacher where Section='{}'".format(sec))
    data=my_database.fetchall()
    for i in data:
        phy_subjects[i[0]]=int(i[1])+1  
    for w in phy_subjects:
        my_database.execute("Select Teacher_Name from master_teacher where Sub='{}' and Section='{}'".format(w,sec))
        teach=my_database.fetchall()[0][0]
        #print(teach)
        if teach=="":
            teach="Mr.X"
        phy_teachers[w]=teach
        my_database.execute("Update student_table set Teacher_Name='{}' where Sub='{}' and Section='{}'".format(phy_teachers[w],w,sec))
        mydb.commit()
    Section_Label.configure(text="Teacher Update Successful")

def subject_allotment(sec):
    """
    The function `subject_allotment` is used to assign subjects to periods and teachers based on certain
    conditions and constraints.
    
    :param sec: The parameter "sec" represents the section for which the subject allotment needs to be
    done
    """
    days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    periods=['Period 1','Period 2','Period 3','Period 4','Period 5','Period 6','Period 7','Period 8','Period 9']
    half_day_periods=['Period 1','Period 2','Period 3','Period 4','Period 5','Period 6']
    phy_subjects={}
    phy_teachers={}
        
    unocc="unoccupied"
    #random.shuffle(phy_subjects)
    my_database.execute("Select Sub,Credits from master_teacher where Section='{}'".format(sec))
    data=my_database.fetchall()
    for i in data:
        phy_subjects[i[0]]=int(i[1])+1
    print(phy_subjects)
    for w in phy_subjects:
        #print(w)
        my_database.execute("Select Teacher_Name from master_teacher where Sub='{}' and Section='{}'".format(w,sec))
        teach=my_database.fetchall()[0][0]
        print(teach)
        if teach=="":
            teach="Mr.X"
        phy_teachers[w]=teach
        
        for day in days:
            for period in periods:
                my_database.execute("Select count(0) from student_table where WeekDay='{}' and Sub='{}' and Section='{}'".format(day,unocc,sec))
                master_day=my_database.fetchall()[0][0]
                if master_day>3:
                    my_database.execute("Select count(0) from student_table where Sub='{}' and Section='{}'".format(w,sec))
                    week_count=my_database.fetchall()[0][0]
                    if int(week_count)<phy_subjects[w]:
                        my_database.execute("Select count(0) from student_table where Sub='{}' and WeekDay='{}' and Section='{}'".format(w,day,sec))
                        day_count=my_database.fetchall()[0][0]
                        if day_count<2:
                            my_database.execute("Select count(0) from student_table where Period='{}' and WeekDay='{}' and Teacher_Name='{}'".format(period,day,phy_teachers[w]))
                            double_class_check=my_database.fetchall()[0][0]
                            if double_class_check==0:
                                my_database.execute("Select Sub from student_table where Period='{}' and WeekDay='{}' and Section='{}'".format(period,day,sec))
                                data=my_database.fetchall()[0][0]
                            
                                if data==unocc:
                                    if random.randint(1,2)==2:
                                        my_database.execute("Update student_table set Sub='{}',Teacher_Name='{}' where Period='{}' and WeekDay='{}' and Section='{}'".format(w,phy_teachers[w],period,day,sec))
                                        mydb.commit()
                                    
    left_out_periods=['Period 7','Period 8','Period 9']
    for w in phy_subjects:
        for day in days:
            for period in left_out_periods:
                    my_database.execute("Select count(0) from student_table where Sub='{}' and Section='{}'".format(w,sec))
                    week_count=my_database.fetchall()[0][0]
                    if week_count<phy_subjects[w]:
                        my_database.execute("Select count(0) from student_table where Sub='{}' and WeekDay='{}' and Section='{}'".format(w,day,sec))
                        day_count=my_database.fetchall()[0][0]
                        if day_count<2:
                            my_database.execute("Select count(0) from student_table where Period='{}' and WeekDay='{}' and Teacher_Name='{}'".format(period,day,phy_teachers[w]))
                            double_class_check=my_database.fetchall()[0][0]
                            if double_class_check==0:
                                my_database.execute("Select Sub from student_table where Period='{}' and WeekDay='{}' and Section='{}'".format(period,day,sec))
                                data=my_database.fetchall()[0][0]
                            
                                if data==unocc:
                                    if random.randint(1,2)==2:
                                        my_database.execute("Update student_table set Sub='{}',Teacher_Name='{}' where Period='{}' and WeekDay='{}' and Section='{}'".format(w,phy_teachers[w],period,day,sec))
                                        mydb.commit()
                                        
def add_teacher(name,sub,creds,sec):
    """
    The function `add_teacher` adds a teacher to a specific section in a database, with the teacher's
    name, subject, credentials, and section as input parameters.
    
    :param name: The name parameter is the name of the teacher that you want to add
    :param sub: sub is the subject that the teacher teaches
    :param creds: The parameter "creds" in the "add_teacher" function is used to specify the credentials
    or qualifications of the teacher being added
    :param sec: sec refers to the section or class for which the teacher is being added. It is a string
    that represents the section or class identifier
    :return: The function does not explicitly return anything.
    """
    Section_Label.configure(text="")
    if name=="" or sub=="" or sec=="":
        Section_Label.configure(text="Fill all the fields")
        return
    my_database.execute("Select count(0) from login_info where User_Name='{}' and User_Role='Teacher'".format(name))
    if my_database.fetchall()[0][0]==0:
        Section_Label.configure(text="Teacher not found")
        return
            
    my_database.execute("Select sub from master_teacher where Section='{}'".format(sec))
    subject=my_database.fetchall()
    default_teachers={}
    if len(subject)==0:
        print("Empty!")
        default_teachers[sub]="Mr."+sub
    for w in subject:
        print(w[0])
        if sub not in w[0]:
            print(sub)
            default_teachers[sub]="Mr."+w[0]
    print(default_teachers)
    my_database.execute("Select count(0) from master_teacher where  Sub='{}' and Section='{}'".format(sub,sec))
    record= my_database.fetchall()
    if len(record)==0 or record[0][0]==0:
        for substitute in default_teachers:
            my_database.execute("Insert into master_teacher values('%s','%s','%s','%s')"%(default_teachers[substitute],substitute,sec,creds))
            mydb.commit()
    my_database.execute("Update master_teacher set Teacher_Name='{}' where Sub='{}' and Section='{}'".format(name,sub,sec))
    mydb.commit()
    addition_of_section(sec)



def salvador(name,passw,role,prn,num,section):
    """
    The function `salvador` takes in several parameters, including name, password, role, PRN, number,
    and section, and performs various operations based on the values of these parameters.
    
    :param name: The name of the user. It is a string value
    :param passw: The parameter "passw" is used to store the password for the user
    :param role: The role parameter is used to specify the role of the user. It can be either "Teacher"
    or "Student"
    :param prn: PRN stands for "Permanent Registration Number". It is a unique identification number
    assigned to each student or individual in an educational institution or organization
    :param num: The parameter "num" represents the phone number of the user
    :param section: The section parameter is used to specify the section of a class. It is typically
    used in educational settings to differentiate between different groups of students within the same
    class
    :return: The function does not explicitly return anything.
    """
    print(name,passw,role,prn)
    if name=="" or passw=="" or role=="" or prn=="":
        l4.configure(text="Fill all the fields")
        print("No fields")
        return
    else:
        if role=="Teacher":
            section=""
        elif role=="Student":
            num=""
        my_database.execute("Select count(0) from login_info where User_Name='{}' and PRN='{}'".format(name,prn))
        record=my_database.fetchall()
        print(record)
        if record[0][0]==0:
            my_database.execute('Insert into login_info(User_Name,PassWord,User_Role,PRN,Phone_No,section) values("%s","%s","%s","%s","%s","%s")'%(name,passw,role,prn,num,section))
            mydb.commit()
            l4.configure(text="Added!")
        else:
            my_database.execute("Update login_info set PassWord='{}',User_Role='{}',Phone_No='{}',section='{}' where User_name='{}' and PRN='{}'".format(passw,role,num,section,name,prn,section))
            mydb.commit()
            l4.configure(text="Updated!")
def deletion_of_student(prn,student):
    """
    The function `deletion_of_student` deletes a student from a database based on their PRN (Personal
    Registration Number) and username.
    
    :param prn: PRN (Permanent Registration Number) is a unique identification number assigned to each
    student in a college or university. It is used to identify the student in various administrative and
    academic processes
    :param student: The "student" parameter is the name of the student that you want to delete from the
    database
    :return: nothing.
    """
    if prn=="" or student=="":
        l4.configure(text="Fill all the fields")
        print("No fields")
        return
    else:
        my_database.execute("select count(0) from login_info where PRN='{}' and User_Name ='{}'".format(prn,student))
        if (my_database.fetchall()[0][0]==0):
            print("User does not exist")
            l3.configure(text="User does not exist")

        else:
            my_database.execute("Delete from login_info where PRN='{}' and User_Name='{}'".format(prn,student))
            mydb.commit()
            l3.configure(text="Deleted!")

def update_of_timetable(sub1,sub2,sec,period,day):
    """
    The function `update_of_timetable` updates the timetable of a student by replacing one subject with
    another subject for a specific section, period, and day.
    
    :param sub1: The current subject that needs to be updated in the timetable
    :param sub2: The new subject that you want to update in the timetable
    :param sec: The "sec" parameter represents the section of the student. It is used to identify the
    specific section of students for which the timetable is being updated
    :param period: The parameter "period" refers to the specific period or class time slot for which you
    want to update the timetable. It could be a number or a string representing the period, such as "1st
    period", "2nd period", "Period 3", etc
    :param day: The day parameter represents the day of the week for which the timetable is being
    updated
    :return: nothing (None).
    """
    if sub1=="" or sub2=="" or sec=="" or period=="" or day=="":
        l3.configure(text="Enter all fields")
        return
    my_database.execute("Select count(0) from student_table where Sub='{}' and Section='{}' and Period='{}' and WeekDay='{}'".format(sub1,sec,period,day))
    subject_exists=my_database.fetchall()[0][0]
    if subject_exists==0:
        l3.configure(text="Subject/Period is wrong!")
    else:
        my_database.execute("Select Teacher_Name from master_teacher where Sub='{}' and Section='{}'")
        teacher=my_database.fetchall()[0][0]
        my_database.execute("Update student_table set Sub='{}',Teacher_Name='{}' where Sub='{}' and Section='{}' and Period='{}' and WeekDay='{}'".format(sub2,teacher,sub1,sec,period,day))
        mydb.commit()
        l3.configure(text="Updated!")
    return


    



###PAGE 0:ADD USER

user_page=w.CTkFrame(admin,width=admin.winfo_screenwidth(),height=s,fg_color='#0b3444')
user_page.pack()
user_page.grid_rowconfigure(0, weight= 1)
user_page.grid_rowconfigure(4, weight= 2)



image1=w.CTkImage(dark_image=open(r"C:\Users\pg401\Downloads\image files\blue_bg.png"),size=(t,s))
bg_img=w.CTkLabel(user_page,text="",image=image1)
bg_img.place(relx=0,rely=0,relheight=1,relwidth=1)



title=w.CTkFrame(user_page,width=0.5*s,height=0.5*t,fg_color='#0b3444')
title.place(relx=0.47,rely=0.20,anchor='center')
title_label=w.CTkLabel(title,text="Add User",pady=10,height=10,font=("Product Sans",35))
title_label.place(relx=0.35,rely=0.4)

button_frame=w.CTkFrame(user_page,width=t,height=s/9,fg_color='#0b3444')
button_frame.grid(row=0)
b0=w.CTkButton(button_frame,text="Add User",command=lambda:None)
b0.place(relx=0.057,rely=0.5,anchor='center')
b1=w.CTkButton(button_frame,text="Assign Teacher",command=lambda:show_teacher())
b1.place(relx=0.167,rely=0.5,anchor='center')
b2=w.CTkButton(button_frame,text="Show Section",command=lambda:show_section1())
b2.place(relx=0.2775,rely=0.5,anchor='center')
b3=w.CTkButton(button_frame,text="Teach TT",command=lambda:show_teacher1())
b3.place(relx=0.388,rely=0.5,anchor='center')
b4=w.CTkButton(button_frame,text="Delete Student",command=lambda:show_deletion())
b4.place(relx=0.499,rely=0.5,anchor='center')
b5=w.CTkButton(button_frame,text="Update TimeTable",command=lambda:show_update())
b5.place(relx=0.61,rely=0.5,anchor='center')

page2=w.CTkFrame(user_page,fg_color='#0b3444')
page2.grid(row=2,pady=230)
page2.grid_rowconfigure(3, weight= 1)

User_name=tk.StringVar()
Pass_Word=tk.StringVar()
Role=tk.StringVar()
PRN=tk.StringVar()
Phone_No=tk.StringVar()
Sect=tk.StringVar()


e0=w.CTkEntry(page2,textvariable=User_name,width=100)
l0=w.CTkLabel(page2,text="Enter UserName")
l0.grid(row = 0, column = 0, sticky = 'nsew', padx = 20, pady = 2)
e0.grid(row = 0, column = 1, sticky = 'nsew', padx = 20, pady = 2)
#Input password
e1=w.CTkEntry(page2,textvariable=Pass_Word,width=100)
e1.grid(row = 1, column = 1, sticky = 'nsew', padx = 20, pady = 2)
e1.bind("<Up>",focus_previous_widget)
l1=w.CTkLabel(page2,text="Enter Password")
l1.grid(row = 1, column = 0, sticky = 'nsew', padx = 20, pady = 2)
e2=w.CTkEntry(page2,textvariable=Role,width=100)
e2.bind("<Up>",focus_previous_widget)
e2.grid(row = 2, column = 1, sticky = 'nsew', padx = 20, pady = 2)
l2=w.CTkLabel(page2,text="Enter Role")
l2.grid(row = 2, column = 0, sticky = 'nsew', padx = 20, pady = 2)
e3=w.CTkEntry(page2,textvariable=PRN,width=100)
e3.grid(row = 3, column = 1, sticky = 'nsew', padx = 20, pady = 2)
e3.bind("<Up>",focus_previous_widget)
l3=w.CTkLabel(page2,text="Enter PRN")
l3.grid(row = 3, column = 0, sticky = 'nsew', padx = 20, pady = 2)
e4=w.CTkEntry(page2,textvariable=Phone_No,width=100)
e4.grid(row = 4, column = 1, sticky = 'nsew', padx = 20, pady = 2)
e4.bind("<Up>",focus_previous_widget)
l4=w.CTkLabel(page2,text="Enter Phone_No")
l4.grid(row = 4, column = 0, sticky = 'nsew', padx = 20, pady = 2)
e5=w.CTkEntry(page2,textvariable=Sect,width=100)
e5.grid(row = 5, column = 1, sticky = 'nsew', padx = 20, pady = 2)
e5.bind("<Up>",focus_previous_widget)
l5=w.CTkLabel(page2,text="Enter Section")
l5.grid(row = 5, column = 0, sticky = 'nsew', padx = 20, pady = 2)


#Save Button
save_frame=w.CTkFrame(user_page,width=0.1*page2.winfo_width(),height=0.1*page2.winfo_height(),fg_color='#0b3444')
save_frame.place(relx=0.5,rely=0.72,anchor='center')
save_frame.grid_rowconfigure(2,weight=1)
b0=w.CTkButton(save_frame,text="Save",fg_color='#0b3444',command=lambda:salvador(User_name.get(),Pass_Word.get(),Role.get(),PRN.get(),Phone_No.get(),Sect.get()))
b0.grid(row = 0, column = 0, columnspan = 1, sticky = 'nsew')
l4=w.CTkLabel(save_frame,text="",fg_color='#0b3444')
l4.grid(row = 1, column = 0, columnspan = 1, sticky = 'nsew')







####PAGE 1:Assign Teachers####

teacher_page=w.CTkFrame(admin,width=admin.winfo_screenwidth(),height=s,fg_color='#0b3444')
teacher_page.pack()


teacher_page.grid_rowconfigure(0, weight= 1)
teacher_page.grid_rowconfigure(3, weight= 2)

image1=w.CTkImage(dark_image=open(r"C:\Users\pg401\Downloads\image files\blue_bg.png"),size=(t,s))
bg_img=w.CTkLabel(teacher_page,text="",image=image1)
bg_img.place(relx=0,rely=0,relheight=1,relwidth=1)


title=w.CTkFrame(teacher_page,width=0.5*s,height=0.5*t,fg_color='#0b3444')
title.place(relx=0.47,rely=0.20,anchor='center')
title_label=w.CTkLabel(title,text="Assign Teacher",pady=10,height=10,font=("Product Sans",35))
title_label.place(relx=0.35,rely=0.4)


button_frame=w.CTkFrame(teacher_page,width=t,height=s/9,fg_color='#0b3444')
button_frame.grid(row=0)
b0=w.CTkButton(button_frame,text="Add User",command=lambda:show_user())
b0.place(relx=0.057,rely=0.5,anchor='center')
b1=w.CTkButton(button_frame,text="Assign Teacher",command=lambda:None)
b1.place(relx=0.167,rely=0.5,anchor='center')
b2=w.CTkButton(button_frame,text="Show Section",command=lambda:show_section1())
b2.place(relx=0.2775,rely=0.5,anchor='center')
b3=w.CTkButton(button_frame,text="Teach TT",command=lambda:show_teacher1())
b3.place(relx=0.388,rely=0.5,anchor='center')
b4=w.CTkButton(button_frame,text="Delete Student",command=lambda:show_deletion())
b4.place(relx=0.499,rely=0.5,anchor='center')
b5=w.CTkButton(button_frame,text="Update TimeTable",command=lambda:show_update())
b5.place(relx=0.61,rely=0.5,anchor='center')

page1=w.CTkFrame(teacher_page,fg_color='#0b3444')
page1.grid(row=2,pady=260)
page1.grid_rowconfigure(3, weight= 1)
Teacher_Name=tk.StringVar()
SubJect=tk.StringVar()
SecTion=tk.StringVar()
Credits=tk.StringVar()
#Input Name
e0=w.CTkEntry(page1,textvariable=Teacher_Name,width=100)
l0=w.CTkLabel(page1,text="Enter Teacher_Name")
l0.grid(row = 0, column = 0, sticky = 'nsew', padx = 20, pady = 2)
e0.grid(row = 0, column = 1, sticky = 'nsew', padx = 20, pady = 2)
#Input password
e1=w.CTkEntry(page1,textvariable=SubJect,width=100)
e1.grid(row = 1, column = 1, sticky = 'nsew', padx = 20, pady = 2)
#Binding
e1.bind("<Tab>",focus_next_window)
l1=w.CTkLabel(page1,text="Enter Subject")
l1.grid(row = 1, column = 0, sticky = 'nsew', padx = 20, pady = 2)
e2=w.CTkEntry(page1,textvariable=Credits,width=100)
e2.grid(row = 2, column = 1, sticky = 'nsew', padx = 20, pady = 2)
l2=w.CTkLabel(page1,text="Enter Credits")
l2.grid(row = 2, column = 0, sticky = 'nsew', padx = 20, pady = 2)
e3=w.CTkEntry(page1,textvariable=SecTion,width=100)
e3.grid(row = 3, column = 1, sticky = 'nsew', padx = 20, pady = 2)
l3=w.CTkLabel(page1,text="Enter Section")
l3.grid(row = 3, column = 0, sticky = 'nsew', padx = 20, pady = 2)
#Save Button
print(Teacher_Name.get(),SubJect.get(),SecTion.get())
save_frame=w.CTkFrame(teacher_page,width=0.1*page1.winfo_width(),height=0.2*page1.winfo_height(),fg_color='#0b3444')
save_frame.place(relx=0.5,rely=0.69,anchor='center')
save_frame.grid_rowconfigure(2,weight=1)
b0=w.CTkButton(save_frame,text="Save",fg_color='#0b3444',command=lambda:add_teacher(Teacher_Name.get(),SubJect.get(),Credits.get(),SecTion.get()))
b0.grid(row = 0, column = 0, columnspan = 1, sticky = 'nsew')
Section_Label=w.CTkLabel(save_frame,text="",fg_color='#0b3444')
Section_Label.grid(row = 1, column = 0, columnspan = 1, sticky = 'nsew')














####PAGE2(A):Show Section####


section1_page=w.CTkFrame(admin,width=admin.winfo_screenwidth(),height=s,fg_color='#0b3444')
section1_page.pack()
section1_page.grid_rowconfigure(0, weight= 1)
section1_page.grid_rowconfigure(3, weight= 2)
image1=w.CTkImage(dark_image=open(r"C:\Users\pg401\Downloads\image files\blue_bg.png"),size=(t,s))
bg_img=w.CTkLabel(section1_page,text="",image=image1)
bg_img.place(relx=0,rely=0,relheight=1,relwidth=1)
title=w.CTkFrame(section1_page,width=0.5*s,height=0.5*t,fg_color='#0b3444')

title.place(relx=0.47,rely=0.20,anchor='center')
title_label=w.CTkLabel(title,text="Show Section TT",pady=10,height=10,font=("Product Sans",35))
title_label.place(relx=0.28,rely=0.7)

a1=tk.StringVar()
a2=tk.StringVar()
a3=tk.StringVar()

button_frame=w.CTkFrame(section1_page,width=t,height=s/9,fg_color='#0b3444')
button_frame.grid(row=0)
b0=w.CTkButton(button_frame,text="Add User",command=lambda:show_user())
b0.place(relx=0.057,rely=0.5,anchor='center')
b1=w.CTkButton(button_frame,text="Assign Teacher",command=lambda:show_teacher())
b1.place(relx=0.167,rely=0.5,anchor='center')
b2=w.CTkButton(button_frame,text="Show Section",command=lambda:None)
b2.place(relx=0.2775,rely=0.5,anchor='center')
b3=w.CTkButton(button_frame,text="Teach TT",command=lambda:show_teacher1())
b3.place(relx=0.388,rely=0.5,anchor='center')
b4=w.CTkButton(button_frame,text="Delete Student",command=lambda:show_deletion())
b4.place(relx=0.499,rely=0.5,anchor='center')
b5=w.CTkButton(button_frame,text="Update TimeTable",command=lambda:show_update())
b5.place(relx=0.61,rely=0.5,anchor='center')

page2=w.CTkFrame(section1_page,fg_color='#0b3444')
page2.grid(row=2,pady=310)
page2.grid_rowconfigure(3, weight= 1)



student=tk.StringVar()

e2=w.CTkEntry(page2,textvariable=student,width=100)
e2.grid(row = 3, column = 1, sticky = 'nsew', padx = 20, pady = 2)
l2=w.CTkLabel(page2,text="Enter Section")
l2.grid(row = 3, column = 0, sticky = 'nsew', padx = 20, pady = 2)
#Save Button
save_frame=w.CTkFrame(section1_page,width=0.1*page2.winfo_width(),height=0.1*page2.winfo_height(),fg_color='#0b3444')
save_frame.place(relx=0.5,rely=0.68,anchor='center')
save_frame.grid_rowconfigure(2,weight=1)

b0=w.CTkButton(save_frame,text="Save",fg_color='#0b3444',command=lambda:show_section2())
b0.grid(row = 0, column = 0, columnspan = 1, sticky = 'nsew')
l3=w.CTkLabel(save_frame,text="",fg_color='#0b3444')
l3.grid(row = 1, column = 0, columnspan = 1, sticky = 'nsew')


###PAGE3:SECTION TIMETABLE
section2_page=w.CTkFrame(admin, height = admin.winfo_screenheight(), width = s/9,fg_color='#0b3444')
section2_page.pack()
image1=w.CTkImage(dark_image=open(r"C:\Users\pg401\Downloads\image files\blue_bg.png"),size=(t,s))
bg_img=w.CTkLabel(section2_page,text="",image=image1)
bg_img.place(relx=0,rely=0,relheight=1,relwidth=1)



def section_table():

    section=student.get()
    title="  "+section+" "+"TimeTable"
    print(title)
    
    #style=Style()
    #style.configure('TButton',font=('arial',10,'bold'),borderwidth='4')
    #style.map(style.map('W.TButton', foreground = [('active', '!disabled', 'blue')],background = [('active', 'white')],))
    
    button_frame=w.CTkFrame(section2_page,width=t,height=s/9,fg_color='#0b3444')
    button_frame.pack()
    b0=w.CTkButton(button_frame,text="Go Back",command=lambda:restart_app())
    b0.place(relx=0.057,rely=0.5,anchor='center')


    game_frame = w.CTkFrame(section2_page,width=10080,height=1220,fg_color='#0b3444')
    game_frame.grid_rowconfigure(1,weight=1)
    game_frame.grid_columnconfigure(0,weight=3)
    game_frame.grid_columnconfigure(1,weight=1)
    head_text=w.CTkTextbox(game_frame,fg_color='#0b3444',font=("Product Sans",30),width=300)
    head_text.place(relx=0.5,rely=0.3,anchor='center')
    head_text.insert(w.END,title)
    game_frame.pack(padx=100,pady=120,expand=1,fill='both')

    
    my_tt = tk.ttk.Treeview(game_frame)
    
    my_tt.place(relx=0.5,rely=0.35,anchor='center')
    my_tt['columns'] = ('WeekDay','1st Slot','2nd Slot','3rd Slot', '4th Slot','5th Slot','6th Slot','7th Slot','8th Slot','9th Slot')
    my_tt.column('#0',width=0,stretch=0)
    my_tt.column('WeekDay',anchor='center',width=80)
    my_tt.column('1st Slot',anchor='center',width=80)
    my_tt.column('2nd Slot',anchor='center',width=80)
    my_tt.column('3rd Slot',anchor='center',width=80)
    my_tt.column('4th Slot',anchor='center',width=80)
    my_tt.column('5th Slot',anchor='center',width=80)
    my_tt.column('6th Slot',anchor='center',width=80)
    my_tt.column('7th Slot',anchor='center',width=80)
    my_tt.column('8th Slot',anchor='center',width=80)
    my_tt.column('9th Slot',anchor='center',width=80,)
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
    
    for day in days:
        in_day=day
        my_database.execute("Select Sub from student_table where WeekDay='{}' and Section='{}'".format(in_day,section))
        baby_data=my_database.fetchall()
        day_tup=(in_day,)
        baby_data.insert(0,day_tup)
        my_tt.insert('',END, values=baby_data)
        print(baby_data)
    

    

####PAGE 4:TEACHER TIMETABLE
teacher1_page=w.CTkFrame(admin,width=admin.winfo_screenwidth(),height=s,fg_color='#0b3444')
teacher1_page.pack()
teacher1_page.grid_rowconfigure(0, weight= 1)
teacher1_page.grid_rowconfigure(3, weight= 2)

image1=w.CTkImage(dark_image=open(r"C:\Users\pg401\Downloads\image files\blue_bg.png"),size=(t,s))
bg_img=w.CTkLabel(teacher1_page,text="",image=image1)
bg_img.place(relx=0,rely=0,relheight=1,relwidth=1)

title=w.CTkFrame(teacher1_page,width=0.5*s,height=0.5*t,fg_color='#0b3444')
title.place(relx=0.47,rely=0.20,anchor='center')
title_label=w.CTkLabel(title,text="Show Teacher",pady=10,height=10,font=("Product Sans",35))
title_label.place(relx=0.34,rely=0.7)

a1=tk.StringVar()
a2=tk.StringVar()
a3=tk.StringVar()

button_frame=w.CTkFrame(teacher1_page,width=t,height=s/8,fg_color='#0b3444')
button_frame.grid(row=0)
b0=w.CTkButton(button_frame,text="Add User",command=lambda:show_user())
b0.place(relx=0.057,rely=0.5,anchor='center')
b1=w.CTkButton(button_frame,text="Assign Teacher",command=lambda:show_teacher())
b1.place(relx=0.167,rely=0.5,anchor='center')
b2=w.CTkButton(button_frame,text="Show Section",command=lambda:show_section1())
b2.place(relx=0.2775,rely=0.5,anchor='center')
b3=w.CTkButton(button_frame,text="Teach TT",command=lambda:None)
b3.place(relx=0.388,rely=0.5,anchor='center')
b4=w.CTkButton(button_frame,text="Delete Student",command=lambda:show_deletion())
b4.place(relx=0.499,rely=0.5,anchor='center')
b5=w.CTkButton(button_frame,text="Update TimeTable",command=lambda:show_update())
b5.place(relx=0.61,rely=0.5,anchor='center')

page3=w.CTkFrame(teacher1_page,fg_color='#0b3444')
page3.grid(row=2,pady=310)
page3.grid_rowconfigure(3, weight= 1)
Teach=tk.StringVar()







e2=w.CTkEntry(page3,textvariable=Teach,width=100)
e2.grid(row = 3, column = 1, sticky = 'nsew', padx = 20, pady = 2)
l2=w.CTkLabel(page3,text="Enter Teacher Name")
l2.grid(row = 3, column = 0, sticky = 'nsew', padx = 20, pady = 2)
#Save Button
save_frame=w.CTkFrame(teacher1_page,width=0.1*page3.winfo_width(),height=0.1*page3.winfo_height(),fg_color='#0b3444')
save_frame.place(relx=0.5,rely=0.69,anchor='center')
save_frame.grid_rowconfigure(2,weight=1)
b0=w.CTkButton(save_frame,text="Save",fg_color='#0b3444',command=lambda:show_teacher2())
b0.grid(row = 0, column = 0, columnspan = 1, sticky = 'nsew')
l3=w.CTkLabel(save_frame,text="",fg_color='#0b3444')
l3.grid(row = 1, column = 0, columnspan = 1, sticky = 'nsew')


###PAGE4:TEACHER TIMETABLE
teacher2_page=w.CTkFrame(admin, height = 1920, width = 1080,fg_color='#0b3444')
teacher2_page.pack()

image1=w.CTkImage(dark_image=open(r"C:\Users\pg401\Downloads\image files\blue_bg.png"),size=(t,s))
bg_img=w.CTkLabel(teacher2_page,text="",image=image1)
bg_img.place(relx=0,rely=0,relheight=1,relwidth=1)

button_frame=w.CTkFrame(teacher2_page,width=t,height=s/9,fg_color='#0b3444')
button_frame.pack()
b0=w.CTkButton(button_frame,text="Go Back",command=lambda:restart_app())
b0.place(relx=0.057,rely=0.5,anchor='center')


def teacher_table():
    Teacher_Name=Teach.get()
    #print(Teacher_Name)

    title="  "+Teacher_Name+" "+"TT"

    #style=Style()
    #style.configure('TButton',font=('arial',10,'bold'),borderwidth='4')
    #style.map(style.map('W.TButton', foreground = [('active', '!disabled', 'blue')],background = [('active', 'white')],))





    game_frame = w.CTkFrame(teacher2_page,width=1080,height=1920,fg_color='#0b3444')
    game_frame.grid_rowconfigure(1,weight=1)
    game_frame.grid_columnconfigure(0,weight=3)
    game_frame.grid_columnconfigure(1,weight=1)
    head_text=w.CTkTextbox(game_frame,fg_color='#0b3444',font=("Product Sans",26))
    head_text.place(relx=0.5,rely=0.3,anchor='center')
    head_text.insert(w.END,title)
    game_frame.pack(padx=200,pady=168,expand=1,fill='both')
    


    my_tt = tk.ttk.Treeview(game_frame)
    my_tt.place(relx=0.5,rely=0.35,anchor='center')
    my_tt['columns'] = ('WeekDay','1st Slot','2nd Slot','3rd Slot', '4th Slot','5th Slot','6th Slot','7th Slot','8th Slot','9th Slot')
    my_tt.column('#0',width=0,stretch=0)
    my_tt.column('WeekDay',anchor='center',width=80)
    my_tt.column('1st Slot',anchor='center',width=80)
    my_tt.column('2nd Slot',anchor='center',width=80)
    my_tt.column('3rd Slot',anchor='center',width=80)
    my_tt.column('4th Slot',anchor='center',width=80)
    my_tt.column('5th Slot',anchor='center',width=80)
    my_tt.column('6th Slot',anchor='center',width=80)
    my_tt.column('7th Slot',anchor='center',width=80)
    my_tt.column('8th Slot',anchor='center',width=80)
    my_tt.column('9th Slot',anchor='center',width=80,)
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
    periods=['Period 1','Period 2','Period 3','Period 4','Period 5','Period 6','Period 7','Period 8','Period 9']
    print(Teacher_Name)
    my_database.execute("Select * from student_table where Teacher_Name='{}'".format(Teacher_Name))
    all_data=my_database.fetchall()
    for day in days:
        baby_data=[]
        in_day=day
        for period in periods:
            my_database.execute("Select Sub,Section from student_table where WeekDay='{}' and Teacher_Name='{}' and Period='{}'".format(in_day,Teacher_Name,period))
            infant_data=my_database.fetchall()
            #print(infant_data)
            unocc_tuple=('Unoccupied',)
            if len(infant_data)<1:
                infant_data.insert(0,unocc_tuple)
        #print(infant_data)
            baby_data.append(infant_data[0])
    #baby_data=my_database.fetchall()
        day_tup=(in_day,)
        baby_data.insert(0,day_tup)
        my_tt.insert(parent='',index='end',text='',
        values=(baby_data))
        #print(baby_data)
        


#####PAGE5:STUDENT ADDITION
delete_page=w.CTkFrame(admin,width=admin.winfo_screenwidth(),height=s/9,fg_color='#0b3444')
delete_page.pack()
delete_page.grid_rowconfigure(0, weight= 1)
delete_page.grid_rowconfigure(3, weight= 2)
image1=w.CTkImage(dark_image=open(r"C:\Users\pg401\Downloads\image files\blue_bg.png"),size=(t,s))
bg_img=w.CTkLabel(delete_page,text="",image=image1)
bg_img.place(relx=0,rely=0,relheight=1,relwidth=1)

title=w.CTkFrame(delete_page,width=0.5*s,height=0.5*t,fg_color='#0b3444')
title.place(relx=0.47,rely=0.20,anchor='center')
title_label=w.CTkLabel(title,text="Delete Student",pady=10,height=10,font=("Product Sans",35))
title_label.place(relx=0.34,rely=0.6)

a1=tk.StringVar()
a2=tk.StringVar()
a3=tk.StringVar()

button_frame=w.CTkFrame(delete_page,width=t,height=s/8,fg_color='#0b3444')
button_frame.grid(row=0)
b0=w.CTkButton(button_frame,text="Add User",command=lambda:show_user())
b0.place(relx=0.057,rely=0.5,anchor='center')
b1=w.CTkButton(button_frame,text="Assign Teacher",command=lambda:show_teacher())
b1.place(relx=0.167,rely=0.5,anchor='center')
b2=w.CTkButton(button_frame,text="Show Section",command=lambda:show_section1())
b2.place(relx=0.2775,rely=0.5,anchor='center')
b3=w.CTkButton(button_frame,text="Teach TT",command=lambda:show_teacher1())
b3.place(relx=0.388,rely=0.5,anchor='center')
b4=w.CTkButton(button_frame,text="Delete Student",command=lambda:None)
b4.place(relx=0.499,rely=0.5,anchor='center')
b5=w.CTkButton(button_frame,text="Update TimeTable",command=lambda:show_update())
b5.place(relx=0.61,rely=0.5,anchor='center')


page3=w.CTkFrame(delete_page,fg_color='#0b3444')
page3.grid(row=2,pady=300)
page3.grid_rowconfigure(3, weight= 1)
a1=tk.StringVar()
a2=tk.StringVar()
a3=tk.StringVar()




e1=w.CTkEntry(page3,textvariable=a1,width=100)
e1.grid(row = 1, column = 1, sticky = 'nsew', padx = 20, pady = 2)
l1=w.CTkLabel(page3,text="Enter PRN")
l1.grid(row = 1, column = 0, sticky = 'nsew', padx = 20, pady = 2)
e2=w.CTkEntry(page3,textvariable=a2,width=100)
e2.grid(row = 3, column = 1, sticky = 'nsew', padx = 20, pady = 2)
l2=w.CTkLabel(page3,text="Enter Student Name")
l2.grid(row = 3, column = 0, sticky = 'nsew', padx = 20, pady = 2)

#Save Button
save_frame=w.CTkFrame(delete_page,width=0.1*page3.winfo_width(),height=0.1*page3.winfo_height(),fg_color='#0b3444')
save_frame.place(relx=0.5,rely=0.68,anchor='center')
save_frame.grid_rowconfigure(2,weight=1)
b0=w.CTkButton(save_frame,text="Save",fg_color='#0b3444',command=lambda:deletion_of_student(a1.get(),a2.get()))
b0.grid(row = 0, column = 0, columnspan = 1, sticky = 'nsew')
l3=w.CTkLabel(save_frame,text="",fg_color='#0b3444')
l3.grid(row = 1, column = 0, columnspan = 1, sticky = 'nsew')




#####PAGE6:UPDATE TIMETABLE
update_page=w.CTkFrame(admin,width=admin.winfo_screenwidth(),height=s,fg_color='#0b3444')
update_page.pack()
image1=w.CTkImage(dark_image=open(r"C:\Users\pg401\Downloads\image files\blue_bg.png"),size=(t,s))
bg_img=w.CTkLabel(update_page,text="",image=image1)
bg_img.place(relx=0,rely=0,relheight=1,relwidth=1)
title=w.CTkFrame(update_page,width=0.5*s,height=0.5*t,fg_color='#0b3444')
title.place(relx=0.47,rely=0.20,anchor='center')
title_label=w.CTkLabel(title,text="Update TT",pady=10,height=10,font=("Product Sans",35))
title_label.place(relx=0.47,rely=0.6)

update_page.grid_rowconfigure(0, weight= 1)
update_page.grid_rowconfigure(4, weight= 2)

button_frame=w.CTkFrame(update_page,width=t,height=s/9,fg_color='#0b3444')
button_frame.grid(row=0)
b0=w.CTkButton(button_frame,text="Add User",command=lambda:show_user())
b0.place(relx=0.057,rely=0.5,anchor='center')
b1=w.CTkButton(button_frame,text="Assign Teacher",command=lambda:show_teacher())
b1.place(relx=0.167,rely=0.5,anchor='center')
b2=w.CTkButton(button_frame,text="Show Section",command=lambda:show_section1())
b2.place(relx=0.2775,rely=0.5,anchor='center')
b3=w.CTkButton(button_frame,text="Teach TT",command=lambda:show_teacher1())
b3.place(relx=0.388,rely=0.5,anchor='center')
b4=w.CTkButton(button_frame,text="Delete Student",command=lambda:show_deletion())
b4.place(relx=0.499,rely=0.5,anchor='center')
b5=w.CTkButton(button_frame,text="Update TimeTable",command=lambda:None)
b5.place(relx=0.61,rely=0.5,anchor='center')

page4=w.CTkFrame(update_page,fg_color='#0b3444')
page4.grid(row=2,pady=240)
page4.grid_rowconfigure(3, weight= 1)

sub_list=[]
sec_list=[]
period_list=[]
day_list=[]
selected_subject_origin=tk.StringVar()
selected_subject_destination=tk.StringVar()
selected_day=tk.StringVar()
selected_period=tk.StringVar()
selected_period=tk.StringVar()
selected_section=tk.StringVar()
my_database.execute("Select Section,Weekday,Period,Sub from student_table")
for q in my_database.fetchall():
    sub_list.append(q[3])
    sec_list.append(q[0])
    period_list.append(q[2])

sub_list=list(set(sub_list))
sec_list=list(set(sec_list))
period_list=list(set(period_list))
day_list=['Monday','Tuesday','Wednesday','Thursday','Friday']
period_list.sort()

#MAKE DRAG DOWN OPTIONS TO SELECT WHICH PERIOD TO UPDATE
subject_selection_origin=w.CTkOptionMenu(page4,variable=selected_subject_origin,values=sub_list,command=None)
subject_selection_origin.grid(row=3,column=1,padx=20)
subject_label_origin=w.CTkLabel(page4,text="Select Subject to change from",fg_color='#0b3444')
subject_label_origin.grid(row=3,column=0,padx=20)
subject_selection_destination=w.CTkOptionMenu(page4,variable=selected_subject_destination,values=sub_list,command=None)
subject_selection_destination.grid(row=4,column=1,padx=20)
subject_label_destination=w.CTkLabel(page4,text="Select Subject to change to",fg_color='#0b3444')
subject_label_destination.grid(row=4,column=0,padx=20)
section_selection=w.CTkOptionMenu(page4,variable=selected_section,values=sec_list,command=None)
section_selection.grid(row=0,column=1,padx=20)
section_label=w.CTkLabel(page4,text="Select Section",fg_color='#0b3444')
section_label.grid(row=0,column=0,padx=20)
period_selection=w.CTkOptionMenu(page4,variable=selected_period,values=period_list,command=None)
period_selection.grid(row=2,column=1,padx=20)
period_label=w.CTkLabel(page4,text="Select Period",fg_color='#0b3444')
period_label.grid(row=2,column=0,padx=20)
day_selection=w.CTkOptionMenu(page4,variable=selected_day,values=day_list,command=None)
day_selection.grid(row=1,column=1,padx=20)
day_label=w.CTkLabel(page4,text="Select Day",fg_color='#0b3444')
day_label.grid(row=1,column=0,padx=20)

#Save Button
save_frame=w.CTkFrame(update_page,width=0.1*page4.winfo_width(),height=0.1*page4.winfo_height(),fg_color='#0b3444')
save_frame.place(relx=0.5,rely=0.71,anchor='center')
save_frame.grid_rowconfigure(2,weight=1)
b0=w.CTkButton(save_frame,text="Save",fg_color='#0b3444',command=lambda:update_of_timetable(selected_subject_origin.get(),selected_subject_destination.get(),selected_section.get(),selected_period.get(),selected_day.get()))
b0.grid(row = 0, column = 0, columnspan = 1, sticky = 'nsew')
l3=w.CTkLabel(save_frame,text="",fg_color='#0b3444')
l3.grid(row = 1, column = 0, columnspan = 1, sticky = 'nsew')



admin.mainloop()

# WhatsApp_Selenium.run_program()
