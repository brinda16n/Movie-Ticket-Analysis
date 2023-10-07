from database import *
import pandas as pd
import streamlit as st
import plotly.express as px

def read():
    result = view_all_movie_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Movie_ID','Name','Language','Genre','Director','Actor'])
    with st.expander("View all Movies"):
        st.dataframe(df)
    with st.expander("Movie Genre Visualization"):
        task_df = df['Genre'].value_counts().to_frame()
        task_df = task_df.reset_index()
        st.dataframe(task_df)
        p1 = px.pie(task_df, names='index', values='Genre')
        st.plotly_chart(p1)

def read1():
    result = view_all_user_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['User_ID','Name','Password','Address'])
    with st.expander("View all Users"):
        st.dataframe(df)


def read2():
    result = view_all_theatre_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Theatre_ID','Theatre_Name','Pincode','No_Shows_PerDay'])
    with st.expander("View all Theatres"):
        st.dataframe(df)

def read3():
    result = view_all_booking_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Booking_ID','Movie_ID','User_ID','Number Of Tickets'])
    with st.expander("View all Bookings"):
        st.dataframe(df)

def read4():
    result = view_all_visit_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['User_ID','Theatre_ID','Visit Date'])
    with st.expander("View all visit details"):
        st.dataframe(df)