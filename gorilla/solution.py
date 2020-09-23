from sys import stdin

class Organism(object):
    def __init__(self,name):
        self.name = name
        self.gene = ""

def read_penalties(filename):
    file = open(filename)

    penalties = {}
    letters = []
    for index,line in enumerate(file):
        if index < 6:
            continue
        split = line.rsplit()
        if index == 6:
            penalties = {x:{} for x in split}
            letters = split
            continue
        penalties[split[0]] = {x:int(v) for (x, v) in zip(letters, split[1:])}
    
    file.close()
    return penalties

def parse_input():
    organisms = []
    current_organism = None
    for line in stdin:
        if line[0] == ">":
            split = line.rsplit()
            current_organism = Organism(split[0][1:])
            organisms.append(current_organism)
        else:
            current_organism.gene += line.replace("\n","")
    return organisms

def construct_table(o1, o2, penalties):
    m,n = len(o1.gene), len(o2.gene)
    M = [[0 for _ in range(n+1)] for _ in range(m+1) ]
    
    for i in range(0, m):
        M[i+1][0] = M[i][0] + penalties["*"][o1.gene[i]]
    for j in range(0, n):
        M[0][j+1] = M[0][j] + penalties["*"][o2.gene[j]]

    for i in range(m):
        for j in range(n):
            penalty = penalties[o1.gene[i]][o2.gene[j]]
            alignment = penalty + M[i][j]
            gap1 = penalties["*"][o1.gene[i]] + M[i][j+1]
            gap2 = penalties["*"][o2.gene[j]] + M[i+1][j]
            M[i+1][j+1] = max(alignment,gap1,gap2)

    return M

def trace_back(M, o1, o2, penalties):
    i, j = len(o1.gene), len(o2.gene)
    results_o1, results_o2 = "", ""

    while i > 0 or j > 0:
        if M[i][j] == M[i-1][j-1] + penalties[o1.gene[i-1]][o2.gene[j-1]] :
            i-=1
            j-=1
            results_o1 += o1.gene[i]
            results_o2 += o2.gene[j]
        elif M[i][j] == M[i-1][j] + penalties["*"][o1.gene[i-1]]:
            i -= 1
            results_o1 += o1.gene[i]
            results_o2 += "-"
        else:
            j-=1
            results_o1 += "-"
            results_o2 += o2.gene[j]

    # Reversing the strings since they are constructed in reverse order
    return results_o1[::-1], results_o2[::-1]

penalties = read_penalties("data/BLOSUM62.txt")
organisms = parse_input()

for i in range(len(organisms)):
    for j in range(i+1, len(organisms)):
        M = construct_table(organisms[i], organisms[j], penalties)
        res1,res2 = trace_back(M, organisms[i], organisms[j], penalties)
        print(organisms[i].name + "--" + organisms[j].name + ": "+ str(M[-1][-1]))
        print(res1)
        print(res2)
