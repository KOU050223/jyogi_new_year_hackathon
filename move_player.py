import pyxel
from constants import PLAYER_W, PLAYER_H

def move_player(app):
    # プレイヤーの移動
    if pyxel.btnp(pyxel.KEY_LEFT):
        app.player_x = max(app.player_x - 18, 0) # 20px左に移動
        app.player_w = PLAYER_W    # 画像を左向きに
    if pyxel.btnp(pyxel.KEY_RIGHT):
        app.player_x = min(app.player_x + 18, pyxel.width - PLAYER_W)
        app.player_w = -PLAYER_W   # 画像を右向きに
    if pyxel.btnp(pyxel.KEY_UP):
        app.player_y = max(app.player_y - 20, 0)
    if pyxel.btnp(pyxel.KEY_DOWN):
        app.player_y = min(app.player_y + 20, pyxel.height - PLAYER_H)