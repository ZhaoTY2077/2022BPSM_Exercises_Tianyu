def get_at_content(some_dna):
    length = len(some_dna)
    a_content = some_dna.upper().count("A")
    t_content = some_dna.upper().count("T")
    at_ratio = (a_content + t_content) / length
    return round(at_ratio, 2)




