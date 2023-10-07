import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pes1ug20cs542_movie1"
)
c = mydb.cursor()

def create_movie_table():
    c.execute('CREATE TABLE IF NOT EXISTS MOVIE(Movie_ID TEXT, Name TEXT, Language TEXT, Genre TEXT,Director TEXT, '
                  'Actor TEXT)')



def add_movie_data(mid,mname,lang,genre,dir,actor):
    c.execute('INSERT INTO MOVIE(Movie_ID,Name,Language,Genre,Director,Actor) VALUES (%s,%s,%s,%s,'
              '%s,%s)',

              (mid,mname,lang,genre,dir,actor))
    mydb.commit()


def view_all_movie_data():
    c.execute('SELECT * FROM MOVIE')
    data = c.fetchall()
    return data


def view_only_movieID():
    c.execute('SELECT Movie_ID FROM MOVIE')
    data = c.fetchall()
    return data


def get_movie(mid):
    c.execute('SELECT * FROM MOVIE WHERE Movie_ID="{}"'.format(mid))
    data = c.fetchall()
    return data


def edit_movie_data(new_movie_id,new_movie_name,new_movie_lang,new_movie_genre,new_movie_dir,new_movie_actor,mid):
    c.execute("UPDATE MOVIE SET Movie_ID=%s, Name=%s, Language=%s, Genre=%s, Director=%s, Actor=%s WHERE "
              "Movie_ID=%s", (new_movie_id,new_movie_name,new_movie_lang,new_movie_genre,new_movie_dir,new_movie_actor,mid))
    mydb.commit()
    #data = c.fetchall()
    #return data


def delete_movie_data(mid):
    c.execute('DELETE FROM MOVIE WHERE Movie_ID="{}"'.format(mid))
    mydb.commit()

def create_user_table():
    c.execute('CREATE TABLE IF NOT EXISTS USER(User_ID TEXT, Name TEXT, Password TEXT, Address TEXT)')

def add_user_data(uid,name,password,addr):
    c.execute('INSERT INTO USER(User_ID,Name,Password,Address) VALUES (%s,%s,%s,%s)',

              (uid,name,password,addr))
    mydb.commit()

def view_all_user_data():
    c.execute('SELECT * FROM USER')
    data = c.fetchall()
    return data

def view_only_userID():
    c.execute('SELECT User_ID FROM USER')
    data = c.fetchall()
    return data

def get_user(uid):
    c.execute('SELECT * FROM USER WHERE User_ID="{}"'.format(uid))
    data = c.fetchall()
    return data

def edit_user_data(new_usr_id,new_usr_name,new_passwrd,new_address,old_usrid):
    c.execute("UPDATE USER SET User_ID=%s, Name=%s, Password=%s, Address=%s WHERE "
              "User_ID=%s", (new_usr_id,new_usr_name,new_passwrd,new_address,old_usrid))
    mydb.commit()

def delete_user_data(uid):
    c.execute('DELETE FROM User WHERE User_ID="{}"'.format(uid))
    mydb.commit()


def create_theatre_table():
    c.execute('CREATE TABLE IF NOT EXISTS THEATRE(Theatre_ID TEXT, Theatre_Name TEXT, Pincode TEXT, No_Shows_PerDay TEXT)')

def add_theatre_data(tid,name,pincode,no_of_shows):
    c.execute('INSERT INTO THEATRE(Theatre_ID,Theatre_Name,Pincode,No_Shows_PerDay) VALUES (%s,%s,%s,%s)',

              (tid,name,pincode,no_of_shows))
    mydb.commit()

def view_all_theatre_data():
    c.execute('SELECT * FROM THEATRE')
    data = c.fetchall()
    return data

def view_only_theatreID():
    c.execute('SELECT Theatre_ID FROM THEATRE')
    data = c.fetchall()
    return data


def get_theatre(tid):
    c.execute('SELECT * FROM THEATRE WHERE Theatre_ID="{}"'.format(tid))
    data = c.fetchall()
    return data

