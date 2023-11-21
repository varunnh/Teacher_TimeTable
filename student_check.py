
import mysql.connector
mydb= mysql.connector.connect( host="127.0.0.1", user= "root", password = "Varun123$", database="python_project1")
print(mydb)
my_database= mydb.cursor(buffered=True)
import random


def refresh_table():
    my_database.execute("Delete from student_table Where WeekDay='Monday'")
    my_database.execute("Delete from student_table Where WeekDay='Tuesday'")
    my_database.execute("Delete from student_table Where WeekDay='Wednesday'")
    my_database.execute("Delete from student_table Where WeekDay='Thursday'")
    my_database.execute("Delete from student_table Where WeekDay='Friday'")
    my_database.execute("Delete from student_table Where WeekDay='Saturday'")
    my_database.execute("Delete from student_table Where WeekDay='Sunday'")    
    mydb.commit()
    my_database.execute("Delete from master_teacher")
    mydb.commit()

def addition_of_section(sec):
    days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    periods=['Period 1','Period 2','Period 3','Period 4','Period 5','Period 6','Period 7','Period 8','Period 9']
    unocc="unoccupied"
    default_val='Mr.X'
    my_database.execute("Select count(0) from student_table where Section='{}'".format(sec))
    section_count=my_database.fetchall()[0][0]
    if section_count==0:
        for day in days:
            for period in periods:
                my_database.execute('Insert into student_table values("%s","%s","%s","%s","%s")'%(sec,day,period,unocc,default_val))
                mydb.commit()
            
def subject_allotment(sec):
    days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    periods=['Period 1','Period 2','Period 3','Period 4','Period 5','Period 6','Period 7','Period 8','Period 9']
    half_day_periods=['Period 1','Period 2','Period 3','Period 4','Period 5','Period 6']
    phy_subjects={'Mechanical':4,'Electrical':5,'Maths':5,'Physics':6,'Python':6,'Physics Lab':3,'Python Lab':2}
    phy_teachers={}
        
    unocc="unoccupied"
    #random.shuffle(phy_subjects)
    
    for w in phy_subjects:
        print(w)
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
                                        
def add_teacher(name,sub,sec):
    default_teachers={'Mechanical':'Mr.Mechanical','Electrical':'Mr.Electrical','Maths':'Mr.Maths','Physics':'Mr.Physics','Python':'Mr.Python','Physics Lab':'Mr.Physics Lab','Python Lab':'Mr.Python Lab'}
    my_database.execute("Select count(0) from master_teacher where Teacher_Name='{}' and Sub='{}' and Section='{}'".format(name,sub,sec))
    if my_database.fetchall()[0][0]==0:
        for substitute in default_teachers:
            my_database.execute('Insert into master_teacher values("%s","%s","%s")'%(default_teachers[substitute],substitute,sec))
            mydb.commit()
        my_database.execute("Update master_teacher set Teacher_Name='{}' where Sub='{}' and Section='{}'".format(name,sub,sec))
        mydb.commit()
    addition_of_section(sec)
    subject_allotment(sec)

add_teacher('Mr.Harikrishnan','Python','1A')
#refresh_table
