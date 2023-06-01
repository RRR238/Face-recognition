import keras
import os
import cv2
import numpy as np
from datetime import datetime
import ctypes
import time
import keyboard

model = keras.models.load_model(r"C:\Users\DELL\Desktop\env_classifier")

def capture_image(save_path):
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    result, image = cam.read()
    cv2.imwrite(save_path, image)
    cam.release()

def import_images(directory):
    images = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        img = cv2.imread(f)
        img = cv2.resize(img,(640,480))
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_norm = img_RGB/255
        images.append(img_norm)
    return np.array(images)

def pred(img):
    p = model.predict(img,verbose=0)[0][0]
    return p

while True:
    timestamp = str(datetime.now().month) + str(datetime.now().day) + str(datetime.now().hour) + str(datetime.now().minute) + str(datetime.now().second) + ".jpg"
    path = r"C:\Users\DELL\Desktop\face_recognition\test\face_" + timestamp
    capture_image(path)
    imag = import_images(r"C:\Users\DELL\Desktop\face_recognition\test")
    prob = pred(imag)
    if prob <= 0.5:
        print("Clear")
        os.remove(path)
        time.sleep(5)
    else:
        ctypes.windll.user32.LockWorkStation()
        os.startfile(r"C:\Users\DELL\Desktop\alert_alert.mp3")
        cv2.imwrite(r"C:\Users\DELL\Desktop\face_recognition\invaders\face_" + timestamp, 255*imag[0])
        os.remove(path)
        keyboard.wait('enter')






