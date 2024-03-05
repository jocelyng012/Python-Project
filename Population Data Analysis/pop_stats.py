'''
CS 210 Winter 2023 Project 6
Author: Jocelyn Guan
Credit: Help hours
Description: Population Data Analysis
'''

import json
import statistics

def read_data(file_name: str, keys: list) -> list:
    '''
    read file's data and take a list as a argument,
    take keys to find its data into arrays

    >>> read_data('pop.json', ['pop2023'])
    [return a lists of a list that consist the data of 
    'pop2023']
    '''

    list_w_data = []

    with open(file_name, 'r') as data:
        new_data = json.load(data)

    for order_list in keys:
        new_list = []

        for i in range (len(new_data)):
            #print(i)
            new_list.append(new_data[i][order_list])

        list_w_data.append(new_list)

    return list_w_data


print(read_data('pop.json', ['pop2023', 'pop2020']))


def stats(an_array):
    '''
    take a list as a argument and calculate 
    the min, max, range, mean, mode, var, and 
    stdev

    >>> stats([a list return from read_data])
    [return a list of calculation]
    '''

    stats_dict = {
        'min': round(min(an_array), 2), 
        'max': round(max(an_array), 2), 
        'range': round(abs(max(an_array) - min(an_array)), 2),
        'mean': round(statistics.mean(an_array), 2), 
        'mode': round(statistics.mode(an_array), 2),
        'var': round(statistics.variance(an_array), 2), 
        'stdev': round(statistics.stdev(an_array), 2)
    }

    return stats_dict


def print_stats(file_name):
    '''
    it calculate and print the vaule that return 
    from stats and read_data functions

    >>> print_stats([a file name])
    [print a table with all the values]
    '''
  
    total = read_data(file_name,['pop2023', 'growth', 'density'])

    pop = total[0]
    growth = total[1]
    density = total[2]

    total_pop = []

    for num in pop:
        if num >= 10000:
            total_pop.append(num)

    population = stats(total_pop)
    growth = stats(growth)
    density = stats(density)
    

    print('            +-------------+-------------+-------------+-------------+-------------+-------------+-------------+')
    print(f"            |{'min' :<13}|{'max' :<13}|{'range' :<13}|{'mean' :<13}|{'mode' :<13}|{'variance' :<13}|{'st.dev.' :<13}|")
    print('            +-------------+-------------+-------------+-------------+-------------+-------------+-------------+')
    print(f"population |{population['min'] :<13}|{population['max'] :<13} |{population['range'] :<13}|{population['mean'] :<13}|{population['mode'] :<13}|{population['var'] :<13}|{population['stdev'] :<13}|")
    print('            +-------------+-------------+-------------+-------------+-------------+-------------+-------------+')
    print(f"growth     |{growth['min'] :<13}|{growth['max'] :<13}|{growth['range'] :<13}|{growth['mean'] :<13}|{growth['mode'] :<13}|{growth['var'] :<13}|{growth['stdev'] :<13}|")
    print('            +-------------+-------------+-------------+-------------+-------------+-------------+-------------+')
    print(f"density     |{density['min'] :<13}|{density['max'] :<13} |{density['range'] :<13}|{density['mean'] :<13}|{density['mode'] :<13}|{density['var'] :<13}|{density['stdev'] :<13}|")
    print('            +-------------+-------------+-------------+-------------+-------------+-------------+-------------+')

    return    


if __name__ == "__main__":
    print_stats('population.json')