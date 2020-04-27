from tkinter import*
from PIL import ImageTk
class student:
    def __init__(self,root):
      self.root=root
      self.root.title("Student Management System")
      self.root.geometry("1350x700+0+0")

      title=Label(self.root,text="Student Managemnt System",bd=10,relief=GROOVE,font=("time new roman",40,"bold"),bg="yellow",fg="red")
      title.pack(side=TOP,fill=X)

      Manage_frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
      Manage_frame.place(x=20,y=90,width=350,height=560)

      detail_frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
      detail_frame.place(x=500,y=90,width=750,height=560)

root=Tk()
ob=student(root)
root.mainloop()


