import streamlit as st

def run_study():

    st.title("📖 Biotechnology Study Mode")

    question = st.text_input("Ask a Biotechnology question:")

    if question:

        q = question.lower().strip()

        if "pcr" in q:
            st.success("""
1. PCR stands for Polymerase Chain Reaction.
2. It amplifies DNA.
3. It produces millions of copies.
4. Used in disease diagnosis.
5. Uses Taq polymerase.
6. Denaturation separates strands.
7. Annealing binds primers.
8. Extension builds DNA.
9. Widely used in labs.
10. Important biotechnology tool.
""")

        elif "crispr" in q:
            st.success("""
1. CRISPR is a gene editing tool.
2. It comes from bacteria.
3. Cas9 cuts DNA.
4. Used in genetic research.
5. Can modify genes.
6. Helps treat diseases.
7. Very precise method.
8. Used in biotechnology.
9. Revolutionized genetics.
10. Powerful biotech tool.
""")

        elif "cloning" in q:
            st.success("""
1. Cloning makes identical copies.
2. Can clone genes or organisms.
3. Dolly was a cloned sheep.
4. Used in research.
5. Helps study genes.
6. Artificial cloning in labs.
7. Natural cloning exists.
8. Used in agriculture.
9. Ethical issues exist.
10. Important biotech process.
""")

        elif "dna replication" in q:
            st.success("""
1. DNA replication copies DNA.
2. Happens before cell division.
3. Semi-conservative process.
4. Helicase unwinds DNA.
5. Primase adds primers.
6. DNA polymerase builds strands.
7. Okazaki fragments form.
8. Ligase joins fragments.
9. Ensures genetic continuity.
10. Essential for life.
""")

        else:
            st.error("❌ Topic not available. Try PCR, CRISPR, Cloning, DNA Replication.")
