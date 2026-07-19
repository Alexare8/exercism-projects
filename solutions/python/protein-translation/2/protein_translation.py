PROTEIN_LOOKUP = {"AUG": "Methionine",
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
    "UGG": "Tryptophan"}


def proteins(strand: str) -> str:
    """Translate an RNA string into proteins."""
    result = []
    for i in range(len(strand) // 3):
        if (codon := strand[i * 3: i * 3 + 3]) in ["UAA", "UAG", "UGA"]:
            break
        protein = PROTEIN_LOOKUP[codon]
        result.append(protein)
    return result
