import os
from PIL import Image
import csv
import numpy as np
from scipy import stats
import random
import time

# Define the path to the folder containing the images
folder_path = "../images/og_ss"

# Define the dimensions for the cropped images
crop_width = 250
crop_height = 250

# b9752b
LIGHT_BROWN = (185, 75, 43)

# 85715c
GREY = (85, 71, 92)

# 472303
DARK_BROWN = (47, 23, 3)

# Define the name of the CSV file to be created
csv_file_name = "../data/image_data.csv"


def euclidian_distance(point1, point2):
    """Calculates the euclidian distance between two points"""
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return distance ** 0.5


def classify(point):
    """Classifies a point as either light, medium, or dark"""
    # Calculate the distance to each color
    light_distance = euclidian_distance(point, LIGHT_BROWN)
    grey_distance = euclidian_distance(point, GREY)
    dark_distance = euclidian_distance(point, DARK_BROWN)

    # Return the color with the shortest distance
    if light_distance < grey_distance and light_distance < dark_distance:
        return 'light'
    elif grey_distance < light_distance and grey_distance < dark_distance:
        return 'grey'
    else:
        return 'dark'


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

            if counter % 25 == 0:
                print("Loading: " + str(counter) + "/" + str(num_images))

            # Open the image file
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)

            # Crop the image
            width, height = image.size
            left = (width - crop_width) / 2
            top = (height - crop_height) / 2
            right = (width + crop_width) / 2
            bottom = (height + crop_height) / 2
            image = image.crop((left, top, right, bottom))

            # Save the cropped image with a new filename
            new_filename = f"img_{counter}.png"

            img_array = np.array(image).round().astype(int)

            # Calculate the mean and median values for each color channel
            r_mode = np.mean(img_array[:, :, 0])
            g_mode = np.mean(img_array[:, :, 1])
            b_mode = np.mean(img_array[:, :, 2])

            ###### WILL NEED TO CHANGE THIS TO THE PATH OF THE FOLDER CONTAINING THE IMAGES ######
            new_image_path = os.path.join('../images/renamed', new_filename)

            cl = classify((r_mode, g_mode, b_mode))

            image.save(new_image_path)

            # Write the filename and class to the CSV file
            writer.writerow([new_image_path, cl, r_mode, g_mode, b_mode])

            # Increment the counter
            counter += 1


print("Done!")
