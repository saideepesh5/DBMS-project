import datetime
import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector



def main():
    win=Tk()
    app=Login_Window(win)       
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\dell\OneDrive\Desktop\webproject\librarybgnew.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="lightgray")
        frame.place(x=810, y=170, width=340, height=450)

        img1 = Image.open(r"C:\Users\dell\OneDrive\Desktop\webproject\newloginicon.jpg")
        img1 = img1.resize((100, 100))
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="lightgray", borderwidth=0)
        lblimg1.place(x=930, y=175, width=100, height=100)

        get_str = Label(frame, text="Admin_login", font=("times new roman", 20, "bold"), fg="RoyalBlue", bg="lightgray")
        get_str.place(x=95, y=100)


        # Label


        username = lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="RoyalBlue", bg="lightgray")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="RoyalBlue", bg="lightgray")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame,show="*",font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)


        # Show password button
        self.show_password_var = tk.IntVar()
        self.show_password_checkbox = tk.Checkbutton(self.root, text="",bg="black", variable=self.show_password_var, command=self.toggle_password_visibility)
        self.show_password_checkbox.place(x=1090, y=420)

        

        # Icon image
        img2 = Image.open(r"C:\Users\dell\OneDrive\Desktop\webproject\loginusernamelogo.jpg")
        img2 = img2.resize((25, 25))
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg1.place(x=850, y=323, width=25, height=25)

        img3 = Image.open(r"C:\Users\dell\OneDrive\Desktop\webproject\passwordlogo.jpg")
        img3 = img3.resize((25, 25))
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg1.place(x=850, y=395, width=25, height=25)

        # login button
        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # registerbutton
        loginbtn = Button(frame, text="New User Register",command=self.register_window, font=("times new roman", 10, "bold"), borderwidth=0, relief=RIDGE, fg="blue", bg="lightgray", activeforeground="white", activebackground="black")
        loginbtn.place(x=10, y=350, width=120)

        # forgetbutton
        loginbtn = Button(frame, text="Forget Password",command=self.forgot_password_window,font=("times new roman", 10, "bold"), borderwidth=0, relief=RIDGE, fg="blue", bg="lightgray", activeforeground="white", activebackground="black")
        loginbtn.place(x=10, y=380, width=120)

        # Reset Button
        self.btnreset = tk.Button(self.root, text="Reset", command=self.reset,font=("times new roman", 10, "bold"), borderwidth=0, relief=RIDGE, fg="blue", bg="lightgray", activeforeground="white", activebackground="black")
        self.btnreset.place(x=1000, y=525, width=120)


    def reset(self):
        self.txtuser.delete(0, 'end')
        self.txtpass.delete(0, 'end')
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def toggle_password_visibility(self):
        if self.show_password_var.get() == 1:
            self.txtpass.config(show="")
        else:
            self.txtpass.config(show="*")



    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root2)

        elif self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu":
            messagebox.showinfo("Success", "Welcome to codewithkiran channel, please subscribe to my channel",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Saideepesh5##", database="library", port=3306)
            my_cursor= conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                       self.txtuser.get(),
                                                                                       self.txtpass.get()
                                                                                    ))
            row=my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Username & password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only admin")
                if open_main:
                    self.new_window = Toplevel(self.root)  # Use self.root, not self.new_window
                    self.app = LibraryManagementSystem(self.new_window)
                    self.reset()
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # ===============================reset password========================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the Security Question",parent=self.root2)
        elif self.txt_security_A.get()=="":
            messagebox.showerror("Error","Please Enter the answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please  enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Saideepesh5##", database="library", port=3306)
            my_cursor= conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value =(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security_A.get())
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please enter correct answer",parent=self.root2)
            else:
                query = "UPDATE register SET password = %s WHERE email = %s"
                value = (self.txt_new_password.get(), self.txtuser.get())  # Include the email address
                my_cursor.execute(query, value)


                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset,please login with new password",parent=self.root2)
                self.root2.destroy()
            

    #=====================================forgot password========================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Saideepesh5##", database="library", port=3306)
            my_cursor= conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error","Please enter the valid user name",parent=self.root2)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                self.root2.configure(bg="powderblue")  # Set the background color

                l=Label(self.root2,text="Forget Password",font=("times new roman", 15, "bold"), fg="red", bg="powderblue")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),fg="blueviolet",bg="powderblue")
                security_Q.place(x=50,y=80)
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15),state="readonly")
                self.combo_security_Q["values"]=("Select","Your favorite book or movie?","City where you were born?","Your favorite color?")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="blueviolet",bg="powderblue")
                security_A.place(x=50,y=150)
                self.txt_security_A=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security_A.place(x=50,y=180,width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), fg="blueviolet", bg="powderblue")
                new_password.place(x=50, y=220)

                self.txt_new_password = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_new_password.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Reset", command=self.reset_pass, font=("times new roman", 15, "bold"), fg="blueviolet", bg="powderblue")
                btn.place(x=100, y=290)


         


            




