import cv2
import time

cap=cv2.VideoCapture('D:\\AR\\fatigue_driving\\Fatigue-Driven-Detection-Based-on-CNN\\test.jpg')
while cap.isOpened():
	ret,frame=cap.read()
	cv2.imshow('capture', frame)
	time.sleep(0.050)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		 break
cap.release()
cv2.destroyAllWindows()