import pyxel
from constants import *

def draw_layout(score, time, life, items):
    # 背景
    pyxel.rect(0, 0, SCREEN_WIDTH, 20, 7)  # 上部バー
    pyxel.rect(0, 100, SCREEN_WIDTH, 20, 7)  # 下部バー
    
    # SCORE
    pyxel.text(SCORE_X, SCORE_Y, f"SCORE: {score}", 1)
    # TIME
    pyxel.text(TIME_X, TIME_Y, f"TIME: {time}", 1)
    # LIFE
    pyxel.text(LIFE_X, LIFE_Y, f"LIFE:", 1)
    for i in range(life):
        pyxel.blt(LIFE_X + 30 + i * 10, LIFE_Y, 0, 0, 0, 8, 8, 0)  # LIFEアイコン
    # ITEM
    pyxel.text(ITEM_X, ITEM_Y, "ITEM", 1)
    pyxel.rectb(ITEM_X + 20, ITEM_Y, 30, 10, 1)

    # メイン画面
    pyxel.rectb(0, 20, SCREEN_WIDTH, 80, 7)