class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # =============variable=================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        # ====================================bg image==================================
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\dell\OneDrive\Desktop\webproject\registerbg.jpg") #r convert backward slash into forward slash
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1) #rel=relation image cover window as own
        # ================================left image======================================
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\dell\OneDrive\Desktop\webproject\quotes.jpg") #r convert backward slash into forward slash
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=520)

        # ==================main fram===========
        frame=Frame(self.root,bg="gainsboro")
        frame.place(x=520,y=100,width=800,height=520)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="navy",bg="gainsboro")
        register_lbl.place(x=20,y=20)

        # =================label and entry=====================
        # --------------------row 1
        fname=Label(frame,text="First Name ",font=("times new roman",15,"bold"),fg="blueviolet",bg="gainsboro")
        fname.place(x=50,y=100)
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name ",font=("times new roman",15,"bold"),fg="blueviolet",bg="gainsboro")
        lname.place(x=370,y=100)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)
        #-------------------row 2 
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="blueviolet",bg="gainsboro")
        contact.place(x=50,y=170)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="blueviolet",bg="gainsboro")
        email.place(x=370,y=170)
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        # ----------------------row 3

        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),fg="blueviolet",bg="gainsboro")
        security_Q.place(x=50,y=240)
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15),state="readonly")
        self.combo_security_Q["values"]=("Select","Your favorite book or movie?","City where you were born?","Your favorite color?")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="blueviolet",bg="gainsboro")
        security_A.place(x=370,y=240)
        self.txt_security_A=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security_A.place(x=370,y=270,width=250)

        # ---------------------row 4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="blueviolet",bg="gainsboro")
        pswd.place(x=50,y=310)
        self.txt_pswd=ttk.Entry(frame,show="*",textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="blueviolet",bg="gainsboro")
        confirm_pswd.place(x=370,y=310)
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        # ===================check button=================
        self.var_check=IntVar() #integer data type IntVar
        checkbtn = Checkbutton(frame, text="I Agree The Terms & Conditions", variable=self.var_check, font=("times new roman", 15, "bold"), fg="blueviolet", bg="gainsboro", onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # =======================buttons=======================
        btnreg = Button(frame, text="Register", command=self.register_data, font=("times new roman", 18, "bold"), width=25, fg="blueviolet", bg="gainsboro")
        btnreg.place(x=10, y=440, width=300)

        btnlogin = Button(frame, text="Login", command=self.return_login,font=("times new roman", 18, "bold"), width=25, fg="blueviolet", bg="gainsboro", borderwidth=1)
        btnlogin.place(x=390, y=440, width=300)

    # ================function declaration=========================

    def register_data(self):
        if self.var_fname.get() == "":
            messagebox.showerror("Error", "First Name is required",parent=self.root)
        elif self.var_email.get() == "":
            messagebox.showerror("Error", "Email is required",parent=self.root)
        elif self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "Security Question is required",parent=self.root)
        elif self.var_pass.get() =="":
            messagebox.showerror("Error","Please Enter password",parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and Confirm Password must be the same",parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error","Please agree our terms and condition",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Saideepesh5##", database="library", port=3306)
            my_cursor= conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_fname.get(),
                                                                                self.var_lname.get(),
                                                                                self.var_contact.get(),
                                                                                self.var_email.get(),
                                                                                self.var_securityQ.get(),
                                                                                self.var_securityA.get(),
                                                                                self.var_pass.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully",parent=self.root)
                self.root.destroy()

    def return_login(self):
        self.root.destroy()


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        # ===============================variable===============================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue=StringVar()
        self.finalprice=StringVar()
        

        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times mew roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)
        # =======================================DataFrameLeft===============================
        DataFrameLeft=LabelFrame(frame,text="Library Member Information",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times mew roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type :",font=("arial",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        comMember=ttk.Combobox(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.member_var,width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_NO=Label(DataFrameLeft,bg="powder blue",text="PRN No :",padx=2,font=("arial",12,"bold"))
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID_No :",font=("arial",12,"bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="FirstName :",font=("arial",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="powder blue",text="LastName :",font=("arial",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address1 :",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address2 :",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="PostCode :",font=("arial",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile :",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)


        lblBookId=Label(DataFrameLeft,bg="powder blue",text=" BookId :",font=("arial",12,"bold"),padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text=" BookTitle :",font=("arial",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuther=Label(DataFrameLeft,bg="powder blue",text=" Auther :",font=("arial",12,"bold"),padx=2,pady=6)
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.auther_var,width=29)
        txtAuther.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text=" DateBorrowed :",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,bg="powder blue",text=" DateDue :",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text=" DaysOnBook :",font=("arial",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.daysonbook,width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text=" LateReturnFine :",font=("arial",12,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lateratefine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverdate=Label(DataFrameLeft,bg="powder blue",text=" DateOverdate :",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        txtDateOverdate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateoverdue,width=29)
        txtDateOverdate.grid(row=7,column=3)
        
        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text=" ActualPrice :",font=("arial",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.finalprice,width=29)
        txtActualPrice.grid(row=8,column=3)

        


        # ==========================================DataFrame Right==================================

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times mew roman",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text (DataFrameRight, font=("arial",12, "bold"), width=32, height=16, padx=2,pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listBooks=["Head Firt Book","Learn Python The Hard Way","Python Programming", "Secrete Rahshy", "Python CookBook", "Into to Machine Learning", "Fluent Python","Machine tecno","My Python","Joss Ellif guru", "Elite Jungle python", "Jungli Python", "Mumbai Python","Pune Python","Machine python", "Advance Python","Inton Python", "RedChilli Python","Ishq Python"]
        books_info = {"Head Firt Book": {"Book ID": "BKID001", "Author": "Author 1", "Price": "$29.99"},"Learn Python The Hard Way": {"Book ID": "BKID002", "Author": "Author 2", "Price": "$19.99"},"Python Programming": {"Book ID": "BKID003", "Author": "Author 3", "Price": "$24.99"},"Secrete Rahshy": {"Book ID": "BKID004", "Author": "Author 4", "Price": "$14.99"},"Python CookBook": {"Book ID": "BKID005", "Author": "Author 5", "Price": "$34.99"},"Into to Machine Learning": {"Book ID": "BKID006", "Author": "Author 6", "Price": "$39.99"},"Fluent Python": {"Book ID": "BKID007", "Author": "Author 7", "Price": "$31.99"},"Machine Tecno": {"Book ID": "BKID008", "Author": "Author 8", "Price": "$27.99"},"My Python": {"Book ID": "BKID009", "Author": "Author 9", "Price": "$22.99"},"Joss Ellif Guru": {"Book ID": "BKID010", "Author": "Author 10", "Price": "$23.99"},"Elite Jungle Python": {"Book ID": "BKID011", "Author": "Author 11", "Price": "$28.99"},"Jungli Python": {"Book ID": "BKID012", "Author": "Author 12", "Price": "$19.99"},"Mumbai Python": {"Book ID": "BKID013", "Author": "Author 13", "Price": "$29.99"},"Pune Python": {"Book ID": "BKID014", "Author": "Author 14", "Price": "$18.99"},"Machine Python": {"Book ID": "BKID015", "Author": "Author 15", "Price": "$26.99"},"Advance Python": {"Book ID": "BKID016", "Author": "Author 16", "Price": "$36.99"},"Inton Python": {"Book ID": "BKID017", "Author": "Author 17", "Price": "$21.99"},"RedChilli Python": {"Book ID": "BKID018", "Author": "Author 18", "Price": "$30.99"},"Ishq Python": {"Book ID": "BKID019", "Author": "Author 19", "Price": "$17.99"}}







        def SelectBook(event=""):
              value = str(listBox.get(listBox.curselection()))
              x = value
              if x in books_info:
                   book_details = books_info[x]
                   self.bookid_var.set(book_details["Book ID"])
                   self.booktitle_var.set(x)
                   self.auther_var.set(book_details["Author"])
                   self.finalprice.set(book_details["Price"])
                   d1 = datetime.datetime.today()
                   d2 = datetime.timedelta(days=15)
                   d3 = d1 + d2
                   # Format date and time as strings
                   formatted_d1 = d1.strftime('%Y-%m-%d %H:%M:%S')
                   formatted_d3 = d3.strftime('%Y-%m-%d %H:%M:%S')
                   self.dateborrowed_var.set(formatted_d1)
                   self.datedue_var.set(formatted_d3)
                   self.daysonbook.set(15)
                   self.lateratefine_var.set("Rs.50")
                   self.dateoverdue.set("NO")
                
                    


        listBox=Listbox (DataFrameRight, font=("arial", 12, "bold"), width=20, height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        # ====================================Button Frame==========================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button (Framebutton, text="Add Data",command=self.adda_data, font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0,column=0)
        btnAddData=Button (Framebutton, text="Show Data",command=self.showData,font=("arial",12,"bold"), width=23,bg="blue",fg="white")
        btnAddData.grid(row=0, column=1)
        btnAddData=Button (Framebutton, text="Update",command=self.update, font=("arial", 12, "bold"), width=23, bg="blue",fg="white")
        btnAddData.grid(row=0, column=2)
        btnAddData=Button (Framebutton, text="Delete",command=self.delete,font=("arial",12,"bold"),width=23, bg="blue",fg="white")
        btnAddData.grid(row=0, column=3)
        btnAddData=Button (Framebutton, text="Reset", command=self.reset,font=("arial", 12, "bold"),width=23, bg="blue",fg="white")
        btnAddData.grid(row=0, column=4)
        btnAddData=Button (Framebutton, text="Exit", command=self.iExit,font=("arial", 12, "bold"),width=23, bg="blue",fg="white") 
        btnAddData.grid(row=0, column=5)

        # ====================================Information Frame==========================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1530,height=195)

        Table_frame=Frame (FrameDetails, bd=6, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0,y=2, width=1460, height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk. Treeview (Table_frame, column=("memebertype", "prnno", "idno", "firtname","lastname", "adress1", "adress2", "postid", "mobile", "bookid", "booktitle", "auther","dateborrowed", "datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        
        self.library_table.heading("memebertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN No.")
        self.library_table.heading("idno", text="ID_NO")
        self.library_table.heading("firtname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("adress1", text="Address1")
        self.library_table.heading("adress2", text="Address2")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("mobile", text="Mobile Number")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("auther", text="Auther")
        self.library_table.heading("dateborrowed", text="Date Of Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="DaysOnBook")
        self.library_table.heading("latereturnfine", text="LateReturnFine")
        self.library_table.heading("dateoverdue", text="DateOverDue")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("memebertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("idno", width=100)
        self.library_table.column("firtname", width=100)
        self.library_table.column("lastname", width=108)
        self.library_table.column("adress1", width=100)
        self.library_table.column("adress2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("auther", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=180)
        self.library_table.column("latereturnfine", width=108)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

        self.fatch_data()
        self.library_table.bind("<<TreeviewSelect>>", self.get_cursor)


    def adda_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="Saideepesh5##", database="library", port=3306)
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO library_mang VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                             (self.member_var.get(), self.prn_var.get(), self.id_var.get(), self.firstname_var.get(),
                              self.lastname_var.get(), self.address1_var.get(), self.address2_var.get(),
                              self.postcode_var.get(), self.mobile_var.get(), self.bookid_var.get(),
                              self.booktitle_var.get(), self.auther_var.get(), self.dateborrowed_var.get(),
                              self.datedue_var.get(), self.daysonbook.get(), self.lateratefine_var.get(),
                              self.dateoverdue.get(), self.finalprice.get()))
            conn.commit()
            self.fatch_data()
            conn.close()

            messagebox.showinfo("Success", "Member has been inserted successfully",parent=self.root)
   
            self.member_var.set("")
            self.prn_var.set("")
            self.id_var.set("")
            self.firstname_var.set("")
            self.lastname_var.set("")
            self.address1_var.set("")
            self.address2_var.set("")
            self.postcode_var.set("")
            self.mobile_var.set("")
            self.bookid_var.set("")
            self.booktitle_var.set("")
            self.auther_var.set("")
            self.dateborrowed_var.set("")
            self.datedue_var.set("")
            self.daysonbook.set("")
            self.lateratefine_var.set("")
            self.dateoverdue.set("")
            self.finalprice.set("")

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        
    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Saideepesh5##", database="library", port=3306)
        my_cursor = conn.cursor() 
        my_cursor.execute("select * from library_mang")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0])
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue.set(row[16]),
        self.finalprice.set(row[17])

    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END, "PRN No:\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END, "ID No: \t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END, "FirstName:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END, "LastName:\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END, "Address1:\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END, "Address2:\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END, "Post Code: \t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END, "Mobile No: \t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book ID:\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Book Title:\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END, "Auther:\t\t"+ self.auther_var.get() + "\n")
        self.txtBox.insert (END, "DateBorrowed: \t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END, "DateDue: \t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "DaysOnBook: \t\t"+ self.daysonbook.get() + "\n")
        self.txtBox.insert(END, "LateRate Fine:\t\t"+ self.lateratefine_var.get() + "\n")
        self.txtBox.insert(END, "DateOverDue:\t\t"+ self.dateoverdue.get() + "\n")
        self.txtBox.insert(END, "FinallPrice:\t\t"+ self.finalprice.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook.set(""),
        self.lateratefine_var.set(""),
        self.dateoverdue.set(""),
        self.finalprice.set("")
        self.txtBox.delete("1.0", END)
        

    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error", "First Selct the Member",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="Saideepesh5##", database="library",port=3306)
            my_cursor=conn.cursor()
            query="delete from library_mang where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query, value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("Success", "Memeber has been Deleted",parent=self.root)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno ("Library managemnt System", "Do you want to exit",parent=self.root)
        if iExit>0:
            self.root.destroy()
            return
    

    def update(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Saideepesh5##",database="library",port=3306)
        my_cursor = conn.cursor()
        my_cursor.execute(
        "UPDATE library_mang SET Member=%s, ID=%s, FirstName=%s, LastName=%s, Address1=%s, Address2=%s, Postid=%s, Mobile=%s, Bookid=%s, BookTitle=%s, Auther=%s, Dateborrowed=%s, Datedue=%s, Daysofbook=%s, Latereturnfine=%s, Dateoverdue=%s, Finalprice=%s WHERE PRN_NO=%s",
        (
            self.member_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.auther_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook.get(),
            self.lateratefine_var.get(),
            self.dateoverdue.get(),
            self.finalprice.get(),
            self.prn_var.get(),
        ))
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success", "Member has been updated",parent=self.root)

if __name__ == "__main__":
    main()
