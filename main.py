from tkinter import *
import tkinter.messagebox as MsgBox
from hashlib import sha512
from MindMedia import DBoperations,register_form
from MindMedia.session_handler import add_session,set_up_current_sessions

class RootWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("User Login")
        width = 780
        height = 450
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        # self.root.resizable(0, 0)

        # =======================================VARIABLES=====================================
        self.Email = StringVar()
        self.pwd = StringVar()

        # =====================================FRAMES====================================
        TitleFrame = Frame(self.root, height=100, width=640, bd=1, relief=SOLID)
        TitleFrame.pack(side=TOP)
        RegisterFrame = Frame(self.root)
        RegisterFrame.pack(side=TOP, pady=20)

        # =====================================LABEL WIDGETS=============================
        lbl_title = Label(TitleFrame, text="MindMedia", font="monaco 23 bold", bd=20, width=600, fg='blue', bg='pink')
        lbl_title.pack()
        lbl_email = Label(RegisterFrame, text="E-mail:", font=('comic sans ms', 20), bd=30)
        lbl_email.grid(row=1)
        lbl_pwd = Label(RegisterFrame, text="Password:", font=('comic sans ms', 20), bd=30)
        lbl_pwd.grid(row=3)
        self.lbl_result = Label(RegisterFrame, text="", font=('arial', 18))
        self.lbl_result.grid(row=5, columnspan=2)

        # =======================================ENTRY WIDGETS===========================
        email = Entry(RegisterFrame, font=('arial', 20), textvariable=self.Email, width=15)
        email.grid(row=1, column=1)
        pass1 = Entry(RegisterFrame, font=('arial', 20), textvariable=self.pwd, width=15, show='*')
        pass1.grid(row=3, column=1)

        # ========================================BUTTON WIDGETS===============================
        btn_register = Button(RegisterFrame, font=('arial', 20), text="SignUp", command=self.signup_window,
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

    def signup_window(self):
        self.root.destroy()
        register_form.signup_window()

    def hashing(self):
        passwd = self.pwd.get()
        enc = sha512(passwd.encode())
        return enc.hexdigest()

    # method for calling login window....
    def Login(self):
        if self.Email.get() == "" or self.pwd.get() == "":
            MsgBox.showinfo("MindMedia", "Fill all the fields...!")
        else:
            authorize = DBoperations.authorize(self.Email.get(),self.hashing())
            if authorize == []:
                MsgBox.showinfo('MindMedia','Invalid Credentials...!')
            else:
                set_up_current_sessions()
                add_session(self.Email.get())
                MsgBox.showinfo('MindMedia','Successfully logged in...!')


def login_window():
    rootwindow = RootWindow()
    rootwindow.root.mainloop()

# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    login_window()
