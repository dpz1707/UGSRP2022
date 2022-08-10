# UGSRP2022
the makeOffline folder contains the major tools that I built during my time over the summer to assist in the research

All detection should be made in python using torchhub, so detection should not be done through the terminal. Algorithms should go in the pt_files subfolder in the algorithms file

splitDataset.py is used to split the dataset into training and validation sets
ultralyticsYolo.py is a simplified version of the official ultralytics yolov5 training guide
zipClean.py is the main file I used as it parses a zip file and pulls out images containing workzone objects, according to a set of parameters


finalIntegration.py contains the final workflow, which integrates the classification algorithm with computer vision
