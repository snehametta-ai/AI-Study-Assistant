import streamlit as st

def run_study():

    st.subheader("📖 Study Mode")

    topic = st.selectbox(
        "Choose a topic",
        [
            "DNA",
            "Genetics",
            "Biotechnology",
            "Microbiology",
            "Cell",
            "Protein",
            "Enzymes",
            "PCR",
            "CRISPR"
        ]
    )

    if topic == "DNA":
        st.success(
            "DNA (Deoxyribonucleic Acid) carries genetic instructions used in growth, development, and reproduction."
        )

    elif topic == "Genetics":
        st.success(
            "Genetics is the study of genes, heredity, and variation in living organisms."
        )

    elif topic == "Biotechnology":
        st.success(
            "Biotechnology uses living organisms, cells, and biological systems to create useful products."
        )

    elif topic == "Microbiology":
        st.success(
            "Microbiology is the study of microorganisms such as bacteria, fungi, viruses, and protozoa."
        )

    elif topic == "Cell":
        st.success(
            "The cell is the basic structural and functional unit of life."
        )

    elif topic == "Protein":
        st.success(
            "Proteins are molecules made of amino acids that perform many functions in living organisms."
        )

    elif topic == "Enzymes":
        st.success(
            "Enzymes are biological catalysts that speed up chemical reactions in living organisms."
        )

    elif topic == "PCR":
        st.success(
            "PCR (Polymerase Chain Reaction) is a laboratory technique used to amplify DNA."
        )

    elif topic == "CRISPR":
        st.success(
            "CRISPR is a gene-editing technology that allows scientists to modify DNA sequences with high precision."
        )
