from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
#import pymysql
import mysql.connector
from tkinter import messagebox
#import MySQLdb
#import sqlite3

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Record Book")   # That's the main window i.e initialising the constructor, given height, width, title
        self.root.geometry("1350x700+0+0")
         
        title=Label(self.root,bd=10,relief=GROOVE,text="Student Record Book",font=("times new roman",40,"bold"),bg="lightgreen",fg="darkblue")
        title.pack(side=TOP,fill=X)
        
        img1=Image.open("D:\IIIT\Python\Project\logo.png")
        img1=img1.resize((68,58),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)#button1 place it in the label with help of button making button in self.root
        b1.place(x=230,y=13)

        ###all variables
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()        # variable to be used for entry in database
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        

        self.search_by=StringVar()
        self.search_txt=StringVar()
        #Manage Frame
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="gold")
        Manage_Frame.place(x=20,y=100,width=450,height=530)
        
        m_title=Label(Manage_Frame,text="Student Data :",font=("times new roman",20,"bold"),bg="gold",fg="darkgreen")
        m_title.grid(row=0,columnspan=2,pady=12)

        lbl_roll=Label(Manage_Frame,text="Roll No:",font=("times new roman",20,"bold"),fg="purple")
        lbl_roll.grid(row=1,column=0,pady=5,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=5,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name:",font=("times new roman",20,"bold"),fg="purple")
        lbl_name.grid(row=2,column=0,pady=5,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=5,padx=20,sticky="w")
        
        lbl_Email=Label(Manage_Frame,text="Email:",font=("times new roman",20,"bold"),fg="purple")
        lbl_Email.grid(row=3,column=0,pady=5,padx=20,sticky="w")

        txt_Email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        lbl_Gender=Label(Manage_Frame,text="Gender:",font=("times new roman",20,"bold"),fg="purple")
        lbl_Gender.grid(row=4,column=0,pady=5,padx=20,sticky="w")
         
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state="readonly")
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4,column=1,padx=20,pady=5)
        
        lbl_Contact=Label(Manage_Frame,text="Contact:",font=("times new roman",20,"bold"),fg="purple")
        lbl_Contact.grid(row=5,column=0,pady=5,padx=20,sticky="w")

        txt_Contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=5,padx=20,sticky="w")

        lbl_dob=Label(Manage_Frame,text="D.O.B:",font=("times new roman",20,"bold"),fg="purple")
        lbl_dob.grid(row=6,column=0,pady=5,padx=20,sticky="w")

        txt_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=5,padx=20,sticky="w")

        lbl_address=Label(Manage_Frame,text="Address:",font=("times new roman",20,"bold"),fg="purple")
        lbl_address.grid(row=7,column=0,pady=5,padx=20,sticky="w")
        
        self.txt_Address=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_Address.grid(row=7,column=1,pady=5,padx=20,sticky="w")
        #ButtonFrame
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="violet")
        btn_Frame.place(x=10,y=460,width=410)

        AddBtn=Button(btn_Frame,text="Add",width=10,command=self.add_students,bg="lightgreen").grid(row=0,column=0,padx=10,pady=10)
        updateBtn=Button(btn_Frame,text="Update",width=10,command=self.update_data,bg="lightgreen").grid(row=0,column=1,padx=10,pady=10)
        deleteBtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data,bg="lightgreen").grid(row=0,column=2,padx=10,pady=10)
        ClearBtn=Button(btn_Frame,text="Clear",width=10,command=self.clear,bg="lightgreen").grid(row=0,column=3,padx=10,pady=10)

        #DetailFrame
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="OliveDrab1")
        Detail_Frame.place(x=500,y=100,width=750,height=530)
        
        lbl_search=Label(Detail_Frame,text="Search By:",font=("times new roman",20,"bold"),bg="OliveDrab1",fg="darkblue")
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        
        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=("Roll_No","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)
        
        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        
        searchBtn=Button(Detail_Frame,command=self.search_data,text="Search",font=("times new roman",11,"bold"),width=9,bg="yellow").grid(row=0,column=3,padx=10,pady=5)
        showallBtn=Button(Detail_Frame,text="Show All",width=9,command=self.fetch_data,font=("times new roman",11,"bold"),bg="yellow").grid(row=0,column=4,padx=10,pady=5)

        #####table frame
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=700,height=440)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.configure(command=self.Student_table.xview)
        scroll_y.configure(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact No.")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("Address",text="Address")
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("Address",width=100)
        self.Student_table['show']='headings'
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.Roll_No_var.get()=="" or self.email_var.get()=="" or self.email_var.get()==""or self.gender_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="" or self.txt_Address.get=="":
             messagebox.showerror("Error","All fields are required")
        else: 
            mydb=mysql.connector.connect(host="localhost",user="root",password="",database="stm")

            mycursor=mydb.cursor()

            s="INSERT INTO students values(%s,%s,%s,%s,%s,%s,%s)"
            b1=(self.Roll_No_var.get(),
                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.txt_Address.get('1.0',END))
            mycursor.execute(s,b1)
            mydb.commit()
            self.fetch_data()
            self.clear()
            mydb.close()
            messagebox.showinfo("Success","Data has been inserted")
    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="stm")

        mycursor=con.cursor()
        s='Select * from students'
        mycursor.execute(s)
        rows=mycursor.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")     
        self.email_var.set("")     
        self.gender_var.set("")     
        self.contact_var.set("")     
        self.dob_var.set("")     
        self.txt_Address.delete("1.0",END) 
    
    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        #print(row)
        #con=mysql.connector.connect(host="localhost",user="root",port=3307,password="",database="student")
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])     
        self.email_var.set(row[2])     
        self.gender_var.set(row[3])     
        self.contact_var.set(row[4])     
        self.dob_var.set(row[5])     
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])
    
    def update_data(self):
        mydb=mysql.connector.connect(host="localhost",user="root",password="",database="stm")

        mycursor=mydb.cursor()

        s="UPDATE students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll=%s"
        b1=(
            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.dob_var.get(),
            self.txt_Address.get('1.0',END),
            #self.Roll_No_var.get()
            self.Roll_No_var.get())

        mycursor.execute(s,b1)
        mydb.commit()
        self.fetch_data()
        self.clear()
        mydb.close()
    def delete_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="stm")
        mycursor=con.cursor()
        a="delete from students where roll=%s"
        b=self.Roll_No_var.get()
        mycursor.execute(a,(b,))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    def search_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="stm")

        mycursor=con.cursor()
        a=self.search_by.get()
        print(a)
        s=""
        if(a=="Roll_No"): s=("Select * from student where roll ='"+ self.search_txt.get() + "'")
        if(a=="Name"): s="Select * from student where name name ='"+ self.search_txt.get() + "'" 
        if(a=="Contact"): s="Select * from student where contact ='"+ self.search_txt.get() + "'"       
        mycursor.execute(s)
        rows=mycursor.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        


root=Tk()
ob=Student(root)
root.mainloop()    