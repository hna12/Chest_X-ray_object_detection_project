# Chest_X-ray_object_detection_project
Kaggle - VinBigData chest X-ray abnormalities detection contest </br>
url: https://www.kaggle.com/competitions/vinbigdata-chest-xray-abnormalities-detection/overview </br>

### ๐ซIntroduction
* Why Chest X-ray?
  * Chest X-ray๋ ๊ธฐ๋ณธ์ค์ ๊ธฐ๋ณธ์ธ ๊ฒ์ฌ.
  * ์๋ช๊ณผ ์ง๊ฒฐ๋๋ ๋ถ์์ด๊ธฐ ๋๋ฌธ์ ์ ํํ ์ง๋จ์ด ํ์ํ๋ค.
  * ๋ค๋ฅธ ๋ถ์์ X-ray์๋ ๋ค๋ฅด๊ฒ ๋์น  ๊ฐ๋ฅ์ฑ์ด ์๋ ๋ถ์๋ผ ๋ง๊ณ  ๋ง์ X-ray data์ค chest X-ray๋ฅผ ์ ํํ์๋ค.
  
* Why Chest X-ray needs AI?
  * ์๋ฅผ ๋ค์ด ์ข์ ํ๋์ ๊ฒฝ์ฐ ์ข์์ด ํฌ๋ค๋ฉด ๋๊ตฌ๋ ํ๋์ด ๊ฐ๋ฅํ๋ค. ํ์ง๋ง ๋ง์ฝ ๊ฒฐ์ ์ size๊ฐ ์๋ค๋ฉด ๋์น  ์ ์๋ ๊ฐ๋ฅ์ฑ์ด ์๋ค.
  * ์ด๋ ๊ฒ ๋ณ๋ณ์ ๋์น์ง ์๊ธฐ์ํด AI๊ฐ ์์ฌ์ ๋์์ด ๋์ด ์ง๋จ์ ๋์์ด ๋  ์ ์๋ค.
  * ๋ํ ์ผ๋ฐ X-ray ์ ๋ฌธ์์ฌ(๋ฐฉ์ฌ์ ๊ณผ)๊ฐ ์๋๋๋ผ๋ ํ๋์ ๋์์ ๋ฐ์ ์ ์๊ธฐ๋๋ฌธ์ AI๋ฅผ ์ด์ฉํ๋ค๋ฉด ์ข ๋ ์ ํํ๊ฒ ํ๋์ด ๊ฐ๋ฅํ  ๊ฒ์ด๋ค.
* purpose </br>
ํ์ ๊ด๋ จ๋ 14๊ฐ์ง์ ์ง๋ณ์ detectingํ์ฌ data augmentation์ ๋ฐ๋ฅธ ์ฌ๋ฌ model์ performance ๋น๊ต

### ๐ซMaterials & Methods
* Materials
  * Vietnam hospitals dataset </br>
  (the Hospital 108 and the Hanoi Medical University Hospital)
  * train images: 15,000 (normal: 10,606, patient: 4,394)
  * test images: 3,000
  * bbox info: image_id, class_id, x_min, y_min, x_max, y_max
  * image size: 512 x 512
  * ๋ณ๋ช ์ฌ์ ์กฐ์ฌ: </br>
  https://www.notion.so/63d70daf163d4c82b4027d85a9bc9e86

* Methods
  * Tools: OpenCV, PyTorch, numpy, pandas, sklearn, seaborn, matplotlib
  * Augmentations: Rotation(90ยบ), Flip(horizontal), Zoomin(10%), Cutmix, CLAHE, Equlization, Mosaic
  * Models: EfficientDet(์์ ), Faster R-CNN(๋ดํ,ํ๋), YOLOX(์ํ)
  * Workflow
   <img src="https://user-images.githubusercontent.com/61971952/193194200-5f44aa1e-2fd4-410a-be1b-1d16b6be21cc.png" width=70% height=70%>

### ๐ซResults
* EDA
  * ์ ์์ธ์ ๋ฐ์ดํฐ๋ฅผ ์ญ์ ํ๊ณ  ์ ์ ์์ ํ์ ๋ฐ์ดํฐ๋ง ๋จ์
  * ๋ผ๋ฒจ ๊ฐ์ ๊ทน๋จ์ ์ธ ์ ์ฐจ์ด -> ๋ฐ์ดํฐ ๋ถ๊ท ํ
  * ๋จ์ผ ์ด๋ฏธ์ง์์ ๋ค์ค ๋ผ๋ฒจ
  * <img src="https://user-images.githubusercontent.com/61971952/193209874-ebc78a59-5b58-4816-8412-c841a3b6099f.png" width="600" height="400"/>

