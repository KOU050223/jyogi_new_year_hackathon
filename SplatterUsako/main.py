# title: Splatter Usako
# author: KOUHEI UOZUMI
# desc: A Pyxel platformer example
# site: https://kou050223.github.io/jyogi_new_year_hackathon/
# license: MIT
# version: 1.0

import pyxel
from core.layout import draw_layout
from entities.player import Player
from constants import *

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Splatter Usako")
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
        if pyxel.btn(pyxel.KEY_A):
            self.player.x = max(self.player.x - 2, 0)
            self.player.w = PLAYER_W
        if pyxel.btn(pyxel.KEY_D):
            self.player.x = min(self.player.x + 2, SCREEN_WIDTH - PLAYER_W)
            self.player.w = -PLAYER_W
        if pyxel.btn(pyxel.KEY_W):
            self.player.y = max(self.player.y - 2, 20)
        if pyxel.btn(pyxel.KEY_S):
            self.player.y = min(self.player.y + 2, SCREEN_HEIGHT - 20)
        # プレイヤーの位置制限
        self.player.x = max(0, min(self.player.x, min(SCREEN_WIDTH - self.player.w,48)))
        self.player.y = max(0, min(self.player.y, min(SCREEN_HEIGHT - self.player.h, 51)))
        # プレイヤーのアニメーション

        print(self.player.x, self.player.y)
        # プレイヤーの当たり判定


    def draw(self):
        pyxel.cls(0)
        # UIレイアウトの描画
        draw_layout(self.score, self.time, self.life, self.items)
        # プレイヤーの描画
        self.player.draw()
        
if __name__ == '__main__':
    app = App()