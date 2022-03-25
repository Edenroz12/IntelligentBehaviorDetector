from ImageProcessing import *
from ImageEmotionsAnalyzer import *


def main():
    a = '0'
    while a not in ['1', '2']:
        a = input("enter 1 if you want take picture or 2 if you want upload a picture: ")
    if a == '1':
        test_image_one = take_picture()
    else:  # a == '2'
        path = get_path_with_dialog()
        test_image_one = upload_picture(path)
    start_analyzing(test_image_one)


if __name__ == '__main__':
    main()
