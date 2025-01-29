import pygame as pg
from pygame.locals import *
from pygame.math import Vector2
# import gif_pygame
from Game.source import *
from icecream import ic
from Game.LevelsGame import LG
from Game.source import backgroundSection

class CameraGroup(pg.sprite.Group):
    def __init__(self, 
                 game: object = None):
        super().__init__(self)

        self.game = game
        self.displaySurface = pg.display.get_surface()
        # camera offset
        self.offset: Vector2 = Vector2()
        self.half: Vector2 = (self.displaySurface.get_size()[0] // 2, self.displaySurface.get_size()[1] // 2)
        self.cameraRect = pg.Rect(10, 10, 10, 10)
        self.keyboardSpeed = None
        self.mouseSpeed = None
        self.setBackground()

    
    def setBackground(self) -> None:
        self.source= backgroundSection(LG.currentLevel)
        # self.gifBackgtound = gif_pygame.load('Images/Back/gif/2.gif')
        # self.gifRect = self.gifBackgtound.get_rect()
        self.backgroundSurface = pg.image.load(self.source).convert_alpha()
        # self.backgroundRect = self.backgroundSurface.get_rect(center = self.half)
        self.backgroundRect = self.backgroundSurface.get_rect()
        # ic(self.backgroundRect)


    def cameraCenter(self, target):
        self.offset.x = target.rect.centerx - self.half[0]
        self.offset.y = target.rect.centery - self.half[1]


    def customDraw(self, player):
        self.cameraCenter(player)
        # background offset
        # self.displaySurface.blit(self.gifBackgtound, self.gifRect)
        self.backgroundOffset = self.backgroundRect.topleft - self.offset
        self.displaySurface.blit(self.backgroundSurface, self.backgroundOffset)
        
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.center):
            offsetPosition = sprite.rect.topleft - self.offset
            self.displaySurface.blit(sprite.imageRot, offsetPosition)
