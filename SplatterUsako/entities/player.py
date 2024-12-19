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
        x, self.y, 0, 0, 0, self.w, self.h, 0,0,0.7)

    # def update(self):
        # プレイヤーの位置制限
        # self.x = max(100, min(self.x, SCREEN_WIDTH - self.w))
        # self.y = max(20, min(self.y, min(SCREEN_HEIGHT - self.h, 51)))