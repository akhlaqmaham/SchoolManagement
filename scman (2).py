from tkinter import*
import tkinter.messagebox
import tkinter.messagebox
from table import*


class SchoolLogin: 
    def __init__(self,master):
        self.master=master
        self.master.title('School Management System')
        self.master.geometry('1100x750')
        self.master.config(bg='cadet blue')
        self.frame= Frame(self.master, bg='cadet blue')
        self.frame.pack()


        self.username= StringVar()
        self.password=StringVar()

        self.lblTitle= Label( self.frame, text='School Login System', relief='solid', font=('Georgia',60,'bold'), fg='black', bg='cadet blue')
        self.lblTitle.grid( row= 0, column= 1, pady=70)
        self.username=Label(self.frame, text='Username:', font=('arial',30,'bold'), fg='black', bg='cadet blue')
        self.password=Label(self.frame,text='Password:',font=('arial',30,'bold'), fg='black', bg='cadet blue')
        self.username.grid(row=1,column=0,sticky=W, pady=10)
        self.password.grid(row=2,column=0,sticky=W, pady=10)
        self.enter1=Entry(self.frame)
        self.enter2=Entry(self.frame)
        self.enter1.grid(row=1,column=1,sticky=W, pady=10)
        self.enter2.grid(row=2,column=1,sticky=W, pady=10)
        self.enter1_button=Button(self.frame, text='Login', bg='brown', fg='black', width=15,command=self.reveal)
        self.enter2_button=Button(self.frame, text='School Policies', bg='brown', fg='black' , width=15, command=self.policy)
        self.enter3_button=Button(self.frame, text='Registeration', fg='black' , bg='brown' , width=15, command=self.register)
        self.enter5_button= Button(self.frame, text='Exit', fg='black', bg='brown', width=15, command=self.Exit)
        self.enter4_button= Button(self.frame, text="GLO's", fg='black', bg='brown', width=15, command=self.glo)
        self.enter1_button.grid(row=3,column=1,sticky=W, pady=19)
        self.enter2_button.grid(row=4, column=1, sticky=W, pady=4)
        self.enter3_button.grid(row=5, column=1, sticky=W, pady=15)
        self.enter4_button.grid(row=6, column=1, sticky=W, pady=10)
        self.enter5_button.grid(row=7, column=1, sticky=W, pady=13)

    def glo(self):
        self.open= Toplevel(self.master)
        self.glo=GLO(self.open)
              
    def reveal(self):
        user=(self.enter1.get())
        password=(self.enter2.get())
        if ((user=='admin') and (password=='admin')):
            self.Login_window()
        else:
            tkinter.messagebox.showinfo('Incorrect Username or Password', 'You entered incorrect username or password')
    def Exit(self):
        self.Exit= tkinter.messagebox.askyesno('School Login System', 'confirm if you want to exit')
        if self.Exit>0:
            self.master.destroy()
        return

    def policy(self):
        self.wind= Toplevel(self.master)
        self.policy= School_Policy(self.wind)
    
    def Login_window(self):
        self.window= Toplevel(self.master)
        self.ap= School_System(self.window)
        
    def register(self):
        self.window=Toplevel(self.master)
        self.reg= Registeration(self.window)

