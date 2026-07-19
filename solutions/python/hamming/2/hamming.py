def distance(strand_a: str, strand_b: str) -> int:
    """Calculate the Hamming distance between two strands of DNA"""
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(gene_a != gene_b for gene_a, gene_b in zip(strand_a, strand_b))
