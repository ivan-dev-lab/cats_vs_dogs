# программа распределяет массив фотографий с собаками кошками по каталогам ( train, test, control ) c собаками и кошками
import shutil
import os

ROOT_DIR = "D:/!BackUp/программирование/python/Ai/данные/cats_vs_dogs"

def create_dirs (dir_name: str) -> None:
    path = os.path.join(ROOT_DIR, dir_name)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    os.makedirs(os.path.join(path, "cats"))
    os.makedirs(os.path.join(path, "dogs"))

def copy_images (start_idx: int, end_idx: int, src: str, dst: str) -> None:
    for i in range(start_idx, end_idx):
        shutil.copy(src=os.path.join(src, "cat."+str(i)+".jpg"), 
                    dst=os.path.join(dst, "cats", "cat."+str(i)+".jpg"))
        shutil.copy(src=os.path.join(src, "dog."+str(i)+".jpg"), 
                    dst=os.path.join(dst, "dogs", "dog."+str(i)+".jpg"))
        
        print(i, end_idx, sep="/")

def allocate ():
    [create_dirs(path) for path in ["train", "test", "control"]]

    dataset_size = len(os.listdir(os.path.join(ROOT_DIR, "images")))

    # значения делятся на 2, т.к необходимо создать 2 каталога для сохранения данных, т.е train_size - объем всего каталога / 2 = объемы каталогов cats/ и dogs/
    train_size, test_size, control_size = (int((0.7*dataset_size)/2), int((0.20*dataset_size)/2), int((0.10*dataset_size)/2))

    copy_images(start_idx=0, end_idx=train_size, src=os.path.join(ROOT_DIR, "images"), dst=os.path.join(ROOT_DIR, "train"))
    copy_images(start_idx=train_size, end_idx=test_size, src=os.path.join(ROOT_DIR, "images"), dst=os.path.join(ROOT_DIR, "test"))
    copy_images(start_idx=test_size, end_idx=control_size, src=os.path.join(ROOT_DIR, "images"), dst=os.path.join(ROOT_DIR, "control"))