class GLO:
    def __init__(self,master):
        self.master=master
        self.master.title("GLO's")
        self.master.geometry('1100x750')
        self.frame=Frame(self.master)
        self.frame.pack()


        self.title1= Label(self.frame,text="General Learner Outcomes (GLOs)", font=('Georgia',30,'bold','underline'), fg='brown', pady=30)
        self.title1.grid(row=1, column=0, sticky=W)
        self.g1= Label(self.frame, text="GLO 1: RESPONSIBILITY:", font=('calibri',20,'bold','underline'), fg='black', pady=8)
        self.g1.grid(row=2, column=0, sticky=W)
        self.ab1= Label(self.frame, text="Takes responsibility for one's own learning." ,font=('cambria',15), fg='black')
        self.ab1.grid(row=3, column=0, sticky=W)
        self.g2= Label(self.frame, text="GLO 2: COOPERATION:", font=('calibri',20,'bold','underline'), fg='black', pady=8)
        self.g2.grid(row=4, column=0, sticky=W)
        self.ab2= Label(self.frame, text="Understands that people must work together.", font=('cambria',15), fg='black')
        self.ab2.grid(row=5, column=0, sticky=W)
        self.g3= Label(self.frame, text="GLO 3: THINKING:", font=('calibri',20,'bold','underline'), fg='black', pady=8)
        self.g2.grid(row=6, column=0, sticky=W)
        self.ab3= Label(self.frame, text="Engage in critical thinking and problem solving.", font=('cambria',15), fg='black')
        self.ab3.grid(row=7, column=0, sticky=W)
        self.g4= Label(self.frame, text="GLO 4: QUALITY WORK:", font=('calibri',20,'bold','underline'), fg='black', pady=8)
        self.g4.grid(row=8, column=0, sticky=W)
        self.ab4= Label(self.frame, text="Recognizes and produces quality work.", font=('cambria',15), fg='black')
        self.ab4.grid(row=9, column=0, sticky=W)
        self.g5= Label(self.frame, text="GLO 5: COMMUNICATION:", font=('calibri',20,'bold','underline'), fg='black', pady=8)
        self.g5.grid(row=10, column=0, sticky=W)
        self.ab5= Label(self.frame, text="Communicates effectively in various situations.",font=('cambria',15), fg='black')
        self.ab5.grid(row=11, column=0, sticky=W)
        self.g6= Label(self.frame, text="GLO 6: TECHNOLOGY:",  font=('calibri',20,'bold','underline'), fg='black', pady=8)
        self.g6.grid(row=12, column=0, sticky=W)
        self.ab6= Label(self.frame, text="Uses technology effectively and ethically." , font=('cambria',15), fg='black')
        self.ab6.grid(row=13, column=0 , sticky=W)
                    

class School_Policy:
    def __init__(self,master):
        self.master=master
        self.master.title('School Poilicies')
        self.master.geometry('1500x750')
        self.frame=Frame(self.master)
        self.frame.pack()


        self.title= Label(self.frame,  text= 'School Policies & Disciplinary Guidelines:', font=('Georgia',30,'bold','underline'), fg='brown', pady=30)
        self.title.grid(row=1, column=0, sticky=W)
        self.a= Label(self.frame, text=' -Be punctual, report to school and class on time. School begins at 8:00 a.m.', font=('cambria',17), fg='black')
        self.a.grid(row=2, column=0, sticky=W)
        self.b= Label(self.frame, text=" -Strive to be present every school day. In case of absence, parents should call the school in the morning of the absence and notify the teacher in writing upon the student's return to school.", font=('cambria',16), fg='black')
        self.b.grid(row=3, column=0, sticky=W)
        self.c= Label(self.frame, text=" -Buildings and the campus will be kept clean and neat. Do not deface or damage school property. Students who vandalize the school property will make restitution.", font=('cambria',17), fg='black')
        self.c.grid(row=4, column=0, sticky=W)
        self.d= Label(self.frame, text=" -The following are not allowed in school unless prior permission is granted by the school staff:", font=('cambria',17),fg='black')
        self.d.grid(row=5, column=0, sticky=W)
        self.e= Label(self.frame, text="            ~radios, cell phones, pagers and other electrical equipment.", font=('cambria',17), fg='black')
        self.e.grid(row=6, column=0, sticky=W)
        self.f= Label(self.frame, text="            ~yoyos, darts, sling shots, and other potentially dangerous toys, pets.", font=('cambria',17), fg='black')
        self.f.grid(row=7, column=0, sticky=W)
        self.g= Label(self.frame, text="            ~valuables, extra money, computer games, items of sentimental value.", font=('cambria', 17), fg='black')
        self.g.grid(row=8, column=0, sticky=W)
        self.h= Label(self.frame, text=" -Remain within school boundaries at all times. Students leaving the campus must have a Student Pass and must be accompanied by a parent/guardian.", font=('cambria', 17), fg='black')
        self.h.grid(row=9, column=0, sticky=W)
        self.i= Label(self.frame, text=" -Avoid using abusive or profane language and gestures.", font=('cambria',17), fg='black')
        self.i.grid(row=10, column=0, sticky=W)
        self.j= Label(self.frame, text=" -Buying/selling of personal items and trading are not allowed.", font=('cambria', 17), fg='black')
        self.j.grid(row=11, column=0, sticky=W)
        self.k= Label(self.frame, text=" -Respect each other. Avoid bumping into or hurting others. Rough contact sports and games are not allowed.", font=('cambria',17), fg='black')
        self.k.grid(row=12, column=0, sticky=W)
        self.l= Label(self.frame, text=" -Students are expected to attend school regularly and to attend all classes.", font=('cambria',17), fg='black')              
        self.l.grid(row=13, column=0, sticky=W)
        self.m= Label(self.frame, text=" -Students are expected to be on time for school and classes.", font=('cambria',17), fg='black')
        self.m.grid(row=14, column=0, sticky=W)
        self.n= Label(self.frame, text=" -Students are expected to contribute to a safe school environment free from fear. Acts of violence, weapons and contraband are never acceptable.", font=('cambria',17), fg='black')
        self.n.grid(row=15,column=0, sticky=W)
       

