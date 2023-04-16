import pyxel

from assets.font.PyxelUnicode import PyxelUnicode

class Chatbox:
    def __init__(self,image,nom,question,rep1 = None,rep2 = None,rep3 = None):
        self.font = PyxelUnicode("assets/font/pixelmix.ttf", 20)
        self.image = image
        self.nom_chat = nom
        self.question = question
        self.reponse1 = rep1
        self.reponse2 = rep2
        self.reponse3 = rep3
        if self.reponse1 is not None:
            self.selected = 1
        elif self.reponse2 is not None:
            self.selected = 2
        elif self.reponse3 is not None:
            self.selected = 3

    def dess(self):
        pyxel.rect(0,500,1350,430,0)
        self.image.dess(0,376)
        for k in range(5):
            pyxel.line(0,500+k,1350,500+k,7)
            pyxel.line(204 + k, 505, 204 + k, 555, 7)
            pyxel.line(0, 555 + k, 208, 555 + k, 7)
            pyxel.line(k,505,k,555,7)
            if self.reponse1 is not None and self.reponse2 is not None and self.reponse3 is not None:
                pyxel.line(800+k,504,800+k,680,7)
        self.font.text(40,520,self.nom_chat)
        if self.reponse1 == None and self.reponse2== None and self.reponse3 == None:
            if len(self.question) <= 90:
                self.font.text(20, 600, self.question)
            elif len(self.question) <= 180:
                self.font.text(20, 570, self.question[:90])
                if self.question[90] == " ":
                    self.font.text(20, 600, self.question[91:])
                else:
                    self.font.text(20, 600, self.question[90:])
            else:
                self.font.text(20, 570, self.question[:90])
                if self.question[90] == " ":
                    self.font.text(20, 600, self.question[91:180])
                else:
                    self.font.text(20, 600, self.question[90:180])
                if self.question[180] == " ":
                    self.font.text(20, 630, self.question[181:])
                else:
                    self.font.text(20, 630, self.question[180:])
        else:
            if len(self.question) <= 50:
                self.font.text(20, 600, self.question)
            elif len(self.question) <= 100:
                self.font.text(20, 570, self.question[:50])
                if self.question[50] == " ":
                    self.font.text(20, 600, self.question[51:])
                else:
                    self.font.text(20, 600, self.question[50:])
            else:
                self.font.text(20, 570, self.question[:50])
                if self.question[50] == " ":
                    self.font.text(20, 600, self.question[51:100])
                else:
                    self.font.text(20, 600, self.question[50:100])
                if self.question[100] == " ":
                    self.font.text(20, 630, self.question[101:])
                else:
                    self.font.text(20, 630, self.question[100:])
            if not self.reponse1 is None:
                self.font.text(850,520,self.reponse1)
            if not self.reponse2 is None:
                self.font.text(850,580,self.reponse2)
            if not self.reponse3 is None:
                self.font.text(850,640,self.reponse3)
            if self.selected == 1:
                pyxel.tri(815,522,815,542,835,532,7)
            if self.selected == 2:
                pyxel.tri(815,582,815,602,835,592,7)
            if self.selected == 3:
                pyxel.tri(815,642,815,662,835,652,7)
            if pyxel.btnp(pyxel.KEY_UP):
                if self.selected == 2:
                    if self.reponse1 is not None:
                        self.selected = 1
                if self.selected == 3:
                    if self.reponse2 is not None:
                        self.selected = 2
                    elif self.reponse1 is not None:
                        self.selected = 1
            if pyxel.btnp(pyxel.KEY_DOWN):
                if self.selected == 2:
                    if self.reponse3 is not None:
                        self.selected = 3
                if self.selected == 1:
                    if self.reponse2 is not None:
                        self.selected = 2
                    elif self.reponse3 is not None:
                        self.selected = 3
                        
                        
        def chooseAnswer(self):
            pass