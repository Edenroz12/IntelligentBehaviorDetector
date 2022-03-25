from matplotlib import pyplot as plt
from tkinter import Tk, filedialog
import cv2


def take_picture():
    # define a video capture object
    vid = cv2.VideoCapture(0)

    while vid.isOpened():
        ret, frame = vid.read()
        frame = cv2.flip(frame, 1)
        cv2.imshow('frame', frame)
        if cv2.waitKey(20) == ord('s'):
            test_image_one = frame
            vid.release()
            break
    # input("Press Enter to continue...")

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return test_image_one


def upload_picture(path):
    return plt.imread(path)


def get_path_with_dialog():
    Tk().withdraw()
    return filedialog.askopenfilename(title='Select Image',
                                      initialdir='',
                                      filetypes=(('jpg / jpeg files', '*.jpg'), ('jpg / jpeg files', '*.jpeg'),
                                                 ('png files', '*.png')))
