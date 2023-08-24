from json import load, dump, loads
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QListWidget
import os
from fsforge import take_fs_snapshot
from json import load

os.path.abspath(__file__)


structure = take_fs_snapshot("programme/")

liste_niveaux = []
liste_chapitres = []

a_rajouter = ""

with open("exercices.json", "r+", encoding="utf-8") as jsonFile:
    data = load(jsonFile)
    exercices_supprime = []

    for i in range(len(data)):
        if not(os.path.exists("programme/" + data[i]["fichier"])):
            exercices_supprime.append(i)

    exercices_supprime.reverse()

    for i in exercices_supprime:
        del data[i]

    jsonFile.seek(0)  # rewind
    dump(data, jsonFile)
    jsonFile.truncate()


with open("exercices.json", "r+", encoding="utf-8") as jsonFile:
    data = load(jsonFile)

    for cle1, valeur1 in structure.items():
        liste_niveaux.append(cle1)
        for cle2, valeur2 in structure[cle1].items():
            for exercice, useless in valeur2.items():
                in_json = False
                for i in range(len(data)):
                    if data[i]["fichier"] ==  cle1 + "/" + cle2 + "/" + exercice:
                        in_json = True
                        break
                if not(in_json):
                    json = "\t{\n"
                    json += '\t\t"nom" : "a donner",\n'
                    json += '\t\t"description" : "' + exercice + '",\n'
                    json += '\t\t"niveau" : "' + cle1 + '",\n'
                    json += '\t\t"fichier" : "' + cle1 + "/" + cle2 + "/" + exercice + '",\n'
                    json += '\t\t"theme" : "' + cle2.replace("_", " ") + '",\n'
                    json += '\t\t"exemple" : "generation_pdf/' + cle1 + "_" + cle2 + "_" + exercice[:len(exercice)-3] + 'pdf'+'"\n'
                    json += '\t},\n'
                    
                    if ".pdf" in json:
                        a_rajouter += json

with open("exercices.json", "r", encoding="utf-8") as jsonFile:
    contenu = jsonFile.read()
contenu = contenu.replace("[", "[\n")
contenu = contenu.replace(", {", ",\n\t{\n\t\t")
contenu = contenu.replace(', "', ',\n\t\t"')
contenu = contenu.replace(":", " : ")
if len(a_rajouter) > 3:
    contenu = contenu[:len(contenu)-1]+",\n"+a_rajouter[:len(a_rajouter)-2]+"\n]"

with open("exercices.json", "w", encoding="utf-8") as jsonFile:
    jsonFile.write(contenu)



"""
contenu = "[\n"


for cle1, valeur1 in structure.items():
    liste_niveaux.append(cle1)
    chapitre = []
    for cle2, valeur2 in structure[cle1].items():
        chapitre.append(cle2)
        for exercice, useless in valeur2.items():
            try:
                for i in range(len(loaded_json)):
                    if loaded_json[i]["fichier"]
            except:        
                json = "\t{\n"
                json += '\t\t"nom" : "a donner",\n'
                json += '\t\t"description" : "' + exercice + '",\n'
                json += '\t\t"niveau" : "' + cle1 + '",\n'
                json += '\t\t"fichier" : "' + cle1 + "/" + cle2 + "/" + exercice + '",\n'
                json += '\t\t"theme" : "' + cle2.replace("_", " ") + '",\n'
                json += '\t\t"exemple" : "generation_pdf/' + cle1 + "_" + cle2 + "_" + exercice[:len(exercice)-3] + 'pdf'+'"\n'
                json += '\t},\n'
                contenu += json

    liste_chapitres.append(chapitre)
    
contenu = contenu[:len(contenu)-2] + "\n]"
    
with open("listes_exercices.json", "w", encoding='utf-8') as fi: 
    fi.write(contenu)
"""