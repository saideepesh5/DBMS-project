from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

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
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
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

        btnlogin = Button(frame, text="Login", font=("times new roman", 18, "bold"), width=25, fg="blueviolet", bg="gainsboro", borderwidth=1)
        btnlogin.place(x=390, y=440, width=300)

    # ================function declaration=========================

    def register_data(self):
        if self.var_fname.get() == "":
            messagebox.showerror("Error", "First Name is required")
        elif self.var_email.get() == "":
            messagebox.showerror("Error", "Email is required")
        elif self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "Security Question is required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and Confirm Password must be the same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error","Please agree our terms and condition")
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
                messagebox.showinfo("Success","Register Successfully")
                

            

        

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
