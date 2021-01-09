# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры:
#   размер (для пальто)
#   рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod
from random import randint


class Clothes(ABC):
    name: str

    def __init__(self, name: str):
        self.name = name

    @property
    @abstractmethod
    def cloth(self):
        pass

    def __str__(self):
        return f'`Type: {self.name}`. Amount of cloth: {self.cloth}'


class Coat(Clothes):
    _v: float

    def __init__(self, v):
        super().__init__('coat')
        self._v = v

    @property
    def cloth(self):
        return self._v / 6.5 + 0.5


class Costume(Clothes):
    _h: float

    def __init__(self, h):
        super().__init__('costume')
        self._h = h

    @property
    def cloth(self):
        return 2 * self._h + 0.3


class RandomFactory:
    @staticmethod
    def get_random_clothes():
        clothes_type = randint(0, 1)
        clothes_size = randint(1, 12)
        return Costume(clothes_size) if clothes_type == 0 else Coat(clothes_size)


if __name__ == '__main__':
    clothes = [RandomFactory.get_random_clothes() for i in range(2)]

    for cloth in clothes:
        print(cloth)

    total_cloth = sum(c.cloth for c in clothes)

    print(total_cloth)
