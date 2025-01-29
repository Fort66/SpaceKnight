import pygame as pg
from pygame.locals import *

from dataclasses import dataclass, field


@dataclass
class BackgroundScreen:
    imageBackground: str = field(default = '')
    screen: object = field(default = None)
    speed: int = field(default = 0)
    long: int = 1
    transformation: bool = False
    scrolling: bool = False
    
    
    def __post_init__(self):
        self.scrWidht = self.screen.get_width()
        self.scrHeight = self.screen.get_height()
        
        self.bg = pg.transform.scale(pg.image.load(self.imageBackground).convert(), (self.scrWidht, self.scrHeight))
        
        self.bgList = [self.bg for _ in range(3)]
        
        self.bgRectLeft = self.bgList[0].get_rect()
        self.bgRectCenter = self.bgList[1].get_rect()
        self.bgRectRight = self.bgList[2].get_rect()
        
    
    def eventKey(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_RIGHT]:
            self.scroll('right')
            
        if keys[pg.K_LEFT]:
            self.scroll('left')

    
    def scroll(self, direction):
        if direction =='right':
            if self.bgRectCenter.x <= - self.scrWidht:
                self.bgRectCenter.x = 0
            self.bgRectCenter.x -= self.speed
            
        if direction =='left':
            if self.bgRectCenter.x >= self.scrWidht:
                self.bgRectCenter.x = 0
            self.bgRectCenter.x += self.speed

        self.bgRectLeft.x = self.bgRectCenter.x - (self.bgRectCenter[2] - self.speed)
        self.bgRectRight.x = self.bgRectCenter.x + (self.bgRectCenter[2] - self.speed)

    def blitBG(self):
        self.screen.blit(self.bgList[0], self.bgRectLeft)
        self.screen.blit(self.bgList[1], self.bgRectCenter)
        self.screen.blit(self.bgList[2], self.bgRectRight)