import cv2

imagePath = r'C:\\Users\\sondors\\Desktop\\5.jpg'
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


wordCascade = cv2.CascadeClassifier(r"C:\\Users\\sondors\Desktop\\cascade.xml")

words = wordCascade.detectMultiScale(
gray,
scaleFactor=1.3,
minNeighbors=3,
minSize=(70,30)
)
print('!!!')
print("[INFO] Found {0} words!".format(len(words)))

for (x, y, w, h) in words:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    while True:
        cv2.imshow("", image)
        if cv2.waitKey():
            break


  


















