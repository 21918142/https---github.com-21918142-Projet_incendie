#########################################################################
# Groupe MPCI 1
# Celine DJADEL
# Zinaïda BENAOUDIA
# Yamcel ABDESSLAM
# Kévin SU
# Brice AUGUSTIN
# Lilya LAHJAILY
# https://github.com/21918142/https---github.com-21918142-Projet_incendie
#########################################################################

# IMPORT DES LIBRAIRIES :
import tkinter as tk
import random

# CONSTANTES :
LARGEUR = 800
HAUTEUR = 500

# VARIABLES GLOBALES :
terrain = []


# FONCTIONS :


def genere_terrain() :
    global terrain
    w = 0
    for i in range(0,LARGEUR,10) :
        for j in range(0,HAUTEUR,10) :
            terrain.append([i, j, random.choice(["blue","green","yellow"]), 0])
            canvas.create_rectangle((i,j,i+10,j+10), fill=terrain[w][2])
            w +=1

# PROGRAMME :
# / Fenetre /
racine = tk.Tk()
racine.title("Simulation de la propagation d'un incendie")

canvas = tk.Canvas(racine, width = LARGEUR , height = HAUTEUR)
canvas.grid(column = 1, row = 1, columnspan = 1, rowspan = 5)

Bouton1 = tk.Button(racine, text = "Génère un terrain", command = genere_terrain)
Bouton1.grid(column = 0, row = 1)















# / Gestion de la fenetre /
racine.mainloop()
