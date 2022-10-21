dnaseq = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'
print(len(dnaseq))

exon1 = dnaseq[0:63]
exon2 = dnaseq[90:123]

#print(exon1)
#print(exon2)

codingseq = exon1+exon2
print(codingseq)

print(len(codingseq))
percen = len(codingseq)/len(dnaseq)
print(str(int(percen*100))+"%")

intron = dnaseq[63:90]
intron_low = intron.lower()
longseq = exon1+intron_low+exon2
print(longseq)

