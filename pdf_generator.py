from reportlab.pdfgen import canvas

def create_pdf(notes):

    filename = "study_notes.pdf"

    pdf = canvas.Canvas(filename)

    y = 800

    pdf.setTitle("AI Study Assistant Notes")

    pdf.drawString(100, y, "AI Study Assistant Notes")

    y -= 30

    for note in notes:

        pdf.drawString(100, y, note)

        y -= 20

        # Start a new page if needed
        if y < 50:
            pdf.showPage()
            y = 800

    pdf.save()

    return filename
