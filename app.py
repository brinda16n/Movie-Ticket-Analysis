import streamlit as st
import mysql.connector

from create import *
from database import *
from delete import *
from read import *
from update import *
from queries import *

def main():
    st.title("Movie Ticket Booking App")
    menu = ["Add", "View", "Edit", "Remove","Show me queries","Show me function"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_movie_table()
    create_user_table()
    create_theatre_table()
    create_booking_table()
    create_visit_table()

    if choice == "Add":
        menu = ["Movie","User","Theatre","Booking","Visit"]
        choice1 = st.sidebar.selectbox("Menu", menu)
        if choice1 == "Movie":
            create()
        if choice1 == "User":
            create1()
        if choice1 == "Theatre":
            create2()
        if choice1 == "Booking":
            create3()
        if choice1 == "Visit":
            create4()

    elif choice == "View":
        menu = ["Movie", "User","Theatre","Booking","Visit"]
        choice1 = st.sidebar.selectbox("Menu", menu)
        if choice1 == "Movie":
            read()
        if choice1 == "User":
            read1()
        if choice1 == "Theatre":
            read2()
        if choice1 == "Booking":
            read3()
        if choice1 == "Visit":
            read4()

    elif choice == "Edit":
        menu = ["Movie", "User","Theatre","Booking","Visit"]
        choice1 = st.sidebar.selectbox("Menu", menu)
        if choice1 == "Movie":
            update()
        if choice1 == "User":
            update1()
        if choice1 == "Theatre":
            update2()
        if choice1 == "Booking":
            update3()
        if choice1 == "Visit":
            update4()


    elif choice == "Remove":
        menu = ["Movie", "User","Theatre","Booking","Visit"]
        choice1 = st.sidebar.selectbox("Menu", menu)
        if choice1 == "Movie":
            delete()
        if choice1 == "User":
            delete1()
        if choice1 == "Theatre":
            delete2()
        if choice1 == "Booking":
            delete3()
        if choice1 == "Visit":
            delete4()

    elif choice == "Show me queries":
        query_page()

    elif choice == "Show me function":
        function_page()




if __name__ == '__main__':
    main()