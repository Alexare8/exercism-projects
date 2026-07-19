def to_rna(dna_strand: str) -> str:
    """Returns the RNA transcription of a given DNA strand."""
    dna_to_rna = {"G": "C", "C": "G", "T": "A", "A": "U"}
    return "".join(dna_to_rna[char] for char in dna_strand)