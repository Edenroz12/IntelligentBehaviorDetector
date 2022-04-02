import cv2


class CreateImage:
    @staticmethod
    def get_picture(image_path):
        return cv2.imread(image_path)
