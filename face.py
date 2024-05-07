from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from facerecog import Face_Recognition

class face_reg:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("My First Website")

        #first imag
        img=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\image1.jpg")
        img=img.resize((300,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=300,height=150)

        #second imag
        img1=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\image2.jpg")
        img1=img1.resize((300,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=300,height=150)

        #third imag
        img2=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\image3.jpg")
        img2=img2.resize((300,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=300,height=150)

        img3=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\bg1.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION SOFTWARE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #STUDENT BUTTON
        img4=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\student.jpg")
        img4=img4.resize((220,180),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=180)

        b1_1=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="red")
        b1_1.place(x=200,y=270,width=220,height=40)

        #face detection button
        img5=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\st.png")
        img5=img5.resize((220,180),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=180)

        b2_1=Button(bg_img,text="FACE DETECTOR",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="dark blue",fg="red")
        b2_1.place(x=500,y=270,width=220,height=40)

        # attendance button
        img6=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\att.jpg")
        img6=img6.resize((220,180),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b2.place(x=800,y=100,width=220,height=180)

        b2_1=Button(bg_img,text="ATTENDANCE",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="red")
        b2_1.place(x=800,y=270,width=220,height=40)


        #help button
        img7=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\help.jpg")
        img7=img7.resize((220,180),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b2=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b2.place(x=1100,y=100,width=220,height=180)

        b2_1=Button(bg_img,text="HELP",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="red")
        b2_1.place(x=1100,y=270,width=220,height=40)

        # train button
        img8=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\TRAIN.jpg")
        img8=img8.resize((220,180),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b2=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b2.place(x=200,y=350,width=220,height=180)

        b2_1=Button(bg_img,text="TRAIN",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="dark blue",fg="red")
        b2_1.place(x=200,y=520,width=220,height=40)

        # photos button
        img9=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\PH.jpg")
        img9=img9.resize((220,180),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b2=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b2.place(x=500,y=350,width=220,height=180)

        b2_1=Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="dark blue",fg="red")
        b2_1.place(x=500,y=520,width=220,height=40)

         # developer button
        img10=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\dev.jpg")
        img10=img10.resize((220,180),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b2=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b2.place(x=800,y=350,width=220,height=180)

        b2_1=Button(bg_img,text="DEVELOPER",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="red")
        b2_1.place(x=800,y=520,width=220,height=40)


        # exit button
        img11=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\EXIt.jpg")
        img11=img11.resize((220,180),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b2=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b2.place(x=1100,y=350,width=220,height=180)

        b2_1=Button(bg_img,text="EXIT",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="red")
        b2_1.place(x=1100,y=520,width=220,height=40)

    def open_img(self):
        os.startfile("data")





#*****************function************

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


#*****************function************

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    






    

if __name__ == "__main__":
    root= Tk()
    m=face_reg(root)
    root.mainloop()

    