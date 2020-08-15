from rotate_matrix import OwnImage
import os
import random


def main():
    images = get_images()
    for image in images:
        own_image = OwnImage(image)
        random_rotations = random.randint(1, 3)
        print('Image: {}. Rotations: {}'.format(image, random_rotations))
        for rotation in range(random_rotations):
            own_image.rotate_at_90()
        new_name = image.split('.')[0] + '_rotate.png'
        own_image.save(new_name)

    for image in images:
        own_image = OwnImage(image)
        own_image.mirror()
        new_name = image.split('.')[0] + '_mirror.png'
        own_image.save(new_name)


def get_images():
    return filter(lambda file: file.split('.')[-1] == 'jpg', os.listdir('.'))


if __name__ == '__main__':
    main()
