from sys import exit


from loguru import logger

logger.add(
    'logs/error.log',
    format='{time} {level} {message}',
    level = 'ERROR'
)


@logger.catch
def main():
    import pygame as pg
    pg.init()
    from classes.classGame import Game
    
    game = Game()
    game.runGame()
    
    pg.quit()

if __name__ == '__main__':
    # для отладки игры
    main()
    exit()

    # для продакшн
    '''
    try:
        main()
    finally:
        pg.quit()
        exit()
    '''