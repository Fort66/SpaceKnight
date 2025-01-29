import pygame as pg

class Switch:
    def __init__(self, 
                 x, 
                 y, 
                 width, 
                 height, 
                 colorOn, 
                 colorOff, 
                 colorSlider, 
                 font, 
                 fontSize, 
                 fontBold,
                 soundPath = None,
                 slider = None):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colorOn = colorOn
        self.colorOff = colorOff
        self.colorSlider = colorSlider
        self.isOn = False
        self.font = pg.font.SysFont(font, fontSize, fontBold)
        self.soundPath = soundPath
        self.slider = slider


    def onClick(self, volumeValue):
        if self.isOn:
            if self.soundPath:
                pg.mixer.music.load(self.soundPath)
                pg.mixer.music.set_volume(volumeValue)
                pg.mixer.music.play(-1)
            else:
                pg.mixer.music.stop()
                

    def draw(self, screen):
        if self.isOn:
            pg.draw.rect(screen, self.colorOn, (self.x, self.y, self.width, self.height))
            pg.draw.rect(screen, self.colorSlider, (self.x + self.width - 20, self.y, 20, self.height))
            text = self.font.render("", True, ('white'))
        else:
            pg.draw.rect(screen, self.colorOff, (self.x, self.y, self.width, self.height))
            pg.draw.rect(screen, self.colorSlider, (self.x, self.y, 20, self.height))
            text = self.font.render("Тест", True, ('white'))

        text_rect = text.get_rect(center = (self.x + self.width / 2, self.y + self.height / 2))
        screen.blit(text, text_rect)
        
    def toggle(self):
        self.isOn = not self.isOn

    def handleEvent(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.x < event.pos[0] < self.x + self.width and self.y < event.pos[1] < self.y + self.height:
                self.toggle()

    def update(self, screen):
        self.draw(screen)
        self.onClick(self.slider.getValue())
    
# # Demonstration
# pygame.init()
# screen = pygame.display.set_mode((640, 480))

# # font = pygame.font.SysFont("Arial", 24, bold=True)

# switch = Switch(x = 100, 
#                 y = 100, 
#                 width = 60, 
#                 height = 20, 
#                 color_on = ('green'), 
#                 color_off = ('red'), 
#                 color_slider = ('grey'), 
#                 font = 'Arial', 
#                 fontSize = 24, 
#                 fontBold = True)

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         switch.handle_event(event)

#     screen.fill((0, 0, 0))
#     switch.update(screen)
#     pygame.display.flip()
#     pygame.time.Clock().tick(60)

# pygame.quit()