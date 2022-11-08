def aa_per(pro_seq, aa_list = ["A", "I", "L", "M", "F", "W", "Y", "V"]):
    length = len(pro_seq)
    resi_totalnum = 0
    for aa_resi in aa_list:
        resi_totalnum = resi_totalnum + pro_seq.upper().count(aa_resi)

    ratio = resi_totalnum/length
    return ratio*100
