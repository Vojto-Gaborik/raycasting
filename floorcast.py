import pygame as pg
import numpy as np
from player import *
from map import *


def main():
    pg.init()
    win = pg.display.set_mode((2000, 1000)) # WINDOW
    win.fill((0, 0, 0)) # balablbllad
    pg.display.set_caption('GAME')

    map = Map(int(input('Enter size of the maze: ')))
    #print(map.endpoint)
    for i in range(len(map.grid)):
        print(map.grid[i])
    player = Player(1.5 * (1000 / len(map.grid)), 1.5 * (1000 / len(map.grid)), map.grid)

    run = True
    while run:
        pg.draw.rect(win, (50, 50, 50), pg.Rect(0, 0, 2000, 1000))

        for y in range(len(map.grid)):
            for x in range(len(map.grid[0])):
                if map.grid[y][x] == 0:
                    pg.draw.rect(win, (255, 255, 255),
                                 pg.Rect(0 + x * 1000 / len(map.grid), 0 + y * 1000 / len(map.grid), 1000 / 8 - 1,
                                         1000 / 8 - 1))
                else:
                    pg.draw.rect(win, (50, 50, 50),
                                 pg.Rect(0 + x * 1000 / len(map.grid), 0 + y * 1000 / len(map.grid), 1000 / 8 - 1,
                                         1000 / 8 - 1))

        pg.draw.rect(win, (255, 0, 0), pg.Rect(player.x - 15, player.y - 15, 30, 30))
        pg.draw.line(win, (255, 0, 0), (player.x, player.y),
                     (player.x + np.cos(player.rotation) * 50, player.y - np.sin(player.rotation) * 50), 5)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            player.move_forward()
        if keys[pg.K_s]:
            player.move_back()
        if keys[pg.K_a]:
            player.rotate_left()
        if keys[pg.K_d]:
            player.rotate_right()

        player.rays(win, map.grid)

        pg.display.update()


if __name__ == '__main__':
    main()
    pg.quit()
