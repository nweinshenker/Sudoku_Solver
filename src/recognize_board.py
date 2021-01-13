import cv2
import numpy as np
import os


def normalize_path():
    try:
        cur_dir = os.getcwd()
        file_path = os.path.normpath("".join([cur_dir, "/../test_images/sudoku-puzzle-1.png"]))
        print(os.path.isfile(file_path))
        if not os.path.isfile(file_path):
            print('Invalid Image path'.format(str(file_path)))
        
        return file_path
    except OSError as err:
        print('OS Error occurred {}'.format(err))

def display_image():
    path = normalize_path()
    img = cv2.imread(path)
    print(type(img))

if __name__ == '__main__':
    display_image()