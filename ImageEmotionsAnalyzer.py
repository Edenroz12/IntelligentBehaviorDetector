import cv2
from fer import FER
from MyEmoji import *


class ImageAnalyzer:
    def __init__(self, image):
        self.__image = image

    def analyze_emotions(self):
        emo_detector = FER(mtcnn=True)
        # Use the top Emotion() function to call for the dominant emotion in the image
        dominant_emotion, emotion_score = emo_detector.top_emotion(self.__image)
        print(dominant_emotion, emotion_score)
        if dominant_emotion.lower() == 'angry':
            return Angry('./emojis_images/' + dominant_emotion + '.png')
        elif dominant_emotion.lower() == 'disgust':
            return Disgust('./emojis_images/' + dominant_emotion + '.png')
        elif dominant_emotion.lower() == 'fear':
            return Fear('./emojis_images/' + dominant_emotion + '.png')
        elif dominant_emotion.lower() == 'happy':
            return Happy('./emojis_images/' + dominant_emotion + '.png')
        elif dominant_emotion.lower() == 'sad':
            return Sad('./emojis_images/' + dominant_emotion + '.png')
        elif dominant_emotion.lower() == 'surprise':
            return Surprise('./emojis_images/' + dominant_emotion + '.png')
        elif dominant_emotion.lower() == 'neutral':
            return Neutral('./emojis_images/' + dominant_emotion + '.png')
        else:
            raise ValueError('Undefined Emotion')

    def emoji_and_text(self, dominant_emotion):
        cv2.putText(img=self.__image,
                    text=dominant_emotion.get_description(),
                    org=(90, 90),
                    fontFace=cv2.FONT_HERSHEY_TRIPLEX,
                    fontScale=1.7,
                    color=(8, 8, 8),
                    thickness=3)

        # draw emoji
        emoji_img = cv2.imread(dominant_emotion.get_img_path())

        image = self.__image.copy()

        x_offset, y_offset = 570, 50

        y1, y2 = y_offset, y_offset + emoji_img.shape[0]
        x1, x2 = x_offset, x_offset + emoji_img.shape[1]

        alpha_s = emoji_img[:, :, 2] / 255.0
        alpha_l = 1.0 - alpha_s

        for c in range(0, 3):
            image[y1:y2, x1:x2, c] = (alpha_s * emoji_img[:, :, c] +
                                      alpha_l * image[y1:y2, x1:x2, c])

        seconds = 3
        cv2.imshow('My Image', image)
        cv2.waitKey(seconds * 1000)
