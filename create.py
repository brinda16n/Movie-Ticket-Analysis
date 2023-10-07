import streamlit as st
from database import *


def create():
    col1, col2 = st.columns(2)
    with col1:
        movie_id = st.text_input("Movie Id: ")
        movie_name = st.text_input("Movie Name:")
        movie_lang = st.text_input("Language:")
        movie_actor = st.text_input("Actor:")
    with col2:
        movie_genre = st.selectbox("Genre", ["Action", "Comedy", "Horror", "Drama", "Romance"])
        movie_dir = st.text_input("Director:")

    if st.button("Add Movie"):
        add_movie_data(movie_id,movie_name,movie_lang,movie_genre,movie_dir,movie_actor)
        st.success("Successfully added Movie: {}".format(movie_name))

def create1():
    col1, col2 = st.columns(2)
    with col1:
        user_id = st.text_input("User Id: ")
        user_name = st.text_input("User Name:")

    with col2:
        user_pwd = st.text_input("Password: ")
        user_adrs = st.text_input("Address:")

    if st.button("Add User"):
        add_user_data(user_id,user_name,user_pwd,user_adrs)
        st.success("Successfully added User: {}".format(user_name))

def create2():
    col1, col2 = st.columns(2)
    with col1:
        t_id = st.text_input("Theatre Id: ")
        t_name = st.text_input("Theatre Name:")

    with col2:
        t_pin = st.text_input("Pincode: ")
        t_no = st.slider(label="Number_Of_Shows",min_value=0,max_value=10)

    if st.button("Add Theatre"):
        add_theatre_data(t_id,t_name,t_pin,t_no)
        st.success("Successfully added Theatre: {}".format(t_name))


def create3():
    col1, col2 = st.columns(2)
    with col1:
        b_id = st.text_input("Booking Id: ")
        uid = st.text_input("User ID:")

    with col2:
        mid = st.text_input("Movie ID:")
        no_of_ts = st.number_input("Number of tickets:")

    if st.button("Add Booking"):
        add_booking_data(b_id,mid,uid,no_of_ts)
        st.success("Successfully added Booking: {}".format(b_id))

def create4():
    col1, col2 = st.columns(2)
    with col1:
        uid = st.text_input("User ID:")
        tid = st.text_input("Theatre ID:")

    with col2:
        vd = st.date_input("Visit date:")

    if st.button("Add Visit"):
        add_visit_data(uid,tid,vd)
        st.success("Successfully added Visit details: {} and {}".format(uid,tid))