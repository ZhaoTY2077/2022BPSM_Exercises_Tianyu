def aa_per(pro_seq, aa_resi):
    length = len(pro_seq)
    resi_num = pro_seq.upper().count(aa_resi)
    ratio = resi_num/length
    return ratio*100

