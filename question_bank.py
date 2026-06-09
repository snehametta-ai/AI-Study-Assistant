import random

def get_questions():
    bank = [
        {"question": "Who discovered PCR?", "options": ["Kary Mullis", "Watson", "Crick", "Darwin"], "answer": "Kary Mullis"},
        {"question": "DNA is made of?", "options": ["Proteins", "Nucleotides", "Lipids", "Vitamins"], "answer": "Nucleotides"},
        {"question": "CRISPR is used for?", "options": ["Gene editing", "Respiration", "Digestion", "Photosynthesis"], "answer": "Gene editing"},
        {"question": "Plasmids are found in?", "options": ["Bacteria", "Plants", "Humans", "Viruses"], "answer": "Bacteria"},
        {"question": "Restriction enzymes do?", "options": ["Cut DNA", "Make RNA", "Build proteins", "Destroy cells"], "answer": "Cut DNA"},
        {"question": "Gel electrophoresis is used for?", "options": ["DNA separation", "Cell growth", "Protein folding", "Fermentation"], "answer": "DNA separation"},
        {"question": "DNA replication is?", "options": ["Conservative", "Semi-conservative", "Random", "Indirect"], "answer": "Semi-conservative"},
        {"question": "PCR enzyme is?", "options": ["Ligase", "Taq polymerase", "Helicase", "Primase"], "answer": "Taq polymerase"},
        {"question": "Fermentation is done by?", "options": ["Microorganisms", "Animals", "Plants", "Fungi only"], "answer": "Microorganisms"},
        {"question": "ELISA is used for?", "options": ["Disease detection", "DNA cutting", "Cloning", "Breathing"], "answer": "Disease detection"},
    ] * 10  # enough questions

    random.shuffle(bank)
    return bank[:10]
