import mysql.connector as MySQL
import tkinter.messagebox as MsgBox

def db_connection():
    global conn, cursor
    conn = MySQL.connect(host='localhost', database='mindmediadb',
                         username='root', password='mysql')
    cursor = conn.cursor()
    return

def db_close():
    conn.close()
    cursor.close()
    return


def account_check(email,uname=None):
    db_connection()
    cursor.execute(f"SELECT email,username,password,pp_link FROM Users WHERE email='{email}' or username='{uname}'")
    result = cursor.fetchall()
    db_close()
    return result


def authorize(email,passwd):
    db_connection()
    cursor.execute(f"SELECT * FROM Users WHERE email='{email}' and password='{passwd}'")
    result = cursor.fetchall()
    db_close()
    return result


def create_user(email,uname,pwd):
    db_connection()
    cursor.execute("INSERT INTO Users (email, username, password) VALUES(%s, %s, %s)",
                   (str(email), str(uname), str(pwd),))
    conn.commit()
    db_close()
    return


def fetch_starts_with(string):
    db_connection()
    cursor.execute(f"SELECT username,email,pp_link FROM Users WHERE username LIKE '{string}%'")
    return cursor.fetchall()


def add_to_request(user1,user2):
    db_connection()
    cursor.execute(f"SELECT * FROM Requests WHERE sender='{user1}' AND receiver='{user2}'")
    res1 = cursor.fetchall()
    cursor.execute(f"SELECT * FROM Friends WHERE (frnd1='{user1}' OR frnd1='{user2}') AND "
                   f"(frnd2='{user1}' OR frnd2='{user2}')")
    res2 = cursor.fetchall()
    if res1 != []:
        return "already_requested"
    elif res2 != []:
        return "already_friends"
    else:
        cursor.execute(f"INSERT INTO Requests VALUES('{user1}','{user2}')")
        conn.commit()
    db_close()


def fetch_friends(given_name):
    db_connection()
    cursor.execute(f"SELECT frnd1 FROM Friends WHERE frnd2='{given_name}'")
    res1 = cursor.fetchall()
    cursor.execute(f"SELECT frnd2 FROM Friends WHERE frnd1='{given_name}'")
    res2 = cursor.fetchall()
    res = res1+res2
    conn.close()
    return res


def delete_friends(frnd1,frnd2):
    db_connection()
    cursor.execute(f"DELETE FROM Friends WHERE (frnd1='{frnd1}' OR frnd1='{frnd2}') AND "
                   f"(frnd2='{frnd1}' OR frnd2='{frnd2}')")
    conn.commit()
    db_close()


def fetch_from_requests(username):
    db_connection()
    cursor.execute(f"SELECT sender FROM Requests WHERE receiver='{username}'")
    result = cursor.fetchall()
    conn.close()
    return result


def add_to_friends(frnd1,frnd2):
    db_connection()
    cursor.execute(f"INSERT INTO Friends VALUES ('{frnd1}','{frnd2}')")
    conn.commit()
    conn.close()


def del_from_request(user1,user2):
    db_connection()
    cursor.execute(f"DELETE FROM Requests WHERE sender='{user2}' AND receiver='{user1}'")
    conn.commit()

def fetch_comments(post_id):
    try:
        db_connection()
        cursor.execute(f"SELECT * FROM Comments WHERE post_id='{post_id}'")
        result = cursor.fetchall()
        conn.close()
        return result
    except:
        conn.close()
        print("fetch comment error error!")

def add_comment(post_id,comment,username):
    try:
        db_connection()
        cursor.execute(f"INSERT INTO Comments VALUES ('{post_id}','{comment}','{username}')")
        conn.commit()
        conn.close()
    except:
        conn.close()
        print("Comment add error!")

def add_post(post_id,posted_by,type,caption,likes,images_id):
    try:
        db_connection()
        cursor.execute("INSERT into Posts VALUES (?,?,?,?,?,?)",(post_id,posted_by,type,caption,likes,images_id))
        conn.commit()
        db_close()
    except:
        print("Add post error!")
        db_close()


def get_new_postid():
    try:
        db_connection()
        cursor.execute(f"SELECT * FROM Last_post")
        return int(cursor.fetchall()[0][0])
    except:
        print("Last_post_id update error")
        db_close()

def update_last_postid():
    try:
        db_connection()
        cursor.execute(f"UPDATE Last_post SET last_id=last_id+1")
        conn.commit()
    except:
        print("Last_post_id update error")

def fetch_user_posts(frnd_list):
    try:
        db_connection()
        lis=[]
        # for every friend the public posts get fetched again and again
        # as post_id's are unique we can track duplicate post this way
        # fetch_list maintains a list of all the post_id's fetched so far
        fetch_list=[]
        print("friend list:",frnd_list)
        for x in frnd_list:
            cursor.execute(f"SELECT * FROM Posts WHERE posted_by='{x}' OR type='public'")
            val = cursor.fetchall()
            if val[0] not in fetch_list:
                # adding result if post_id is new
                lis.extend(val)
                fetch_list.append(val[0])
        print("returned list is ",lis)
        return lis
    except:
        print("Post fetch error!")


def update_profilepic(email,path):
    try:
        db_connection()
        cursor.execute(f"select * from Userpic where posted_by='{email}'")
        # cursor.execute(f"SELECT pp_link FROM Users WHERE email='{email}'")
        if len(cursor.fetchall())>0:
            cursor.execute(f"update Userpic set path='{path}' where posted_by='{email}'")
            conn.commit()
        else:
            cursor.execute(f"insert into Userpic values('{email}','{path}')")
            conn.commit()
    except:
        print("User pic update error!")



def get_profilepic(uname):
    try:
        db_connection()
        cursor.execute(f"select path from Userpic where posted_by='{uname}'")
        print(cursor.fetchall()[0][0])
    except:
        print("prof pic get error!")


def change_username(email,new_name):
    try:
        db_connection()
        cursor.execute(f"UPDATE Users SET username='{new_name}' WHERE email='{email}'")
        conn.commit()
    except:
        print("Change username error!!!")

def change_passwd(uname,pwd):
    db_connection()
    cursor.execute(f"UPDATE Users SET password='{pwd}' WHERE username='{uname}'")
    conn.commit()
    conn.close()


# get_profilepic('bob')

# def fetch_user_name(email):
#     db_connection()
#     cursor.execute(f"SELECT username FROM Users WHERE username='{email}'")
#     result = cursor.fetchall()
#     db_close()
#     return result
