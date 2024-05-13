import cv2 

image = cv2.imread("Shajariyan.jpg")
resize_imgage = cv2.resize(image ,[450 , 550])
gray_image =cv2.cvtColor(resize_imgage , cv2.COLOR_BGR2GRAY)
x = 0
for i in range(160):
    gray_image[116-x:160-x , 0+x:1+x] = 0
    if x >= 115 :
        gray_image[0:160-x , 0+x:1+x] = 0
    x+= 1
    
cv2.imshow("Black Tape ",gray_image)
cv2.imwrite("Black_Tape.jpg" , gray_image)
cv2.waitKey()