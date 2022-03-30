import abc
from datetime import datetime


# TODO image position related to text

class Emoji(abc.ABC):
    def __init__(self, name, img_path, description):
        self.__name = name
        self.__img_path = img_path
        self.__description = description
        self.__creation_date = datetime.now().date()

    def get_name(self):
        return self.__name

    def get_img_path(self):
        return self.__img_path

    def get_description(self):
        return self.__description

    def get_creation_date(self):
        return self.__creation_date

    def __str__(self):
        return f'Name: {self.__name} | Description: {self.__description} | Creation Date: {self.__creation_date}'

    def __repr__(self):
        return f'Name: {self.__name} | Description: {self.__description} | Creation Date: {self.__creation_date}'


class Angry(Emoji):
    def __init__(self, img_path):
        super().__init__('Angry', img_path, 'You are angry, relax')


class Disgust(Emoji):
    def __init__(self, img_path):
        super().__init__('Disgust', img_path, 'You are disgusted, ew')


class Fear(Emoji):
    def __init__(self, img_path):
        super().__init__('Fear', img_path, 'You are afraid, calm down!')


class Happy(Emoji):
    def __init__(self, img_path):
        super().__init__('Happy', img_path, 'You are happy, have fun!')


class Neutral(Emoji):
    def __init__(self, img_path):
        super().__init__('Neutral', img_path, 'You are neutral, ok')


class Sad(Emoji):
    def __init__(self, img_path):
        super().__init__('Sad', img_path, 'You are sad, do not cry')


class Surprise(Emoji):
    def __init__(self, img_path):
        super().__init__('Surprise', img_path, 'You are surprised, shock!')
