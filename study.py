import streamlit as st

def run_study():
    st.title("📚 AI Study Assistant")

    question = st.text_input("Ask a question:")

    def get_answer(q):
        q = q.lower()

        if "pcr" in q:
            return "PCR is used to amplify DNA."
        elif "crispr" in q:
            return "CRISPR is a gene editing tool."
        else:
            return "Topic not available."

    if question:
        st.success(get_answer(question))