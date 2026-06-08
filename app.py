import streamlit as st

st.title("📚 AI Study Assistant")

if "notes" not in st.session_state:
    st.session_state.notes = []

question = st.text_input("Ask your question:")

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

if question:
    answer = get_answer(question)

    st.success(answer)

    if st.button("💾 Save Note"):
        note = f"Q: {question}\nA: {answer}\n"
        st.session_state.notes.append(note)
        st.success("Note saved!")

st.header("📒 Saved Notes")

if st.session_state.notes:
    all_notes = "\n".join(st.session_state.notes)

    st.text_area("Your Notes", all_notes, height=200)

    st.download_button(
        label="📥 Download Notes",
        data=all_notes,
        file_name="study_notes.txt",
        mime="text/plain"
    )
else:
    st.info("No notes saved yet.")