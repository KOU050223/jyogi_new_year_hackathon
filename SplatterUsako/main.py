# title: Splatter Usako
# author: KOUHEI UOZUMI
# desc: A Pyxel platformer example
# site: https://kou050223.github.io/jyogi_new_year_hackathon/
# license: MIT
# version: 1.0

import pyxel
from core.layout import draw_layout
from systems.timer import count_timer
from entities.player import Player
from constants import *

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Splatter Usako")
        # アセットロード
        pyxel.load("assets/usako.pyxres")
        # system関係
        self.player = Player()
        self.score = 0
        self.time = 1000 # タイマーの初期値
        self.life = 5
        self.zanki = 3
        self.items = []
        self.state = "GAME"
        #ジャンプ関係
        self.is_jumping = False
        self.jump_velocity = 0
        self.gravity = 1
        self.jump_strength = 10
        self.max_jump_height = 25
        # アニメーション関係
        self.panchframe = 0
        self.is_panching = False
        self.is_squating = False   # しゃがみ状態
        self.kickframe = 0
        self.is_kicking = False # キック状態

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.state == "TITLE":
            pass

        if self.state == "GAME":
            count_timer(self)
            self.update_player()
        
        if self.state == "GAMEOVER":
            pass
        
        if self.state == "CLEAR":
            pass
        
        # デバッグ用
        if pyxel.btnp(pyxel.KEY_O):
            print(self.is_jumping,self.jump_velocity,self.gravity,        self.jump_strength,self.max_jump_height)
        if pyxel.btnp(pyxel.KEY_P):
            print(self.player.x,self.player.y)
    def draw(self):
        pyxel.cls(0)
        if self.state == "TITLE":
            print("TITLE")
            pass

        if self.state == "GAME":
            # print("GAME")
            # UIレイアウトの描画
            draw_layout(self.score, self.time, self.life, self.items)

            # プレイヤーの描画
            if not self.is_panching and not self.is_squating and not self.is_kicking:
                self.player.draw()
            # パンチアニメーションの変化
            if self.is_panching:    
                # x,y,img,u,v,w,h,colkey,rotate,scale
                # 0,56 32,56 64,56 96,56
                pyxel.blt(self.player.x, self.player.y, 0, self.panchframe * 32, 56, 32, 48, 0,0,0.7)
            # しゃがみアニメーションの変化
            if self.is_squating:
                pyxel.blt(self.player.x, self.player.y, 0, 0, 104, 24, 48, 0,0,0.7)
            # 歩行アニメーションの変化
            # キックアニメーションの変化

        if self.state == "GAMEOVER":
            print("GAMEOVER")
            pass
        
        if self.state == "CLEAR":
            print("CLEAR")
            pass
        

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

        # パンチ処理
        if pyxel.btnp(pyxel.KEY_U):
            self.is_panching = True
            self.panchframe = 1
        if self.is_panching:
            self.panchframe += 1
            if self.panchframe >= 4:
                self.panchframe = 0
                self.is_panching = False


        # しゃがみ処理
        if pyxel.btn(pyxel.KEY_S):
            self.is_squating = True
        else:
            self.is_squating = False

        # キック処理（しゃがみかつパンチ）
        if self.is_panching and self.is_squating:
            self.is_kicking = True
            self.kickframe = 1

        ### プレイヤーの当たり判定



if __name__ == '__main__':
    app = App()