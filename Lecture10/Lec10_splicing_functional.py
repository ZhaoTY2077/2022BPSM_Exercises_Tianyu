#!/usr/bin/python3

def r_seq(s):
    rs = []
    for i in s:
        if i == 'A':
            r = 'T'
        elif i == 'T':
            r = 'A'
        elif i == 'C':
            r = 'G'
        elif i == 'G':
            r = 'C'
        rs.append(r)
    return ''.join(rs)


def cut_seq(s,motif,cut_posi):
    s_posi = 0
    result_seq = []
    while True:
        e_posi = s[s_posi:].find(motif,s_posi,len(s))
        if e_posi != -1:
            result_seq.append(s[s_posi:e_posi+cut_posi])
            s_posi = e_posi+cut_posi
        else:
            result_seq.append(s[s_posi:])
            break
    return result_seq



# main
s = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'
motif = 'GAATTC'
print("5'-3'", cut_seq(s,motif,1))
print("3'-5'",cut_seq(s,r_seq(motif),len(motif)-1))
