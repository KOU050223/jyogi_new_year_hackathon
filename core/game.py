from systems.movement import move_player
import pyxel
from constants import *

class Game:
    def __init__(self):
        self.score = 0
        self.player_x = 72
        self.player_y = -16
        self.is_alive = True

    def update(self):
        move_player(self)

    def draw(self):
        # プレイヤーの描画
        pyxel.blt(self.player_x, self.player_y, 0, 0, 0, PLAYER_W, PLAYER_H)
