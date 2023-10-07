import streamlit as st
from database import *
import pandas as pd

def query_page():
    list_of_us = [i[0] for i in view_only_userID()]
    selected_u = st.selectbox("Which user?", list_of_us)
    if selected_u:
        result = q1(selected_u)
        df1 = pd.DataFrame(result, columns=['Movies'])
        if st.button("Show movies watched by user"):
            st.dataframe(df1)
    st.markdown(" ")
    if st.button("Show users who have not watched any movie"):
        res = q2()
        df1 = pd.DataFrame(res, columns=['Users'])
        if res:
            st.dataframe(df1)
    st.markdown(" ")
    if st.button("Show count of movies watched by users"):
        res = q3()
        df1 = pd.DataFrame(res, columns=['User',"Number Of Movies"])
        if res:
            st.dataframe(df1)

#def set_page():
#    if st.button("Show users who have watched two particular movies"):
#        col1, col2 = st.columns(2)
#        list_of_ms = [i[0] for i in view_only_movieID()]
#        #list_of_movs = [fetchMovieNames(i)[0] for i in list_of_ms]
#        with col1:
#            movie1 = st.selectbox("Select Movie one",list_of_ms)
#        with col2:
#            movie2 = st.selectbox("Select Movie two",list_of_ms)
#        if st.button("Show result"):
#            res = q4(movie1,movie2)
#            df = pd.DataFrame(res,columns=['Movies'])
#            st.dataframe(df)











