from zipfile import ZipFile
import zipfile
from io import StringIO
from PIL import Image
import imghdr
import os
import io
import matplotlib
from Algorithm.main import *
import cv2
import argparse
import time
import requests
import yaml
import tqdm
import torchvision
from turtle import color

import pandas as pd
import seaborn
import numpy as np

model = get_model() #gets model from main.py in the Algorithm folder
directory = r'C:\Users\nydan\PycharmProjects\C2Smart\detected' #directory that images will be saved in

with ZipFile("Staten Island.zip", "r") as zip_ref: #put zip file to be parsed here, followed by "r"
   list_of_files = zip_ref.namelist() #pulls all subfolders and files into a one-level list
   state = 0
   help = 0
   for elem in list_of_files:

        if (state%50 != 0):    #pulls 50 images at most from a file, if after cycling through 50 images nothing is detected, skips to next folder
            s = StringIO()
            #print(elem, file=s)
            result = s.getvalue()
            #print(result)
            result = result[:-1]  #modifications to split name from extension. Without this step the next processes may give errors due to naming compatibility
            ending = result[-24:] #modifications to split name from extension. Without this step the next processes may give errors due to naming compatibility
            ext = os.path.splitext(elem)[-1]
            if ((ext == ".jpg") or (ext == ".png")):
                in_bytes = zip_ref.read(elem)
                img = cv2.imdecode(np.fromstring(in_bytes, np.uint8), cv2.IMREAD_COLOR)
                image = Image.open(io.BytesIO(in_bytes))
                results = model(image) #run image through model
                dataframe = results.pandas().xyxy[0]
                print(dataframe)
                isempty = dataframe.empty #if the dataframe is empty, .empty returns True
                if (isempty == False):
                    os.chdir(directory)
                    rgb_im = image.convert("RGB")
                    rgb_im.save("c" + ending)


                state += 1
                help = 0

        else:
            help += 1
            if (help == 2400): #skips to next folder
                state += 1
            else:
                continue








