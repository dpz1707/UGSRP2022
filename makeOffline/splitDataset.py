import os
import shutil
import glob
import random

#This dataset splitter works by randomly selecting an image from the main image folder and moving that image and the respective label to their respective validation datasets

source_folder = r"C:\Users\nydan\PycharmProjects\C2Smart\images - Copy\\"       #source folder for all images .jpg
destination_folder = r"C:\Users\nydan\PycharmProjects\C2Smart\valImTest\\"      #destination folder for image .jpg

source_folder_label = r"C:\Users\nydan\PycharmProjects\C2Smart\labelstxt1 - Copy\\"    #source folder for all image labels
destination_folder_label = r"C:\Users\nydan\PycharmProjects\C2Smart\valLabelTest\\"    #source folder for all destination labels


# fetch all files
file_path_type = [r"C:\Users\nydan\PycharmProjects\C2Smart\images - Copy\*.jpg"]  #skips past subfolders and operates as essentially one layer of tree directory
file_path_type_label = [r"C:\Users\nydan\PycharmProjects\C2Smart\labelstxt1 - Copy\*.txt"]

for x in range(126): #determines your split. This is calculated by hand, so if you want to pull 80 images from the main folder, use 80
    images = glob.glob(random.choice(file_path_type))
    random_image = random.choice(images)

    where = random_image.rfind("\\")
    newName = random_image[where+1:] #selects a random image from the main image folder

    source = source_folder + newName
    destination = destination_folder + newName #moves the image file to the validation image folder

    pureName = os.path.splitext(newName)[0] #gets the file name without extensions. For example, 42ndStCone.jpg would become 42ndStCone
    labelName = pureName + ".txt"
    source_label = source_folder_label + labelName #gets respective label and moves it
    destination_label = destination_folder_label + labelName

    shutil.move(source, destination)
    shutil.move(source_label, destination_label)
