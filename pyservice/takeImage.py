import cv2

cam0 = cv2.VideoCapture(0)
cam1 = cv2.VideoCapture(2)

'''
while True:
    ret, image = cam0.read()
    cv2.imshow('Imagetest',image)
    k = cv2.waitKey(1)
    if k != -1:
        break
cv2.imwrite('/home/pi/Desktop/Kusch/images/parcel.jpg' ,image)
cam0.release()
cv2.destroyAllWindows()
'''

ret, image = cam0.read()
cv2.imwrite('/home/pi/Desktop/Kusch/images/parcel.jpg' ,image)
cam0.release()
cv2.destroyAllWindows()

ret, image = cam1.read()
cv2.imwrite('/home/pi/Desktop/Kusch/images/taken.jpg' ,image)
cam1.release()
cv2.destroyAllWindows()

