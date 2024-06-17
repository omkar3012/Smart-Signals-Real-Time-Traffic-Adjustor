# Smart Signals: A Real-Time Traffic Adjustor

A dynamic traffic light adjustor to judiciously distribute green signal times in order to reduce wait times at intersections, using Image Recognition, Time Series Analysis and a variety of algorithms.
It's key features include
1. Image Detection-based traffic light controller based on intensity of incoming traffic
2. Traffic light set for a longer/shorter duration of time accordingly
3. Predicts traffic intensity based on the day of the week

## Objectives
1. To reduce pollution caused by vehicles waiting at the traffic signals/ in congestion.
2. To make the traffic signaling process more efficient, fast, and capable of working without human interference.\
3. To expedite the time taken by emergency vehicles to reach their destinations.



## System Diagram
### System Diagram:
![Major Project System Diagram](https://github.com/omkar3012/Smart-Signals-Real-Time-Traffic-Adjustor/assets/95969528/13e15560-45f7-44ff-9415-1b0bc226b591)

### Image Processing sub-system diagram

![Major_Project_System_Diagram_Image_Processing_submodule](https://github.com/omkar3012/Smart-Signals-Real-Time-Traffic-Adjustor/assets/95969528/3244d1a3-71a3-4c52-9814-30694e98bb27)

### Object Detection sub-system diagram
![Major_Project_System_Diagram_Object_Detection_submodule](https://github.com/omkar3012/Smart-Signals-Real-Time-Traffic-Adjustor/assets/95969528/42d3acfa-55d4-4038-97bb-90d1a971562b)

### Vehicle Prediction sub-system diagram
![Major_Project_System_Diagram_Vehicle_Prediction_module](https://github.com/omkar3012/Smart-Signals-Real-Time-Traffic-Adjustor/assets/95969528/420391d1-49ee-48c8-ae55-2a9c58552a96)

## Methodology
1. Vehicle Detection Module
Input taken from traffic signal camera 
Image Processing using OpenCV
Object Detection using YOLOv2 (trained on COCO dataset)

2. Vehicle Prediction Module
Random Forest Regressor (Trained on historical traffic data)
Traffic congestion prediction, given date-time conditions

3. Switching Algorithm
Exponential Equation approach, ensures a fair green-time distribution
Takes detection results from Vehicle Detection module
Takes prediction results from Vehicle Prediction module

## Technology Stack
1. Python
2. Sci-kit Learn library
3. YOLOv2 model, DarkFlow software
4. OpenCV image processing library

## Dataset
1. Vehicle Detection (YOLOv2) model: Trained on ![COCO dataset](https://cocodataset.org/#home)
2. Vehicle Prediction (Time Series Analyser) model: Trained on ![traffic data](https://www.kaggle.com/datasets/fedesoriano/traffic-prediction-dataset)

## Preview
### Miniature model:

Input: 

![Miniature_Input](https://github.com/omkar3012/Smart-Signals-Real-Time-Traffic-Adjustor/assets/95969528/2840c461-80c1-4756-b5ff-a5cc02a23728)

Output: 

![Miniature_Output](https://github.com/omkar3012/Smart-Signals-Real-Time-Traffic-Adjustor/assets/95969528/24151dda-24b2-4016-983f-e907912cd716)


### Real-Time Testing:

Input:

![vehicle_real_input](https://github.com/omkar3012/Smart-Signals-Real-Time-Traffic-Adjustor/assets/95969528/3a2b21cb-51b8-4b36-8a4c-14d73cfb10d1)

Output: 

![Vehicle_Detection_Real_Output](https://github.com/omkar3012/Smart-Signals-Real-Time-Traffic-Adjustor/assets/95969528/e672a026-8258-4c18-a235-79679e7c7829)

![Switching_Algo_Output](https://github.com/omkar3012/Smart-Signals-Real-Time-Traffic-Adjustor/assets/95969528/f8ecbc1b-ae38-4586-bdb3-bd74eb802943)


Live-Feed: 

## Future Scope
1. Live-feed directly picked up from traffic cameras to ensure timely traffic management.
2. Introduction of pedestrian, two-wheeler and three-wheeler detection.
3. Detection of emergency vehicles to prioritise them.

