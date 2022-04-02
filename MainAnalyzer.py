from DB_manager import insert_emotion
from ImageProcessing import *
from ImageEmotionsAnalyzer import *


def analyze_and_update(email, image_path):
    image = CreateImage.get_picture(image_path)

    image_analyzer = ImageAnalyzer(image)

    dominant_emotion = image_analyzer.analyze_emotions()
    insert_emotion(email, dominant_emotion)
    image_with_emotion = image_analyzer.emoji_and_text(dominant_emotion)
    cv2.imwrite(image_path, image_with_emotion)
    return dominant_emotion
