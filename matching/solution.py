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
traversing_names = True
n = 0

for (linenumber, line) in enumerate(stdin):
    if line[0] == "#":
        pass
    elif line[0] == "n":
        n = int(line[2:])
    elif line == "\n":
        traversing_names = False
    elif traversing_names:
        person = Person(line)
        mw.append(person)
        if person.id % 2 == 0: free_m.append(person.id)
    elif not traversing_names:
        split = line.replace(" \n", "").split(" ")
        id = int(split[0][:-1]) - 1
        prefs = split[1:]
        prefs = [int(pref) - 1 for pref in prefs]
        if id % 2 == 1:
            prefs = {id: n-rank for (rank, id) in enumerate(prefs)}
        mw[id].prefs = prefs

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

for p in mw:
    if p.id % 2 == 0:
        print(p.name + " -- " + p.partner.name)

