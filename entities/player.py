from constants import *
import pyxel
class Player:
    def __init__(self):
        self.x = PLAYER_INIT_X
        self.y = PLAYER_INIT_Y
        self.w = PLAYER_W
        self.h = PLAYER_H
        self.is_alive = True

    def draw(self):
        pyxel.blt(self.
        x, self.y, 0, 0, 0, self.w, self.h, 0)