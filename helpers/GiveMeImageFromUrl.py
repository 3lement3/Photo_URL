import os
import shutil
import requests
from urllib.request import urlopen
from PIL import Image  # Работа с изображениями
import imghdr  # Определяет тип изображения


# Debug
# url_img = 'https://sun9-5.userapi.com/c206824/v206824136/f6730/xjjeO-kRAh0.jpg'


class GiveMeImageFromUrl:
    """
    Получить файл в директорию из url
    """

    def __init__(self, url):
        self.url_img = url

    def get_img_from_url(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Основной путь
        dir = os.path.join(BASE_DIR, 'media\example.jpg')  # Путь до файла
        print('===')
        print(dir)  # Путь куда ляжет файл
        """
        :return: image file from url
        """
        response = requests.get(self.url_img, stream=True)
        with open(dir, 'wb') as file:
            shutil.copyfileobj(response.raw, file)
        del response
        print(f'Type File: {imghdr.what(dir)}')  # Определяем тип изображения
        file = f'{dir}'
        print(f'Возвращаем: {file}')
        print('===')
        return file

    # Получить обьект img по url
    def get_img_from_url_processed(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Основной путь
        dir = os.path.join(BASE_DIR, 'media\example_result.jpg')  # Путь до файла
        print('===')
        print(dir)  # Path to file
        """
        :return: image file from url
        """
        response = requests.get(self.url_img, stream=True)
        with open(dir, 'wb') as file:
            shutil.copyfileobj(response.raw, file)
        del response
        print(f'Type File: {imghdr.what(dir)}')  # Определяем тип изображения
        file = f'{dir}'
        print(f'Возвращаем: {file}')
        print('===')
        return file


if __name__ == '__main__':
    test = GiveMeImageFromUrl('https://sun9-5.userapi.com/c206824/v206824136/f6730/xjjeO-kRAh0.jpg')
    foo = test.get_img_from_url()
    print(type(foo))
