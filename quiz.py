import streamlit as st

def run_quiz():
    st.title("🧪 Biotechnology MCQ Quiz")

    quiz = [
        {
            "question": "What is PCR used for?",
            "options": ["Protein synthesis", "DNA amplification", "Cell division", "RNA destruction"],
            "answer": "DNA amplification"
        },
        {
            "question": "CRISPR is mainly used for:",
            "options": ["Photosynthesis", "Gene editing", "Digestion", "Respiration"],
            "answer": "Gene editing"
        }
    ]

    score = 0
    user_answers = []

    for i, q in enumerate(quiz):
        choice = st.radio(q["question"], q["options"], key=i)
        user_answers.append((choice, q["answer"]))

    if st.button("Submit Quiz"):
        for ans, correct in user_answers:
            if ans == correct:
                score += 1

        st.success(f"Your Score: {score}/{len(quiz)}")