dnaseq = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
comp_seq = dnaseq.replace('A','t').replace('C','g').replace('T','a').replace('G','c')
print(comp_seq.upper())
