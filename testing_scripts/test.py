import os

from keras import models
import cv2 as cv
from sklearn import model_selection
import numpy as np
from sklearn.metrics import accuracy_score

model = models.load_model('./rotation_model')

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder,filename))
        img = cv.resize(img, (512,512), interpolation=cv.INTER_AREA)
        if img is not None:
            images.append(img)
    return images

furry_images = load_images_from_folder('./validation_set/furry')
cartoon_images = load_images_from_folder('./validation_set/cartoon')


labels = []
for x in range(len(furry_images)):
    labels.append(1.0)
for x in range(len(cartoon_images)):
    labels.append(0.0)

images = furry_images + cartoon_images

predicted_labels = model.predict(np.array(images))
fixed_predicted = []
for i in range(len(predicted_labels)):
    if predicted_labels[i][0] >= 0.5:
        predicted_labels[i][0] = 1.0
    else:
        predicted_labels[i][0] = 0.0
    fixed_predicted.append(predicted_labels[i][0])

acc = accuracy_score(labels, fixed_predicted)
print(acc)
