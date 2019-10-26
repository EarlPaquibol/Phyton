# DNA_strand ("ATTGC") # return "TAACG"

def DNA_strand(dna):
    dna = list(dna)
    for i,e in enumerate(dna):
        if e == 'A':
            dna[i] = 'T'
        elif e == 'T':
            dna[i] = 'A'
        elif e == 'G':
            dna[i] = 'C'
        elif e == 'C':
            dna[i] = 'G'
    return ''.join(dna)



print(DNA_strand('ATAGC'))

# def DNA_strand(dna):
#     return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))

pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strands(dna):
    for x in dna:
        print(pairs[x])




print(DNA_strands('ATAGC'))
