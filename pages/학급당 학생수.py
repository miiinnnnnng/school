import streamlit as st
import pandas as pd


data = pd.read_csv("서울 학급당 학생수.csv")

if "ID" not in st.session_state:
    st.session_state["ID"] = "None"

ID = st.session_state["ID"]

with st.sidebar:
    st.caption(f'{ID}님 접속중')
    
with st.form("input"):
    #unique 중복값 제외하고 하나씩
    REGION = st.multiselect("자치구", data['region'].unique())
    SCHOOL = st.multiselect("학교급", data['school'].unique())
    submitted = st.form_submit_button("조회")
    
    if submitted:
        name_list = []
        result = data["year"].drop_duplicates().sort_values().reset_index(drop=True)

        for re in REGION:
            for sc in SCHOOL:
                name = f"{re}_{sc}"
                name_list.append(name)
                selected_df = data[ (data['region'] == re)& (data['school'] == sc)]
                selected_df = selected_df[["year","student"]].rename(columns={"student": name})
                result = pd.merge(result, selected_df, on='year').sort_values('year')           
            
        
        st.line_chart(data=result, x='year', y=name_list,use_container_width=True)