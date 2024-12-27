import pyxel
from constants import *

def count_timer(self):
    # タイマーのカウント
    self.time -= 0.03
    # タイマーが0になったらゲームオーバー
    if self.time <= 0:
        self.state = "GAMEOVER"
        self.time = 0
    if self.state == "CLEAR":
        self.score = self.score + self.time * 10
    # ステージクリア時にスコアに加算
