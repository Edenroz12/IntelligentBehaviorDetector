import cv2
from fer import FER
from matplotlib import pyplot as plt


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


def emoji_and_text(face_image, dominant_emotion):
    cv2.putText(img=face_image,
                text=f'You are {dominant_emotion}',
                org=(90, 90),
                fontFace=cv2.FONT_HERSHEY_TRIPLEX,
                fontScale=1.7,
                color=(8, 8, 8),
                thickness=3)

    # draw emoji
    emoji_img = cv2.imread("emojis_images/" + dominant_emotion + ".png")

    image = face_image.copy()

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
