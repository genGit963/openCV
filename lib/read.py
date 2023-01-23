import cv2

img = cv2.imread('/home/gen/Pictures/wallpaperflare.com_wallpaper.jpg')

img_resize = cv2.resize(img, (0,0), fx=0.20, fy=0.20)

cv2.imshow("image", img_resize);
cv2.waitKey(0)