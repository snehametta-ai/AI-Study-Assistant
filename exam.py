import streamlit as st
import question_bank

def run_exam():

    st.subheader("🎯 Exam Mode")

    questions = question_bank.get_questions()

    score = 0

    for i, q in enumerate(questions):

        st.write(f"Q{i+1}. {q['question']}")

        answer = st.radio(
            "Choose answer:",
            q["options"],
            key=f"exam_{i}"
        )

        if answer == q["answer"]:
            score += 1

    if st.button("Submit Exam"):
        st.success(
            f"🎉 Exam Completed! Your Score: {score}/{len(questions)}"
        )
