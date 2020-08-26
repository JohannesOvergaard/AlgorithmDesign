from sys import stdin

class Person(object):
    def __init__(self, line):
        id, name = line.split(" ")
        self.id = int(id) - 1
        self.name = name.rsplit()[0]
        self.prefs = None
        self.partner = None

mw = []
free_m = []
n = 0

def pass_preferences(lineNr):
    for (linenumber, line) in enumerate(stdin, lineNr):
        split = line.replace(" \n", "").split(" ")
        id = int(split[0][:-1]) - 1
        prefs = [int(pref) - 1 for pref in split[1:]]
        if id % 2 == 1:
            prefs = {id: n-rank for (rank, id) in enumerate(prefs)}
        mw[id].prefs = prefs

def pass_names(lineNr):
    for (linenumber, line) in enumerate(stdin, lineNr):
        if line == "\n":
            pass_preferences(linenumber)
        else:
            person = Person(line)
            mw.append(person)
            if person.id % 2 == 0: free_m.append(person.id)

def pass_start():     
    for (linenumber, line) in enumerate(stdin):
        if line[0] == "#":
            pass
        elif line[0] == "n":
            n = int(line[2:])
            pass_names(linenumber)


def run_Gale_Shapley():
    while len(free_m) > 0 and len(mw[free_m[0]].prefs) > 0:
        m = mw[free_m[0]]
        w = mw[m.prefs.pop(0)]

        if w.partner is None:
            w.partner = m
            m.partner = w
            free_m.pop(0)
        elif w.prefs[m.id] > w.prefs[w.partner.id]:
            free_m.pop(0)
            free_m.append(w.partner.id)
            w.partner = m
            m.partner = w

def print_result():
    for p in mw:
        if p.id % 2 == 0:
            print(p.name + " -- " + p.partner.name)

pass_start()
run_Gale_Shapley()
print_result()
