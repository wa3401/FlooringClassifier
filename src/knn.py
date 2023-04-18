from make_csv import *


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
        point.append(euclidian_distance(test_point, point[2:]))

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
    # run something
    print("Hello World")


if __name__ == "__main__":
    main()
