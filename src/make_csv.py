import os
from PIL import Image
import csv
import numpy as np
import random
import time

# Define the path to the folder containing the images
folder_path = "../images/og_ss"

# Define the dimensions for the cropped images
crop_width = 250
crop_height = 250

# Define the name of the CSV file to be created
csv_file_name = "../data/image_data.csv"



# Open the CSV file for writing and write the header row
with open(csv_file_name, mode='w', newline='') as csv_file:
    # Initialize a counter for the image names
    counter = 1
    writer = csv.writer(csv_file)
    writer.writerow(['filename', 'rMean', 'gMean', 'bMean', 'rMedian', 'gMedian', 'bMedian'])
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

            img_array = np.array(image)
        
            # Calculate the mean and median values for each color channel
            r_mean = np.mean(img_array[:,:,0])
            g_mean = np.mean(img_array[:,:,1])
            b_mean = np.mean(img_array[:,:,2])
            r_median = np.median(img_array[:,:,0])
            g_median = np.median(img_array[:,:,1])
            b_median = np.median(img_array[:,:,2])
            
            ###### WILL NEED TO CHANGE THIS TO THE PATH OF THE FOLDER CONTAINING THE IMAGES ######
            new_image_path = os.path.join('../images/renamed', new_filename)
            
            image.save(new_image_path)

            # Write the filename and class to the CSV file
            writer.writerow([new_image_path, r_mean, g_mean, b_mean, r_median, g_median, b_median])

            # Increment the counter
            counter += 1




print("Done!")
