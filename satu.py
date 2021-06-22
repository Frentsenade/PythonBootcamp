# a = "A"
# t = "T"
# c = "C"
# g = "G"
def countMol2(dna):
    countA = dna.count("A")
    countT = dna.count("T")
    countC = dna.count("C")
    countG = dna.count("G")

    print("A : {}, T : {}, G : {}, C : {}".format(countA, countT, countG, countC))

molecule = "ATGACXaaGTGGUA"
s = molecule.upper()

def countMol(dna):
    counts = {"A": 0, "T": 0, "G": 0, "C": 0}
    for x in dna:
        if x in counts:   
            counts[x] += 1
    return counts

dna = input("Input molecule sequence : ")
dnaUp = dna.upper()

print(countMol(dnaUp))
print(countMol(s))
countMol2(s)