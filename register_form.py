from tkinter import *
import tkinter.messagebox as MsgBox
from hashlib import sha512
from MindMedia import DBoperations,main

class RootWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("User Registration")
        width = 800
        height = 525
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        # self.root.resizable(0, 0)

        # =======================================VARIABLES=====================================
        self.Email = StringVar()
        self.Uname = StringVar()
        self.pwd1 = StringVar()
        self.pwd2 = StringVar()

        # =====================================FRAMES====================================
        TitleFrame = Frame(self.root, height=100, width=640, bd=1, relief=SOLID)
        TitleFrame.pack(side=TOP)
        RegisterFrame = Frame(self.root)
        RegisterFrame.pack(side=TOP, pady=20)

        # =====================================LABEL WIDGETS=============================
        lbl_title = Label(TitleFrame, text="MindMedia", font='monaco 23 bold', bd=20, width=600, fg='blue',bg='pink')
        lbl_title.pack()
        lbl_email = Label(RegisterFrame, text="E-mail:", font=('comic sans ms', 18), bd=18)
        lbl_email.grid(row=1)
        lbl_uname = Label(RegisterFrame, text="Username:", font=('comic sans ms', 18), bd=18)
        lbl_uname.grid(row=2)
        lbl_pwd1 = Label(RegisterFrame, text="Password:", font=('comic sans ms', 18), bd=18)
        lbl_pwd1.grid(row=3)
        lbl_pwd2 = Label(RegisterFrame, text="confirm-pwd:", font=('comic sans ms', 18), bd=18)
        lbl_pwd2.grid(row=4)
        self.lbl_result = Label(RegisterFrame, text="", font=('arial', 18))
        self.lbl_result.grid(row=5, columnspan=2)

        # =======================================ENTRY WIDGETS===========================
        email = Entry(RegisterFrame, font=('arial', 20), textvariable=self.Email, width=15)
        email.grid(row=1, column=1)
        username = Entry(RegisterFrame, font=('arial', 20), textvariable=self.Uname, width=15)
        username.grid(row=2, column=1)
        pass1 = Entry(RegisterFrame, font=('arial', 20), textvariable=self.pwd1, width=15, show='*')
        pass1.grid(row=3, column=1)
        pass2 = Entry(RegisterFrame, font=('arial', 20), textvariable=self.pwd2, width=15, show='*')
        pass2.grid(row=4, column=1)

        # ========================================BUTTON WIDGETS===============================
        btn_register = Button(RegisterFrame, font=('arial', 20), text="Register", command=self.Register,
                              bg='pink', fg='black')
        btn_register.grid(row=6, columnspan=1)
        btn_login = Button(RegisterFrame, font=('arial', 20), text="Login", command=self.Login,
                           bg='pink', fg='black')
        btn_login.grid(row=6, column=4)

        # ========================================MENUBAR WIDGETS==================================
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.Exit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.root.config(menu=menubar)

    # =======================================METHODS===========================================

    def Exit(self):
        result = MsgBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            self.root.destroy()
            exit()

    def hashing(self):
        passwd = self.pwd1.get()
        enc = sha512(passwd.encode())
        return enc.hexdigest()

    def Register(self):
        if self.Email.get() == "" or self.Uname.get() == "" or self.pwd1.get() == "" or self.pwd2.get() == "":
            MsgBox.showinfo("MindMedia", "Fill all the fields...!")
            # lbl_result.config(text="Please complete the required field!", fg="orange")
        elif self.pwd1.get() != self.pwd2.get():
            self.lbl_result.config(text="Type the same password in both fields!", fg="red")
        else:
            acc_check = DBoperations.account_check(self.Email.get(), self.Uname.get())
            if acc_check != []:
                MsgBox.showinfo("MindMedia", "Username or Email was already taken...!")
                # lbl_result.config(text="Username is already taken", fg="red")
            else:
                DBoperations.create_user(self.Email.get(), self.Uname.get(), self.hashing())
                self.Email.set("")
                self.Uname.set("")
                self.pwd1.set("")
                self.pwd2.set("")
                MsgBox.showinfo("MindMedia", "User was successfully created...!")
                self.lbl_result.config(text="Successfully Created!", fg="green")

    # method for calling login window....
    def Login(self):
        self.root.destroy()
        main.login_window()
        return


def signup_window():
    rootwindow = RootWindow()
    rootwindow.root.mainloop()

# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    signup_window()
