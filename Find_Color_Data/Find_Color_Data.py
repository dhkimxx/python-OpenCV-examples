import cv2 as cv
import numpy as np

img = cv.imread('lenna.png', cv.IMREAD_COLOR) #test1 이미지 로드
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV) #BGR을 HSV컬러로 변환

mask_g = cv.inRange(img, np.array([0, 250, 0]), np.array([255, 255, 255]))
#녹색값 250 이상 마스킹

mask_v = cv.inRange(img_hsv, np.array([0, 0, 0]), np.array([255, 255, 50]))
#명도값 50 이하 마스킹

yg,xg = np.where(mask_g>0)
xy_g = [(x,y) for x,y in zip(xg,yg)]
#녹색값 250 이상 좌표추출

for xy in xy_g:
    cv.circle(img,xy,20,(0,255,0),2)
#녹색값 250 이상 좌표에 반지름이 20인 초록색 원 그리기

yv,xv = np.where(mask_v>0)
xy_v = [(x,y) for x,y in zip(xv,yv)]
#명도값 50 이하 좌표추출

for xy in xy_v:
    cv.circle(img,xy,20,(0,0,255),2)
#명도값 50 이하 좌표에 반지름이 20인 빨간색 원 그리기

cv.imshow('img',img)
cv.imwrite('lenna_result.png',img)
cv.waitKey(0)

