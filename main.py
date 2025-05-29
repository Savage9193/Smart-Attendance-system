from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from Face_recognition import Face_Recognition
import tkinter
from attendance import Attendance
from developer import Developer
from help import Help
from datetime import datetime
from time import strftime



class Face_recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        # first Image
        img=Image.open(r"D:\Face reacogniton system\college_images\BestFacialRecognition.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_label=Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=500,height=130)

        # second image
        img1=Image.open(r"D:\Face reacogniton system\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_label=Label(self.root,image=self.photoimg1)
        first_label.place(x=500,y=0,width=500,height=130)


        # third image
        img2=Image.open(r"D:\Face reacogniton system\college_images\images.jpg")
        img2=img2.resize((550,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_label=Label(self.root,image=self.photoimg2)
        first_label.place(x=1000,y=0,width=550,height=130)

        # bg Image
        img3=Image.open(r"D:\Face reacogniton system\college_images\bg1.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)


        # Title
        title_label=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("items new roman",35,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=0,width=1530,height=45)


        ####time###
        def tym():
            string =strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,tym)

        lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("items new roman",12,"bold"),bg="white",fg="red")
        lbl.place(x=0,y=0,width=110,height=45)
        tym()


        # Student Button
        img4=Image.open(r"D:\Face reacogniton system\college_images\student.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        btn1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        btn1.place(x=200,y=100,width=220,height=220)


        btn1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("items new roman",15,"bold"),bg="dark blue",fg="white")
        btn1_1.place(x=200,y=300,width=220,height=40)


        # Detect face Button
        img5=Image.open(r"D:\Face reacogniton system\college_images\face_detector.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        btn1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        btn1.place(x=500,y=100,width=220,height=220)


        btn1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("items new roman",15,"bold"),bg="dark blue",fg="white")
        btn1_1.place(x=500,y=300,width=220,height=40)


        # Attendance face Button
        img6=Image.open(r"D:\Face reacogniton system\college_images\report.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        btn1=Button(bg_img,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
        btn1.place(x=800,y=100,width=220,height=220)


        btn1_1=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("items new roman",15,"bold"),bg="dark blue",fg="white")
        btn1_1.place(x=800,y=300,width=220,height=40)


        # Help desk Button
        img7=Image.open(r"D:\Face reacogniton system\college_images\help.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        btn1=Button(bg_img,image=self.photoimg7,command=self.help_desk,cursor="hand2")
        btn1.place(x=1100,y=100,width=220,height=220)


        btn1_1=Button(bg_img,text="Help Desk",command=self.help_desk,cursor="hand2",font=("items new roman",15,"bold"),bg="dark blue",fg="white")
        btn1_1.place(x=1100,y=300,width=220,height=40)


        # Train Button
        img8=Image.open(r"D:\Face reacogniton system\college_images\Train.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        btn1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        btn1.place(x=200,y=380,width=220,height=220)


        btn1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("items new roman",15,"bold"),bg="dark blue",fg="white")
        btn1_1.place(x=200,y=580,width=220,height=40)


        # Photos Button
        img9=Image.open(r"D:\Face reacogniton system\college_images\photos.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        btn1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        btn1.place(x=500,y=380,width=220,height=220)


        btn1_1=Button(bg_img,text="Photos",cursor="hand2",font=("items new roman",15,"bold"),bg="dark blue",fg="white",command=self.open_img)
        btn1_1.place(x=500,y=580,width=220,height=40)


        # Developer Button
        img10=Image.open(r"D:\Face reacogniton system\college_images\Developer2.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        btn1=Button(bg_img,image=self.photoimg10,command=self.developer_data,cursor="hand2")
        btn1.place(x=800,y=380,width=220,height=220)


        btn1_1=Button(bg_img,text="Developer",command=self.developer_data,cursor="hand2",font=("items new roman",15,"bold"),bg="dark blue",fg="white")
        btn1_1.place(x=800,y=580,width=220,height=40)


        # Exit Button
        img11=Image.open(r"D:\Face reacogniton system\college_images\exit.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        btn1=Button(bg_img,image=self.photoimg11,command=self.exitohome,cursor="hand2")
        btn1.place(x=1100,y=380,width=220,height=220)


        btn1_1=Button(bg_img,text="Exit",command=self.exitohome,cursor="hand2",font=("items new roman",15,"bold"),bg="dark blue",fg="white")
        btn1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")
    
    def exitohome(self):
        self.exitohome=tkinter.messagebox.askyesno("Face Recognition","Are you sure want to exit from this project",parent=self.root)
        if self.exitohome:
            self.root.destroy()
        else:
            return





    ####Function buttons###3
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)





if __name__=="__main__":
    root=Tk()
    obj=Face_recognition_System(root)
    root.mainloop()