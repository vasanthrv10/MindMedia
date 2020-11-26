from tkinter import *
from tkinter import font
import tkinter.messagebox as MsgBox
from threading import Thread
from MindMedia.DBoperations import *
from MindMedia.session_handler import  current_user

class Friend_search(Frame):
    def __init__(self,parent):
        super(Friend_search, self).__init__(parent)
        self.set_up_search_frame()

    def set_up_search_frame(self):
        self.search_bar=Entry(self,font=font.Font(size=20))
        self.search_bar.pack()
        self.result_frame=Frame(self)
        self.result_frame.pack()
        self.results={}
        self.t=Thread(target=self.start_fetching)
        self.t.start()

    def start_fetching(self):
        # self.add_result()
        self.prev='^'
        while(True):
            self.res=[]
            search_str=self.search_bar.get()
            if search_str==self.prev:
                pass
            elif search_str != '':
                self.res=fetch_starts_with(search_str)
                # [(we,wewe,wew)]
                for x in self.results:
                    self.results[x].destroy()
            self.prev=search_str
            for x in self.res:
                    self.add_result(x[0],x[1],x[2])



    def add_result(self,name,email,picture):
        temp = Frame(self.result_frame)
        c = Canvas(temp,height=50,width=50,bg='lightgreen')
        c.pack(side=LEFT)
        # img=PhotoImage(file=picture)
        # c.create_image(0,0,image=img)
        Label(temp,text=name,font=font.Font(size=15)).pack(side=LEFT)
        Button(temp,text="Add friend", font=font.Font(size=10),
               command=self.add_friend_button(name)).pack(side=RIGHT,padx=70)
        temp.pack()
        self.results[name] = temp
        # print(self.results)

    def add_friend_button(self,name):
        def add_friend_button_clicked():
            # info_dict=get_info_dict(get_current_user_info())
            res = add_to_request(current_user(),name)
            if res == "already_requested":
                MsgBox.showinfo('MindMedia','You already send request to %s' % name)
            elif res == "already_friends":
                MsgBox.showinfo('MindMedia','You and %s are already friends...!' % name)
        return add_friend_button_clicked



def Run():
    root=Tk()
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)
    w=Friend_search(root)
    w.pack()
    root.mainloop()

if __name__ == '__main__':
    Run()