class Registeration:
    def __init__(self,master):
        self.master=master
        self.master.title(' Online Registeration')
        self.master.geometry('1350x750')
        self.master.config(bg='white')
        self.frame= Frame(self.master, bg='white')
        self.frame.pack()

        self.lbl3Title= Label(self.frame, text='Registeration Form', relief='solid', font=('Georgia',60,'bold'), fg='black')
        self.lbl3Title.grid(row=0, column=0,pady=40)
        self.name1= Label(self.frame, text='First Name: ______________________', font=('camria',20,'bold'), fg='black')
        self.name1.grid(row=1, column=0,sticky=W)
        self.name2= Label(self.frame, text='Last Name: ______________________', font=('cambria',20,'bold'), fg='black')
        self.name2.grid(row=2, column=0,sticky=W)
        self.gen= Label(self.frame, text='Gender: ', font=('camria',20,'bold'), fg='black')
        self.gen.grid(row=3, column=0, sticky='w')
        self.check1=Checkbutton(self.frame, text='Female')
        self.check1.grid(row=3, column=1)
        self.check2=Checkbutton(self.frame, text='Male')
        self.check2.grid(row=3, column=2, columnspan=1)
        self.contact= Label(self.frame, text='Contact Number: ___________________', font=('camria',20,'bold'), fg='black')
        self.contact.grid(row=4, column=0, sticky='w')
        self.email= Label(self.frame, text='Email: ________________', font=('camria',20,'bold'), fg='black')
        self.email.grid(row=5, column=0,sticky=W)
        self.f=Label(self.frame, text='Father Name: ____________________', font=('camria',20,'bold'), fg='black')
        self.f.grid(row=6,column=0,sticky=W)
        self.fp=Label(self.frame, text="Father's Profession: _______________________ ", font=('camria',20,'bold'), fg='black')
        self.fp.grid(row=7,column=0,sticky=W)
        self.fn=Label(self.frame, text="Father's Contact Number: __________________", font=('camria',20,'bold'), fg='black')
        self.fn.grid(row=8,column=0,sticky=W)
        self.m=Label(self.frame, text="Mother's Name: _______________________ ", font=('camria',20,'bold'), fg='black')
        self.m.grid(row=9,column=0,sticky=W)
        self.mp=Label(self.frame, text="Mother's Profession: _________________ ", font=('camria',20,'bold'), fg='black')
        self.mp.grid(row=10,column=0,sticky=W)
        self.mn=Label(self.frame, text= "Mother's Contact Number: __________________", font=('camria',20,'bold'), fg='black')
        self.mn.grid(row=11,column=0,sticky=W)
        self.ad= Label(self.frame, text='Address: __________________', font=('camria',20, 'bold'), fg='black')
        self.ad.grid(row=12,column=0,sticky=W)
        self.fee=Label(self.frame, text='Registration Fee= 1000', font=('camria',15), fg='black')
        self.fee.grid(row=17,column=2,sticky=E, pady=25)
        self.r= Label(self.frame, text="*You have to fill the above form and then submit it to the school's office.", font=('camria',13), fg='black')
        self.r.grid(row=30, column=0, sticky=W)
        self.rule= Label(self.frame, text="*The last date of submission is 1st August 2019.", font=('camria',13), fg='black')
        self.rule.grid(row=31, column=0, sticky=W)
        self.ab= Label(self.frame, text="*The test for registered candiadates will take place on 4th August 2019 at 9:00 am .", font=('camria',13), fg='black')
        self.ab.grid(row=32, column=0, sticky=W)
        
        
