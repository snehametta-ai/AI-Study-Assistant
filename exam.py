import streamlit as st
import time
from question_bank import get_questions
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import datetime


# ---------- PDF CERTIFICATE ----------
def generate_certificate(name, score, total, percent, grade):

    buffer = BytesIO()
    c = canvas.Canvas(buffer)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(100, 750, "BIOTECHNOLOGY EXAM CERTIFICATE")

    c.setFont("Helvetica", 12)
    c.drawString(100, 700, f"Name: {name}")
    c.drawString(100, 680, f"Score: {score}/{total}")
    c.drawString(100, 660, f"Percentage: {percent:.1f}%")
    c.drawString(100, 640, f"Grade: {grade}")
    c.drawString(100, 620, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    c.save()
    buffer.seek(0)

    return buffer


# ---------- EXAM SYSTEM ----------
def run_exam():

    st.header("⏱️ Exam Mode")

    questions = get_questions()

    # ---------- TIMER ----------
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()

    duration = 20 * 60
    elapsed = time.time() - st.session_state.start_time
    remaining = int(duration - elapsed)

    if remaining > 0:
        st.info(f"Time Left: {remaining//60:02d}:{remaining%60:02d}")
    else:
        st.error("⛔ Time is up!")

    # ---------- STORE ANSWERS ----------
    if "exam_answers" not in st.session_state:
        st.session_state.exam_answers = {}

    # ---------- QUESTIONS ----------
    for i, q in enumerate(questions):

        st.session_state.exam_answers[i] = st.radio(
            q["question"],
            q["options"],
            key=f"exam_{i}"
        )

    # ---------- SUBMIT ----------
    if st.button("Submit Exam") or remaining <= 0:

        score = 0

        for i, q in enumerate(questions):
            if st.session_state.exam_answers.get(i) == q["answer"]:
                score += 1

        total = len(questions)
        percent = (score / total) * 100

        if percent >= 90:
            grade = "A+"
        elif percent >= 80:
            grade = "A"
        elif percent >= 70:
            grade = "B"
        elif percent >= 60:
            grade = "C"
        else:
            grade = "D"

        st.success(f"Score: {score}/{total}")
        st.info(f"Percentage: {percent:.1f}%")
        st.info(f"Grade: {grade}")

        # ---------- CERTIFICATE ----------
        name = st.text_input("Enter your name for certificate")

        if name:
            pdf = generate_certificate(name, score, total, percent, grade)

            st.download_button(
                "📥 Download Certificate",
                pdf,
                file_name="biotech_certificate.pdf",
                mime="application/pdf"
            )
