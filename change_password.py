
from tkinter import *
from tkinter import font
from hashlib import sha512
from MindMedia.DBoperations import account_check,change_passwd

class Change_password_dialog(Frame):
    def __init__(self,parent,uname):
        super(Change_password_dialog, self).__init__(parent)
        self.username=uname
        self.user_pass=account_check(email='',uname=uname)[0][2]
        self.setup_pass_change()

    def setup_pass_change(self):
        Label(self,text="Change password",font="monaco 23 bold", fg='blue',bg='pink').pack()
        self.main_frame=Frame(self)
        self.main_frame.pack()
        Label(self.main_frame,text="Current password: ",font=('comic sans ms',15)).grid(pady=10)
        self.cur_pass=Entry(self.main_frame,font=font.Font(size=15),show='*')
        self.cur_pass.grid(row=0,column=1,pady=10)
        Label(self.main_frame,text="New password: ",font=('comic sans ms',15)).grid(row=1,column=0,pady=10)
        self.pass1 = Entry(self.main_frame,font=font.Font(size=15),show='*')
        self.pass1.grid(row=1, column=1,pady=10)
        Label(self.main_frame,text="Confirm password: ",font=('comic sans ms',15)).grid(row=2,column=0,pady=10)
        self.pass2 = Entry(self.main_frame,font=font.Font(size=15),show='*')
        self.pass2.grid(row=2, column=1,pady=10)
        Button(self,text="Okay",font=font.Font(size=15),command=self.on_submit, bg='pink').pack(pady=10)
        self.notify_label = Label(self, text='', font=font.Font(size=10))
        self.notify_label.pack(side=BOTTOM)

    def cur_pass_hash(self):
        passwd = self.cur_pass.get()
        enc = sha512(passwd.encode())
        return enc.hexdigest()


    def on_submit(self):
        if self.cur_pass_hash()==self.user_pass:
            if self.pass1.get()==self.pass2.get():
                self.passwd = sha512(self.pass1.get().encode())
                self.hashed_pass = self.passwd.hexdigest()
                change_passwd(self.username,self.hashed_pass)
            else:
                self.notify_label['fg'] = 'red'
                self.notify_label['text'] = '**Passwords entered do not match!**'
                self.notify_label.pack()
        else:
            self.notify_label['fg']='red'
            self.notify_label['text']='**Wrong password entered**'
            self.notify_label.pack()


root=Tk()
root.title('MindMedia')
Change_password_dialog(root,'alice').pack()
root.mainloop()
