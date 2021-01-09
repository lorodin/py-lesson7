# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству
# ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
#   сложение (add()),
#   вычитание (sub()),
#   умножение (mul()),
#   деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
# (с округлением до целого) деление клеток, соответственно.
#
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
#
# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
#
# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class CellException(Exception):
    message: str

    def __init__(self, message: str):
        self.message = message


class Cell:
    size: int

    def __init__(self, size: int):
        if size < 1:
            raise CellException("Error. Cell size must be more 0")
        self.size = size

    def __add__(self, other):
        return Cell(self.size + other.size)

    def __sub__(self, other):
        return Cell(self.size - other.size)

    def __mul__(self, other):
        return Cell(self.size * other.size)

    def __truediv__(self, other):
        return Cell(self.size // other.size)

    @staticmethod
    def make_order(cell, cols: int):
        row = '*' * cols
        rows_count = int((cell.size - cell.size % cols) / cols)
        rows = [row for i in range(rows_count)]
        if cell.size % cols != 0:
            rows.append('*' * (cell.size % cols))
        return '\n'.join(rows)


if __name__ == '__main__':
    cell1 = Cell(10)
    cell2 = Cell(5)
    print('Example sum Cell(10) + Cell(5)')
    print(Cell.make_order(cell1 + cell2, 5))

    print('\nExample sub Cell(10) - Cell(5)')
    print(Cell.make_order(cell1 - cell2, 5))

    print('\nExample mull Cell(7) * Cell(4)')
    print(Cell.make_order(Cell(7) * Cell(4), 5))

    print('\nExample div Cell(10) / Cell(5)')
    print(Cell.make_order(cell1 / cell2, 5))
