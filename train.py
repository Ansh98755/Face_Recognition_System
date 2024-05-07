from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("My First Website")


        title_lbl=Label(self.root,text="Train Data",font=("times new roman",35,"bold"),fg="white",bg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\image2.jpg")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1530,height=325)

        
        #button
        
        b2=Button(self.root,text="Train Data",cursor="hand2",command=self.train_classifier,font=("times new roman",50,"bold"),bg="blue",fg="white")
        b2.place(x=0,y=380,width=1530,height=60)


        title_lbl=Label(self.root,text="Train Data",font=("times new roman",35,"bold"),fg="white",bg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_bottom=Image.open(r"C:\Users\ayush\Pictures\Saved Pictures\image1.jpg")
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=450,width=1530,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]

        try:
            for image in path:
                img=Image.open(image).convert('L')
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13
            ids=np.array(ids)

        #============== face classifier training=============
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")
            messagebox.showinfo("Result","Training Dataset Completed!!!")
            cv2.destroyAllWindows()
        except Exception as e:
            messagebox.showerror("Error", f"Failed during training: {e}")
            cv2.destroyAllWindows()




if __name__ == "__main__":
    root= Tk()
    m=Train(root)
    root.mainloop()