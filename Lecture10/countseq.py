dnaseq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
countA = dnaseq.count('A')
countT = dnaseq.count('T')
length = len(dnaseq)
quotient = (countA+countT)/length
print(quotient)
