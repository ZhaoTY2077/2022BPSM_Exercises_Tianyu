dnaseq = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'
motif = 'GAATTC'

posi = dnaseq.find(motif)+1
print(posi)

cutposi = posi+2
print("the position of cut is between base No."+str(posi), "and base No."+str(cutposi))

len_second = len(dnaseq)-posi
print("the length of second fragment is "+str(len_second),"and the length of another fragment is "+str(len(dnaseq)-len_second))

#for i in len(dnaseq)


