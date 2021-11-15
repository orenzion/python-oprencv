import cv2

# 0 mode is for grayscale, -1 color image, 1 image unchanged
img = cv2.imread('assets/me_and_yuli.jpg',0)

# resize image
img = cv2.resize(img, (700, 600))

# rotate image
img = cv2.rotate(img,cv2.ROTATE_180)

# write img to file
cv2.imwrite('img_img.jpg',img)

# show image
cv2.imshow('Image',img) 
# wait infinite amount of time untill any keyboard is pressed   
cv2.waitKey(0)
# destroy all wndows
cv2.destroyAllWindows()