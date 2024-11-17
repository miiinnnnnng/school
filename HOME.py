import streamlit as st
import pandas as pd
import time

st.title("2024 사임동반 성적관리 서비스")
st.image('children.jpeg')

dat = pd.read_csv('members.csv')
dat["PW"] = dat["PW"].astype(str)

with st.form("loginform"):
    ID = st.text_input("ID", 
                    placeholder="아이디를 입력하세요.")
    PW = st.text_input("Password", 
                    placeholder="비밀번호를 입력하세요.",
                    type='password')
    submit_button = st.form_submit_button("로그인")

if submit_button:
    if not ID or not PW:
        st.warning("ID와 Password를 모두 입력해주세요.")
    else:
        user = dat[(dat["ID"]==ID)&(dat["PW"]==PW)]

        if not user.empty:
            st.success(f"{ID}님 환영합니다!")
            st.session_state["ID"]=ID
            progress_text = "로그인 중입니다. 잠시만 기다려주세요."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(1)
                my_bar.empty()
        else:
            st.warning('사용자정보가 일치하지 않습니다.')