import numpy as np


def euclidian_distance(point1, point2):
    """Calculates the euclidian distance between two points"""
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return distance ** 0.5


def get_point(image):

    img_array = np.array(image).round().astype(int)

    r_mean = np.mean(img_array[:, :, 0])
    g_mean = np.mean(img_array[:, :, 1])
    b_mean = np.mean(img_array[:, :, 2])

    return [r_mean, g_mean, b_mean]
