import cv2
img=cv2.imread('cflower.jpg')

gryflower=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #changes into grey color
cv2.imwrite('grey.jpg',gryflower)

rgbflower=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #changes in rgb colors
cv2.imwrite('color.jpg',rgbflower)
