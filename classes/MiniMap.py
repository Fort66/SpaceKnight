import pygame as pg
from Game.ScreenGame import win
from icecream import ic

class MiniMap:
    def __init__(self, 
                 group = None,
                 game = None): 
        self.game = game
        self.group = group
        self.mapSize = (win.screen.get_width() / 4, win.screen.get_height() / 4)
        self.mapSurface = pg.Surface(self.mapSize, pg.SRCALPHA)
        self.mapSurface.fill((0, 100, 0, 50))
        self.mapRect = self.mapSurface.get_rect()
        self.ratioX = self.mapSize[0] / self.group.backgroundRect[2]
        self.ratioY = self.mapSize[1] / self.group.backgroundRect[3]


    def drawPlayer(self):
        for player in self.game.playersSpritesGroup:
            pg.draw.circle(self.mapSurface, 'yellow', (int(player.rect.centerx * self.ratioX), int(player.rect.centery * self.ratioY)), 2)


    def drawEnemy(self):
        for enemy in self.game.enemiesSpritesGroup:
            pg.draw.circle(self.mapSurface, 'red', (int(enemy.rect.centerx * self.ratioX), int(enemy.rect.centery * self.ratioY)), 2)

    
    def drawPlayerBullet(self):
        for bullet in self.game.playersBulletsGroup:
            pg.draw.circle(self.mapSurface, 'yellow', (int(bullet.rect.centerx * self.ratioX), int(bullet.rect.centery * self.ratioY)), 1)


    def drawEnemyBullet(self):
        for bullet in self.game.enemiesBulletsGroup:
            pg.draw.circle(self.mapSurface, 'red', (int(bullet.rect.centerx * self.ratioX), int(bullet.rect.centery * self.ratioY)), 1)


    def update(self):
        self.mapSurface.fill((0, 100, 0, 50))
        self.drawPlayer()
        self.drawEnemy()
        self.drawPlayerBullet()
        self.drawEnemyBullet()
        win.screen.blit(self.mapSurface, (win.screen.get_width() - self.mapSize[0], win.screen.get_height() - self.mapSize[1]))


