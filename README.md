# Mask-NoMask-LIVE Detection Alarm 
### **YOLOv5** architecture used for train the object detection model. 


### Dataset - [kaggle link](https://www.kaggle.com/datasets/akhilsharmaa/mask-nomask-yolov5)
This is **annoted & preproccesed** data that is formated in the **YOLOv5 supported formated**. You only have to feed the `dataset.yaml` file in the YOLOv5 training command.

<img width="964" alt="Screenshot 2023-05-07 at 11 56 36 AM" src="https://user-images.githubusercontent.com/74103314/236661564-a983b8ed-d019-4edc-aa44-0cba01163d9f.png">


<br> 

# Training the MODEL 
![val_batch1_labels](https://user-images.githubusercontent.com/74103314/236662698-ac88f6f8-ac9f-49f6-a07c-f2562bb1454c.jpg)

Model [model_link](https://github.com/akhilsharmaa/NO-MASK-Detection-YOLOv5/blob/main/model.pt) is train using  **736 training images & 184 validation images** not same resolution. **30 epochs** are done on the dataset. The Epoch summary after running 30 epochs on the dataset: 

```      
      Epoch    GPU_mem   box_loss   obj_loss   cls_loss     Instances        Size
      29/29         0G    0.03029    0.02481   0.001696          92        416: 1
                 Class     Images  Instances          P           R         mAP50   
                   all        184       1042      0.891        0.794         0.87      0.467
```

