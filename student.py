from tkinter import*
from PIL import ImageTk
class student:
    def __init__(self,root):
      self.root=root
      self.root.title("Student Management System")
      self.root.geometry("1350x700+0+0")

      title=Label(self.root,text="Student Managemnt System",font=("time new roman",40,"bold"),bg="yellow",fg="red")
      title.pack(side=TOP)

root=Tk()
ob=student(root)
root.mainloop()


