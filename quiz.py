import streamlit as st

def run_quiz():

    st.header("🧪 Biotechnology Quiz")

    questions = [
        {
            "question": "What is PCR used for?",
            "options": ["Protein synthesis", "DNA amplification", "Cell division", "RNA destruction"],
            "answer": "DNA amplification"
        },
        {
            "question": "CRISPR is mainly used for:",
            "options": ["Photosynthesis", "Gene editing", "Digestion", "Respiration"],
            "answer": "Gene editing"
        },
        {
            "question": "Cloning produces:",
            "options": ["Different organisms", "Identical copies", "Mutations", "RNA molecules"],
            "answer": "Identical copies"
        },
        {
            "question": "DNA is composed of:",
            "options": ["Proteins", "Nucleotides", "Lipids", "Vitamins"],
            "answer": "Nucleotides"
        },
        {
            "question": "The enzyme used in PCR is:",
            "options": ["Ligase", "Helicase", "Taq Polymerase", "Primase"],
            "answer": "Taq Polymerase"
        },
        {
            "question": "Which technology allows gene editing?",
            "options": ["ELISA", "CRISPR", "Fermentation", "Microscopy"],
            "answer": "CRISPR"
        },
        {
            "question": "Plasmids are commonly found in:",
            "options": ["Plants", "Animals", "Bacteria", "Viruses"],
            "answer": "Bacteria"
        },
        {
            "question": "DNA replication occurs during:",
            "options": ["S Phase", "M Phase", "G0 Phase", "Cytokinesis"],
            "answer": "S Phase"
        },
        {
            "question": "Fermentation is carried out mainly by:",
            "options": ["Microorganisms", "Animals", "Plants", "Minerals"],
            "answer": "Microorganisms"
        },
        {
            "question": "Biotechnology combines biology with:",
            "options": ["History", "Technology", "Geography", "Politics"],
            "answer": "Technology"
        }
    ]

    # ---------- SESSION STATE ----------
    if "quiz_score" not in st.session_state:
        st.session_state.quiz_score = 0

    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    # ---------- QUESTIONS ----------
    for i, q in enumerate(questions):

        st.session_state[f"q_{i}"] = st.radio(
            q["question"],
            q["options"],
            key=f"quiz_{i}"
        )

    # ---------- SUBMIT ----------
    if st.button("📋 Submit Quiz"):

        score = 0

        for i, q in enumerate(questions):
            if st.session_state[f"q_{i}"] == q["answer"]:
                score += 1

        st.session_state.quiz_score = score
        st.session_state.submitted = True

    # ---------- RESULT ----------
    if st.session_state.submitted:

        score = st.session_state.quiz_score
        total = len(questions)
        percentage = (score / total) * 100

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        else:
            grade = "D"

        st.success(f"🎯 Score: {score}/{total}")
        st.info(f"📊 Percentage: {percentage:.1f}%")
        st.info(f"🏆 Grade: {grade}")

        if percentage >= 80:
            st.balloons()
