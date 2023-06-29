# [Real-Time-Face-Mask-Detection-Alarm ](https://youtu.be/q1qlpDHZvZQ)
### **YOLOv5** architecture used for train the object detection model. 


### Dataset - [kaggle link](https://www.kaggle.com/datasets/akhilsharmaa/mask-nomask-yolov5)
This is **annoted & preproccesed** data that is formated in the **YOLOv5 supported formated**. You only have to feed the `dataset.yaml` file in the YOLOv5 training command.
DEMO Video [link](https://youtu.be/q1qlpDHZvZQ)


https://github.com/akhilsharmaa/Real-Time-Face-Mask-Detection-YOLOv5/assets/74103314/8f605092-4e2d-44dd-993d-e6aa7d948d3d


# Training the MODEL 
Model [model_link](https://github.com/akhilsharmaa/NO-MASK-Detection-YOLOv5/blob/main/model.pt) is train using  **736 training images & 184 validation images** not same resolution. **30 epochs** are done on the dataset. The Epoch summary after running 30 epochs on the dataset: 

![val_batch1_labels](https://user-images.githubusercontent.com/74103314/236662698-ac88f6f8-ac9f-49f6-a07c-f2562bb1454c.jpg)

```      
      Epoch    GPU_mem   box_loss   obj_loss   cls_loss     Instances        Size
      29/29         0G    0.03029    0.02481   0.001696          92        416: 1
                 Class     Images  Instances          P           R         mAP50   
                   all        184       1042      0.891        0.794         0.87      0.467
```

