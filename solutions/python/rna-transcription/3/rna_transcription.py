dna_to_rna = str.maketrans("GCTA", "CGAU")


def to_rna(dna_strand: str) -> str:
    """Returns the RNA transcription of a given DNA strand."""
    return dna_strand.translate(dna_to_rna)