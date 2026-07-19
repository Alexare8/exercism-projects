from itertools import islice

PROTEIN_DICT = {"AUG": "Methionine",
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
                "UGA": "STOP"}


def proteins(strand: str) -> str:
    "Translate an RNA string into proteins."
    result = []
    for codon in batched(strand, 3):
        protein = PROTEIN_DICT[codon]
        if protein == "STOP":
            break
        result.append(protein)
    return result


# Python 3.12 brings a batched() method to itertools.
# This rough equivalent is based on the one in the python 3.12 docs.
def batched(iterable, n) -> str:
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := "".join(islice(it, n)):
        yield batch