* Augmentation์ ๋ฐ๋ฅธ dataset ์ข๋ฅ
  * category A: no augmentation (4,394์ฅ)
  * category B: rotation, flip, zoomin (17,576์ฅ)
  * categroy C: rotation, flip, zoomin, cutmix, CLAHE, equalization, mosaic (30,758์ฅ)
  * category D: ๋ฐ์ดํฐ ๋ถ๊ท ํ ํด์๋ฅผ ์ํด ๊ฐ์ฅ ์ ์ ์์ ๋ผ๋ฒจ์ ๊ฐ๋ ์ฌ์ง๋ง augmentation์ ์ ์ฉํ๊ณ  ๋๋จธ์ง ๋ผ๋ฒจ์ down sampling (5,999์ฅ)
  * <img src="https://user-images.githubusercontent.com/61971952/193212025-c29832b9-b649-41f9-8e58-7ad8a5b25c56.png" width="400" height="200"/>
  </br>

  Category A | Category B | Category C | Category D
  ------|-------|-------|-------|
   ์๋ณธ | ROTATION | ROTATION | ROTATION 
   &nbsp; | FLIP | FLIP | FLIP 
   &nbsp; | ZOOM IN | ZOOM IN | ZOOM IN 
   &nbsp; |  | CUTMIX | CUTMIX
   &nbsp; |  | CLAHE | CLAHE
   &nbsp; |  | EQUALIZATION | EQUALIZATION
   &nbsp; |  | MOSAIC | MOSAIC
  </br>
  
* Model์ ๋ฐ๋ฅธ ์ฑ๋ฅ ๋น๊ต(kaggle score)
</br>

Model | Category A | Category B | Category C | Category D
-------|-------|-------|-------|-------|
EfficientDet | 0.038 | 0.046 | 0.052 | --
Faster R-CNN | 0.012 | 0.098 | 0.013 | --
YOLOX  |  0.021  | 0.068 | 0.147 | 0.070
   
</br>
* ์์ธก ์ด๋ฏธ์ง
<img src = "https://user-images.githubusercontent.com/61971952/197476506-f159bd0a-d6ac-41b6-8a06-229f5eb3b9ea.png" width = 40% height = 40%>

### ๐ซDiscussion
* Bio์ trend์ธ object detection ์ ๊ณต๋ถํ๊ธฐ ์ํ์ฌ ์ ํํ ํ๋ก์ ํธ
* ํ์ต data์์์ train & valid๋ก ๋๋์ง ์๊ณ  Group K-Fold๋ฅผ ์ฌ์ฉํ๋ ์ด์ ?
  * ์ ์ data set์ ๋ํ์ฌ ์ ํ๋๋ฅผ ํฅ์์ํฌ ์ ์๋ค.
  * โต training/validation/test ์ธ๊ฐ์ ์ง๋จ์ผ๋ก ๋ถ๋ฅํ๋ ๊ฒ๋ณด๋ค training & test๋ก๋ง ๋ถ๋ฅ์ ํ์ตํ  data๊ฐ ๋ ๋ง๊ฒ๋์ด underfitting๋ฑ ์ฑ๋ฅ์ด ๋ฏธ๋ฌ๋๋ model๋ก ํ์ต๋์ง ์๋๋ก ํจ.
  * ๋ํ 1๊ฐ์ ์ด๋ฏธ์ง์ ๋ค์ค label์ด๋ฏ๋ก ์์ธก์ ์ ํ๋๋ฅผ ํ์คํ ํ๊ฐํ๊ธฐ์ํด train set & valid์ ํฌํจ๋ image๊ฐ ๊ฒน์น์ง ์๋๋ก ํ๊ธฐ์ํ์ฌ k-fold์ค์์๋ group k-fold๋ฅผ ์ฌ์ฉํ์๋ค.
  * ํ์ง๋ง ํ์ต ์๊ฐ์ด ๊ฝค ์ค๋๊ฑธ๋ ค ์๊ฐ์ k = 1 ๋ก ์ธํํด ๋์์. </br>
(์ฆ, kfold๋ฅผ ํ์ง ์๊ณ  train:valid = 8:2๋ก ๋ฐ์ดํฐ์์ ๋ณ๋๋ก ๋๋  ํ์ตํ ๊ฒ๊ณผ ๊ฐ์.)
  * 10epoch์ผ๋ก ํ์ต์ k=1๋ก๋ง ๋ณธ๊ฒ๊ณผ k=5๋ก ํ์ฌ ์ฑ๋ฅ์ ๋น๊ตํ ๊ฒฐ๊ณผ public score๊ฐ 0.014์์ 0.025๋ก ํฅ์๋จ์ ํ์ธํ  ์ ์์๋ค. 
  * ๊ทธ๋ฌ๋ฏ๋ก ๋ฐ์ดํฐ๋ฅผ augmenationํ B์ C๋ ์ ๋๋ก k = 5๋ก ์ธํํด์ ํ์ตํ๋ค๋ฉด ๋ ์ข์ ์ฑ๋ฅ์ ๋ณด์์ ๋ฏ ํ๋ค.

   </br>

   k | EPOCH | Score | EPOCH | Score
   -------|-------|-------|-------|-------|
   1 | 10e | 0.014 | 20e | 0.016
   5 | 10e | 0.025 | 20e | 0.024

   </br>

