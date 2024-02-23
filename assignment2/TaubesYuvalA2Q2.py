file_path = r"C:\School\uni\Comp 1012\assignment2\seq1.txt"

def translate_codon(codon):
    codon_protein = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine", 
        "UUG": "Leucine",
        "UCU": "Serine", 
        "UCC": "Serine", 
        "UCA": "Serine", 
        "UCG": "Serine",
        "UAU": "Tyrosine", 
        "UAC": "Tyrosine",
        "UGU": "Cysteine", 
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP", 
        "UAG": "STOP", 
        "UGA": "STOP",
    }
    return codon_protein[codon]

def translate_rna(rna_sequence):
    proteins = []
    i = 0
    while i < len(rna_sequence):
        codon = rna_sequence[i:i+3]
        protein = translate_codon(codon)
        if protein == "STOP":
            break
        proteins.append(protein)
        i += 3
    return proteins

def count_occurrences(proteins):
    protein_count = {}
    for protein in proteins:
        protein_count[protein] = protein_count.get(protein, 0) + 1
    return protein_count

def print_result(protein_count):
    print("Protein Occurrences:")
    for protein, count in protein_count.items():
        print(f"{protein}: {count}")
    max_protein = max(protein_count, key=protein_count.get)
    print(f"Protein '{max_protein}' has the most occurrence with {protein_count[max_protein]} repetitions in the RNA sequence")

def main(file_path):
    with open(file_path, 'r') as file:
        rna_sequence = file.read().replace('\n', '')
        proteins = translate_rna(rna_sequence)
        protein_count = count_occurrences(proteins)
        print_result(protein_count)


main(file_path)