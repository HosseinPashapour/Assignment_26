import cv2

image = cv2.imread("Angry_men.jpg" )
sad_man_img = cv2.resize(image ,[1100 , 700])
happy_man_img= cv2.rotate(sad_man_img, cv2.ROTATE_180)

cv2.imshow("Happy_Men" ,happy_man_img)
cv2.imwrite("Happy_men.jpg" , happy_man_img)
cv2.waitKey()