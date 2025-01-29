import pygame as pg

class Slider:
    def __init__(self, 
                 x, 
                 y, 
                 width, 
                 height, 
                 minValue, 
                 maxValue, 
                 value, 
                 step,
                 text,):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.minValue = minValue
        self.maxValue = maxValue
        self.value = value
        self.step = step
        self.sliderWidth = 20
        self.sliderHeight = 20
        self.sliderX = x + (value - minValue) / (maxValue - minValue) * (width - self.sliderWidth)
        self.sliderY = y + height // 2 - self.sliderHeight // 2
        self.dragging = False

        self.text = text
        self.font = pg.font.SysFont('Arial', 24)


    def draw(self, screen):
        pg.draw.rect(screen, ('white'), (self.x, self.y, self.width, self.height), 2)
        pg.draw.rect(screen, ('darkblue'), (self.sliderX, self.sliderY, self.sliderWidth, self.sliderHeight))

    def handleEvent(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.x < event.pos[0] < self.x + self.width and self.y < event.pos[1] < self.y + self.height:
                self.dragging = True
                self.sliderX = max(self.x, min(event.pos[0] - self.sliderWidth // 2, self.x + self.width - self.sliderWidth))
                self.value = self.minValue + (self.sliderX - self.x) / (self.width - self.sliderWidth) * (self.maxValue - self.minValue)
                self.value = round(self.value / self.step) * self.step
        elif event.type == pg.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pg.MOUSEMOTION and self.dragging:
            self.sliderX = max(self.x, min(event.pos[0] - self.sliderWidth // 2, self.x + self.width - self.sliderWidth))
            self.value = self.minValue + (self.sliderX - self.x) / (self.width - self.sliderWidth) * (self.maxValue - self.minValue)
            self.value = round(self.value / self.step) * self.step

    def getValue(self):
        return self.value

    
    def update(self, screen):
        self.draw(screen)
        value_text = self.font.render(f"{self.text}: {self.getValue():.2f}", True, ('yellow'))
        screen.blit(value_text, (self.x, self.y + 30))

