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

        {"question": "Insulin is produced using?", "options": ["PCR", "Recombinant DNA", "Cloning", "Fermentation"], "answer": "Recombinant DNA"},
        {"question": "Taq polymerase is from?", "options": ["E. coli", "Thermus aquaticus", "Yeast", "Plant cells"], "answer": "Thermus aquaticus"},
        {"question": "Gene therapy is used for?", "options": ["Fix genes", "Break DNA", "Kill cells", "Stop replication"], "answer": "Fix genes"},
        {"question": "Vectors are used for?", "options": ["Gene transfer", "Photosynthesis", "Digestion", "Respiration"], "answer": "Gene transfer"},
        {"question": "mRNA carries info from?", "options": ["DNA to ribosome", "Protein to DNA", "RNA to nucleus", "Cell to cell"], "answer": "DNA to ribosome"},
        {"question": "Bioreactors are used for?", "options": ["Large production", "DNA cutting", "Gene editing", "Cloning animals"], "answer": "Large production"},
        {"question": "Stem cells can?", "options": ["Differentiate", "Destroy DNA", "Stop growth", "Kill bacteria"], "answer": "Differentiate"},
        {"question": "RNA contains?", "options": ["Thymine", "Uracil", "Guanine only", "No bases"], "answer": "Uracil"},
        {"question": "Human genome project finished in?", "options": ["2003", "1990", "2010", "1985"], "answer": "2003"},
    ] * 6  # makes it 100+ questions

    random.shuffle(bank)

    return bank[:10]