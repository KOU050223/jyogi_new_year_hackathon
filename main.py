import pyxel
import PyxelUniversalFont as puf


class App:
    def __init__(self):
        pyxel.init(160, 120, title="Jyogi Usako Game")
        # font設定
        self.writer = puf.Writer("misaki_gothic.ttf")

        # アセットロード
        pyxel.load("assets/usako.pyxres")

        self.score = 0
        self.player_x = 72
        self.player_y = -16
        self.player_dy = 0
        self.is_alive = True
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()


    def draw(self):
        pyxel.cls(12)
        # blt(x, y, img, u, v, w, h, [colkey], [rotate], [scale])
        pyxel.blt(70, 50, 0, 0, 0, 18, 49, 0, 0, 0.8)

        # Draw title
        pyxel.text(65, 30, "Usako Games", pyxel.frame_count % 16)

        # draw(x座標, y座標, テキスト, フォントサイズ, 文字の色(16:モザイク))
        # 背景色はデフォルト値(-1:透明)
        self.writer.draw(60, 40, "うさこゲームズ!", 7)

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
