'''
Класс TextGroup представляет собой группу текстовых объектов.
Класс имеет один атрибут:
group: список текстовых объектов, инициализируемый по умолчанию как пустой список.
Класс имеет один метод:
update: перебирает каждый текстовый объект в списке group и вызывает его метод update.
'''

from dataclasses import dataclass, field

@dataclass
class TextGroup:
    group: list = field(default_factory = list)
    
    def update(self):
        for obj in self.group:
            obj.update()