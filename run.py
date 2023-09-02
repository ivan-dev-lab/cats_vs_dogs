import os
import numpy as np
from pathlib import Path
from keras.preprocessing.image import ImageDataGenerator, image_utils
from keras.models import load_model
from keras import Model
from src.create_model import create_model

def single_prediction (model: Model, img_path: str, sizes: tuple[int]) -> ...:
    img = image_utils.load_img(path=img_path, target_size=sizes)
    img_array = image_utils.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array/255
    predicton = model.predict(img_array)

    return predicton

ROOT_DIR = "D:/!BackUp/программирование/python/Ai/данные/cats_vs_dogs"
train_dir, val_dir, test_dir = os.path.join(ROOT_DIR, "train"), os.path.join(ROOT_DIR, "val"), os.path.join(ROOT_DIR, "test")
train_size, val_size, test_size = len(list(Path(train_dir).rglob("*.jpg"))), len(list(Path(val_dir).rglob("*.jpg"))), len(list(Path(test_dir).rglob("*.jpg")))

if len(list(Path(os.path.join(ROOT_DIR, "images")).rglob("*.jpg"))) > train_size+val_size+test_size:
    raise ValueError("Каталоги с тренировочной, валидационной и тестовой выборками не заполнены до конца")
elif len(list(Path(os.path.join(ROOT_DIR, "images")).rglob("*.jpg"))) < train_size+val_size+test_size:
    raise ValueError("Каталоги с тренировочной, валидационной и тестовой выборками содержат больше файлов, чем исходный каталог")
else:
    img_width, img_height = 32, 32
    
    # проверка наличия сохраненной модели. Если сохраненных моделей в каталоге models/ нет, то будет процесс обучения
    if len(os.listdir("./models/")) == 0:
        input_shape = (img_width, img_height, 3)

        data_gen = ImageDataGenerator(rescale=1/255)
        batch_size = 32

        train_gen = data_gen.flow_from_directory(
            directory=train_dir,
            target_size=(img_width, img_height),
            batch_size=batch_size,
            class_mode="binary"
        )

        val_gen = data_gen.flow_from_directory(
            directory=val_dir,
            target_size=(img_width, img_height),
            batch_size=batch_size,
            class_mode="binary"
        )

        test_gen = data_gen.flow_from_directory(
            directory=test_dir,
            target_size=(img_width, img_height),
            batch_size=batch_size,
            class_mode="binary"
        )

        model = create_model(input_shape)

        model.fit(
            train_gen,
            steps_per_epoch=train_size//batch_size,
            epochs=30,
            validation_data=val_gen,
            validation_steps=val_size//batch_size
        )

        scores = model.evaluate(
            test_gen,
            steps=test_size//batch_size
        )

        print(f"Точность модели на тестовых данных = {scores[1]*100}%")

        model.save("models/Classification.h5")

    model = load_model("models/Classification.h5")
    prediction = single_prediction(model, img_path="images/test_dog.jpg", sizes=(img_width, img_height))

    print(f"На изображении {'кот' if prediction[0][0] < 0.5 else 'собака'} с вероятностью {(1-prediction[0][0])*100 if prediction[0][0] < 0.5 else prediction[0][0]*100}%")