'''
Этот файл для создания объектов (экземпляров классов) для того, чтобы максимально избежать циклического импорта
'''

from UI.classScreenGame import ScreenGame


# экземпляр класса ScreenGame (окно игры)
screen = ScreenGame(size = (1280, 768), 
                    caption = 'Game',
                    color = 'SteelBlue',
                    icon = 'images/icon.jpg', # пример иконки
                    isResizable = False, # изменяемый размер True/False
                    isFullScreen = False) #полноэкранный True/False