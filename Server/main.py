from ImageProcessing import *
from ImageEmotionsAnalyzer import *


def main():
    choice = '0'
    image_creator = None
    choice = input("enter 1 if you want take picture or 2 if you want upload a picture: ")
    if choice == '1':
        image_creator = CameraImage()
    elif choice == '2':
        image_creator = UploadImage()
    else:
        return

    image = image_creator.get_picture()

    image_analyzer = ImageAnalyzer(image)

    dominant_emotion = image_analyzer.analyze_emotions()
    image_analyzer.emoji_and_text(dominant_emotion)


if __name__ == '__main__':
    main()
