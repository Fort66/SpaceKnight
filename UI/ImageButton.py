import pygame as pg
from pygame.locals import *


class ImgButton:
    def __init__(self,
                x,
                y,
                size,
                text,
                imagePath,
                enable = True,
                hoverImagePath = None,
                disableImagePath = None,
                soundPath = None,
                runFunction = None
                ):
        self.x = x
        self.y = y
        self.size = size
        self.text = text
        self.imagePath = imagePath
        self.disableImagePath = disableImagePath
        self.hoverImagePath = hoverImagePath
        self.enable = enable
        self.checkEnabled()
        self.hoverImage = self.image
        self.disableImage = self.image
        self.runFunction = runFunction
        

        if disableImagePath:
            self.disableImage = pg.transform.scale(pg.image.load(self.disableImagePath), self.size).convert_alpha()

        if hoverImagePath:
            self.hoverImage = pg.transform.scale(pg.image.load(self.hoverImagePath), self.size).convert_alpha()  

        self.rect = self.image.get_rect(center = (x, y))

        if soundPath:
            self.sound = pg.mixer.Sound(soundPath)

        self.isHovered = False
        self.isClicked = False


    def onClick(self):
        if self.runFunction:
            self.runFunction()

    def checkEnabled(self):
        self.image = pg.transform.scale(pg.image.load(self.imagePath if self.enable else self.disableImagePath), self.size).convert_alpha()


    def checkHover (self, mousePos):
        if self.enable:
            self.isHovered = self.rect.collidepoint(mousePos)


    def handleEvent(self, event):
        if self.enable:
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and self.isHovered:
                if self.sound:
                    self.sound.play()
                # if self.attribute:
                    self.onClick()




    def update(self, screen):
        currentImage = self.hoverImage if self.isHovered else self.image

        screen.blit(currentImage, self.rect)

        if self.text:
            font = pg.font.SysFont(None, 36)
            textSurface = font.render(self.text, True, 'white' if self.enable else 'dimgray')
            textRect = textSurface.get_rect(center = self.rect.center)
            screen.blit(textSurface, textRect)

        self.checkHover(pg.mouse.get_pos())