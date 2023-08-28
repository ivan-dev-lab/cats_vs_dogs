# программа распределяет массив фотографий с собаками кошками по каталогам ( train, test, control ) c собаками и кошками
import shutil
import os

ROOT_DIR = "D:/!BackUp/программирование/python/Ai/данные/cats_vs_dogs"

def create_dirs (dir_name: str):
    path = os.path.join(ROOT_DIR, dir_name)
    if os.path.exists(path):
        shutil.rmtree(path)
    else:
        os.makedirs(path)
        os.makedirs(os.path.join(path, "cat"))
        os.makedirs(os.path.join(path, "dog"))