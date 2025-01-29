import pygame as pg
from Game.source import soundsSection

SOUNDS = soundsSection()

class SoundGame:
    def __init__(self):
        self.background = None
        self.backgroundPlay = True
        self.playerShotsPlay = True
        self.enemyShotsPlay = True
        self.explosionPlay = True
        self.explosionBulletPlay = True

    def playBackground(self):
        if SOUNDS['playBackground']:
            if self.backgroundPlay:
                self.background = pg.mixer.music.load(SOUNDS['playBackground'])
                pg.mixer.music.set_volume(SOUNDS['playBackgroundVolume'])
                pg.mixer.music.play(-1)

    def playerShots(self):
        if SOUNDS['playerShots']:
            if self.playerShotsPlay:
                channel0 = pg.mixer.Channel(0)
                channel0.set_volume(SOUNDS['playerShotsVolume'])
                self.playerShotSound = pg.mixer.Sound(SOUNDS['playerShots'])
                channel0.play(self.playerShotSound)


    def enemyShots(self):
        if SOUNDS['enemyShots']:
            if self.enemyShotsPlay:
                channel1 = pg.mixer.Channel(1)
                channel1.set_volume(SOUNDS['enemyShotsVolume'])
                self.enemyShotSound = pg.mixer.Sound(SOUNDS['enemyShots'])
                channel1.play(self.enemyShotSound)

    def playExplosion(self):
        if SOUNDS['playExplosion']:
            if self.explosionPlay:
                channel2 = pg.mixer.Channel(2)
                channel2.set_volume(SOUNDS['playExplosionVolume'])
                self.explosionSound = pg.mixer.Sound(SOUNDS['playExplosion'])
                channel2.play(self.explosionSound)
    
    def playExplosionBullet(self):
        if SOUNDS['playExplosionBullet']:
            if self.explosionBulletPlay:
                channel3 = pg.mixer.Channel(3)
                channel3.set_volume(SOUNDS['playExplosionBulletVolume'])
                self.explosionSound = pg.mixer.Sound(SOUNDS['playExplosionBullet'])
                channel3.play(self.explosionSound)


soundGame = SoundGame()