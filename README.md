# UGSRP2022
The makeOffline folder contains the major tools that I built during my time over the summer to assist in my research project

All detection should be made in python using torchhub, so detection should not be done through the terminal. Algorithms should go in the pt_files subfolder in the algorithms file

splitDataset.py is used to split the dataset into training and validation sets
ultralyticsYolo.py is a simplified version of the official ultralytics yolov5 training guide
zipClean.py is the main file I used as it parses a zip file and pulls out images containing workzone objects, according to a set of parameters


finalIntegration.py contains the final workflow, which integrates the classification algorithm with computer vision. Datasets are not provided, although the model training follows standard procedure of jpg files and respectively named label files. Classifier training uses a .csv file, and the columns should be adjusted accordingly. 