* Zoom in augmentation์ 10%๋ก ํ ์ด์ ? </br>
  * 10%๋ณด๋ค ๋ zoom in์ ํ์๊ฒฝ์ฐ ์ด๋ฏธ์ง์ ๊ฐ์ฅ์๋ฆฌ์ ์์นํ๋ ๋ณ๋ณ๋ค์ด ์๋ฆฌ๋ ๊ฒฝ์ฐ๋ค์ด ์์ด์ ์ด๋ฅผ ๋ง๊ธฐ์ํด 10%์ ๋๋ง zoom in์ ํ์๋ค.
* normalization ํ ๋ค์ size(512x512) ์ฌ์ ์์ ์ ์ํํจ์๋ฐ๋ผ ๊ฐ์ ๊ฐ์ ๊ฐ๊ฒ๋๋ ๊ฒฝ์ฐ๊ฐ ์์๋ค.
  * ๋ณ๋ณ์ด ๋๋ฌด๋ ์์ bbox์ y_max์ y_min์ด ๋ณ ์ฐจ์ด๊ฐ ๋์ง ์์๊ธฐ ๋๋ฌธ. </br>
์ด๋ฐ ๋ฐ์ดํฐ๋ก์ธํด ํ์ต์ ์ค๋ฅ๊ฐ ๋ฐ์ํ์ฌ ํด๋น ๋ฐ์ดํฐ(10๊ฐ ๋ฏธ๋ง)๋ ์ญ์ ํ๊ธฐ๋ก ํจ.
* Model selection
  * 1 stage model
    * YOLOX: 1 stage์์ ์ ๋ชํ๊ณ  ์๋๊ฐ ๋น ๋ฅด๊ธฐ๋๋ฌธ์ ์ฌ์ฉํจ.
    * EfficientDet (one-stage detector paradigm ๊ธฐ๋ฐ์ผ๋ก ๊ตฌ์ฑ๋จ): ์ฌ๋๋ค์ด ์ฃผ๋ก ์ฌ์ฉํ๋ YOLO v5๋ณด๋ค average precision์ด ์ข๊ธฐ๋๋ฌธ์ ์ ํ.
  * 2 stage model
    * Faster R-CNN: ์ด์  ์์์์ ์ฌ์ฉํ๋ model์ด 1 stage๋ผ์ 2 stage ๊ณต๋ถ ๊ฒธ ์ฌ์ ํ ํ์ญ์ผ๋ก ์ฐ์ด๊ณ  ์๋ ๊ธฐ์ด์ ์ธ ๋ชจ๋ธ์ด๋ผ์ ์ ํํ์์.
* ํ์ตํ๋ data ์์ด 15,000์ฅ์ธ์ค ์์์ง๋ง data๋ฅผ ๋ถ์ํ ๊ฒฐ๊ณผ ์ ์์ธ์ ์ ์ธํ ํ์์ data๋ 4,394์ฅ์ด์๋ค. </br>
  * ์ง๋ณ์ ํ์ตํด์ผํ๋ model์ด๊ธฐ๋๋ฌธ์ ํ์์ data๋ง ๊ฐ๊ณ  ํ์ต์ ์์ผ์ผํ๋๋ฐ data์ ์์ด ๋๋ฌด ์ ์ด ์์ ๋๋ฆฌ๊ธฐ ์ํ์ฌ ์ฌ๋ฌ augmentation์ ์ ์ฉํด๋ณด์๋ค.
  * Augmentation์ ๋ฐ๋ฅธ ์ฑ๋ฅ ํ๊ฐ๋ฅผ ๋น๊ตํด ๋ณด๊ธฐ์ํด augmentation์ ์ํ A๊ทธ๋ฃน๊ณผ ๊ธฐ๋ณธ์ ์ธ augmentation์ ํ B๊ทธ๋ฃน, ๋ง์ง๋ง์ผ๋ก ๊ธฐ๋ณธ์ ์ธ augmentation์ธ ์ฌ๋ฌ ๋ค์ํ ๊ธฐ๋ฒ๊น์ง ์ ์ฉํ C๊ทธ๋ฃน์ผ๋ก ๋๋์๋ค.
  * ๊ทธ ๊ฒฐ๊ณผ 3๊ฐ์ model ๋ชจ๋ augmentation์ ํ๋ฉด ํ ์๋ก ์ฑ๋ฅ์ด ํฅ์๋จ์ ํ์ธํ์๋ค.
