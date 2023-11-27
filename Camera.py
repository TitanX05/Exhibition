import cv2
import numpy as np
import numpy as np
from imutils import contours
from webcolors import rgb_to_name
color = []
cubecolor = (0,0,0)
cubelineSize = 2
def getcolor(r,g,b): # compare rgb values and return color
    if (r >= 140 and r <= 185 ) and (g >= 80 and g <= 130) and (b > 3 and b < 75):
        return 'b'
    elif (r >= 150 and r <= 250 ) and (g >= 125 and g < 210) and (b >= 125 and b < 200):
        return 'w'
    elif (r >= 15 and r <= 80 ) and (g > 135 and g < 180) and (b > 145 and b < 200):
        return 'y'
    elif (r > 15 and r <= 100 ) and (g >= 77 and g <= 145) and (b > 100 and b < 200):
        return 'o'
    elif (r >= 55 and r <= 100 ) and (g >= 50 and g < 100) and (b >= 100 and b < 255):
        return 'r'
    elif (r >= 70 and r <= 125 ) and (g > 95 and g <= 140) and (b > 40  and b <= 100):
        return 'g'
    
def drawCube(img, cubesize, cubeshape, start_point): # start_poing (100, 60)
    cubecell = int(cubesize / cubeshape)
    # draw horizontal lines first
    for i in range(cubeshape + 1):
        start_line = (start_point[0], start_point[1] + i * cubecell)
        end_line = (start_point[0] + cubesize, start_point[1] + i * cubecell)
        cv2.line(img, start_line, end_line, cubecolor, 2)
    
    for i in range(cubeshape + 1):
        start_line = (start_point[0] + i * cubecell, start_point[1])
        end_line = (start_point[0] + i * cubecell, start_point[1] + cubesize)
        cv2.line(img, start_line, end_line, cubecolor, cubelineSize)

    return img

def showlable(img,index): 
    if index == 1: 
        cv2.putText(cubeImg, "Show face which contain red cubie at center", (int(17), 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0))
        cv2.imshow("cube",cubeImg)
    elif index == 2: 
        cv2.putText(cubeImg, "Show face which contain green cubie at center", (int(17), 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0))
        cv2.imshow("cube",cubeImg)
    elif index == 3: 
        cv2.putText(cubeImg, "Show face which contain orange cubie at center", (int(17), 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0))
        cv2.imshow("cube",cubeImg)
    elif index == 4: 
        cv2.putText(cubeImg, "Show face which contain blue cubie at center", (int(17), 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0))
        cv2.imshow("cube",cubeImg)
    elif index == 5: 
        cv2.putText(cubeImg, "Show face which contain yellow cubie at center", (int(17), 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0))
        cv2.imshow("cube",cubeImg)
    elif index == 6: 
        cv2.putText(cubeImg, "Show face which contain white cubie at center", (int(17), 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0))
        cv2.imshow("cube",cubeImg)
    else:
        pass



cap = cv2.VideoCapture(0)
index = 1
while True:
    cubeImg = np.zeros((480,640))
    res, cubeImg = cap.read()
    cv2.waitKey(10)
    drawCube(cubeImg,180,3,(100,60))
    cv2.imshow("cube",cubeImg)
    showlable(cubeImg, index)
    if cv2.waitKey(1) == ord('w'): # extracting color from cube after click 'c' on keyboard
        index = index + 1
        print("start processing")
        showlable(cubeImg, index)
        img = cubeImg.copy()
        img1 = img[60:120,100:160]
        img2 = img[60:120,160:220]
        img3 = img[60:120,220:280]
        img4 = img[120:180,100:160]
        img5 = img[120:180,160:220]
        img6 = img[120:180,220:280]
        img7 = img[180:240,100:160]
        img8 = img[180:240,160:220]
        img9 = img[180:240,220:280]
        pixel = [img1, img2, img3, img4, img5, img6, img7, img8, img9] 
        
        for i in pixel: # white balancing of image
            r, g, b = cv2.split(i)
            r_avg = cv2.mean(r)[0]
            g_avg = cv2.mean(g)[0]
            b_avg = cv2.mean(b)[0] 
            print(int(r_avg),int(g_avg),int(b_avg))
            res = getcolor(int(r_avg),int(g_avg),int(b_avg))
            color.append(res)

        print(color)
    if cv2.waitKey(10) == ord('q'):
        break
