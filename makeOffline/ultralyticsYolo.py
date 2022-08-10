#Reference https://github.com/ultralytics/yolov5
'''
Perform these commands in the terminal
git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
'''

import torch
import os
os.environ["DATASET_DIRECTORY"] = "/content/datasets"
import glob
from IPython.display import Image, display

'''
Terminal command: !python train.py --img 416 --batch 16 --epochs 10 --data {dataset.location}/data.yaml --weights yolov5n.pt --cache
'''

'''
Terminal command: !python detect.py --weights runs/train/exp2/weights/best.pt --img 416 --conf 0.7 --source {dataset.location}/test/images
'''


for imageName in glob.glob('/content/yolov5/runs/detect/exp/*.jpg'): #assuming JPG
    display(Image(filename=imageName))
    print("\n")