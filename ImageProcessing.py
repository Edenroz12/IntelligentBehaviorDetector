from tkinter import Tk, filedialog
import cv2


def take_picture():
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


def upload_picture(path):
    return cv2.imread(path)


def get_path_with_dialog():
    Tk().withdraw()
    return filedialog.askopenfilename(title='Select Image',
                                      initialdir='',
                                      filetypes=(('jpg / jpeg files', '*.jpg'),
                                                 ('jpg / jpeg files', '*.jpeg'),
                                                 ('png files', '*.png')))
