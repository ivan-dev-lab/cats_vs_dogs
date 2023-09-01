import os
from pathlib import Path
  
ROOT_DIR = "D:/!BackUp/программирование/python/Ai/данные/cats_vs_dogs"
train_dir, val_dir, test_dir = os.path.join(ROOT_DIR, "train"), os.path.join(ROOT_DIR, "val"), os.path.join(ROOT_DIR, "test")
train_soze, val_size, test_size = len(list(Path(train_dir).rglob("*.jpg"))), len(list(Path(val_dir).rglob("*.jpg"))), len(list(Path(test_dir).rglob("*.jpg")))

if len(list(Path(os.path.join(ROOT_DIR, "images")).rglob("*.jpg"))) > train_soze+val_size+test_size:
    raise ValueError("Каталоги с тренировочной, валидационной и тестовой выборками не заполнены до конца")
elif len(list(Path(os.path.join(ROOT_DIR, "images")).rglob("*.jpg"))) < train_soze+val_size+test_size:
    raise ValueError("Каталоги с тренировочной, валидационной и тестовой выборками содержат больше файлов, чем исходный каталог")
else:
    img_width, img_height = 32, 32
    input_shape = (img_width, img_height, 3)

    