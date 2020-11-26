from MindMedia.widgets.TabbedWidget import TabbedWidget
from tkinter import *
from tkinter.font import Font
from MindMedia.friends_main import *
from MindMedia.user_settings_page import *
from MindMedia.session_handler import current_user

w = None
def Run(root,curr_user):
    global w
    w = TabbedWidget(root, 25, 300, font=Font(size=15), tab_dir='left')
    w.pack()
    w.add_tab('Settings', User_settings(w.get_tab_area(), curr_user))
    w.add_tab('Friends',Friends_main_tab(w.get_tab_area(),curr_user))
    return w

root = Tk()
Run(root,current_user())
root.mainloop()
