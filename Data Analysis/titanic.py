'''
CS 210 Winter 2023 Project 7
Author: Jocelyn Guan
Credit: Help hours
Description: Data Analysis
'''

#import titanic
import csv
import statistics
import matplotlib.pyplot as plt


def load_data(file_name: str, type: dict) -> dict:
    '''
    '''

    item_dict = {}
    new_list = []

    with open(file_name, 'r') as in_file:
        csv_reader = csv.reader(in_file)
        titles = next(csv_reader)

        for line in csv_reader:
            new_list.append(line)

        for items in type:
            item_key = (items, type[items])
            type1 = type[items]
            item_dict[item_key] = []

            for data_idx in range (len(titles)):
                if titles[data_idx] == items:
                    idx = data_idx

            for line in new_list:
                item_dict[item_key].append(type1(line[idx]))

    return item_dict

print(load_data('titanic_clean.csv', {'PassengerId': int}))


def summarize(data: dict):

    for each_key in data.keys():
        
        if each_key[1] == int or each_key[1] == float:
            data_int = data[each_key]
    
            total_data_int = []
        
            for num_item in data_int:
                data_1 = float(num_item)
                total_data_int.append(data_1)
    
            print(f'Statistics for {each_key[0]}:')
            print(f'    min:{(float(round(min(total_data_int), 1))):>7.1f}')
            print(f'    max:{(float(round(max(total_data_int), 1))):>7.1f}')
            print(f'   mean:{(float(round(statistics.mean(total_data_int), 1))):>7.1f}')
            print(f'  stdev:{(float(round(statistics.stdev(total_data_int), 1))):>7.1f}')
            print(f'   mode:{(float(round(statistics.mode(total_data_int), 1))):>7.1f}')
        
        if each_key[1] == str:
            data_str = data[each_key]

            data_str_dict = {}

            for each_item in data_str:
                if each_item in data_str_dict:
                    data_str_dict[each_item] += 1
                else:
                    data_str_dict[each_item] = 1
            
            max_word = max(data_str_dict, key = data_str_dict.get)
            print(f'Statistics for {each_key[0]}:')
            print(f'Number of unique values: {len(data_str_dict)}')
            print(f'      Most common value: {(max_word)}')
        
    return


#summarize((load_data('titanic_clean.csv', titanic_types)))


def pearson_corr(x: list, y: list) -> float:
    '''
    '''

    if not len(x) == len(y):
        raise ValueError('The list parameters must have the same number of elements.')
    
    for i in x:
        if type(i) == str:
            raise ValueError('pearson_corr only works with int or float lists.')

    x_bar = statistics.mean(x)
    y_bar = statistics.mean(y)
    x_std = statistics.stdev(x)
    y_std = statistics.stdev(y)
    
    num = 0.0

    for i in range(len(x)):
        num = num + (x[i] - x_bar) * (y[i] - y_bar)
        
    corr = round(num / ((len(x) - 1) * x_std * y_std), 2)

    #print(corr)
    
    return corr

#pearson_corr(list(load_data('titanic_clean.csv', {'Age': float})), list(load_data('titanic_clean.csv', {'Survived': int})))



def survivor_vis(data: dict, col_1: tuple, col_2: tuple):
    '''
    '''

    #data = load_data('titanic_clean.csv', {'PassengerId': int})
    #col_1 = col_tuple('Age')
    #col_2 = col_tuple('Survived')

    x = data[col_1]
    y = data[col_2]

    survived = load_data('titanic_clean.csv', {'Survived': int})
    survived_list = survived[('Survived', int)]

    x_survived = []
    y_survived = []

    x_died = []
    y_died = []
    
    for i in range (len(survived_list)):
        if survived_list[i] == 1:
            y_survived.append(y[i])
            x_survived.append(x[i])
        else:
            y_died.append(y[i])
            x_died.append(x[i])

    plt.scatter(x_survived, y_survived, marker='o', c='pink', label='Survived')
    plt.scatter(x_died, y_died, marker='x',c='blue', label='Died')

    labelx = col_1[0]
    labely = col_2[0]

    plt.title('Survival of Titanic Passengers')
    plt.xlabel(f'{labelx}')
    plt.ylabel(f'{labely}')
    plt.legend()
    #plt.savefig(f'scatter_{col_1[0]}_{col_2[0]}.png')
    plt.show()

    return

#data = load_data('titanic_clean.csv',{'Age': float, 'Fare': float})

#survivor_vis(data, ('Age', float) , ('Fare', float))