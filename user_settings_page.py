from tkinter import *
from tkinter import font
from MindMedia.DBoperations import update_profilepic,change_username,get_profilepic
from MindMedia.session_handler import current_user,get_current_user_email
from MindMedia.widgets.TileButton import TiledButton
from tkinter.filedialog import askopenfilename
from MindMedia.create_post_dialog import Create_post_dialog
from PIL import Image,ImageTk
# change username
# change profile picture
# change password
# logout

class User_settings(Frame):
    def __init__(self,parent,curr_user):
        super(User_settings, self).__init__(parent)
        self.curr_user_email=get_current_user_email()
        self.curr_user=curr_user
        self.f1=font.Font(size=25)
        self.f2=font.Font(size=15)
        self.setup_settings()

    def setup_settings(self):
        Label(self,text="Account settings",font=self.f1).pack()
        self.mid_frame=Frame(self)
        self.user_prof_canvas=Canvas(self,height=100,width=100,bg='lightgreen')
        self.load_user_prof_pic()
        Label(self,text=self.curr_user,font=self.f2).pack()
        Label(self, text=self.curr_user_email, font=self.f2).pack()
        self.user_prof_canvas.pack()
        self.mid_frame.pack()
        TiledButton(self.mid_frame,text="Change username",hover=False,command=self.create_change_user_name,
                    h=50,w=200,font=self.f2).grid()
        TiledButton(self.mid_frame,text="Change password",hover=False,command=self.change_pass,
                    h=50,w=200,font=self.f2).grid(row=0,column=1)
        TiledButton(self.mid_frame,text="Change profile picture",hover=False,command=self.change_prof_pic,
                    h=50,w=200,font=self.f2).grid(row=1,column=0)
        TiledButton(self.mid_frame,text="Logout",hover=False,command=self.logout,h=50,w=200,
                    font=self.f2).grid(row=1,column=1)



    def load_user_prof_pic(self):
        self.user_prof_pic=get_profilepic(self.curr_user)
        if self.user_prof_pic is None:
            self.user_prof_pic = "H:\\Python\\MindMedia\\images\\login_bgimage.jpg"
        self.img=self.resize_image(self.user_prof_pic,100,100)
        self.user_prof_canvas.create_image(50,50,image=self.img)


    def change_pass(self):
        self.pop_up=Toplevel()
        Create_post_dialog(self.pop_up,self.curr_user).pack()
        self.pop_up.mainloop()

    def create_change_user_name(self):
        # function works!!
        self.pop_up=Toplevel()
        Label(self.pop_up,text="Enter new username:",font=font.Font(size=15)).pack()
        self.pop_up.uname=Entry(self.pop_up,font=font.Font(size=15))
        self.pop_up.uname.pack()
        self.uname = self.pop_up.uname.get()
        Button(self.pop_up,text="okay",command=self.change_user_name).pack()
        self.pop_up.mainloop()

    def change_user_name(self):
        change_username(get_current_user_email(),self.uname)


    def change_prof_pic(self):
        filename=askopenfilename()
        self.img=self.resize_image(filename,100,100)
        self.user_prof_canvas.create_image(50,50,image=self.img)
        update_profilepic(self.curr_user,filename)

    def logout(self):
        # write code to resst the current user variable
        # and load the signup/login page
        pass

    def resize_image(self, img_path, h, w):
        img = Image.open(img_path)
        img = img.resize((h, w), Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)

root=Tk()
User_settings(root,'alice').pack()
root.mainloop()
