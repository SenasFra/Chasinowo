import pyxel

pyxel.init(40,40) #tailles des jetons

def update():
    if pyxel.btnp(pyxel.KEY_U):
        print("active")
        #choisir un nom
        with open("./token_50.py", "w") as fichier:
            fichier.write("import pyxel\n")
            fichier.write("class Token_50:\n")
            fichier.write("    def __init__(self):\n")
            fichier.write("        pass\n")
            fichier.write("    def dess(self,x,y):\n")
            for x in range(40):
                for y in range(40):
                    c = pyxel.pget(x, y)
                    if not c == 5: #la couleur du fond du token
                        txt = "        pyxel.pset(x+" +str(x) + ",y+" + str(y) + "," + str(c) + ")"
                        fichier.write(txt+"\n")

def draw():
    for x in range(6):
        for y in range(4):
            pyxel.image(0).load(0, 0, "../token_50.png")
            pyxel.blt(0, 0, 0, 0, 0, 40, 40) # taille de l'image

pyxel.run(update,draw)