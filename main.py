# title: Pyxel Jump
# author: Takashi Kitao
# desc: A Pyxel simple game example
# site: https://github.com/kitao/pyxel
# license: MIT
# version: 1.0

import pyxel
import PyxelUniversalFont as puf


class App:
    def __init__(self):
        pyxel.init(160, 120, title="Jyogi Usako Game")
        # font設定
        self.writer = puf.Writer("misaki_gothic.ttf")

        pyxel.cls(7)

        self.score = 0
        self.player_x = 72
        self.player_y = -16
        self.player_dy = 0
        self.is_alive = True
        self.far_cloud = [(-10, 75), (40, 65), (90, 60)]
        self.near_cloud = [(10, 25), (70, 35), (120, 15)]
        self.floor = [(i * 60, pyxel.rndi(8, 104), True) for i in range(4)]
        self.fruit = [
            (i * 60, pyxel.rndi(0, 104), pyxel.rndi(0, 2), True) for i in range(4)
        ]
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()


    def draw(self):
        pyxel.cls(12)

        # Draw title
        pyxel.text(55, 41, "Jyogi Usako Game", pyxel.frame_count % 16)

        # draw(x座標, y座標, テキスト, フォントサイズ, 文字の色(16:モザイク))
        # 背景色はデフォルト値(-1:透明)
        self.writer.draw(50, 50, "うさこゲームズ!", 7)

        # Draw player
        pyxel.blt(
            self.player_x,
            self.player_y,
            0,
            16 if self.player_dy > 0 else 0,
            0,
            16,
            16,
            12,
        )

        # Draw score
        s = f"SCORE {self.score:>4}"
        pyxel.text(5, 4, s, 1)
        pyxel.text(4, 4, s, 7)


App()
