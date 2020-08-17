class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n_rows = len(self.matrix)
        self.n_cols = len(self.matrix[0])

    def zero(self):
        zero_positions = self.__get_zero_positions()
        zero_rows, zero_cols = self.__get_zero_rows_and_cols(zero_positions)
        for zero_row in zero_rows:
            self.__zero_matrix_row(zero_row)
        for zero_col in zero_cols:
            self.__zero_matrix_col(zero_col)

    def __get_zero_positions(self):
        zero_positions = []
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.matrix[i][j] == 0:
                    zero_positions.append((i, j))
        return zero_positions

    @staticmethod
    def __get_zero_rows_and_cols(zero_positions):
        unique_rows = set()
        unique_cols = set()
        for zero_position in zero_positions:
            unique_rows.add(zero_position[0])
            unique_cols.add(zero_position[1])
        return unique_rows, unique_cols

    def __zero_matrix_row(self, row):
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if i == row:
                    self.matrix[i][j] = 0

    def __zero_matrix_col(self, col):
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if j == col:
                    self.matrix[i][j] = 0

    def __str__(self):
        result = ''
        for i in range(self.n_rows):
            result += '|'
            is_first = True
            for j in range(self.n_cols):
                if is_first:
                    result += str(self.matrix[i][j])
                    is_first = False
                else:
                    result += ' ' + str(self.matrix[i][j])
            result += '|\n'
        return result

    def __eq__(self, other):
        for rows in zip(self.matrix, other.matrix):
            row1, row2 = rows
            if row1 != row2:
                return False
        return True
