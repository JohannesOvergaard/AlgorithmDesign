from sys import stdin

def read_blosum(filename):
    file = open(filename)

    blosum_map = {}
    letters = []
    for index,line in enumerate(file):
        if index < 6:
            continue
        split = line.rsplit()
        if index == 6:
            blosum_map = {x:{}for x in split}
            letters = split
            continue
        blosum_map[split[0]] = {x:int(v) for (x, v) in zip(letters, split[1:])}
    
    file.close()
    return blosum_map

class Organism(object):
    def __init__(self,name):
        self.name = name
        self.gene = ""

def parse_input():
    organisms = []
    current_organism = None
    for line in stdin:
        if(line[0] == ">"):
            split = line.rsplit()
            current_organism = Organism(split[0][1:])
            organisms.append(current_organism)
        else:
            current_organism.gene += line.replace("\n","")
    return organisms

def sequence_alignment(o1,o2,blosum_map):
    m,n = len(o1.gene), len(o2.gene)

    M = [[0 for _ in range(n+1)] for _ in range(m+1) ]
    
    for i in range(0, m):
        M[i+1][0] = M[i][0] + blosum_map["*"][o1.gene[i]]
    for j in range(0, n):
        M[0][j+1] = M[0][j] + blosum_map["*"][o2.gene[j]]

    for i in range(m):
        for j in range(n):
            penalty = blosum_map[o1.gene[i]][o2.gene[j]]
            alignment = penalty + M[i][j]
            gap1 = blosum_map["*"][o1.gene[i]] + M[i][j+1]
            gap2 = blosum_map["*"][o2.gene[j]] + M[i+1][j]
            M[i+1][j+1] = max(alignment,gap1,gap2)
    return M

def trace_back(M,o1,o2):
    i = len(o1.gene)
    j = len(o2.gene)
    results_o1 = ""
    results_o2 = ""
    [print(v) for v in M]
    while i != 0 and j != 0:
        alignment = M[i-1][j-1]
        gap1 = M[i-1][j]
        gap2 = M[i][j-1]
        maximum = max(alignment,gap1,gap2)

        #print(i,j, o1.gene[i-1], o2.gene[j-1])
        #print(" ", alignment, gap1, gap2)
        if alignment == maximum:
            i-=1
            j-=1
            results_o1 += o1.gene[i]
            results_o2 += o2.gene[j]
        elif gap1 == maximum:
            i -= 1
            results_o1 += o1.gene[i]
            results_o2 += "-"
        else:
            j-=1
            results_o1 += "-"
            results_o2 += o2.gene[j]
        #print("  "+results_o1)
        #print("  "+results_o2)
    return results_o1[::-1],results_o2[::-1]

blosum_map = read_blosum("data/BLOSUM62.txt")
organisms = parse_input()
for i in range(len(organisms)):
    for j in range(i+1, len(organisms)):
                
        M = sequence_alignment(organisms[i],organisms[j],blosum_map)
        res1,res2 = trace_back(M,organisms[i],organisms[j])
        print(organisms[i].name + "--" + organisms[j].name + ": "+ str(M[-1][-1]))
        print(res1)
        print(res2)