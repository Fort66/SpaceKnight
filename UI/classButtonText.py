import pygame as pg
from pygame.locals import *
from pygame.image import load
from pygame.transform import scale, flip

from dataclasses import dataclass, field, InitVar

pg.init()

@dataclass
class ButtonText:
    pos: tuple = (0, 0)
    size: tuple = (0, 0)

    text: str = None
    font: InitVar[str] = None
    font_size: int = 26

    disabledColor: str | tuple[int, int, int] = 'grey'
    bgColor: str | tuple[int, int, int] = (144, 184, 218)
    textColor: str | tuple[int, int, int] = (255, 255, 255)
    hoverColor: str | tuple[int, int, int] = (23, 74, 117)
    clickColor: str | tuple[int, int, int] = (73, 107, 135)

    rounding: int = 0

    onEnabled: bool = True
    isHovered: bool = False
    isClicked: bool = False

    onClickReference: object = None
    referenceArgs: tuple = field(default_factory = tuple)
    referenceKwargs: dict = field(default_factory = dict)

    def __post_init__(self, font: str):
        self.rect = pg.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.font = pg.font.Font(font, self.font_size) if font else pg.font.SysFont('Arial', self.font_size)

    def handleEvent(self, event):
        if self.onEnabled:
            if event.type == MOUSEMOTION:
                self.isHovered = self.rect.collidepoint(event.pos)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and self.isHovered:
                    self.isClicked = True
                    if self.onClickReference:
                        self.onClickReference(*self.referenceArgs, **self.referenceKwargs)
            if event.type == MOUSEBUTTONUP:
                self.isClicked = False

    def update(self, surface):
        if self.isClicked:
            self.color = self.clickColor
        elif self.isHovered:
            self.color = self.hoverColor
        else:
            self.color = self.bgColor

        self.roundedRect = pg.draw.rect(surface, self.color, self.rect, border_radius = self.rounding)

        if self.text:
            if self.onEnabled:
                textSurface = self.font.render(self.text, True, self.textColor)
            else:
                textSurface = self.font.render(self.text, True, self.disabledColor)
                textSurface.fill(self.disabledColor, special_flags = pg.BLEND_RGBA_MULT)
            textRect = textSurface.get_rect(center = self.roundedRect.center)
            
            surface.blit(textSurface, textRect)