class School_System:
    def __init__(self,master):
        self.master=master
        self.master.title('School Management System')
        self.master.geometry('1350x750')
        self.master.config()
        self.frame1=Frame(self.master, bg='cadet blue',)
        #self.frame1.grid(sticky='WNES')
        
        self.second_screen = None
        self.menu=Label(self.frame1, text='        HOME         ', font=('cambria',30,'bold','underline'),fg='black', bg='cadet blue')
        self.menu.grid(row=1, column=0, pady=30 )
        self.button1=Button(self.frame1, text='     Attendence    ', font=('calibri',15,'bold'), bg='cadet blue',command=self.open_attendance)
        self.button1.grid(row=2, column=0, pady=8)
        self.button2=Button(self.frame1, text='       Announced Result      ', font=('calibri',15,'bold'), bg='cadet blue', command=self.open_result)
        self.button2.grid(row=3, column=0, pady=8)
        self.button3= Button(self.frame1, text='      Academic Calendar     ', font=('calibri',15,'bold'), bg='cadet blue', command=self.open_calendar)
        self.button3.grid(row=4, column=0, pady=8)
        self.button4= Button(self.frame1, text='       Time Table     ', font=('calibri',15,'bold'), bg='cadet blue',command=self.open_timetable)
        self.button4.grid(row=5, column=0, pady=8)
        self.fee_5= Label(self.frame1, text='       Fee Structure     ', font=('calibri',15,'bold'), bg='cadet blue', fg='black')
        self.fee_5.grid(row=7, column=0, pady=8)
        self.button6= Button(self.frame1, text='    > For Kindergarten ', font=('arial',15,'bold'), fg='brown', relief=RIDGE , bg='cadet blue', command=self.open_kin)
        self.button6.grid(row=8, column=0, pady=2)
        self.button7= Button(self.frame1, text='    >For Primary   ', font=('arial',15,'bold'), fg='brown', relief=RIDGE , bg='cadet blue', command=self.open_primary)
        self.button7.grid(row=9, column=0, pady=2)
        self.button8= Button(self.frame1, text='    >For Secondary   ', font=('arial',15,'bold'), fg='brown', relief=RIDGE , bg='cadet blue', command=self.open_second)
        self.button8.grid(row=10, column=0, pady=2)
        self.button9= Button(self.frame1, text='      Faculty     ', font=('arial',15,'bold'), fg='black' , bg='cadet blue', command=self.faculty)
        self.button9.grid(row=6, column=0, pady=10)
        self.button10= Button(self.frame1, text='     LOGOUT     ', font=('arial',15,'bold'), fg='black' , bg='cadet blue', command=self.logout)
        self.button10.grid(row=30, column=0, pady=100)
        self.frame1.pack(fill=Y ,side=LEFT)


        self.frame2=Frame(self.master, bg='white',width='1050', height='750', bd=50)
        self.frame2.pack()
        
        self.lbl2Title= Label(self.frame2, text= 'Welcome To School Management System ', relief='solid', font=('Georgia',40,'bold'), fg='black', pady=20)
        self.lbl2Title.pack( )


    def open_result(self):
         if(self.second_screen != None):
             self.second_screen.destroy()


             table = Table(self.frame2, ["NAME", "PERCENTAGE", "GRADE"], column_minwidths=[None, None, None])
             table.pack(expand=True, fill=X, padx=10,pady=10)
             
             table.set_data([['BISMA','92%','A+'],['AMIR','91.5%','A+'], ['BASIT','90%','A+'],['ASAD','87%','A'],['DANISH','85%','A'],['FAUZIA','82%','A'],['FARZANA','80.7%','A'],['MAHAM','80.5','A'],['FAHAD','78%','B+'],['ZUBIA','77.7%','B+'],['ZOYA','72%','B+'],['ZAID','67%','B-'],['FARAZ','65%','B-'],['DUA','60%','B-']])
             table.cell(0,0)

             self.second_screen= table

        
    def open_attendance(self):

        #children = self.frame2.winfo_children()
        #if(len(children) > 1):
        #    children[1].destroy()

        if(self.second_screen != None):
            self.second_screen.destroy()
        
        table = Table(self.frame2, ["STUDENTS NAME", "ROLL NUMBER", "TOTAL CLASSES",'ATTENDED','ABSENT','PERCENTAGE'], column_minwidths=[None, None, None])
        table.pack(expand=True, fill=X, padx=10,pady=10)

        table.set_data([['AMIR','1','210','200','10','95.2'],['ASAD','2','210','210','0','100'], ['BASIT','3','210','210','0','100'],['BISMA','4','210','205','5','97.6'],['DANISH','5','210','150','60','71.4'],['FAUZIA','6','210','200','10','95.2'],['FARZANA','7','210','210','0','100'], ['FARAZ','8','210','210','0','100'],['FAHAD','9','210','205','5','97.6'],['ZUBIA','10','210','150','60','71.4'],['ZAID','11','210','200','10','95.2'],['ZOYA','12','210','210','0','100'], ['ZEHRA','13','210','210','0','100'],['ZAIN','14','210','205','5','97.6'],['ZOHA','15','210','150','60','71.4']])
        table.cell(0,0)

        self.second_screen = table

    def open_timetable(self):
        if(self.second_screen != None):
            self.second_screen.destroy()

        table = Table(self.frame2, ["MONDAY", "TUESDAY", "WEDNESDAY",'THURSDAY','FRIDAY'], column_minwidths=[None, None, None])
        table.pack(expand=True, fill=X, padx=10,pady=10)
        table.set_data([['SCIENCE','MATHS','HISTORY','URDU','ARTS'],['COMPUTER','GEOGRAPHY','ENGLISH','SCIENCE','HISTORY'], ['MATHS','URDU','MATHS','SCIENCE','ISLAMIAT'],['ISLAMIAT','HISTORY','MATHS','ARTS','ENGLISH'],['BREAK','BREAK','BREAK','BREAK','BREAK'],['MATHS','URDU','MATHS','SCIENCE','ISLAMIAT'],['MATHS','URDU','MATHS','SCIENCE','ISLAMIAT'],['MATHS','URDU','MATHS','SCIENCE','ISLAMIAT']])
        table.cell(0,0)

        self.second_screen = table
        
    def open_calendar(self):
        if(self.second_screen != None):
            self.second_screen.destroy()


            table = Table(self.frame2, ["MONTH", "EVENTS"], column_minwidths= ([None, None]))
            table.pack(expand=True, fill=X, padx=10,pady=10)
            table.set_data([['JANUARY','WINTER VACATIONS'], ['FEBRUARY', 'FINAL EXAMS'],['5th FEBRUARY HOLIDAY','DEFENCE DAY'],['3rd MARCH','RESLT DAY'],['23rd MARCH HOLIDAY','PAKISTAN DAY'],['1st MAY','NEW SESSION'],['JUNE & JULY','SUMMER VACATIONS'],['1st AUGUST','BACK TO SCHOOL'],['6th AUGUST','EID MILAN PARTY'],['14th AUGUST','INDEPENDANCE DAY'],['SEPTEMBER','MONTHLY TEST'],['15th OCTOBER','MID-TERM'],['NOVEMBER',"PARENT'S TEACHER MEETING"],['5th DECEMBER','PICNIC'],['25th DECEMBER HOLIDAY',"QUAID's DAY"]])
            table.cell(0,0)

            self.second_screen=table

    def open_kin(self): 
        if(self.second_screen != None):
            self.second_screen.destroy()

        table = Table(self.frame2, ["FEE DESCRIPTION", "CHARGES"], column_minwidths=[None, None])
        table.pack(expand=True, fill=X, padx=10,pady=10)
        table.set_data([['MONTHLY FEES','3000'],['ANNUAL FEES','36000'],['STATIONARY FEES','2000'],['ADMISSION FEES','1000'],['SWIMMING CLASSES','1500'],['FOR FRUITS AND MILK','1000'],['SECURITY DEPOSIT(NON-REFUNDABLE)','2000']])
        table.cell(0,0)

        self.second_screen = table
       

    def open_primary(self):
        if(self.second_screen != None):
            self.second_screen.destroy()

        table = Table(self.frame2, ["FEE DESCRIPTION", "CHARGES"], column_minwidths=[None, None])
        table.pack(expand=True, fill=X, padx=10,pady=10)
        table.set_data([['MONTHLY FEES','4000'],['ANNUAL FEES','48000'],['STATIONARY FEES','2500'],['ADMISSION FEES','1000'],['GYM CLASSES','1500'],['SECURITY DEPOSIT(NON-REFUNDABLE)','2000']])
        table.cell(0,0)

        self.second_screen = table
      

    def open_second(self):
        if(self.second_screen != None):
            self.second_screen.destroy()

        table = Table(self.frame2, ["FEE DESCRIPTION", "CHARGES"], column_minwidths=[None, None])
        table.pack(expand=True, fill=X, padx=10,pady=10)
        table.set_data([['MONTHLY FEES','5000'],['ANNUAL FEES','60000'],['STATIONARY FEES','800'],['ADMISSION FEES','1500'],['LAB CHARGES','1500'],['SECURITY DEPOSIT(NON-REFUNDABLE)','2000']])
        table.cell(0,0)

        self.second_screen = table
        

    def faculty(self):
         if(self.second_screen != None):
            self.second_screen.destroy()


            table = Table(self.frame2, ["SUBJECTS", "TEACHERS' NAME", "CLASSES ASSIGNED"], column_minwidths=[None, None])
            table.pack(expand=True, fill=X, padx=10,pady=10)
            table.set_data([['MATHS','MS.FAIZA','I,II,II'],['','MS.SANIA','VII,VIII'],['SCIENCE','MS.MIDHAT','II,III,VI'],['','MS.HAMEEZA','VII,VII'],['ENGLISH','MS.FAUZIA','I,II,III,IV'],['','MS.SAIMA','V,VIII,X'],['','MS.SAMREEN','VI,VI,IX'],['URDU','MS.TAHIRA','I,II,IV'],['ISLAMIAT','MS.SARA','II,III','X'],['','MS.KIRAN','V,VII,VIII'],['HISTORY','MS.SHAHEEN','VII,VIII,IX'],['COMPUTER','MS.IQRA','II,III,IV'],['','MS.AMNA','VI,VII,VIII,IX'],['ARTS','MS.SAMRAH','I,II,III,IV'],['','MS.ABIDA','V,VI,VII,VIII']])
            table.cell(0,0)


            self.second_screen = table
        
        

    def logout(self):
        self.logout= tkinter.messagebox.askyesno('School Login System', 'confirm if you want to logout')
        if self.logout>0:
            self.master.destroy()
        return
        
                                  
root=Tk()
app=SchoolLogin(root)



root.mainloop()

        
        
                                 
