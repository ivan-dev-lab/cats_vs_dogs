# программа распределяет массив фотографий с собаками кошками по каталогам ( train, test, control ) c собаками и кошками
import shutil
import os

ROOT_DIR = "D:/!BackUp/программирование/python/Ai/данные/cats_vs_dogs"

def create_dirs (dir_name: str):
    path = os.path.join(ROOT_DIR, dir_name)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    os.makedirs(os.path.join(path, "cat"))
    os.makedirs(os.path.join(path, "dog"))


def check_len (dir_name: str, dir_size: int) -> bool:
    if len(os.listdir(dir_name)) == dir_size:
        return True
    else: return False

def allocate ():
    [create_dirs(path) for path in ["train", "test", "control"]]

    dataset_size = len(os.listdir(os.path.join(ROOT_DIR, "images")))
    train_size, test_size, control_size = (0.7*dataset_size, 0.15*dataset_size, 0.15*dataset_size)

    for img_name in os.listdir(os.path.join(ROOT_DIR, "images")):
        src = os.path.join(ROOT_DIR, "images", img_name)
        print("images",src.split("\\")[-1:][0] ,sep="/", end=" -> ")

        pet = "cat" if img_name.find("cat") != -1 else "dog"

        # Предполагаемый метод работы функции check_len в условиях, что она проверяет заполненность всего каталога в целом, в случае если он не заполнен, то проверяет заполненность его подкаталогов: cat/ и dog/ , каждый из которых должен содержать в себе [кол-во файлов в каталоге]/2

        if check_len(os.path.join(ROOT_DIR, "train"), dir_size=train_size) == False:
            if check_len(os.path.join(ROOT_DIR, "train", pet), dir_size=train_size/2) == False:
                dst = os.path.join(ROOT_DIR, "train", pet, img_name)
            else: continue
        elif check_len(os.path.join(ROOT_DIR, "test"), dir_size=test_size) == False:
            if check_len(os.path.join(ROOT_DIR, "test", pet), dir_size=test_size/2) == False:
                dst = os.path.join(ROOT_DIR, "test", pet, img_name)
            else: continue
        elif check_len(os.path.join(ROOT_DIR, "control"), dir_size=control_size) == False:
            if check_len(os.path.join(ROOT_DIR, "control", pet), dir_size=control_size/2) == False:
                dst = os.path.join(ROOT_DIR, "control", pet, img_name)
            else: continue
        
        print(dst.split("\\")[1], dst.split("\\")[2], dst.split("\\")[3], sep="/", end=" -> ")
        print(len(os.listdir("/".join(dst.split("\\")[:-1]))))
        shutil.copy(src, dst)   

allocate()