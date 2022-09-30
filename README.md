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
![다운로드](https://user-images.githubusercontent.com/61971952/193208507-db90dc58-47ec-4ceb-9f6a-591c7c5d1644.png)

* Augmentation에 따른 dataset 종류
  * category A: no augmentation (4,394장)
  * category B: rotation, flip, zoomin
  * categroy C: rotation, flip, zoomin, cutmix, CLAHE, equalization, mosaic, cutmix+mosaic
  * category D(for data imbalance issue)

### Discussion

### MEMO
##### Faster R-CNN
Faster R-CNN use the 'Pascal VOC dataset format'.
In 'Pascal VOC format', the bbox is represented as [x_min, y_min, x_max, y_max']

##### YOLO
In 'YOLO', the bbox is represented as [x_mid, y_mid, width, height]
