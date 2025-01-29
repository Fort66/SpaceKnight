import pygame as pg

# from MenuUI.MenuScreens.soundMenu import setSound

class Checkbox:
    def __init__(self, 
                 x, 
                 y, 
                 width, 
                 height, 
                 color, 
                 text,
                 soundPath = None,
                 slider = None,
                 font = None,
                 chanelNum = None,
                 function = None):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.font = font
        self.checked = False
        self.playSound = False
        self.text = text
        self.soundPath = soundPath
        self.slider = slider
        self.font = pg.font.SysFont("Arial", 18)
        self.chanelNum = chanelNum
        self.function = function

    # def onClick(self, volumeValue):
        # if self.checked == True and not self.playSound:
        #     self.playSound = True
        #     if not self.chanelNum:
        #         pg.mixer.music.load(self.soundPath)
        #         pg.mixer.music.set_volume(volumeValue)
        #         pg.mixer.music.play(-1)
        #     else:
        #         pg.mixer.Channel(self.chanelNum).set_volume(volumeValue)
        #         pg.mixer.Channel(self.chanelNum).play(pg.mixer.Sound(self.soundPath))
        # elif self.checked == False:
        #     self.playSound = False
        #     pg.mixer.music.stop()
        #     if self.chanelNum:
        #         pg.mixer.Channel(self.chanelNum).stop()
            
    def onClick(self, volumeValue):
        if self.checked and not self.playSound:
            self.playSound = True
            self.function()
        elif self.checked == False:
            self.playSound = False
            pg.mixer.music.pause()
            self.playSound = False

# channel0 = pg.mixer.Channel(0)
#                 channel0.set_volume(SOUNDS['playerShotsVolume'])
#                 self.playerShotSound = pg.mixer.Sound(SOUNDS['playerShots'])
#                 channel0.play(self.playerShotSound)


    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        if self.checked:
            pg.draw.line(screen, ('black'), (self.x + 5, self.y + 5), (self.x + self.width - 5, self.y + self.height - 5), 5)
            pg.draw.line(screen, ('black'), (self.x + 5, self.y + self.height - 5), (self.x + self.width - 5, self.y + 5), 5)


    def handleEvent(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.x < event.pos[0] < self.x + self.width and self.y < event.pos[1] < self.y + self.height:
                self.checked = not self.checked


    def update(self, screen):
        # self.onClick(self.slider.getValue())
        self.draw(screen)
        self.onClick(self.slider.getValue())
        text = self.font.render(self.text, True, ('yellow'))
        screen.blit(text, (self.x + self.width + 10, self.y))

# # Demonstration
# pygame.init()
# screen = pygame.display.set_mode((640, 480))

# font = pygame.font.SysFont("Arial", 24)

# checkbox = Checkbox(100, 100, 20, 20, (255, 255, 255), font, text = "Checkbox")

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         checkbox.handle_event(event)

#     screen.fill((0, 0, 0))
#     # checkbox.draw(screen)
#     # text = font.render("Checkbox", True, (255, 255, 255))
#     # screen.blit(text, (checkbox.x + checkbox.width + 10, checkbox.y))
#     checkbox.update(screen)
#     pygame.display.flip()
#     pygame.time.Clock().tick(60)

# pygame.quit()