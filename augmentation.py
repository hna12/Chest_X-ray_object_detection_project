# Importing library
!pip install albumentations==0.4.6
import cv2
import json
from PIL import Image
from tqdm import tqdm
import imgaug.augmenters as iaa
import albumentations as A
from albumentations.pytorch.transforms import ToTensorV2

import torch
import torchvision

from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision.models.detection import FasterRCNN

from google.colab.patches import cv2_imshow

# ROTATION 90º
def rotation_image(path, image_list):
    for path in image_list:
        img = cv2.imread(path)
        (h, w) = img.shape[:2]
        (cX, cY) = (w/2, h/2)
        M = cv2.getRotationMatrix2D((cX,cY), 90, 1.0)
        rotated_img = cv2.warpAffine(img, M, (w,h))
        img_name = path.split('/')[-1].split('.')[0]
        cv2.imwrite(f'{path}/{img_name}'+'_rotated.png', rotated_img)

# FLIP(HORIZONTAL)
def flip_image(path, image_list):
    for path in image_list:
        img = cv2.imread(path)
        flipped_img = cv2.flip(img, 1)
        img_name = path.split('/')[-1].split('.')[0]
        cv2.imwrite(f'{path}/{img_name}'+'_flip.png', flipped_img)

# ZOOM IN 10%
def zoom_image(path, image_list):
    for path in image_list:
        img = cv2.imread(path)
        augment_img_zoom = iaa.Affine(scale=(1.1))
        zoom_image = augment_img_zoom.augment_image(img)
        img_name = path.split('/')[-1].split('.')[0]
        cv2.imwrite(f'{path}/{img_name}'+'_zoom.png', zoom_image)

# CLAHE(Contrast Limited Adaptive Histogram Equalization)
def clahe_image(path, image_list):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    for path in image_list:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        clahe_img = clahe.apply(img)
        img_name = path.split('/')[-1].split('.')[0]
        cv2.imwrite(f'{path}/{img_name}'+'_clahe.png', clahe_img)

# EQUALIZEHIST
def equ_image(path, image_list):
    for path in image_list:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        equ_img = cv2.equalizeHist(img)
        img_name = path.split('/')[-1].split('.')[0]
        cv2.imwrite(f'{path}/{img_name}'+'_equ.png', equ_img)

