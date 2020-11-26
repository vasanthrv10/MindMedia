
from MindMedia.DBoperations import account_check
from pickle import loads, dumps


def set_up_current_sessions():
    global current_sessions
    current_sessions = {}


def save_current_user_info(email):
    with open('session.txt', 'wb') as f:
        data = dumps(email)
        f.write(data)


def get_current_user_email():
    with open('session.txt', 'rb') as f:
        data = f.readline()
        data = loads(data)
        # print(data)
        return data


def add_session(gnemail):
    # gnemail,gnusername, gnpass, gnprof_link=account_check(gnemail)[0]
    # global current_sessions
    # info_dict={'email':gnemail,'password':gnpass,'username':gnusername,'profile_pic_link':gnprof_link}
    # if gnemail not in current_sessions:
    # current_sessions[gnemail]=info_dict
    #
    # # 'b@gmail':{'email':gnemail,'password':gnpass,'username':gnusername,'profile_pic_link':gnprof_link}
    # print("Session creation successful!!")
    save_current_user_info(gnemail)
    # else:
    #     print("Session aldready saved for user!!")


def get_info_dict(email):
    user = get_current_user_email()
    gnemail, gnusername, gnpass, gnprof_link = account_check(email)[0]
    info_dict = {'email': gnemail, 'username': gnusername, 'password': gnpass, 'pp_link': gnprof_link}
    return info_dict['username']

def current_user():
    cu = get_info_dict(get_current_user_email())
    return cu


def log_out(email):
    global current_sessions
    del current_sessions[email]
    # deletes the entry of the email session!
    # it is considered logged out as the session is not recognised anymore!


def remember_logged_in(email):
    pass
    # finish this function at the very end of the project!


# add_session('b@gmail')
# get_info_dict(get_current_user_email())
# print(res)
