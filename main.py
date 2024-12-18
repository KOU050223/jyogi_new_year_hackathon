import pyxel
import PyxelUniversalFont as puf
from move_player import move_player
from constants import PLAYER_W, PLAYER_H

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Jyogi Usako Game")
        # font設定
        self.writer = puf.Writer("misaki_gothic.ttf")

        # アセットロード
        pyxel.load("assets/usako.pyxres")

        self.score = 0
        # プレイヤーの初期値
        # 座標
        self.player_x = 72
        self.player_y = -16
        # サイズ
        self.player_w = PLAYER_W
        self.player_h = PLAYER_H
        self.player_rotate = 0  # 回転
        self.player_scale = 0   # 拡大率 
        self.player_dy = 0
        self.is_alive = True
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        move_player(self)

    def draw(self):
        pyxel.cls(12)
        # blt(x, y, img, u, v, w, h, [colkey], [rotate], [scale])
        # うさこ表示
        pyxel.blt(70, 50, 0, 0, 0, PLAYER_W, PLAYER_H, 0, 0,0.8)

        # リタネコ表示
        # Draw title
        pyxel.text(65, 30, "Usako Games", pyxel.frame_count % 16)

        # draw(x座標, y座標, テキスト, フォントサイズ, 文字の色(16:モザイク))
        # 背景色はデフォルト値(-1:透明)
        self.writer.draw(60, 40, "うさこゲームズ!", 7)

        # Draw score
        s = f"SCORE {self.score:>4}"
        pyxel.text(5, 4, s, 1)

App()