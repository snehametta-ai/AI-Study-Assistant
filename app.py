import streamlit as st
import learn
import question_bank

st.title("📚 AI Study Assistant")

# ---------- MENU ----------
menu = st.sidebar.selectbox(
    "Choose Mode",
    ["Home", "Study Mode", "Quiz", "Exam"]
)

# ---------- SESSION ----------
if "notes" not in st.session_state:
    st.session_state.notes = []

# ---------- SIMPLE AI ANSWER ----------
def get_answer(q):
    q = q.lower()

    if "dna" in q:
        return "DNA carries genetic instructions in living organisms."
    elif "genetics" in q:
        return "Genetics is the study of genes and heredity."
    elif "biotechnology" in q:
        return "Biotechnology uses living organisms to create useful products."
    else:
        return "I am still learning this topic."

# ---------- HOME ----------
if menu == "Home":

    st.subheader("Ask Your Question")

    question = st.text_input("Enter question:")

    if question:
        answer = get_answer(question)
        st.success(answer)

        if st.button("💾 Save Note"):
            st.session_state.notes.append(f"Q: {question}\nA: {answer}")

# ---------- STUDY MODE ----------
elif menu == "Study Mode":
    learn.run_study()

# ---------- QUIZ ----------
elif menu == "Quiz":

    st.subheader("📝 Quiz Mode")

    questions = question_bank.get_questions()

    if "q_index" not in st.session_state:
        st.session_state.q_index = 0
        st.session_state.score = 0

    q = questions[st.session_state.q_index]

    st.write(q["question"])

    answer = st.radio("Choose answer:", q["options"], key=st.session_state.q_index)

    if st.button("Submit Answer"):

        if answer == q["answer"]:
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error(f"Wrong! Correct answer: {q['answer']}")

        st.session_state.q_index += 1

        if st.session_state.q_index >= len(questions):
            st.success(f"🎉 Quiz Finished! Score: {st.session_state.score}/{len(questions)}")

            st.session_state.q_index = 0
            st.session_state.score = 0

# ---------- EXAM ----------
elif menu == "Exam":
    st.subheader("🎯 Exam Mode")
    st.write("Coming soon...")

# ---------- NOTES ----------
st.header("📒 Saved Notes")

if st.session_state.notes:
    st.text_area("Your Notes", "\n".join(st.session_state.notes), height=200)
else:
    st.info("No notes saved yet.")
