import cv2
import cv2.data
import numpy as np
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_label = Label(self.root, text="TRAIN DATA SET", font=("Times New Roman", 35, "bold"), bg="white", fg="red")
        title_label.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"D:\Face reacogniton system\college_images\facialrecognition.png")
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_label = Label(self.root, image=self.photoimg_top)
        first_label.place(x=5, y=55, width=1530, height=325)

        # Button
        btn1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("Times New Roman", 30, "bold"), bg="red", fg="white")
        btn1_1.place(x=0, y=380, width=1530, height=60)

        img_bottom = Image.open(r"D:\Face reacogniton system\college_images\photos.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        second_label = Label(self.root, image=self.photoimg_bottom)
        second_label.place(x=5, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.jpg')]

        faces = []
        ids = []


        # Load the pre-trained Haar cascade for face detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        


        for image in path:
            img = cv2.imread(image)
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            detected_faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in detected_faces:
                face = gray_img[y:y+h, x:x+w]
                id_str = os.path.split(image)[1].split('.')[1]
                id = int(id_str)

                # Resize face to 200x200 for consistency
                face_resized = cv2.resize(face, (200, 200))
                faces.append(face_resized)
                ids.append(id)

        ids = np.array(ids)

        # Create an LBPH face recognizer
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Data Set completed")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()