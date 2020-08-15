import numpy as np
from PIL import Image


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])

    def rotate_at_90(self):
        self.__exchange_triangles()
        self.__exchange_columns()

    def mirror(self):
        self.__exchange_columns()

    def __exchange_triangles(self):
        for i in range(len(self.matrix)):
            row = self.matrix[i]
            for j in range(len(row)):
                if j > i:
                    temp = self.matrix[i][j]
                    self.matrix[i][j] = self.matrix[j][i]
                    self.matrix[j][i] = temp

    def __exchange_columns(self):
        for i in range(len(self.matrix)):
            row = self.matrix[i]
            for j in range(len(row) // 2):
                temp = self.matrix[i][j]
                self.matrix[i][j] = self.matrix[i][len(row) - 1 - j]
                self.matrix[i][len(row) - 1 - j] = temp

    def __str__(self):
        result_string = ''

        for i in range(self.n_rows):
            is_first_elem = True
            row_string = '|'
            for j in range(self.n_cols):
                if is_first_elem:
                    row_string += str(self.matrix[i][j])
                    is_first_elem = False
                else:
                    row_string += ' ' + str(self.matrix[i][j])
            row_string += '|\n'
            result_string += row_string

        return result_string[:-1]

    def __eq__(self, other):
        return all([row1 == row2 for row1, row2 in zip(self.matrix, other.matrix)])


# Image processing
class ColorChannel:
    def __init__(self, one_channel_np_image):
        self.matrix = Matrix(one_channel_np_image)

    def rotate_at_90(self):
        self.matrix.rotate_at_90()

    def mirror(self):
        self.matrix.mirror()


class RedColorChannel(ColorChannel):
    pass


class GreenColorChannel(ColorChannel):
    pass


class BlueColorChannel(ColorChannel):
    pass


class OwnImage:
    def __init__(self, image_path):
        multichannel_np_image = np.array(Image.open(image_path))
        self.red_color_channel = \
            RedColorChannel(multichannel_np_image[:, :, 0])
        self.green_color_channel = \
            GreenColorChannel(multichannel_np_image[:, :, 1])
        self.blue_color_channel = \
            BlueColorChannel(multichannel_np_image[:, :, 2])

    def rotate_at_90(self):
        self.red_color_channel.rotate_at_90()
        self.green_color_channel.rotate_at_90()
        self.blue_color_channel.rotate_at_90()

    def mirror(self):
        self.red_color_channel.mirror()
        self.green_color_channel.mirror()
        self.blue_color_channel.mirror()

    def save(self, new_name):
        new_image = self.get_image()
        new_image.save(new_name)

    def get_image(self):
        return Image.fromarray(self._get_multichannel_array())

    def _get_multichannel_array(self):
        return np.dstack((
            self.red_color_channel.matrix.matrix,
            self.green_color_channel.matrix.matrix,
            self.blue_color_channel.matrix.matrix,
        ))
