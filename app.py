import streamlit as st

st.title("📚 AI Study Assistant")

# ---------- NAVIGATION ----------
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
            st.session_state.notes.append(f"Q: {question}\nA: {answer}\n")
            st.success("Note saved!")

# ---------- STUDY MODE ----------
elif menu == "Study Mode":
    st.subheader("📖 Study Mode")
    st.write("Biotechnology: uses living organisms for products.")
    st.write("Genetics: study of heredity.")
    st.write("DNA: carries genetic information.")

# ---------- QUIZ ----------
elif menu == "Quiz":
    st.subheader("📝 Quiz")

    q1 = st.radio("DNA stands for?", ["Deoxyribonucleic Acid", "Data Network Access", "None"])
    if st.button("Submit Quiz"):
        if q1 == "Deoxyribonucleic Acid":
            st.success("Correct!")
        else:
            st.error("Wrong answer")

# ---------- EXAM ----------
elif menu == "Exam":
    st.subheader("🎯 Exam Mode")
    st.write("Coming soon... (we can upgrade this into full test system)")

# ---------- NOTES ----------
st.header("📒 Saved Notes")

if st.session_state.notes:
    all_notes = "\n".join(st.session_state.notes)

    st.text_area("Your Notes", all_notes, height=200)

    st.download_button(
        "📥 Download Notes",
        all_notes,
        file_name="study_notes.txt",
        mime="text/plain"
    )
else:
    st.info("No notes saved yet.")
