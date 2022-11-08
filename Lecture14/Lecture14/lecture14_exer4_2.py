def kmer(dna_seq,  sliding_win, offset, kmer_found_min):
    DNA_seq = dna_seq.upper()
    kmer_range = list(range(0, len(dna_seq)))
    kmer_max = len(dna_seq)
    kmersfound = []
    startingbase = 0
    while True:
        if (startingbase + sliding_win) < len(dna_seq) + 1 :
            seqout = (DNA_seq)[startingbase : startingbase + sliding_win]
            kmersfound = kmersfound + [seqout]
            startingbase += offset
        else:
            break
    non_redun_set = list(set(kmersfound))

    for kmerfrequencies in non_redun_set:
        if kmerfrequencies.count(kmerfrequencies) > kmer_found_min:
            return (str(kmerfrequencies) + str(kmersfound.count(kmerfrequencies)))
        else:
            return (str(kmerfrequencies) + str(kmersfound.count(kmerfrequencies)))

    # for startingbase in kmer_range:
    #     if (startingbase + sliding_win) < len(dna_seq) + 1:
    #         seqout = (DNA_seq)[startingbase : startingbase + sliding_win]
    #         kmersfound = kmersfound + [seqout]
    # non_redun_set = list(set(kmersfound))
    # for kmerfrequencies in non_redun_set:
    #     if kmerfrequencies.count(kmerfrequencies) > kmer_found_min:
    #         return (str(kmerfrequencies) + str(kmersfound.count(kmerfrequencies)))
    #     else:
    #         return (str(kmerfrequencies) + str(kmersfound.count(kmerfrequencies)))

