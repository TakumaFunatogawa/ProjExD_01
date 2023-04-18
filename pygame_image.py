import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230418/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01-20230418/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    degree = 10
    kk_imgs = []
    for i in range(degree+1):
        kk_imgs.append(pg.transform.rotozoom(kk_img, i, 1.0))
    for i in range(degree):
        kk_imgs.append(pg.transform.rotozoom(kk_img, degree-i-1, 1.0))

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%1600
        tmr += 1
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img, [1600-x, 0])
        screen.blit(kk_imgs[tmr%((degree*2)+1)], [300, 200])

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()