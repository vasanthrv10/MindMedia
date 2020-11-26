
from tkinter import *
from MindMedia.widgets.TabbedWidget import TabbedWidget
from MindMedia.friend_request import RequestTab
from MindMedia.friend_search import Friend_search
from MindMedia.friends_view import ViewFriends
from MindMedia.session_handler import current_user

class Friends_main_tab(Frame):
    def __init__(self,parent,user):
        super(Friends_main_tab, self).__init__(parent)
        self.user=user
        self.setup_friends_tab()

    def setup_friends_tab(self):
        self.main_tab=TabbedWidget(self,h=50,w=100)
        self.main_tab.pack()
        self.main_tab.add_tab('Request',RequestTab(self.main_tab.get_tab_area(),self.user))
        self.main_tab.add_tab('Search', Friend_search(self.main_tab.get_tab_area()))
        self.main_tab.add_tab('View', ViewFriends(self.main_tab.get_tab_area(),self.user))
