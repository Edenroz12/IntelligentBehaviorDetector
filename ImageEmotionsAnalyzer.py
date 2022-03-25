import cv2
from PIL import Image
from fer import FER
from matplotlib import pyplot as plt
import numpy as np


def start_analyzing(test_image_one):
    emo_detector = FER(mtcnn=True)
    # Capture all the emotions on the image
    captured_emotions = emo_detector.detect_emotions(test_image_one)
    # Print all captured emotions with the image
    print(captured_emotions)
    plt.imshow(test_image_one)

    # Use the top Emotion() function to call for the dominant emotion in the image
    dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_one)
    print(dominant_emotion, emotion_score)
    emoji_and_text(test_image_one, dominant_emotion)


def emoji_and_text(test_image_one, dominant_emotion):
    emotions_dict = {'happy': 'happy', 'sad': 'sad', 'surprise': 'surprised', 'neutral': 'neutral', 'fear': 'fear',
                     'disgust': 'disgust',
                     'angry': 'angry'}
    cv2.putText(img=test_image_one,
                text='You are ' + emotions_dict.get(dominant_emotion, ' undefined'),
                org=(90, 90),
                fontFace=cv2.FONT_HERSHEY_TRIPLEX,
                fontScale=1.7,
                color=(8, 8, 8),
                thickness=3)
    rgb_img = cv2.cvtColor(test_image_one, cv2.COLOR_BGR2RGB)

    # draw emoji
    im1_nparray = rgb_img
    im2 = Image.open("emojis_images/" + dominant_emotion + ".png")
    mask_im = Image.open('circle_white2.jpg').resize(im2.size).convert('L')

    im1 = Image.fromarray(im1_nparray)
    im1.paste(im2, (550, 55), mask_im)
    rgb_img = np.array(im1)

    cv2.imshow('My Image', rgb_img)

    seconds = 10

    cv2.waitKey(seconds * 1000)
