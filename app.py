import torch 
import numpy as np
import cv2
import vlc
from playsound import playsound
 

model_path = "model.pt"
alarm = vlc.MediaPlayer("alarm.mp3") # Alarm Sound 

''' Import the YOLO-V5 model '''
model = torch.hub.load('ultralytics/yolov5', 'custom', model_path)

''' Returns 2 objects {Image & is_NoMask_Detected} '''
def detect_NoMask_InFrame(img):

    ''' Fit Image in the model '''
    results = model(img)  
    labels_df = results.pandas().xyxy[0] # Labels DataFrame
    flagNoMask = False
    
    # img = results.show()
    # return img, False;
    
    for ind in labels_df.index:
        # print(result['xmin'], cnt)
        x, y = int(labels_df["xmin"][ind]), int(labels_df["ymin"][ind])
        w, h = int(labels_df["xmax"][ind]), int(labels_df['ymax'][ind])
        confidenceScore = labels_df["confidence"][ind]
        
        if confidenceScore >= 0.4: 
            
            if labels_df["class"][ind]: 
                # if MASK detected 
                color = (0, 255, 0)
                img = cv2.rectangle(img, (x, y), (w, h),  color, 1)
                
            else :  
                # if NO-MASK detected 
                flagNoMask = True
                color = (255, 0, 0)
                img = cv2.rectangle(img, (x, y), (w, h), color, 2)
                img = cv2.putText(img, 'NO-MASK', (x, y-6), cv2.FONT_HERSHEY_SIMPLEX, 
                                  0.6, color, 1,  cv2.LINE_AA)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img, flagNoMask 


''' Take input from the webcam '''
cap = cv2.VideoCapture(0)

while True: 
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect the Frame Objects Using YOLO model 
    frame, noMask = detect_NoMask_InFrame(frame) 
    
    # Play the sound if mask detected
    if noMask : 
        alarm.play()
    else :
        alarm.stop()
    
    cv2.imshow("Webcam", frame)
    
    if cv2.waitKey(100) & 0xff == ord('q'):
        break;

cv.destroyAllWindows()


''' Take Output from images'''
# img_path = "random_test_images/9e6bf0fbabfbde89c74bff7e25af86b3.jpg"
# img = cv2.imread(img_path)

# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img, noMask = detect_NoMask_InFrame(img)
# cv2.imshow("Image", img)
    
# cv2.waitKey(0)
# cv2.destroyAllWindows()