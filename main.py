from langchain_db_chain import execute_few_shot_query
import streamlit as st

st.title("Strive Sports Analytics Hub")
st.subheader("Ask store-related questions and get real-time database answers.")

question = st.text_input("Question: ")

try:
    if question:
        with st.spinner('Running query...'):
            answer = execute_few_shot_query(question)
            response = answer.run(question)
        st.header("Answer")
        st.success(response)
except Exception as e:
    st.error(f"Something went wrong: {e}")
