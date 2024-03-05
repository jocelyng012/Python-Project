'''
CS 210 Winter 2023 Project 6
Author: Jocelyn Guan
Credit: Help hours
Description: Population Data Analysis
'''

import json
import matplotlib.pyplot as plt
import pop_stats


def plot_pop_data(pop, lat, lng):
    '''
    it take the data and plot the data in map,
    shows the population for each cities in the 
    file

    >>> plot_pop_data(pop, lat, lng)
    [return a map with a population scatter]
    '''

    size = []

    for i in pop:
        size.append(i / 1000)
    
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.scatter(lng, lat, size)
    plt.show()
    
    return


def plot_hist(data, n_bins=10):
    '''
    it take the density data from the file
    and plot them into a histogram

    >>> plot_hist(data, n_bins=10)
    [return a histogram that with the density data]
    '''
    
    plt.hist(data, n_bins)
    plt.show()

    return


if __name__ == "__main__":
    file_name = "population.json"
    
    [pop, lat, long, growth, dens] = read_data(file_name, \
        ["pop2023", "lat", "lng", "growth", "density"])
    
    plot_pop_data(pop, lat, long)
    
    #pop = filter_arr(pop, 10000)

    #plot_hist(dens)