import pandas as pd
import streamlit as st
from database import *


def delete():
    result = view_all_movie_data()
    df = pd.DataFrame(result, columns=['Movie_ID','Name','Language','Genre','Director','Actor'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_movies = [i[0] for i in view_only_movieID()]
    selected_movie = st.selectbox("Movie to Delete", list_of_movies)
    st.warning("Do you want to delete {}?".format(selected_movie))
    if st.button("Delete Movie"):
        delete_movie_data(selected_movie)
        st.success("Movie has been deleted successfully")
    new_result = view_all_movie_data()
    df2 = pd.DataFrame(new_result, columns=['Movie_ID','Name','Language','Genre','Director','Actor'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete1():
    result = view_all_user_data()
    df = pd.DataFrame(result, columns=['User_ID','Name','Password','Address'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_users = [i[0] for i in view_only_userID()]
    selected_user = st.selectbox("User to Delete", list_of_users)
    st.warning("Do you want to delete {}?".format(selected_user))
    if st.button("Delete User"):
        delete_user_data(selected_user)
        st.success("User has been deleted successfully")
    new_result = view_all_user_data()
    df2 = pd.DataFrame(new_result, columns=['User_ID','Name','Password','Address'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete2():
    result = view_all_theatre_data()
    df = pd.DataFrame(result, columns=['Theatre_ID','Theatre_Name','Pincode','No_Shows_PerDay'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_ts = [i[0] for i in view_only_theatreID()]
    selected_t = st.selectbox("Theatre to Delete", list_of_ts)
    st.warning("Do you want to delete {}?".format(selected_t))
    if st.button("Delete Theatre"):
        delete_theatre_data(selected_t)
        st.success("Theatre has been deleted successfully")
    new_result = view_all_theatre_data()
    df2 = pd.DataFrame(new_result, columns=['Theatre_ID','Theatre_Name','Pincode','No_Shows_PerDay'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete3():
    result = view_all_booking_data()
    df = pd.DataFrame(result, columns=['Booking_ID','Movie_ID','User_ID','Number Of Tickets'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_bs = [i[0] for i in view_only_bookingID()]
    selected_b = st.selectbox("Theatre to Delete", list_of_bs)
    st.warning("Do you want to delete {}?".format(selected_b))
    if st.button("Delete Booking"):
        delete_booking_data(selected_b)
        st.success("Booking has been deleted successfully")
    new_result = view_all_booking_data()
    df2 = pd.DataFrame(new_result, columns=['Booking_ID','Movie_ID','User_ID','Number Of Tickets'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete4():
    result = view_all_visit_data()
    df = pd.DataFrame(result, columns=['User_ID','Theatre_ID','Visit_Date'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_us = [i[0] for i in view_only_visitID()]
    list_of_ts = [i[1] for i in view_only_visitID()]
    col1, col2 = st.columns(2)
    with col1:
        selected_u = st.selectbox("Select User Id", list_of_us)
    with col2:
        selected_t = st.selectbox("Select Theatre Id", list_of_ts)
    st.warning("Do you want to delete {}?".format(selected_u, selected_t))
    if st.button("Delete Booking"):
        delete_visit_data(selected_u, selected_t)
        st.success("Visit record has been deleted successfully")
    new_result = view_all_visit_data()
    df2 = pd.DataFrame(new_result, columns=['User_ID','Theatre_ID','Visit_Date'])
    with st.expander("Updated data"):
        st.dataframe(df2)