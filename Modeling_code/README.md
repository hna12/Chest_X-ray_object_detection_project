### Modeling10,20e_A.ipynb 
* A dataset을 10,20 epoch 돌린것
* hyperparameter
	* SGD
	* Learning rate = 0.005
	* Momentum = 0.9
	* Weight Decay = 0.0005
* 30e의 경우는 epoch만 바꾼것으로 동일하여 업로드하지 않음
* 시간이 없어 folds setting은 1로 두어 총 한번의 train & validation을 한 코드 (epoch * 1)
### A_10,20e_5fold.ipynb
* A dataset 10epoch 돌린것
* hyperparameter 위와 동일
* 위의 코드들과 달리 folds setting을 5로 두어 총 다섯번의 train & validation을 한 코드.
* 즉, 제대로 group k-fold를 썼다고 보면 됨.
* epoch * 5
* 시간 상 10e, 20e만 진행
