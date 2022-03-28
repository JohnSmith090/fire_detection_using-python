import cv2
import time
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
from sample_data import student
import winsound
duration = 2000  # milliseconds
freq = 440  # Hz
s1=student;
a=s1.name
print(a)
name1="frame"
cap = cv2.VideoCapture(0)  # start video capturing
count = 0
while cap.isOpened():
    ret, img = cap.read()  # capture a frame
    lastimg = cv2.resize(img, (250, 250))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert image to grayscale
    str = name1 + '\\%d.jpg' % count
    cv2.imwrite(str, lastimg)
    time.sleep(0.2)
    count=count+1
    cv2.imshow('img', img)
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

