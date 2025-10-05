def to_rna(dna):

    if len(dna) == 0:
        return ""
    allowed = set("ACGT")
    for ch in dna:
        if ch not in allowed:
            raise ValueError("Недопустимый символ")

    list = []
    dict = {"G": "C", "C": "G", "T": "A", "A": "U"}
    for char in dna:
        list += dict[char]
    return "".join(list)




sequence = "TATGCG"
print("РНК:", to_rna(sequence))
