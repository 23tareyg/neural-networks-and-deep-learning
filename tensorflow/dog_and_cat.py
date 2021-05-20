import matplotlib.pyplot as plt
import os
import cv2
import random

DATA = "/Users/Tare/Downloads/PetImages"

CATEGORIES = ["Dog", "Cat"]

IMG_SIZE = 50

#for category in CATEGORIES:
#    path = os.path.join(DATA,category)
#    for img in os.listdir(path):
#        img_array = cv2.imread(os.path.join(path, img), 0)
#        plt.imshow(img_array, cmap="gray")
#        plt.show()
#        break
#    break

training_data = []

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATA,category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), 0)
                new_array - cv2.resize(img_array, (IMG_SIZE,IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception :
                pass

create_training_data()

print(len(training_data())

random.shuffle(training_data

x = []
y = []

for features, label in training_data:
    x.append(features)
    y.append(label)

x = nparray.(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
