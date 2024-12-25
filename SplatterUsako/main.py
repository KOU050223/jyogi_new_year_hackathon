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

        #ジャンプ関係
        self.is_jumping = False
        self.jump_velocity = 0
        self.gravity = 1
        self.jump_strength = 10
        self.max_jump_height = 25

        pyxel.run(self.update, self.draw)

    def update(self):
        self.update_player()
        # デバッグ用
        if pyxel.btnp(pyxel.KEY_O):
            print(self.is_jumping,self.jump_velocity,self.gravity,        self.jump_strength,self.max_jump_height)
        if pyxel.btnp(pyxel.KEY_P):
            print(self.player.x,self.player.y)

    def draw(self):
        pyxel.cls(0)
        # UIレイアウトの描画
        draw_layout(self.score, self.time, self.life, self.items)
        # プレイヤーの描画
        self.player.draw()
        

    def update_player(self):
        # プレイヤーの移動ロジック (仮)
        if pyxel.btn(pyxel.KEY_A):
            self.player.x = max(self.player.x - 2, 0)
            self.player.w = -PLAYER_W
        if pyxel.btn(pyxel.KEY_D):
            self.player.x = min(self.player.x + 2, SCREEN_WIDTH - PLAYER_W)
            self.player.w = PLAYER_W
        if pyxel.btn(pyxel.KEY_W):
            self.player.y = max(self.player.y - 2, 20)
        if pyxel.btn(pyxel.KEY_S):
            self.player.y = min(self.player.y + 2, SCREEN_HEIGHT - 20)
        # プレイヤーの位置制限
        self.player.x = max(0, min(self.player.x, min(SCREEN_WIDTH - self.player.w,48)))
        self.player.y = max(0, min(self.player.y, min(SCREEN_HEIGHT - self.player.h, 51)))

        # 重力処理
        if not self.is_jumping:
            self.player.y += self.gravity
        
        # プレイヤージャンプ
        # 接地しているときだけジャンプできる
        # プレイヤージャンプ
        if pyxel.btnp(pyxel.KEY_SPACE) and self.player.y == 52:
            self.is_jumping = True
            self.jump_velocity = self.jump_strength

        if self.is_jumping:
            self.player.y -= self.jump_velocity
            self.jump_velocity -= self.gravity
            if self.jump_velocity <= 0:
                self.is_jumping = False
        
        # プレイヤーが地面に着地したら位置を修正
        if self.player.y > 52:
            self.player.y = 52
            self.is_jumping = False

        # プレイヤーのアニメーション(パンチ)
        
        # プレイヤーのアニメーション(しゃがみ)

        # プレイヤーのアニメーション(キック)

        ### プレイヤーの当たり判定



if __name__ == '__main__':
    app = App()