def edit_theatre_data(new_tid, new_tname, new_pincode,new_no,old_tid):
    c.execute("UPDATE THEATRE SET Theatre_ID=%s, Theatre_Name=%s, Pincode=%s, No_Shows_PerDay=%s WHERE "
              "Theatre_ID=%s", (new_tid, new_tname, new_pincode,new_no,old_tid))
    mydb.commit()

def delete_theatre_data(tid):
    c.execute('DELETE FROM THEATRE WHERE Theatre_ID="{}"'.format(tid))
    mydb.commit()

def create_booking_table():
    c.execute('CREATE TABLE IF NOT EXISTS BOOKING(Booking_ID TEXT, Movie_ID TEXT, User_ID TEXT, No_of_Tickets INT)')

def add_booking_data(bid,mid,uid,num):
    c.execute('INSERT INTO BOOKING(Booking_ID, Movie_ID, User_ID, No_of_Tickets) VALUES (%s,%s,%s,%s)',

              (bid,mid,uid,num))
    mydb.commit()

def view_all_booking_data():
    c.execute('SELECT * FROM BOOKING')
    data = c.fetchall()
    return data

def view_only_bookingID():
    c.execute('SELECT Booking_ID FROM BOOKING')
    data = c.fetchall()
    return data

def get_booking(bid):
    c.execute('SELECT * FROM BOOKING WHERE Booking_ID="{}"'.format(bid))
    data = c.fetchall()
    return data

def edit_booking_data(new_bid, new_mid, new_uid, new_num, old_bid):
    c.execute("UPDATE BOOKING SET Booking_ID=%s, Movie_ID=%s, User_ID=%s, No_of_Tickets=%d WHERE "
              "Booking_ID=%s", (new_bid, new_mid, new_uid, new_num, old_bid))
    mydb.commit()

def delete_booking_data(bid):
    c.execute('DELETE FROM BOOKING WHERE Booking_ID="{}"'.format(bid))
    mydb.commit()

def create_visit_table():
    c.execute('CREATE TABLE IF NOT EXISTS VISIT(User_ID TEXT, Theatre_ID TEXT, Visit_Date DATE)')
    #c.execute('ALTER TABLE VISIT ADD PRIMARY KEY(User_ID,Theatre_ID)')

def add_visit_data(uid,tid,visit_date):
    c.execute('INSERT INTO VISIT(User_ID,Theatre_ID,Visit_Date) VALUES (%s,%s,%s)',

              (uid,tid,visit_date))
    mydb.commit()

def view_all_visit_data():
    c.execute('SELECT * FROM VISIT')
    data = c.fetchall()
    return data

def view_only_visitID():
    c.execute('SELECT User_ID,Theatre_ID FROM VISIT')
    data = c.fetchall()
    return data

def get_visit(uid,tid):
    c.execute('SELECT * FROM VISIT WHERE User_ID="{}" AND Theatre_ID="{}"'.format(uid,tid))
    data = c.fetchall()
    return data

def edit_visit_data(uid,tid,vdate,old_uid,old_tid):
    c.execute("UPDATE VISIT SET User_ID=%s, Theatre_ID=%s, Visit_Date=%s WHERE "
              "User_ID=%s AND Theatre_ID=%s", (uid,tid,vdate,old_uid,old_tid))
    mydb.commit()

def delete_visit_data(uid,tid):
    c.execute('DELETE FROM VISIT WHERE User_ID="{}" AND Theatre_ID="{}"'.format(uid,tid))
    mydb.commit()

def q1(uid):
    c.execute("SELECT m.Name FROM (MOVIE m INNER JOIN BOOKING b ON b.Movie_ID = m.Movie_ID) INNER JOIN USER u ON "
              "u.User_ID = b.User_ID WHERE u.user_ID = {}".format(uid))
    data = c.fetchall()
    return data

def q2():
    c.execute("SELECT u.Name FROM USER u LEFT OUTER JOIN BOOKING b ON "
              "u.User_ID = b.User_ID WHERE b.Booking_ID IS NULL")
    data = c.fetchall()
    return data

def q3():
    c.execute("SELECT u.Name,COUNT(b.Booking_ID) FROM USER u NATURAL JOIN BOOKING b"
              " GROUP BY u.User_ID")
    data = c.fetchall()
    return data



