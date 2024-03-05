'''
CS 210 Winter 2023 Project 9
Author: Jocelyn Guan
Credit: Help hours
Description: Clustering
'''

import csv
import math
import random

def load_numerical_data(filename: str, column_titles: list) -> dict:
   
    item_dict = {}
    new_list = []
    list_1 = []

    with open(filename, 'r') as in_file:
        csv_reader = csv.reader(in_file)
        titles = next(csv_reader)

        for line in csv_reader:
            new_list.append(line)

        for items in column_titles:

            for data_idx in range (len(titles)):
                if titles[data_idx] == items:
                    idx = data_idx

            for line in new_list:
                list_1.append(line[idx])

        list_length = int(len(list_1) / len(column_titles))
        first_list = list_1[:list_length]
        second_list = list_1[list_length:]

        for i in range (len(new_list)):
            item_dict[i] = (float(first_list[i]), float(second_list[i]))

    return item_dict

print(load_numerical_data('earthquakes.csv', ('latitude', 'longitude')))


def euclid_dist(point1: tuple, point2: tuple) -> float:
    total = 0
    for idx in range(len(point1)):
        diff = (point1[idx] - point2[idx]) ** 2
        total = total + diff
    
    distance = math.sqrt(total)

    return distance


def create_centroids(k: int, data: dict) -> list:
    centroids = []
    centroids_count = 0
    centroids_keys = []

    while centroids_count < k:
        key = random.randint(1, len(data))
        if key not in centroids_keys:
            centroids.append(data[key])
            centroids_keys.append(key)
            centroids_count += 1

    return centroids

def create_clusters(k: int, centroids: list, values: list, repeats = 100) -> tuple:
    for a_pass in range(repeats):
        print('****PASS', a_pass + 1,'****')
        clusters = []
        for i in range(k):
            clusters.append([])

    pass

        

