from tkinter import *
from MindMedia.DBoperations import fetch_friends, delete_friends
from MindMedia.session_handler import current_user
from tkinter import font


class ViewFriends(Frame):
    def __init__(self, parent, current_user):
        super(ViewFriends, self).__init__(parent)
        self.current_user = current_user
        self.set_up_view_friends()

    def set_up_view_friends(self):
        self.lis = fetch_friends(self.current_user)
        # self.friend_names = [fetch_user_name(x[0])[0] for x in self.lis]
        # print(self.friend_names)
        Label(self, text="Your friends", font=font.Font(size=20)).pack()
        self.frames = []
        F=Frame(self)
        F.pack()
        f2 = Frame(F)
        f2.pack(side=LEFT)
        f3 = Frame(F)
        f3.pack(side=LEFT)
        self.frames.append(F)
        for x in range(len(self.lis)):
            Label(f2,text=self.lis[x],font=font.Font(size=14)).pack(fill=X,padx=10,pady=10)
            Button(f3, text="unfriend", font=font.Font(size=12), bg='lightblue',
                   command=self.delete_friend_button_clicked(self.lis[x])).pack(fill=X,padx=10,pady=10)

    def delete_friend_button_clicked(self, name):
        def action_function():
            delete_friends(self.current_user, name[0])
            self.pack_forget()
        return action_function


# root = Tk()
# w = ViewFriends(root,current_user())
# w.pack()
# root.mainloop()
