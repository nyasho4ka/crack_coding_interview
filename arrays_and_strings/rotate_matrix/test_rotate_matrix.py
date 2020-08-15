import unittest
import rotate_matrix


class RotateMatrixTestCase(unittest.TestCase):
    def setUp(self):
        scalar_matrix = rotate_matrix.Matrix([
            [1]
        ])
        two_by_two_matrix = rotate_matrix.Matrix([
            [1, 2],
            [3, 4]
        ])
        three_by_three_matrix = rotate_matrix.Matrix([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        four_by_four_matrix = rotate_matrix.Matrix([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ])
        self.matrices = [
            scalar_matrix,
            two_by_two_matrix,
            three_by_three_matrix,
            four_by_four_matrix
        ]

        rotate_scalar = rotate_matrix.Matrix([
            [1]
        ])
        rotate_two_by_two = rotate_matrix.Matrix([
            [3, 1],
            [4, 2],
        ])
        rotate_three_by_three = rotate_matrix.Matrix([
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3],
        ])
        rotate_four_by_four = rotate_matrix.Matrix([
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4],
        ])
        self.rotate_matrices = [
            rotate_scalar,
            rotate_two_by_two,
            rotate_three_by_three,
            rotate_four_by_four
        ]

        mirror_scalar = rotate_matrix.Matrix([
            [1]
        ])
        mirror_two_by_two = rotate_matrix.Matrix([
            [2, 1],
            [4, 3],
        ])
        mirror_three_by_three = rotate_matrix.Matrix([
            [3, 2, 1],
            [6, 5, 4],
            [9, 8, 7],
        ])
        mirror_four_by_four = rotate_matrix.Matrix([
            [4, 3, 2, 1],
            [8, 7, 6, 5],
            [12, 11, 10, 9],
            [16, 15, 14, 13],
        ])
        self.mirror_matrices = [
            mirror_scalar,
            mirror_two_by_two,
            mirror_three_by_three,
            mirror_four_by_four,
        ]

    def test_rotate_at_90(self):
        for i, matrices in enumerate(zip(self.matrices, self.rotate_matrices)):
            with self.subTest(i=i):
                matrix, rotate_matrix = matrices
                matrix.rotate_at_90()
                self.assertEqual(
                    matrix,
                    rotate_matrix
                )

    def test_mirror(self):
        for i, matrices in enumerate(zip(self.matrices, self.mirror_matrices)):
            with self.subTest(i=i):
                matrix, mirror_matrix = matrices
                matrix.mirror()
                self.assertEqual(
                    matrix,
                    mirror_matrix
                )
