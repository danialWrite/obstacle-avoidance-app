import cv2
import numpy as np
var = 4
obs1cols=640
obs1cole=660
obs1rows=118
obs1rowe=208

obs2cols=640
obs2cole=660
obs2rows=0
obs2rowe=90
grows=104
growe=208
gcols=10
gcole=134
stop=0
stopk=0
evt = 0
c=255
onetime=1
count = 0
def mouseclick(event,xpos,ypos,flag,param):
    global evt
    if event==cv2.EVENT_LBUTTONDOWN:
        evt=1
        print(xpos,ypos)
    if event==cv2.EVENT_RBUTTONDOWN:
        evt=2
cv2.namedWindow('WINDOW')
cv2.setMouseCallback('WINDOW',mouseclick)
while True:
    ground = np.zeros((312,700,3),dtype = np.uint8)
    ground [:,:] = (255,255,255)
    car = np.zeros((200,200,3),dtype = np.uint8)
    car [:,:] = (255,255,255)
    obstacle1 = np.zeros((90,20,3),dtype = np.uint8)
    obstacle1 [:,:] = (0,0,0)
    obstacle2 = np.zeros((90,20,3),dtype = np.uint8)
    obstacle2 [:,:] = (c,c,c)
    obstacle3 = np.zeros((50,20,3),dtype = np.uint8)
    obstacle3 [:,:] = (0,0,0)

    cv2.circle(car,(60,150),20,(0,0,0),-1)
    cv2.circle(car,(140,150),20,(0,0,0),-1)
    cv2.rectangle(car,(60,90),(140,150),(0,0,0),-1)
    cv2.rectangle(car,(40,70),(160,90),(0,0,0),-1)

    carROI = car[68:172,38:162] # rows = 104 cols = 124
    ground[grows:growe,gcols:gcole]=carROI
    ground[obs1rows:obs1rowe,obs1cols:obs1cole]=obstacle1
    ground[obs2rows:obs2rowe,obs2cols:obs2cole]=obstacle2
    cv2.imshow('WINDOW',ground)

    # if grows ==104:
    #     cols+=1
    #     cols+=1
    #     row
    obs2cols-=var
    obs2cole-=var
    obs1cols-=var
    obs1cole-=var

    if obs1cols==300 and onetime==1:
        c=0
        obs2cols=640
        obs2cole=660
        onetime=0
    if evt == 1 and stop == 0:
        grows-=104
        growe-=104
        stopk=0
        evt=0
        if grows==0:
            stop=1
    if evt == 1 and stop ==1:
        grows+=104
        growe+=104
        evt=0
        if grows==104:
            stop=0
    if evt == 2 and stopk == 0:
        grows+=104
        growe+=104
        stopk =1
        stop=0
    if obs1cols<=4:
        obs1cols=640
        obs1cole=660
    if obs2cols<=4:
        obs2cols=640
        obs2cole=660
    if count >=1000:
        var=5
    if count >=2000:
        var=6
    if count >=3000:
        var=7
    if obs1cols <= 130 and grows ==104 or obs2cols<=130 and grows == 0:
        break
    if cv2.waitKey(1) & 0xff == ord(' '):
        break
    count+=1
