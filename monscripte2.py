etudiant = [
    {"matricule":1000,
    "nom":"jhon",
    "prenom":"doe",
    "note":14},
    {"matricule":2000,
    "nom":"bob",
    "prenom":"carlon",
    "note":9},
    {"matricule":3000,
    "nom":"rayane",
    "prenom":"smith",
    "note":13}
]

def estadmissible(note):
    if (note>10):
     return True
    else:
        return False 

for e in etudiant:
     if (estadmissible(e["note"])):
        print(e["nom"] + ' ' + e["prenom"])