import pygame as pg

from loguru import logger
from sys import exit

pg.init()


logger.add(
    'logs/error.log',
    format='{time} {level} {message}',
    level = 'ERROR'
)


@logger.catch
def main():
    from classes.classGame import Game
    game = Game()
    game.runGame()


if __name__ == '__main__':
    # try:
    main()
    # finally:
    pg.quit()
    exit()

