import os
from PIL import Image
import csv
import numpy as np
from scipy import stats
import random
import time
from helpers import euclidian_distance, get_point

# Define the path to the folder containing the images
folder_path = "../images/og_ss"

classes_folder = "../images/classes"

# Define the dimensions for the cropped images
crop_width = 250
crop_height = 250


def get_classes(path):
    classes = {}
    for filename in os.listdir(path):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_path = os.path.join(path, filename)
            class_name = filename.split(".")[0]
            image = Image.open(image_path)

            # Resize the image
            image = image.resize((crop_width, crop_height))

            means = get_point(image)
            classes[class_name] = means
    return classes


# Define the name of the CSV file to be created
csv_file_name = "../data/image_data.csv"


def classify(point):
    """Classifies a point as either light, medium, or dark"""
    dists = {}
    classes = get_classes(classes_folder)
    for class_name, class_point in classes.items():
        dists[class_name] = euclidian_distance(point, class_point)
    return min(dists, key=dists.get)


# Open the CSV file for writing and write the header row
with open(csv_file_name, mode='w', newline='') as csv_file:
    # Initialize a counter for the image names
    counter = 1
    writer = csv.writer(csv_file)
    writer.writerow(['filename', 'class', 'r_mode', 'g_mode', 'b_mode'])
    num_images = len(os.listdir(folder_path))

    # Loop through all the files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".png") or filename.endswith(".jpg"):

            if counter % 10 == 0:
                print("Loading: " + str(counter) + "/" + str(num_images))

            # Open the image file
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)

            # Resize the image
            image = image.resize((crop_width, crop_height))

            # Save the cropped image with a new filename
            new_filename = f"img_{counter}.png"

            point = get_point(image)

            ###### WILL NEED TO CHANGE THIS TO THE PATH OF THE FOLDER CONTAINING THE IMAGES ######
            new_image_path = os.path.join('../images/renamed', new_filename)

            cl = classify(point)

            image.save(new_image_path)

            # Write the filename and class to the CSV file
            writer.writerow([new_image_path, cl, point[0], point[1], point[2]])

            # Increment the counter
            counter += 1


print("Done!")
