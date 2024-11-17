import streamlit as st
import pandas as pd


if "ID" not in st.session_state:
    st.session_state["ID"] = "None"

ID = st.session_state["ID"]
with st.sidebar:
    st.caption(f'{ID}님 접속중')

df = pd.read_csv("서울특별시교육청 중학교.csv")


st.title(':school:내가 갈 수 있는 중학교는 어디일까?:school:')

color = {'공립':'#37eb91',
         '사립':'#ebbb37',
         '국립':'#0400ff'}
df.loc[:,'color'] = df.copy().loc[:,'설립형태'].map(color)



st.map(df, latitude="위도",
       longitude="경도",
       size=300,
       color = "color")
