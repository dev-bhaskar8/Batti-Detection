################################
################################
#Dev- Bhaskar Syamal
#email- bhaskar.syamal@gmail.com
#Head- Harshil Thakkar
#Faculty- Prof. Denis Ashok S
################################
################################
import cv2
import numpy as np

def vid_masala():
    cap=cv2.VideoCapture(0)

    while True:
        ret,image=cap.read()
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        
        lower_skin = np.array([0,0,0])
        upper_skin = np.array([180,255,60])

        mask = cv2.inRange(hsv, lower_skin, upper_skin)

        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        mask=cv2.medianBlur(mask,5)

        
        im2, cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        
        for c in cnts:
            if cv2.contourArea(c) < 3000:
                continue

            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(image, (x,y), (x+w,y+h), (0, 255, 0), 2)

            
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(image,[box],0,(0,191,255),2)
            

        cv2.imshow('vid_masala', image)
        cv2.imshow('vid_mask_masala', mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    
def vid_stick():
    cap=cv2.VideoCapture(0)

    while True:
        ret,image=cap.read()
        


        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        
        lower_skin = np.array([[20, 100, 100]])
        upper_skin = np.array([30, 255, 255])

        mask = cv2.inRange(hsv, lower_skin, upper_skin)

        mask = cv2.erode(mask, None, iterations=3)
        mask = cv2.dilate(mask, None, iterations=3)
        mask=cv2.medianBlur(mask,5)

        
        im2, cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        
        for c in cnts:
            if cv2.contourArea(c) < 0:
                continue

            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(image, (x,y), (x+w,y+h), (0, 255, 0), 2)

            
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(image,[box],0,(0,191,255),2)
            

        cv2.imshow('vid_stick', image)
        cv2.imshow('vid_stick_masala', mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def stick():
        image=cv2.imread('batti.jpg')
        image = cv2.resize(image, (600, 600), interpolation=cv2.INTER_AREA) 
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        
        lower_skin = np.array([[20, 100, 100]])
        upper_skin = np.array([30, 255, 255])

        mask = cv2.inRange(hsv, lower_skin, upper_skin)

        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        mask=cv2.medianBlur(mask,5)

        
        im2, cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        
        for c in cnts:
            if cv2.contourArea(c) < 0:
                continue

            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(image, (x,y), (x+w,y+h), (0, 255, 0), 2)

            
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(image,[box],0,(0,191,255),2)
            

        cv2.imshow('stick', image)
        cv2.imshow('mask_stick', mask)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
def masala():
        image=cv2.imread('batti.jpg')
        image = cv2.resize(image, (600, 600), interpolation=cv2.INTER_AREA) 
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        
        lower_skin = np.array([0,0,0])
        upper_skin = np.array([180,255,60])

        mask = cv2.inRange(hsv, lower_skin, upper_skin)

        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        mask=cv2.medianBlur(mask,5)

        
        im2, cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        
        for c in cnts:
            if cv2.contourArea(c) < 3000:
                continue

            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(image, (x,y), (x+w,y+h), (0, 255, 0), 2)

            
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(image,[box],0,(0,191,255),2)
            

        cv2.imshow('masala', image)
        cv2.imshow('mask_masala', mask)
        
        if cv2.waitKey(0) & 0xFF == ord('q'):
            
              cv2.destroyAllWindows()

def calibrate():
    try:
        cap = cv2.VideoCapture(0)
        while(True):
            ret,frame = cap.read()
            cv2.imshow('calibrate',frame) 
            if cv2.waitKey(1) & 0xFF == ord('y'):
                cv2.destroyAllWindows()
                break
        image=frame
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


        lower_skin = np.array([30,150,50])
        upper_skin = np.array([255,255,180])

        mask = cv2.inRange(hsv, lower_skin, upper_skin)

        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        mask=cv2.medianBlur(mask,5)


        im2, cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        counter=0
        for c in cnts:
            if cv2.contourArea(c) < 0:
                continue
            x, y, calW, calH = cv2.boundingRect(c)
            cv2.rectangle(image, (x,y), (x+calW,y+calH), (0, 255, 0), 2)
            counter+=1
        if counter>1:
            raise Exception('Calibrate with only one object')
        print('width-',calW,'  ','height-',calH)
        

        cv2.imshow('img',image)


        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            cap.release()
    except Exception as e:
        print('Calibration error has occured.\nPlease recalibrate.')
        

##calibrate()
##masala()
##stick()
##vid_masala()
##vid_stick()
            
