from tkinter import filedialog
import cv2
from abc import ABC, abstractmethod


class CreateImage(ABC):
    @staticmethod
    @abstractmethod
    def get_picture():
        raise not NotImplementedError('get_picture is an abstract method')


class CameraImage(CreateImage):
    @staticmethod
    def get_picture():
        # Define a video capture object
        image = None
        vid = cv2.VideoCapture(0)
        while vid.isOpened():
            ret, frame = vid.read()
            frame = cv2.flip(frame, 1)
            cv2.imshow('frame', frame)
            if cv2.waitKey(20) == ord(' '):
                image = frame
                vid.release()
                break

        # After the loop release the cap object
        vid.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return image


class UploadImage(CreateImage):
    @staticmethod
    def get_picture():
        path = filedialog.askopenfilename(title='Select Image',
                                          initialdir='',
                                          filetypes=(('jpg / jpeg files', '*.jpg'),
                                                     ('jpg / jpeg files', '*.jpeg'),
                                                     ('png files', '*.png')))
        return cv2.imread(path)
