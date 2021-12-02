import cv2
img=cv2.imread('grls.jpg')
print(img)
cv2.imshow('Using cv2',img)
cv2.waitKey(5000)