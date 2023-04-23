"""
Nous sert à faire en sorte que le fond des images soit transparent dans le jeu
"""

import pyxel

pyxel.init(50, 50) #tailles de l'image

def update():
    if pyxel.btnp(pyxel.KEY_U):
        print("active")
        #choisir un nom
        with open("./character/pnj/greycat_backward.py", "w") as fichier:
            fichier.write("import pyxel\n")
            fichier.write("class Greycat_backward:\n")
            fichier.write("    def __init__(self):\n")
            fichier.write("        pass\n")
            fichier.write("    def dess(self,x,y):\n")
            for x in range(50):
                for y in range(50):
                    c = pyxel.pget(x, y)
                    if not c == 11: #la couleur du fond de l'image
                        txt = "        pyxel.pset(x+" +str(x) + ",y+" + str(y) + "," + str(c) + ")"
                        fichier.write(txt+"\n")

def draw():
    for x in range(6):
        for y in range(4):
            pyxel.image(0).load(0, 0, "./character/pnj/greycat_backward.png")
            pyxel.blt(0, 0, 0, 0, 0, 50, 50) # taille de l'image

pyxel.run(update,draw)