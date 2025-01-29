import pygame as pg
from pygame.locals import *
from pygame.image import load
from pygame.transform import scale, flip

from dataclasses import dataclass, field, InitVar

from icecream import ic

pg.init()

@dataclass
class ButtonImage:
    pos: tuple = (0, 0)
    size: tuple = (0, 0)

    text: str = None
    textColor: str | tuple[int, int, int] = 'white'
    font: InitVar[str] = None
    font_size: int = 26
    disabledColorText: str | tuple[int, int, int] = 'grey'

    image: InitVar[str] = None
    hoveredColor: tuple[int, int, int] = (128, 128, 128)
    disabledColor: tuple[int, int, int] = (49, 79, 79)
    hoveredAlpha: int = 128
    disabledAlpha: int = 128

    flipVertical: bool = False
    flipHorizontal: bool = False
    onEnabled: bool = True
    isHovered: bool = False
    isClicked: bool = False

    onClickReference: object = None
    referenceArgs: tuple = field(default_factory = tuple)
    referenceKwargs: dict = field(default_factory = dict)

    def __post_init__(self, font: str, image: str):
        self.image = flip(scale(load(image).convert_alpha(), self.size), self.flipHorizontal, self.flipVertical)
        self.rect = self.image.get_rect(x = self.pos[0], y = self.pos[1])

        self.hoveredColor += (self.hoveredAlpha,)
        self.disabledColor += (self.disabledAlpha,)

        self.shadingImage = self.image.copy()
        self.shadingImage.fill(self.hoveredColor, special_flags = BLEND_RGBA_MULT)
        self.disabledImage = self.image.copy()
        self.disabledImage.fill(self.disabledColor, special_flags = BLEND_RGBA_MULT)

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
        if self.isClicked or not self.onEnabled:
            surface.blit(self.disabledImage, self.rect)
        elif self.isHovered:
            surface.blit(self.image, self.rect)
        else:
            surface.blit(self.shadingImage, self.rect)

        if self.text:
            if self.onEnabled:
                textSurface = self.font.render(self.text, True, self.textColor)
            else:
                textSurface = self.font.render(self.text, True, self.disabledColorText)
                textSurface.fill(self.disabledColorText, special_flags = pg.BLEND_RGBA_MULT)
            textRect = textSurface.get_rect(center = self.rect.center)
            
            surface.blit(textSurface, textRect)