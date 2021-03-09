import cv2
def blue_callback(x):
    blue = cv2.getTrackbarPos('blue', 'img')
    return blue

def green_callback(x):
    green = cv2.getTrackbarPos('green', 'img')
    return  green

def red_callback(x):
    red = cv2.getTrackbarPos('red', 'img')
    return red

def nothing(x):
    pass

def mouse_callback(event, x, y, flags, param):
    global drawing
    b = blue_callback(0)
    g = green_callback(0)
    r = red_callback(0)
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(img, (x,y), 10, (b, g, r), -1)
    elif event == cv2.EVENT_MOUSEMOVE and drawing == True:
        cv2.circle(img, (x,y), 10, (b, g, r), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
    cv2.imshow('img',img)

drawing = False
img = cv2.imread('Lenna.jpg', cv2.IMREAD_COLOR)

if img is None:
    print("이미지 파일을 읽을 수 없습니다.")
    exit(0)

cv2.imshow('img',img)
cv2.createTrackbar('blue','img',0,255,nothing)
cv2.createTrackbar('green','img',0,255,nothing)
cv2.createTrackbar('red','img',0,255,nothing)
cv2.setTrackbarPos('blue','img',255)
cv2.setMouseCallback('img', mouse_callback)
cv2.waitKey(0)
cv2.destroyAllWindows()