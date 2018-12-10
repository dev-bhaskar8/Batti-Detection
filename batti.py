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

global idealMasalaH
global idealMasalaW
global idealStickH
global idealStickW
global unitW
global unitH
global unit
idealMasalaH=20
idealMasalaW=20
idealStickH=20
idealStickW=20
unitW=20
unitH=20
unit=20
trigger=False

def start():
    try:
        cap=cv2.VideoCapture(0)
        global masalaH
        global masalaW
        global stickH
        global stickW

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
                #c = max(cnts, key = cv2.contourArea)
                if cv2.contourArea(c) < 0:
                    continue

                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(image, (x,y), (x+w,y+h), (0, 255, 0), 2)

                
                rect = cv2.minAreaRect(c)
                masalaH=rect[1][1]
                masalaW=rect[1][0]
                
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                cv2.drawContours(image,[box],0,(0,191,255),2)

            lower_skin1 = np.array([[20, 100, 100]])
            upper_skin1 = np.array([30, 255, 255])

            mask1 = cv2.inRange(hsv, lower_skin1, upper_skin1)
            
            im2, cnts1, hierarchy = cv2.findContours(mask1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            
            for c1 in cnts1:
                #c1 = max(cnts1, key = cv2.contourArea)
                if cv2.contourArea(c1) < 0:
                    continue

                (x1, y1, w1, h1) = cv2.boundingRect(c1)
                cv2.rectangle(image, (x1,y1), (x1+w1,y1+h1), (255,0 , 0), 2)

                
                rect1 = cv2.minAreaRect(c1)
                stickH=rect1[1][1]
                stickW=rect1[1][0]
                box1 = cv2.boxPoints(rect1)
                box1 = np.int0(box1)
                cv2.drawContours(image,[box1],0,(0,0,255),2)
                

            cv2.imshow('start', image)
            cv2.imshow('start_mask', mask)
            
            masalaH=masalaH/unit
            masalaW=masalaW/unit
            stickH=stickH/unit
            stickW=stickW/unit
            masalaA=masalaH*masalaW
            idealMasalaA=idealMasalaH*idealMasalaW
            stickA=stickH*stickW
            idealStickA=idealStickH*idealStickW
            if(masalaH<idealMasalaH or masalaH>idealMasalaH or stickH<idealStickH or stickH>idealStickH or masalaW<idealMasalaW or masalaW>idealMasalaW or masalaA<idealMasalaA or masalaA>idealMasalaA or stickA<idealStickA or stickA>idealStickA):
                trigger=True
                print("Faulty detected")
            else:
                pass

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print("Human intervention required.",e)
        cv2.destroyAllWindows()
        cap.release()
    

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
            c = max(cnts, key = cv2.contourArea)
            if cv2.contourArea(c) < 0:
                continue
            x, y, calW, calH = cv2.boundingRect(c)
            cv2.rectangle(image, (x,y), (x+calW,y+calH), (0, 255, 0), 2)
            counter+=1
        if counter>1:
            raise Exception('Calibrate with only one object')
        unitW = calW
        unitH = calH
        global unit
        unit=max(unitW,unitH)
        print("Calibration successul, the unit factor is - ",unit)
        
        cv2.imshow('img',image)


        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            cap.release()
    except Exception as e:
        print('Calibration error has occured.\nPlease recalibrate.')
        cv2.destroyAllWindows()
        cap.release()

def ideal():
    try:
        global idealMasalaH
        global idealMasalaW
        global idealStickH
        global idealStickW
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
                c = max(cnts, key = cv2.contourArea)
                if cv2.contourArea(c) < 0:
                    continue

                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(image, (x,y), (x+w,y+h), (0, 255, 0), 2)

                
                rect = cv2.minAreaRect(c)
                idealMasalaH=rect[1][1]
                idealMasalaW=rect[1][0]
                
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                cv2.drawContours(image,[box],0,(0,191,255),2)

            lower_skin1 = np.array([[20, 100, 100]])
            upper_skin1 = np.array([30, 255, 255])

            mask1 = cv2.inRange(hsv, lower_skin1, upper_skin1)
            
            im2, cnts1, hierarchy = cv2.findContours(mask1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            
            for c1 in cnts1:
                c1 = max(cnts1, key = cv2.contourArea)
                if cv2.contourArea(c1) < 0:
                    continue

                (x1, y1, w1, h1) = cv2.boundingRect(c1)
                cv2.rectangle(image, (x1,y1), (x1+w1,y1+h1), (255,0 , 0), 2)

                
                rect1 = cv2.minAreaRect(c1)
                idealStickH=rect1[1][1]
                idealStickW=rect1[1][0]
                box1 = cv2.boxPoints(rect1)
                box1 = np.int0(box1)
                cv2.drawContours(image,[box1],0,(0,0,255),2)
                

            cv2.imshow('confirm?', image)

            
            
            idealMasalaH=idealMasalaH/unit
            idealMasalaW=idealMasalaW/unit
            idealMasalaA=idealMasalaH*idealMasalaW
            idealStickH=idealStickH/unit
            idealStickW=idealStickW/unit
            idealStickA=idealStickH*idealStickW
            
            

            if cv2.waitKey(1) & 0xFF == ord('y'):
                break
        cap.release()
        cv2.destroyAllWindows()
        print("The dimentions of the ideal product are ",idealMasalaH+idealStickH," units"," by ",idealMasalaW,"units")
    except Exception as e:
        print(e)
        cap.release()
        cv2.destroyAllWindows()
x=1
while(x>0):
    inputtext=input("Write your command $ ")
    if(inputtext == "calibrate"):
        calibrate()
    elif(inputtext == "ideal"):
        ideal()
    elif(inputtext == "start"):
        start()
    elif(inputtext == "quit"):
        quit()
    else:
        print("Please enter a valid command")
