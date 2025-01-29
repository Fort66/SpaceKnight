import pygame as pg
from pygame.font import SysFont, Fonts
from dataclasses import dataclass

@dataclass
class Fonts:
    arial: object = SysFont('Arial', 36)
    roboto: object = SysFont('Roboto', 55)