import pygame as pg
from dataclasses import dataclass
from pygame.display import set_mode, set_caption, set_icon, get_desktop_sizes
from pygame.locals import RESIZABLE, FULLSCREEN
from  pygame.image import load

pg.init()

@dataclass
class ScreenGame:
    size: tuple = (0, 0)
    color: str | tuple[int, int, int] = 'SteelBlue'
    caption: str = 'Game'
    icon: str = ''
    isResizable: bool = False
    isFullScreen: bool = False

    def __post_init__(self):
        if self.isResizable:
            self.win = set_mode(self.size, RESIZABLE)
        elif self.isFullScreen:
            self.currentScreenResolution = get_desktop_sizes()[0]
            print(self.currentScreenResolution)
            self.win = set_mode(self.currentScreenResolution, FULLSCREEN)
        else:
            self.win = set_mode(self.size)
        if self.caption:
            self.caption = set_caption(self.caption)
        if self.icon:
            self.icon = set_icon(load(self.icon))
