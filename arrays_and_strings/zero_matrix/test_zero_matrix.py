import unittest
import zero_matrix


class ZeroMatrixTestCase(unittest.TestCase):
    def test_one_char_matrix(self):
        one_char_matrices = [
            zero_matrix.Matrix([[1]]),
            zero_matrix.Matrix([[0]]),
            zero_matrix.Matrix([[11]]),
            zero_matrix.Matrix([[32]]),
        ]
        zero_one_char_matrices = [
            zero_matrix.Matrix([[1]]),
            zero_matrix.Matrix([[0]]),
            zero_matrix.Matrix([[11]]),
            zero_matrix.Matrix([[32]]),
        ]
        self.matrices_test(one_char_matrices, zero_one_char_matrices)

    def test_two_char_matrix(self):
        two_char_matrices = [
            zero_matrix.Matrix([
                [1, 2],
                [3, 4],
            ]),
            zero_matrix.Matrix([
                [1, 0],
                [3, 4],
            ]),
            zero_matrix.Matrix([
                [0, 2],
                [3, 4],
            ]),
            zero_matrix.Matrix([
                [1, 2],
                [0, 4],
            ]),
            zero_matrix.Matrix([
                [1, 2],
                [3, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0],
                [3, 4],
            ]),
            zero_matrix.Matrix([
                [0, 2],
                [0, 4],
            ]),
            zero_matrix.Matrix([
                [0, 2],
                [3, 0],
            ]),
            zero_matrix.Matrix([
                [1, 0],
                [3, 0],
            ]),
            zero_matrix.Matrix([
                [1, 0],
                [0, 4],
            ]),
            zero_matrix.Matrix([
                [1, 2],
                [0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0],
                [0, 4],
            ]),
            zero_matrix.Matrix([
                [0, 0],
                [3, 0],
            ]),
            zero_matrix.Matrix([
                [0, 2],
                [0, 0],
            ]),
            zero_matrix.Matrix([
                [1, 0],
                [0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0],
                [0, 0],
            ]),
        ]
        zero_two_char_matrices = [
            zero_matrix.Matrix([
                [1, 2],
                [3, 4],
            ]),
            zero_matrix.Matrix([
                [0, 0],
                [3, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0],
                [0, 4],
            ]),
            zero_matrix.Matrix([
                [0, 2],
                [0, 0],
            ]),
            zero_matrix.Matrix([
                [1, 0],
                [0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0],
                [0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0],
                [0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0],
                [0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0],
                [0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0],
                [0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0],
                [0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0],
                [0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0],
                [0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0],
                [0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0],
                [0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0],
                [0, 0],
            ]),
        ]
        self.matrices_test(two_char_matrices, zero_two_char_matrices)

    def test_three_char_matrix(self):
        three_char_matrices = [
            zero_matrix.Matrix([
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [0, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 0, 3],
                [4, 5, 6],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 2, 0],
                [4, 5, 6],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 2, 3],
                [0, 5, 6],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 2, 3],
                [4, 0, 6],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 2, 3],
                [4, 5, 0],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 2, 3],
                [4, 5, 6],
                [0, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 2, 3],
                [4, 5, 6],
                [7, 0, 9],
            ]),
            zero_matrix.Matrix([
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 3],
                [4, 5, 6],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [0, 2, 0],
                [4, 5, 6],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [0, 2, 3],
                [0, 5, 6],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [0, 2, 3],
                [4, 0, 6],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [0, 2, 3],
                [4, 5, 0],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [0, 2, 3],
                [4, 5, 6],
                [0, 8, 9],
            ]),
            zero_matrix.Matrix([
                [0, 2, 3],
                [4, 5, 6],
                [7, 0, 9],
            ]),
            zero_matrix.Matrix([
                [0, 2, 3],
                [4, 5, 6],
                [7, 8, 0],
            ]),
            zero_matrix.Matrix([
                [1, 0, 0],
                [4, 5, 6],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 0, 3],
                [0, 5, 6],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 0, 3],
                [4, 0, 6],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 0, 3],
                [4, 5, 0],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 0, 3],
                [4, 5, 6],
                [0, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 0, 3],
                [4, 5, 6],
                [7, 0, 9],
            ]),
            zero_matrix.Matrix([
                [1, 0, 3],
                [4, 5, 6],
                [7, 8, 0],
            ]),
            zero_matrix.Matrix([
                [1, 2, 0],
                [0, 5, 6],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 2, 0],
                [4, 0, 6],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 2, 0],
                [4, 5, 0],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 2, 0],
                [4, 5, 6],
                [0, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 2, 0],
                [4, 5, 6],
                [7, 0, 9],
            ]),
            zero_matrix.Matrix([
                [1, 2, 0],
                [4, 5, 6],
                [7, 8, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [4, 5, 6],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [0, 2, 3],
                [4, 0, 6],
                [7, 8, 0],
            ]),
            zero_matrix.Matrix([
                [1, 2, 0],
                [4, 0, 6],
                [0, 8, 9],
            ]),
            zero_matrix.Matrix([
                [0, 2, 3],
                [0, 5, 6],
                [0, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 0, 3],
                [4, 0, 0],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 2, 3],
                [0, 0, 6],
                [7, 0, 9],
            ]),
        ]
        zero_three_char_matrices = [
            zero_matrix.Matrix([
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 5, 6],
                [0, 8, 9],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [4, 0, 6],
                [7, 0, 9],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [4, 5, 0],
                [7, 8, 0],
            ]),
            zero_matrix.Matrix([
                [0, 2, 3],
                [0, 0, 0],
                [0, 8, 9],
            ]),
            zero_matrix.Matrix([
                [1, 0, 3],
                [0, 0, 0],
                [7, 0, 9],
            ]),
            zero_matrix.Matrix([
                [1, 2, 0],
                [0, 0, 0],
                [7, 8, 0],
            ]),
            zero_matrix.Matrix([
                [0, 2, 3],
                [0, 5, 6],
                [0, 0, 0],
            ]),
            zero_matrix.Matrix([
                [1, 0, 3],
                [4, 0, 6],
                [0, 0, 0],
            ]),
            zero_matrix.Matrix([
                [1, 2, 0],
                [4, 5, 0],
                [0, 0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 0, 6],
                [0, 0, 9],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 5, 0],
                [0, 8, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 0, 0],
                [0, 8, 9],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 9],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 0, 0],
                [0, 8, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 5, 6],
                [0, 0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 0, 6],
                [0, 0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 5, 0],
                [0, 0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [4, 0, 0],
                [7, 0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 9],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 0, 0],
                [7, 0, 9],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 0, 0],
                [7, 0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 0, 6],
                [0, 0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [4, 0, 6],
                [0, 0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [4, 0, 0],
                [0, 0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 0, 0],
                [0, 8, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 0, 0],
                [7, 0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 0, 0],
                [7, 8, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 5, 0],
                [0, 0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [4, 0, 0],
                [0, 0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [4, 5, 0],
                [0, 0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 0],
                [0, 0, 0],
                [7, 0, 0],
            ]),
            zero_matrix.Matrix([
                [0, 0, 3],
                [0, 0, 0],
                [0, 0, 0],
            ]),
        ]
        self.matrices_test(three_char_matrices, zero_three_char_matrices)

    def matrices_test(self, matrices, zero_matrices):
        for i, matrices in enumerate(zip(matrices, zero_matrices)):
            with self.subTest(i=i):
                matrix, z_matrix = matrices
                matrix.zero()
                self.assertEqual(
                    matrix,
                    z_matrix
                )
