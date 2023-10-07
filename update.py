import datetime

import pandas as pd
import streamlit as st
from database import *


def update():
    result = view_all_movie_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Movie_ID','Name','Language','Genre','Director','Actor'])
    with st.expander("Current Movies"):
        st.dataframe(df)
    list_of_movies = [i[0] for i in view_only_movieID()]
    selected_movie = st.selectbox("Movies to Edit", list_of_movies)
    selected_result = get_movie(selected_movie)
    # st.write(selected_result)
    if selected_result:
        old_mid = selected_result[0][0]
        old_name = selected_result[0][1]
        old_lang = selected_result[0][2]
        old_genre = selected_result[0][3]
        old_director = selected_result[0][4]
        old_actor = selected_result[0][5]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_mid = st.text_input("Movie_ID:", old_mid)
            name = st.text_input("Name:",old_name)
            movie_lang = st.text_input("Language:",old_lang)
            movie_actor = st.text_input("Actor:", old_actor)
        with col2:
            if old_genre == "Action":
                movie_genre = st.selectbox("Genre", ["Action", "Comedy", "Horror", "Drama", "Romance"],index=0)
            if old_genre == "Comedy":
                movie_genre = st.selectbox("Genre", ["Action", "Comedy", "Horror", "Drama", "Romance"],index=1)
            if old_genre == "Horror":
                movie_genre = st.selectbox("Genre", ["Action", "Comedy", "Horror", "Drama", "Romance"],index=2)
            if old_genre == "Drama":
                movie_genre = st.selectbox("Genre", ["Action", "Comedy", "Horror", "Drama", "Romance"],index=3)
            if old_genre == "Romance":
                movie_genre = st.selectbox("Genre", ["Action", "Comedy", "Horror", "Drama", "Romance"],index=4)

            movie_dir = st.text_input("Director:",old_director)
        if st.button("Update Movie"):
            edit_movie_data(new_mid,name,movie_lang,movie_genre,movie_dir,movie_actor,old_mid)
            st.success("Successfully updated details of {}".format(old_mid))

    result2 = view_all_movie_data()
    df2 = pd.DataFrame(result2, columns=['Movie_ID','Name','Language','Genre','Director','Actor'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update1():
    result = view_all_user_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['User_ID','Name','Password','Address'])
    with st.expander("Current Users"):
        st.dataframe(df)
    list_of_users = [i[0] for i in view_only_userID()]
    selected_user = st.selectbox("Users to Edit", list_of_users)
    selected_result = get_user(selected_user)
    # st.write(selected_result)
    if selected_result:
        old_uid = selected_result[0][0]
        old_name = selected_result[0][1]
        old_pwd = selected_result[0][2]
        old_addrs = selected_result[0][3]


        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_uid = st.text_input("User_ID:", old_uid)
            name = st.text_input("Name:",old_name)

        with col2:
            paswrd = st.text_input("Password:",old_pwd)
            address = st.text_input("Address:", old_addrs)

        if st.button("Update User"):
            edit_user_data(new_uid,name,paswrd,address,old_uid)
            st.success("Successfully updated details of {}".format(old_uid))

    result2 = view_all_user_data()
    df2 = pd.DataFrame(result2, columns=['User_ID','Name','Password','Address'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update3():
    result = view_all_booking_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Booking_ID','Movie_ID','User_ID','Number Of Tickets'])
    with st.expander("Current Bookings"):
        st.dataframe(df)
    list_of_bs = [i[0] for i in view_only_bookingID()]
    selected_b = st.selectbox("Bookings to Edit", list_of_bs)
    selected_result = get_booking(selected_b)
    # st.write(selected_result)
    if selected_result:
        old_bid = selected_result[0][0]
        old_mid = selected_result[0][1]
        old_uid = selected_result[0][2]
        old_num = selected_result[0][3]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_bid = st.text_input("Booking ID:", old_bid)
            mid = st.text_input("Movie ID:",old_mid)

        with col2:
            uid = st.text_input("Pincode:",old_uid)
            num = st.number_input("Number of tickets:",old_num)

        if st.button("Update Booking"):
            edit_booking_data(new_bid,mid,uid,num,old_bid)
            st.success("Successfully updated details of {}".format(old_bid))

    result2 = view_all_theatre_data()
    df2 = pd.DataFrame(result2, columns=['Booking_ID','Movie_ID','User_ID','Number Of Tickets'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update3():
    result = view_all_theatre_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Theatre_ID','Theatre_Name','Pincode','No_Shows_PerDay'])
    with st.expander("Current Theatres"):
        st.dataframe(df)
    list_of_ts = [i[0] for i in view_only_theatreID()]
    selected_t = st.selectbox("Theatres to Edit", list_of_ts)
    selected_result = get_theatre(selected_t)
    # st.write(selected_result)
    if selected_result:
        old_tid = selected_result[0][0]
        old_tname = selected_result[0][1]
        old_pin = selected_result[0][2]
        old_no = selected_result[0][3]


        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            t_id = st.text_input("Theatre Id: ",old_tid)
            t_name = st.text_input("Theatre Name:",old_tname)

        with col2:
            t_pin = st.text_input("Pincode: ",old_pin)
            t_no = st.slider(label="Number_Of_Shows", min_value=0, max_value=10,value=old_no)

        if st.button("Update Theatre"):
            edit_booking_data(tid,t_name,t_pin,t_no,old_tid)
            st.success("Successfully updated details of {}".format(old_bid))

    result2 = view_all_theatre_data()
    df2 = pd.DataFrame(result2, columns=['Theatre_ID','Theatre_Name','Pincode','No_Shows_PerDay'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update4():
    result = view_all_visit_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['User_ID','Theatre_ID','Visit_Date'])
    with st.expander("Current Visit details"):
        st.dataframe(df)
    list_of_us = [i[0] for i in view_only_visitID()]
    list_of_ts = [i[1] for i in view_only_visitID()]
    col1, col2 = st.columns(2)
    with col1:
        selected_u = st.selectbox("Select User Id", list_of_us)
    with col2:
        selected_t = st.selectbox("Select Theatre Id", list_of_ts)

    selected_result = get_visit(selected_u,selected_t)
    # st.write(selected_result)
    if selected_result:
        old_uid = selected_result[0][0]
        old_tid = selected_result[0][1]
        old_vd = selected_result[0][2]


        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_uid = st.text_input("User ID:", old_uid)
            new_tid = st.text_input("Theatre ID:",old_tid)

        with col2:
            new_vd = st.date_input("Visit date:",old_vd)

        if st.button("Update Booking"):
            edit_visit_data(new_uid,new_tid,new_vd)
            st.success("Successfully updated details of {} and {}".format(old_uid,old_tid))

    result2 = view_all_visit_data()
    df2 = pd.DataFrame(result2, columns=['User_ID','Theatre_ID','Visit_Date'])
    with st.expander("Updated data"):
        st.dataframe(df2)