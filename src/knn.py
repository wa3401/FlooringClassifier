from helpers import euclidian_distance, get_point
import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt
import csv

crop_width = 250
crop_height = 250


def knn(csv_file_name, test_point, k):
    """Performs k-nearest neighbors classification on a test point"""
    # Read the CSV file into a list of lists
    with open(csv_file_name, mode='r') as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)

    # Remove the header row
    data.pop(0)

    # Calculate the distance from the test point to each point in the data
    for point in data:
        num_point = [float(point[2]), float(point[3]), float(point[4])]
        point.append(euclidian_distance(test_point, num_point))

    # Sort the data by distance (smallest to largest)
    data.sort(key=lambda x: x[3])

    # Get the k nearest neighbors
    neighbors = data[:k]

    # Count the number of each type of neighbor
    light = 0
    grey = 0
    dark = 0
    for neighbor in neighbors:
        if neighbor[1] == 'light':
            light += 1
        elif neighbor[1] == 'grey':
            grey += 1
        else:
            dark += 1

    # Return the most common type of neighbor
    if light > grey and light > dark:
        return 'light'
    elif grey > light and grey > dark:
        return 'grey'
    else:
        return 'dark'


def main():
    # loop through test images
    fig, axs = plt.subplots(nrows=len(os.listdir(
        "../images/test_images")), ncols=1, figsize=(8, 8))
    for i, filename in enumerate(os.listdir("../images/test_images")):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_path = os.path.join("../images/test_images", filename)
            image = Image.open(image_path)
            test_point = get_point(image)
            print(test_point)
            res = knn("../data/image_data.csv", test_point, 5)
            # Add the image and res to a grid
            axs[i].imshow(np.array(image))
            axs[i].axis("off")
            axs[i].set_title(f"Result: {res}")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
