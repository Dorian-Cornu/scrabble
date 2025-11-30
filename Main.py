from tkinter import Tk, Frame, Label, StringVar, Entry, Button
from random import choice

Liste_Teste = [
    "AMOUR","MAJOR","ROUGE","BLEUE","TABLE","CHAIR","MONDE","VOYER","FABLE",
    "ARBRE","POMME","VACHE","FLEUR","NUAGE","LIVRE","RIREZ","TENIR","PLAGE",
    "GAMME","LUMEN","BRUIT","SONAR","COEUR","OCEAN","SANTE","POIDS","ETAGE",
]

Longeur = 5
Essai_max = 6

class Motus:
    def __init__(self, ecran):
        ecran.title("Motus")
        self.__mot = choice(Liste_Teste).upper()
        print(self.__mot)
        self.__essai = 0
        self.__game_over = False
        self.__frame_grid = Frame(ecran, padx=10, pady=10)
        self.__frame_grid.grid(row=0, column=0)
        self.__frame_entree = Frame(ecran, pady=5)
        self.__frame_entree.grid(row=1, column=0)
        self.__grille = [] 
        for ligne in range(Essai_max):
            l = []
            for colonne in range(Longeur):
                case = Label(self.__frame_grid, text=" ", width=4, height=2, relief="solid", font=("Helvetica", 18, "bold"))
                case.grid(row=ligne, column=colonne, padx=3, pady=3)
                l.append(case)
            self.__grille.append(l)
        self.__mot_teste = StringVar()
        self.__valider = Entry(self.__frame_entree, textvariable=self.__mot_teste, font=("Helvetica", 14))
        self.__valider.grid(row=0, column=0, padx=5)
        self.__bouton = Button(self.__frame_entree, text="Essayer", command=self.essai_mot)
        self.__bouton.grid(row=0, column=1, padx=5)
        self.__texte = Label(ecran, text=f"Mot à deviner : {Longeur} lettres — {Essai_max} essais", pady=5)
        self.__texte.grid(row=2, column=0)

    def essai_mot(self):
        if self.__game_over == True:
            return
        teste = self.__mot_teste.get().strip().upper()
        self.__mot_teste.set("")
        ligne = self.__essai
        resultat = self.evaluer_mot(teste, self.__mot)
        for i, ch in enumerate(teste):
            case = self.__grille[ligne][i]
            case.config(text=ch)
            state = resultat[i]
            if state == 'juste':
                case.config(bg="green")  
            elif state == 'present':
                case.config(bg="yellow")  
            else:
                case.config(bg="grey")  
        self.__essai += 1
        if teste == self.__mot:
            self.__game_over = True
            self.__texte.config(text="Victoire")
        elif self.__essai >= Essai_max:
            self.__game_over = True
            self.__texte.config(text="Perdu")
        else:
            self.__texte.config(text=f"Essai {self.__essai}/{Essai_max}")

    def evaluer_mot(self, mot_essai, mot):
        resultat = ['absent'] * len(mot_essai)
        lettres_mot = list(mot)
        for i, ch in enumerate(mot_essai):
            if ch == mot[i]:
                resultat[i] = 'juste'
                lettres_mot[i] = None  
        for i, ch in enumerate(mot_essai):
            if resultat[i] == 'juste':
                continue
            if ch in lettres_mot:
                resultat[i] = 'present'
                indice = lettres_mot.index(ch)
                lettres_mot[indice] = None
            else:
                resultat[i] = 'absent'
        return resultat


ecran = Tk()
jeu = Motus(ecran)
ecran.mainloop()

