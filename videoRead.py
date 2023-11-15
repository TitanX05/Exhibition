import numpy as np 
import cv2 
  
#'WhatsApp_Video_2023-10-29_at_15.59.39_34d538d6.mp4'
  
# Capturing video through webcam 
webcam = cv2.VideoCapture('WIN_20231101_19_03_08_Pro.mp4') 
  
# Start a while loop 
while(1): 
      
    # Reading the video from the 
    # webcam in image frames 
    _, imageFrame = webcam.read() 
  
    # Convert the imageFrame in  
    # BGR(RGB color space) to  
    # HSV(hue-saturation-value) 
    # color space 
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 
  
    # Set range for red color and  
    # define mask 
    red_lower = np.array([136, 87, 111], np.uint8) 
    red_upper = np.array([180, 255, 255], np.uint8) 
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper) 
  
    # Set range for green color and  
    # define mask 
    green_lower = np.array([50, 100, 100], np.uint8) 
    green_upper = np.array([70, 255,255], np.uint8) 
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper) 
  
    # Set range for blue color and 
    # define mask 
    blue_lower = np.array([100,150,0], np.uint8) 
    blue_upper = np.array([140,255,255], np.uint8) 
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper) 

    yellow_lower = np.array([22, 93, 0], np.uint8) 
    yellow_upper = np.array([45, 255, 255], np.uint8) 
    yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper) 

    white_lower = np.array([0,0,240], np.uint8) 
    white_upper = np.array([255,15,255], np.uint8) 
    white_mask = cv2.inRange(hsvFrame, white_lower, white_upper) 

    orange_lower = np.array([10, 100, 20], np.uint8) 
    orange_upper = np.array([25, 255, 255], np.uint8) 
    orange_mask = cv2.inRange(hsvFrame, orange_lower, orange_upper) 
      
    # Morphological Transform, Dilation 
    # for each color and bitwise_and operator 
    # between imageFrame and mask determines 
    # to detect only that particular color 
    kernel = np.ones((5, 5), "uint8") 
      
    # For red color 
    red_mask = cv2.dilate(red_mask, kernel) 
    res_red = cv2.bitwise_and(imageFrame, imageFrame,  
                              mask = red_mask) 
      
    # For green color 
    green_mask = cv2.dilate(green_mask, kernel) 
    res_green = cv2.bitwise_and(imageFrame, imageFrame, 
                                mask = green_mask) 
      
    # For blue color 
    blue_mask = cv2.dilate(blue_mask, kernel) 
    res_blue = cv2.bitwise_and(imageFrame, imageFrame, 
                               mask = blue_mask) 

    yellow_mask = cv2.dilate(yellow_mask, kernel) 
    res_yellow = cv2.bitwise_and(imageFrame, imageFrame, 
                               mask = yellow_mask)
                               
    white_mask = cv2.dilate(white_mask, kernel) 
    res_white = cv2.bitwise_and(imageFrame, imageFrame, 
                               mask = white_mask)  
    
    orange_mask = cv2.dilate(orange_mask, kernel) 
    res_orange = cv2.bitwise_and(imageFrame, imageFrame, 
                               mask = orange_mask) 
   
    # Creating contour to track red color 
    contours, hierarchy = cv2.findContours(red_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
      
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imageFrame, (x, y),  
                                       (x + w, y + h),  
                                       (0, 0, 255), 2) 
              
            cv2.putText(imageFrame, "Red Colour", (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, 
                        (0, 0, 255))     
  
    # Creating contour to track green color 
    contours, hierarchy = cv2.findContours(green_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
      
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imageFrame, (x, y),  
                                       (x + w, y + h), 
                                       (0, 255, 0), 2) 
              
            cv2.putText(imageFrame, "Green Colour", (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX,  
                        1.0, (0, 255, 0)) 
  
    # Creating contour to track blue color 
    contours, hierarchy = cv2.findContours(blue_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (255, 0, 0), 2) 
              
            cv2.putText(imageFrame, "Blue Colour", (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        1.0, (255, 0, 0)) 
            
    contours, hierarchy = cv2.findContours(yellow_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (255, 162, 0), 2) 
              
            cv2.putText(imageFrame, "Yellow Colour", (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        1.0, (255, 162, 0)) 
            
    contours, hierarchy = cv2.findContours(white_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (255, 157, 0), 2) 
              
            cv2.putText(imageFrame, "White Colour", (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        1.0, (255, 157, 0)) 
            
    contours, hierarchy = cv2.findContours(orange_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (255, 157, 0), 2) 
              
            cv2.putText(imageFrame, "Orange Colour", (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        1.0, (255, 157, 0)) 
              
    # Program Termination 
    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame) 
    if cv2.waitKey(10) & 0xFF == ord('q'): 
        webcam.release() 
        cv2.destroyAllWindows() 
        break