* Data๋ด์์ ๋ชจ๋  label์ด ๋น์ทํ ์์ผ๋ก ์กด์ฌํ์ง์๊ณ  ํน์  label์์ฃผ๋ก ์กด์ฌํ๊ณ ์๋ค. ์ฆ, data imbalance๊ฐ ์ฌํ์ํฉ. </br>
  * Data imbalance ๋ฌธ์ ๋ฅผ ํด๊ฒฐํ๊ธฐ ์ํด ๋๋ฌด ๋ง์ ์์ ๊ฐ๊ณ ์๋ ํน์  label(0,3,11,13)์ down samplingํ๊ณ  ์ ์ ์์ ๊ฐ๋ label(1,12)์ ์ฌ๋ฌ๊ฐ์ง augmentation์ผ๋ก up samplingํ๋ ์์์ ํ์๋ค.
  * 1,12์๋ Rotation, Flip, Zoomin, Cutmix, CLAHE, Equalization ์ ์ ์ฉํ๊ณ  </br>
0,3,11,13์ ์ฝ 3,000๊ฐ๋ก down samplingํ์ฌ label๊ฐ์ ๊ทน๋จ์ ์ธ ์ฐจ์ด๊ฐ ์ด๋์ ๋ ํด์๋ D๊ทธ๋ฃน์ ๋ง๋ค์๋ค. </br>
  * ๊ฐ์ฅ ์ฑ๋ฅ์ด ์ข์๊ณ  ํ์ต์๋๊ฐ ๋น ๋ฅธ YOLOX๋ก D๊ทธ๋ฃน์ ํ์ตํ ๊ฒฐ๊ณผ **A๊ทธ๋ฃน์ ๋นํด ์ฑ๋ฅ์ด ํฅ์๋จ** ์ ํ์ธํ  ์ ์์๊ณ  **์์ด ์ ์๋ฐ๋ ๋ถ๊ตฌํ๊ณ  ๊ธฐ๋ณธ 3๊ฐ์ง augmentation์ ํ B๊ทธ๋ฃน๋ณด๋ค ์ฑ๋ฅ์ด ์ข์๋ค.** </br>
  * ํ์ง๋ง ๊ธฐ๋ณธ augmentation์ธ์ ์ถ๊ฐ์ ์ธ augmentation์ ํ๋ C๊ทธ๋ฃน๋ณด๋ค๋ ์ฑ๋ฅ์ด ๋ ๋์๋ค. </br>
(์ด๋ data์ ์์ด 6๋ฐฐ๋ ์ฐจ์ด๊ฐ ๋๊ธฐ๋๋ฌธ์ ๋์จ ๊ฒฐ๊ณผ)
  * C๊ทธ๋ฃน์์ ํจ์ฌ ์ฑ๋ฅ์ด ์ข์๋๊ฒ์ ํตํด data imbalance๋ฅผ ํด๊ฒฐํ๊ฒ๋ณด๋ค๋ data์ ์์ด ์ถฉ๋ถํ ์๋๊ฒ์ด ์ฑ๋ฅํฅ์์ ๋ ๋ง์ ํจ๊ณผ๊ฐ ์์์ ์ ์ถํ  ์ ์์๊ณ  </br>
**imbalance์ data์ ์์ ๋์์ ํด๊ฒฐํ๋ค๋ฉด ์ด๋ณด๋ค ํจ์ฌ ๋ ์ข์ ์ฑ๋ฅ์ ๋ผ ์ ์์ง ์์๊น ์ถ๋ค.**

### Ref
- https://www.kaggle.com/code/dschettler8845/visual-in-depth-eda-vinbigdata-competition-data
- https://www.kaggle.com/code/yerramvarun/pytorch-fasterrcnn-with-group-kfold-14-class
- https://www.kaggle.com/code/pestipeti/vinbigdata-fasterrcnn-pytorch-inference/notebook
- https://www.kaggle.com/code/pestipeti/vinbigdata-fasterrcnn-pytorch-train/notebook

### MEMO
##### Faster R-CNN
Faster R-CNN use the 'Pascal VOC dataset format'.
In 'Pascal VOC format', the bbox is represented as [x_min, y_min, x_max, y_max']

##### YOLO
In 'YOLO', the bbox is represented as [x_mid, y_mid, width, height]
