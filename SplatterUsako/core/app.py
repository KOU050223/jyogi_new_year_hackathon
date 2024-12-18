import pyxel
from core.game import Game

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Jyogi Usako Game")
        pyxel.load("assets/usako.pyxres")
        self.game = Game()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.game.update()

    def draw(self):
        pyxel.cls(12)
        self.game.draw()

if __name__ == "__main__":
    App()
