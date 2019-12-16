import requests
import cv2
import numpy as np

def draw_grid(img):
    pxstep = 100
    line_color=(0, 255, 0)
    thickness=1 
    type=cv2.LINE_AA 
    x = pxstep
    y = pxstep
    while x < img.shape[1]:
        cv2.line(img, (x, 0), (x, img.shape[0]), color=line_color, lineType=type, thickness=thickness)
        x += pxstep

    while y < img.shape[0]:
        cv2.line(img, (0, y), (img.shape[1], y), color=line_color, lineType=type, thickness=thickness)
        y += pxstep

    return cv2.imshow("Android_cam", img)

#Скачать IP Webcam на телефон, в приложении запустить сервер, строкой ниже заменить на свой url
url = "http://192.168.1.11:8080/shot.jpg"

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype = np.uint8)
    img = cv2.imdecode(img_arr, -1)
    cv2.imshow("Android_cam", img)
    draw_grid(img)
    if cv2.waitKey(1) == 27:
        break

