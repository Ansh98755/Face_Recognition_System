from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("My First Website")
        #************ variables************
        self.var_Department=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_stu_id=StringVar()
        self.var_stu_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_gender=StringVar()
        self.var_DOB=StringVar()
        self.var_Phone=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1=StringVar()






        #first imag
        img=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\st1.jpg")
        img=img.resize((300,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=300,height=150)

        #second imag
        img1=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\st2.jpg")
        img1=img1.resize((300,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=300,height=150)

        #third imag
        img2=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\st3.jpg")
        img2=img2.resize((300,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=300,height=150)

        img3=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\nat.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),fg="white",bg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=55,width=1500,height=660)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=720,height=580)

        img_left=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\st2.jpg")
        img_left=img_left.resize((720,100),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=12,y=10,width=720,height=100)

        #current course
        course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="CURRENT COURSE INFORMATION",font=("times new roman",12,"bold"))
        course_frame.place(x=5,y=105,width=700,height=125)

        #department
        dep_label=Label(course_frame,text="DEPARTMENT",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)


        dep_combobox=ttk.Combobox(course_frame,textvariable=self.var_Department,font=("times new roman",12,"bold"),state="read only",width=20)
        dep_combobox["values"]=("Select Department","Computer","IT","MECHANICAL","CIVIL")
        dep_combobox.current(0)
        dep_combobox.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(course_frame,text="COURSE",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combobox=ttk.Combobox(course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="read only",width=20)
        course_combobox["values"]=("Select course","SE","BBA","BE","BCA")
        course_combobox.current(0)
        course_combobox.grid(row=0,column=3,padx=2,pady=10,sticky=W)


         #year
        year_label=Label(course_frame,text="YEAR",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)


        year_combobox=ttk.Combobox(course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only",width=20)
        year_combobox["values"]=("Select year","2019-2023","2020-2024","2021-2025","2022-2026")
        year_combobox.current(0)
        year_combobox.grid(row=1,column=1,padx=2,pady=10)

         #semester
        sem_label=Label(course_frame,text="SEMESTER",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)


        sem_combobox=ttk.Combobox(course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="read only",width=20)
        sem_combobox["values"]=("Select semester","I","II","III","IV","V","VI")
        sem_combobox.current(0)
        sem_combobox.grid(row=1,column=3,padx=2,pady=10)

        #class student information

        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="CLASS STUDENT INFORMATION",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=232,width=700,height=400)

        studentID_label=Label(class_student_frame,text="STUDENT-ID",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_stu_id,width=15,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=5,pady=5)

        #class student name information

        student_name_label=Label(class_student_frame,text="STUDENT-NAME",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_stu_name,width=15,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=5,pady=5)

        #class division
        student_division_label=Label(class_student_frame,text="CLASS DIVISION",font=("times new roman",12,"bold"),bg="white")
        student_division_label.grid(row=1,column=0,padx=5,pady=10,sticky=W)

        student_division_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=15,font=("times new roman",12,"bold"))
        student_division_entry.grid(row=1,column=1,padx=5,pady=5)

        #roll no

        student_roll_label=Label(class_student_frame,text="STUDENT-ROLL.NO",font=("times new roman",12,"bold"),bg="white")
        student_roll_label.grid(row=1,column=2,padx=5,pady=10,sticky=W)

        student_roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=15,font=("times new roman",12,"bold"))
        student_roll_entry.grid(row=1,column=3,padx=5,pady=5)

        #EMAIL

        student_email_label=Label(class_student_frame,text="STUDENT-EMAIL",font=("times new roman",12,"bold"),bg="white")
        student_email_label.grid(row=2,column=0,padx=5,pady=10,sticky=W)

        student_email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=15,font=("times new roman",12,"bold"))
        student_email_entry.grid(row=2,column=1,padx=5,pady=5)

        #address

        student_address_label=Label(class_student_frame,text="STUDENT-ADDRESS",font=("times new roman",12,"bold"),bg="white")
        student_address_label.grid(row=2,column=2,padx=5,pady=10,sticky=W)

        student_address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=15,font=("times new roman",12,"bold"))
        student_address_entry.grid(row=2,column=3,padx=5,pady=5)
        #gender

        student_gender_label=Label(class_student_frame,text="STUDENT-GENDER",font=("times new roman",12,"bold"),bg="white")
        student_gender_label.grid(row=3,column=0,padx=5,pady=10,sticky=W)

        student_gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=15,font=("times new roman",12,"bold"))
        student_gender_entry.grid(row=3,column=1,padx=5,pady=5)

        #DOB

        student_DOB_label=Label(class_student_frame,text="STUDENT-DOB",font=("times new roman",12,"bold"),bg="white")
        student_DOB_label.grid(row=3,column=2,padx=5,pady=10,sticky=W)

        student_DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_DOB,width=15,font=("times new roman",12,"bold"))
        student_DOB_entry.grid(row=3,column=3,padx=5,pady=5)

        #phone number

        student_ph_no_label=Label(class_student_frame,text="STUDENT-PHONE.NO",font=("times new roman",12,"bold"),bg="white")
        student_ph_no_label.grid(row=4,column=0,padx=5,pady=10,sticky=W)

        student_ph_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_Phone,width=15,font=("times new roman",12,"bold"))
        student_ph_no_entry.grid(row=4,column=1,padx=5,pady=5)


        #teacher name

        student_teacher_name_label=Label(class_student_frame,text="TEACHER-NAME",font=("times new roman",12,"bold"),bg="white")
        student_teacher_name_label.grid(row=4,column=2,padx=5,pady=10,sticky=W)

        student_teacher_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=15,font=("times new roman",12,"bold"))
        student_teacher_name_entry.grid(row=4,column=3,padx=5,pady=5)

        #Radiobutton
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=233,width=715,height=70)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        Update_btn=Button(btn_frame,text="Update",command=self.update_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="delete",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="reset",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Photo Sample",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)#,

        update_photo_btn=Button(btn_frame,text="Update Photo Sample",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=3)

        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student details",font=("times new roman",12,"bold"))
        right_frame.place(x=740,y=10,width=720,height=580)

        img_right=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\ss.jpg")
        img_right=img_right.resize((720,100),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=12,y=10,width=720,height=100)

        #******** searching system**********

        searching_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="SEARCH SYSTEM",font=("times new roman",12,"bold"))
        searching_frame.place(x=5,y=110,width=700,height=70)

        search_label=Label(searching_frame,text="SEARCH BY:",font=("times new roman",15,"bold"),bg="red")
        search_label.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        SEARCH_combobox=ttk.Combobox(searching_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        SEARCH_combobox["values"]=("Select ","ROLL-NO","PHONE-NO")
        SEARCH_combobox.current(0)
        SEARCH_combobox.grid(row=0,column=1,padx=2,pady=10)

        search_entry=ttk.Entry(searching_frame,width=12,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=3,padx=5,pady=5)

        search_btn=Button(searching_frame,text="SEARCH",width=15,font=("times new roman",12,"bold"),bg="blue",fg="pink")
        search_btn.grid(row=0,column=3)
    

        show_all_btn=Button(searching_frame,text="SHOW_ALL",width=15,font=("times new roman",12,"bold"),bg="blue",fg="pink")
        show_all_btn.grid(row=0,column=4)

        #***********TABLE FRAME*********

        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="TABLE FRAME",font=("times new roman",12,"bold"))
        table_frame.place(x=5,y=180,width=700,height=350)

        #***************Scrollbar**********

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.student_table=ttk.Treeview(table_frame,columns=("Department","course","Year","Semester","ID","Name","Division","roll","Email","Address","Gender","DOB","Phone-no","Teacher","Photo_Sample_Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Division",text="Division")
        self.student_table.heading("roll",text="roll")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Phone-no",text="Phone-no")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo_Sample_Status",text="Photo_Sample_Status")

        self.student_table["show"]="headings"

        self.student_table.column("Department",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Division",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Phone-no",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo_Sample_Status",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetchdata()

#*************** add function************


    def add_data(self):
        if self.var_Department.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Ayush@987",database="ayushdb1")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                
                                                                                                                self.var_Department.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_stu_id.get(),
                                                                                                                self.var_stu_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_DOB.get(),
                                                                                                                self.var_Phone.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            
                                                                                                            ))
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo("Success","Student details have been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
        

    #### fetch datab#####
    def fetchdata(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Ayush@987",database="ayushdb1")
        my_cursor=conn.cursor()
        my_cursor.execute("select *from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()

           ##### get cursor ######
    def get_cursor(self,event=""):
             cursor_focus=self.student_table.focus()
             content=self.student_table.item(cursor_focus)
             data=content["values"]

             self.var_Department.set(data[0]),
             self.var_course.set(data[1]),
             self.var_year.set(data[2]),
             self.var_sem.set(data[3]),
             self.var_stu_id.set(data[4]),
             self.var_stu_name.set(data[5]),
             self.var_div.set(data[6]),
             self.var_roll.set(data[7]),
             self.var_email.set(data[8]),
             self.var_address.set(data[9]),
             self.var_gender.set(data[10]),
             self.var_DOB.set(data[11]),
             self.var_Phone.set(data[12]),
             self.var_teacher.set(data[13]),
             self.var_radio1.set(data[14])


    ##### update data function ####
    def update_data(self):
        if self.var_Department.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try: 
                Upadate=messagebox.askyesno("Upadte","Do you want to update the details of the Student",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Ayush@987",database="ayushdb1")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set department=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,email=%s,address=%s,gender=%s,DOB=%s,PHONE=%s,TEACHER=%s,PHOTOSAMPLE=%s where student_id=%s",(
                                                                                                                                                                                                            
                                                                                                                                                                                                        self.var_Department.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                                                                        self.var_stu_name.get(),
                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_DOB.get(),
                                                                                                                                                                                                        self.var_Phone.get(),
                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.var_stu_id.get()
                                                                                                                                                                                                    ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student details are successfully updated completely",parent=self.root)
                conn.commit()
                self.fetchdata()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    ###### take photot sample ######
    def generate_dataset(self):
        if self.var_Department.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try: 
                conn=mysql.connector.connect(host="localhost",user="root",password="Ayush@987",database="ayushdb1")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:#x in my result
                    id+=1
                my_cursor.execute("update student set department=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,email=%s,address=%s,gender=%s,DOB=%s,PHONE=%s,TEACHER=%s,PHOTOSAMPLE=%s where student_id=%s",(
                                                                                                                                                                                                            
                                                                                                                                                                                                        self.var_Department.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                                                                        self.var_stu_name.get(),
                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_DOB.get(),
                                                                                                                                                                                                        self.var_Phone.get(),
                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.var_stu_id.get()==str(id+1)
                                                                                                                                                                                                    ))
                conn.commit()
                self.fetchdata()
                conn.close()
             #==================== face detection================
                face_classifier=cv2.CascadeClassifier("C:\\Program Files\\Python312\\Lib\\site-packages\\FolderPath\\cv2\\data\\haarcascade_frontalface_default.xml")
        
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compled!!!!")
                messagebox.showinfo("Present","Attendance Marked !!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)







if __name__ == "__main__":
    root= Tk()
    m=Student(root)
    root.mainloop()