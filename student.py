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
        self.root.title("face Recognition System")

        ###variables#####
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phones=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        # first Image
        img=Image.open(r"D:\Face reacogniton system\college_images\face-recognition.png")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_label=Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=500,height=130)

        # second image
        img1=Image.open(r"D:\Face reacogniton system\college_images\smart-attendance.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_label=Label(self.root,image=self.photoimg1)
        first_label.place(x=500,y=0,width=500,height=130)


        # third image
        img2=Image.open(r"D:\Face reacogniton system\college_images\st1.jpg")
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
        title_label=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM ",font=("items new roman",35,"bold"),bg="white",fg="darkgreen")
        title_label.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=55,width=1480,height=600)


        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"D:\Face reacogniton system\college_images\Hlo.jpeg")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        first_label=Label(Left_frame,image=self.photoimg_left)
        first_label.place(x=5,y=0,width=720,height=130)

        # current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=150)

        #Department
        dep_label=Label(current_course_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","CIVIL","MECHANICAL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)


        #Course
        course_label=Label(current_course_frame,text="Course:",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #Year
        year_label=Label(current_course_frame,text="Year:",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2020-21","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        
        #Semester
        semester_label=Label(current_course_frame,text="Semester:",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Sem-1","Sem-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

       # Class student information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class student information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=250, width=720, height=300)

        # Student ID
        studentId_label = Label(class_student_frame, text="StudentID:", font=("times new roman", 12, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)
        studentId_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=("times new roman", 13, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studentName_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_name, width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        class_div_label = Label(class_student_frame, text="Division:", font=("times new roman", 12, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=20)
        div_combo["values"]=("A","B","C",)
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
        # Roll No
        Roll_NO_label = Label(class_student_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white")
        Roll_NO_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        Roll_NO_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=("times new roman", 13, "bold"))
        Roll_NO_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other",)
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        # DOB
        dob_label = Label(class_student_frame, text="DOB:", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone No
        phone_label = Label(class_student_frame, text="Phone no:", font=("times new roman", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phones, width=20, font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        Address_label = Label(class_student_frame, text="Address:", font=("times new roman", 12, "bold"), bg="white")
        Address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        Address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 13, "bold"))
        Address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher name
        Teacher_label = Label(class_student_frame, text="Teacher Name:", font=("times new roman", 12, "bold"), bg="white")
        Teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        Teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 13, "bold"))
        Teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, text="Take Photo Sample", variable=self.var_radio1, value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(class_student_frame, text="No Photo Sample", variable=self.var_radio1, value="No")
        radiobtn2.grid(row=6, column=1)



        #buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="Update", command=self.Update_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)


        dlt_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        dlt_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

        
        # Right label frame
        RIGHT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        RIGHT_frame.place(x=750,y=10,width=720,height=580)

        img_right=Image.open(r"D:\Face reacogniton system\college_images\student.jpg")
        img_right=img_right.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        first_label=Label(RIGHT_frame,image=self.photoimg_right)
        first_label.place(x=5,y=0,width=720,height=130)

        ######### SEARCH SYSYTEM  ######
        search_frame=LabelFrame(RIGHT_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        

        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show ALL",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #Table frame
        table_frame=Frame(RIGHT_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    ######function declarartion#####
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Feils are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Ziya@123",database="shahvez")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_std_id.get(),
                                                                                                self.var_name.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phones.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_radio1.get()
                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Succes","Student details has been added succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)    
           
    #######Fetch Data####
    def fetch_data(self):   
        conn=mysql.connector.connect(host="localhost",username="root",password="Ziya@123",database="shahvez")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()   

    #######get cursor####
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]


        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])  
        self.var_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phones.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14]) 

    #update function#
    def Update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Feils are Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update student details",parent=self.root)
                if Update:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Ziya@123",database="shahvez")
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE student SET Dep=%s, course=%s, Year=%s, semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where StudentID=%s", (

                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                    
                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                    self.var_phones.get(),
                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                    self.var_std_id.get(),
                                                                                                                                                               ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    
    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required")
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Dp you want to delete this student",parent=self.root)
                if delete:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Ziya@123",database="shahvez")
                    my_cursor=conn.cursor()
                    sql="delete from student where StudentID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    #reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_name.set("")
        self.var_div.set("A")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phones.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    ##Generate data set Take photo Sample###
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                # Debug: Checking variable values
                print(f"Department: {self.var_dep.get()}, Name: {self.var_name.get()}, Student ID: {self.var_std_id.get()}")
                
                conn = mysql.connector.connect(host="localhost", username="root", password="Ziya@123", database="shahvez")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                
                # Debug: Checking fetched ID
                print(f"Fetched ID: {id}")
                
                my_cursor.execute("UPDATE student SET Dep=%s, course=%s, Year=%s, semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where StudentID=%s", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phones.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data on face frontals from OpenCV
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                if face_classifier.empty():
                    raise ValueError("Haarcascade XML file not found or could not be loaded.")
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped
                    return None
                
                cap = cv2.VideoCapture(0)
                if not cap.isOpened():
                    raise ValueError("Webcam could not be opened.")
                
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if not ret:
                        print("Failed to grab frame")
                        break
                    
                    cropped_face = face_cropped(my_frame)
                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)






if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
