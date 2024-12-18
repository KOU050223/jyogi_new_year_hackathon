import pyxel
from core.layout import draw_layout
from entities.player import Player
from constants import *

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Game Layout Example")
        # アセットロード
        pyxel.load("assets/usako.pyxres")
        self.player = Player()
        self.score = 0
        self.time = 190
        self.life = 5
        self.items = []
        pyxel.run(self.update, self.draw)

    def update(self):
        # プレイヤーの移動ロジック (仮)
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player.x = max(self.player.x - 2, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player.x = min(self.player.x + 2, SCREEN_WIDTH - PLAYER_W)
        if pyxel.btn(pyxel.KEY_UP):
            self.player.y = max(self.player.y - 2, 20)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.player.y = min(self.player.y + 2, SCREEN_HEIGHT - 20)

    def draw(self):
        pyxel.cls(0)
        # UIレイアウトの描画
        draw_layout(self.score, self.time, self.life, self.items)
        # プレイヤーの描画
        self.player.draw()

App()