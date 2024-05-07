from tkinter import*
from tkinter import Label,Button,Tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Face Recognition",font=("times new roman",35,"bold"),fg="white",bg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #======== first image==============
        img_top=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\image5.jpg")
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=650,height=700)

        #=========== second image ==============
        img_bottom=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\image4.jpg")
        img_bottom=img_bottom.resize((950,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=660,y=50,width=950,height=700)

        #button
        b2=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",20,"bold"),bg="red",fg="white")
        b2.place(x=350,y=640,width=200,height=40)

#==================== function================
    def face_recog(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Ayush@987", database="ayushdb1")
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)

        try:
            while True:
                ret, img = video_cap.read()
                if ret:
                    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    features = faceCascade.detectMultiScale(gray_image, 1.1, 10)
            
                    for (x, y, w, h) in features:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                        id, confidence = clf.predict(gray_image[y:y+h, x:x+w])
                        confidence = int((100 * (1 - confidence / 300)))

                        if confidence > 77:
                            my_cursor = conn.cursor()
                            my_cursor.execute("SELECT name, roll, department FROM student WHERE student_id=%s", (id,))
                            result = my_cursor.fetchone()
                            if result:
                                name, roll, department = result
                                cv2.putText(img, f"Name: {name}", (x, y-55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                                cv2.putText(img, f"Roll: {roll}", (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                                cv2.putText(img, f"Dept: {department}", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                        else:
                            cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

                    cv2.imshow("Face Recognition", img)
                    if cv2.waitKey(1) == 13:  # 13 is the Enter Key
                        break
        finally:
            video_cap.release()
            cv2.destroyAllWindows()
            conn.close()



               



if __name__ == "__main__":
    root= Tk()
    m=Face_Recognition(root)
    root.mainloop()