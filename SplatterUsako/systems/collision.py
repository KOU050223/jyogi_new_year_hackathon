import pyxel
from constants import *

def player_collision(self,enemy):
    # タイマーのカウント
    self.time -= 0.03
    # タイマーが0になったらゲームオーバー
    # ステージクリア時にスコアに加算
