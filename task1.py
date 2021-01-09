# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class MatrixFormatException(Exception):
    message: str

    def __init__(self, message):
        self.message = message


class Matrix:
    matrix: list

    def __init__(self, data: list):
        self._validate(data)
        self.matrix = data

    def __str__(self):
        result = ''
        for item in self.matrix:
            result += f"{item}\n"
        return result

    def __add__(self, other):
        if type(other) is not Matrix:
            raise MatrixFormatException('Error. Unknown sum operand')

        if len(self.matrix) != len(other.matrix) or len(self.matrix) != 0 and len(self.matrix[0]) != len(
                other.matrix[0]):
            raise MatrixFormatException('Error. Matrix sizes are not equals')

        data = [
            [v + other.matrix[row][column] for column, v in enumerate(item)]
            for row, item in enumerate(self.matrix)
        ]

        return Matrix(data)

    @staticmethod
    def _validate(data: list):
        max_len = -1
        for row, item in enumerate(data):
            if type(item) is not list:
                raise MatrixFormatException(f'Error: row {row} is not list')
            if max_len == -1:
                max_len = len(item)
            if max_len != len(item):
                raise MatrixFormatException(f'Error: columns count must be constant (row {row} length = {len(item)})')
            for column, cell in enumerate(item):
                try:
                    data[row][column] = float(cell)
                except ValueError:
                    raise MatrixFormatException(f'Error: cell (row: {row}, column:{column}) is not number: `{cell}`')


if __name__ == '__main__':
    m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = Matrix([[3, 2, 1], [6, 5, 4], [9, 8, 7]])

    print(f'm1:\n{m1}')
    print(f'm2:\n{m2}')

    print(f'm1 + m2:\n{m1 + m2}')
