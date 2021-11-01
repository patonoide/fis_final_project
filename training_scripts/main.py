import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import cv2 as cv
import os

import sklearn.model_selection as model_selection
from sklearn.metrics import accuracy_score
from keras.models import Sequential
from keras.layers import Dense,MaxPooling2D,Activation,Flatten,Conv2D,BatchNormalization,Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers
from tensorflow.keras import Model
from keras.utils.np_utils import to_categorical
import keras
import tensorflow as tf
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import LabelEncoder


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder,filename))
        img = cv.resize(img, (512,512), interpolation=cv.INTER_AREA)
        if img is not None:
            images.append(img)
    return images

images = load_images_from_folder('./new_furry')
people_images = load_images_from_folder('./cartoons')


model = Sequential()

model.add(tf.keras.Input(shape=(512,512,3)))
# model.add(layers.experimental.preprocessing.Resizing(224,224,interpolation="bilinear",input_shape=(512,512,6)))
# model.add(Conv2D(filters=32,padding="same",kernel_size=(5,5)))
# model.add(Activation('relu'))
# model.add(MaxPooling2D(1,1))

model.add(Conv2D(filters=32,padding="same",kernel_size=(4,4)))
model.add(Activation('relu'))
model.add(MaxPooling2D(1,1))

model.add(Conv2D(filters=32,padding="same",kernel_size=(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(1,1))

model.add(Conv2D(filters=32,padding="same",kernel_size=(2,2)))
model.add(Activation('relu'))
model.add(MaxPooling2D(2,2))

model.add(Conv2D(filters=32,padding="same",kernel_size=(3,3)))
model.add(Activation('relu'))

model.add(Flatten())
model.add(Dense(128))
model.add(Activation("relu"))


model.add(Flatten())
model.add(Dense(64))
model.add(Activation("relu"))


model.add(Flatten())
model.add(Dense(32))
model.add(Activation("relu"))

# model.add(Activation("softmax"))
model.add(Dense(1))
model.add(Activation("sigmoid"))

sgd = Adam(learning_rate=0.001)
loss_fn = tf.keras.losses.BinaryCrossentropy(
    from_logits=False,
    label_smoothing=0,
    axis=-1,
    reduction="auto",
    name="binary_crossentropy",
)


model.compile(loss=loss_fn, optimizer=sgd, metrics=['accuracy'])

labels = []
for x in range(len(images)):
    labels.append(1)
for x in range(len(people_images)):
    labels.append(0)

images = images + people_images


X_train, X_test, y_train, y_test = model_selection.train_test_split(np.array(images), np.array(labels), test_size=0.33)


model.fit(x=X_train, y=y_train, epochs=10)
model.summary()
labels = model.predict(X_test)


model.save('main_model')



