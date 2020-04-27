from tkinter import*
from PIL import ImageTk
from tkinter import ttk
class student:
    def __init__(self,root):
      self.root=root
      self.root.title("Student Management System")
      self.root.geometry("1350x700+0+0")

      title=Label(self.root,text="Student Managemnt System",bd=10,relief=GROOVE,font=("time new roman",40,"bold"),bg="yellow",fg="red")
      title.pack(side=TOP,fill=X)

      # Manage frame

      Manage_frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
      Manage_frame.place(x=20,y=90,width=450,height=600)

      m_title = Label(Manage_frame,text="Manage Students",font=("time new roman",20,"bold"),bg ="crimson",fg="white")
      m_title.grid(row=0,columnspan=2,pady=20)
      

      lbl_roll =Label(Manage_frame,text="Roll Number.",font=("time new roman",10,"bold"),bg ="crimson",fg="white")
      lbl_roll.grid(row=1,column=0,pady=20,sticky="w")

      txt_roll=Entry(Manage_frame,font=("time new roman",15,"bold"),bd=5,relief=GROOVE)
      txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")
      

      lbl_name =Label(Manage_frame,text="Name.",font=("time new roman",10,"bold"),bg ="crimson",fg="white")
      lbl_name.grid(row=2,column=0,pady=20,sticky="w")

      txt_name=Entry(Manage_frame,font=("time new roman",15,"bold"),bd=5,relief=GROOVE)
      txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

      lbl_email=Label(Manage_frame,text="Email.",font=("time new roman",10,"bold"),bg ="crimson",fg="white")
      lbl_email.grid(row=3,column=0,pady=20,sticky="w")

      txt_email=Entry(Manage_frame,font=("time new roman",15,"bold"),bd=5,relief=GROOVE)
      txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

      lbl_gender=Label(Manage_frame,text="Gender",font=("time new roman",10,"bold"),bg ="crimson",fg="white")
      lbl_gender.grid(row=4,column=0,pady=20,sticky="w")

      combo_gender=ttk.Combobox(Manage_frame,font=("time new roman",13,"bold"),state="readonly")
      combo_gender["values"]=("male","female","other")
      combo_gender.grid(row=4,column=1,padx=20,pady=10)



      lbl_contact=Label(Manage_frame,text="Contact.",font=("time new roman",10,"bold"),bg ="crimson",fg="white")
      lbl_contact.grid(row=5,column=0,pady=20,sticky="w")

      txt_contact=Entry(Manage_frame,font=("time new roman",15,"bold"),bd=5,relief=GROOVE)
      txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

      lbl_DOB=Label(Manage_frame,text="D.O.B.",font=("time new roman",10,"bold"),bg ="crimson",fg="white")
      lbl_DOB.grid(row=6,column=0,pady=20,sticky="w")

      txt_DOB=Entry(Manage_frame,font=("time new roman",15,"bold"),bd=5,relief=GROOVE)
      txt_DOB.grid(row=6,column=1,pady=10,padx=20,sticky="w")

      lbl_address=Label(Manage_frame,text="Address.",font=("time new roman",10,"bold"),bg ="crimson",fg="white")
      lbl_address.grid(row=7,column=0,pady=20,sticky="w")

      txt_address=Text(Manage_frame,width=35,height=4,font=("",10))
      txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

      # Button frame
      btn_frame=Frame(Manage_frame,bd=4,relief=RIDGE,bg="crimson")
      btn_frame.place(x=10,y=535,width=430)

      addbtn=Button(btn_frame,text="ADD",width=10).grid(row=0,column=0,padx=10,pady=10)
      addbtn=Button(btn_frame,text="UPDATE",width=10).grid(row=0,column=1,padx=10,pady=10)
      addbtn=Button(btn_frame,text="DELETE",width=10).grid(row=0,column=2,padx=10,pady=10)
      addbtn=Button(btn_frame,text="CLEAR",width=10).grid(row=0,column=3,padx=10,pady=10)
     
      # Detail frame

      detail_frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
      detail_frame.place(x=500,y=90,width=800,height=600)

      lbl_search=Label(detail_frame,text="Search By",font=("time new roman",20,"bold"),bg ="crimson",fg="white")
      lbl_search.grid(row=0,column=0,pady=20,sticky="w")

      combo_search=ttk.Combobox(detail_frame,width=10,font=("time new roman",13,"bold"),state="readonly")
      combo_search["values"]=("Roll No","Name","Contact")
      combo_search.grid(row=0,column=1,padx=20,pady=10)

      txt_search=Entry(detail_frame,font=("time new roman",15,"bold"),bd=5,relief=GROOVE)
      txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

root=Tk()
ob=student(root)
root.mainloop()


