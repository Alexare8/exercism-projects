STOP_CODONS = ["UAA", "UAG", "UGA"]
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
    for i in range(0, len(strand), 3):
        if (codon := strand[i: i + 3]) in STOP_CODONS:
            break
        result.append(PROTEIN_LOOKUP[codon])
    return result
