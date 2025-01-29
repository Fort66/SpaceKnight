import pygame as pg
pg.mixer.pre_init(44100, -16, 2, 2048) # Инициализация звука. Инициализация плейера. (частота, биты (Если значение отрицательное, то будут использоваться подписанные значения выборки. Положительные значения означают, что будут использоваться неподписанные аудиосэмплированные выборки. Неверное значение вызывает исключение), каналы, буфер)

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

from config.createObjects import screen



class Game:
    def __init__(self):
        self.run = True
        self.clock = pg.time.Clock()
        self.fps = 100
        self.winWidth = screen.win.get_width()
        self.winHeight = screen.win.get_height()
        

    def eventGame(self):
        for event in pg.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.run = False


    def runGame(self):
        while self.run:
            screen.win.fill(screen.color)

            # обработка игровых событий
            self.eventGame()


            pg.display.update()
            self.clock.tick(self.fps)