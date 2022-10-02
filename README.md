# Chest_X-ray_object_detection_project
Kaggle - VinBigData chest X-ray abnormalities detection contest </br>
url: https://www.kaggle.com/competitions/vinbigdata-chest-xray-abnormalities-detection/overview </br>

### Introduction
* Why Chest X-ray?
  * Chest X-ray는 기본중에 기본인 검사.
  * 생명과 직결되는 부위이기 때문에 정확한 진단이 필요하다.
  * 다른 부위의 X-ray와는 다르게 놓칠 가능성이 있는 부위라 많고 많은 X-ray data중 chest X-ray를 선택하였다.
  
* Why Chest X-ray needs AI?
  * 예를 들어 종양 판독의 경우 종양이 크다면 누구나 판독이 가능하다. 하지만 만약 결절의 size가 작다면 놓칠 수 있는 가능성이 있다.
  * 이렇게 병변을 놓치지 않기위해 AI가 의사의 도움이 되어 진단에 도움이 될 수 있다.
  * 또한 일반 X-ray 전문의사(방사선과)가 아니더라도 판독에 도움을 받을 수 있기때문에 AI를 이용한다면 좀 더 정확하게 판독이 가능할 것이다.
* purpose </br>
폐와 관련된 14가지의 질병을 detecting하여 data augmentation에 따른 여러 model의 performance 비교

### Materials & Methods
* Materials
  * Vietnam hospitals dataset </br>
  (the Hospital 108 and the Hanoi Medical University Hospital)
  * train images: 15,000 (normal: 10,606, patient: 4,394)
  * test images: 3,000
  * bbox info: image_id, class_id, x_min, y_min, x_max, y_max
  * 병명 사전조사: </br>
  https://www.notion.so/63d70daf163d4c82b4027d85a9bc9e86

* Methods
  * Tools: OpenCV, PyTorch, numpy, pandas, sklearn, seaborn, matplotlib
  * Augmentations: Rotation(90º), Flip(horizontal), Zoomin(10%), Cutmix, CLAHE, Equlization, Mosaic, Cutmix + Mosaic
  * Models: EfficientDet(소정), Faster R-CNN(봉학,현나), YOLOX(수현)
  * Workflow
   ![화면 캡처 2022-09-30 140330](https://user-images.githubusercontent.com/61971952/193194200-5f44aa1e-2fd4-410a-be1b-1d16b6be21cc.png)

### Results
* EDA
  * 정상인의 데이터를 삭제하고 적은 양의 환자 데이터만 남음
  * 라벨 간의 극단적인 양 차이 -> 데이터 불균형
  * 단일 이미지안에 다중 라벨
  * <img src="https://user-images.githubusercontent.com/61971952/193209874-ebc78a59-5b58-4816-8412-c841a3b6099f.png" width="600" height="400"/>

* Augmentation에 따른 dataset 종류
  * category A: no augmentation (4,394장)
  * category B: rotation, flip, zoomin (17,576장)
  * categroy C: rotation, flip, zoomin, cutmix, CLAHE, equalization, mosaic, cutmix+mosaic (30,758장)
  * category D: 데이터 불균형 해소를 위해 가장 적은 양의 라벨을 갖는 사진만 augmentation을 적용하고 나머지 라벨은 down sampling (5,999장)
  * <img src="https://user-images.githubusercontent.com/61971952/193212025-c29832b9-b649-41f9-8e58-7ad8a5b25c56.png" width="400" height="200"/>
  
  
* Model에 따른 성능 비교(kaggle score)
</br>

Model | Category A | Category B | Category C | Category D
-------|-------|-------|-------|-------|
EfficientDet | 0.038 | 0.046 | 0.052 | --
Faster R-CNN | 0.012 | 0.098 | 0.013 | --
YOLOX  |  0.021  | 0.068 | 0.147 | 0.070
   
</br>


### Discussion
* Bio의 trend인 object detection 을 공부하기 위하여 선택한 프로젝트
* Model selection
  * 1 stage model
    * YOLOX: 1 stage에서 유명하고 속도가 빠름
    * EfficientDet (one-stage detector paradigm 기반으로 구성됨): 사람들이 주로 사용하는 YOLO v5보다 average precision이 좋음 
  * 2 stage model
    * Faster R-CNN: 이전 수업에서 사용했던 model이 1 stage라서 2 stage 공부 겸 여전히 현역으로 쓰이고 있는 기초적인 모델
* Data 양이 15,000장인줄 알았는데 data를 분석한 결과 정상인을 제외한 결과 환자의 data는 4,394장이었다. </br>
질병을 학습해야하는 model이기때문에 환자의 data만 갖고 학습을 시켜야하는데 data의 양이 너무 적어 양을 늘리기 위하여 여러 augmentation을 적용해보았다. </br>
 Augmentation에 따른 성능 평가를 비교해 보기위해 augmentation을 안한 A그룹과 기본적인 augmentation을 한 B그룹, 마지막으로 기본적인 augmentation외 여러 다양한 기법까지 적용한 C그룹으로 나누었다. </br>
 그 결과 3개의 model 모두 성능이 향상됨을 확인하였다.
* ✔️Faster r-cnn은 다시 해보기
* 또한 data내에서 모든 label이 비슷한 양으로 존재하지않고 특정 label위주로 존재하고있다. 즉, data imbalance가 심한상황. </br>
Data imbalance 문제를 해결하기 위해 너무 많은 양을 갖고있는 특정 label은 down sampling하고 적은 양의 label에 여러가지 augmentation으로 up sampling하는 작업을 하였다. </br>
가장 적은 양을 갖는 label은 1,12번이었고 가장 많이 존재하는 label은 0,3,11,13이다. </br>
1,12에는 Rotation, Flip, Zoomin, Cutmix, CLAHE, Equalization 하고</br>
0,3,11,13은 약 3,000개로 down sampling하여 label당 데이터 개수를 비슷하게 만들어서 성능을 확인해보았다. → D그룹 </br>
가장 성능이 좋았던 YOLOX로 D그룹을 학습한 결과 A그룹에 비해 성능이 향상됨을 확인할 수 있었고 기본 augmentation
### MEMO
##### Faster R-CNN
Faster R-CNN use the 'Pascal VOC dataset format'.
In 'Pascal VOC format', the bbox is represented as [x_min, y_min, x_max, y_max']

##### YOLO
In 'YOLO', the bbox is represented as [x_mid, y_mid, width, height]
