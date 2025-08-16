from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_recognition


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x850+0+0")
        self.root.title("face Recognition System")

        #first image
        img1=Image.open(r"college_images\BestFacialRecognition.jpg")
        img1= img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img2=Image.open(r"college_images\facialrecognition.png")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third image
        img3=Image.open(r"college_images\images.jpg")
        img3 = img3.resize((550, 130), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        #bg image
        img4=Image.open(r"college_images\bgimg.jpg")
        img4 = img4.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img5=Image.open(r"college_images\student.jpg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


        #Detect face button
        img6=Image.open(r"college_images\face_detector1.jpg")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)


        #Attendence face button
        img7=Image.open(r"college_images\attendence.jpg")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendence",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        
        #Help face button
        img8=Image.open(r"college_images\HelpDesk.jpg")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
    
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)


        #Train face button
        img9=Image.open(r"college_images\Train.jpg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
    
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)


        #Photos Button
        img10=Image.open(r"college_images\photos.jpg")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
    
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)


        #Developer Button
        img11=Image.open(r"college_images\Developer (2).jpg")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
    
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)


        #Exit Button
        img12=Image.open(r"college_images\exit.jpg")
        img12 = img12.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)
    
        b1=Button(bg_img,image=self.photoimg12,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    #===================Functions buttons==================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Face_recognition(self.new_window)




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()


