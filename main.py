THRESHOLD = 13
SEASON_REQ = 3

import sys
import pandas as pd

from statistics import mean, median, sum



def choose_func(name, values):
    if name == mean:
        mean(values)
    elif name == sum:
        sum(values)
    elif name == median:
        median(values)

features = ["cnt", "t1", "hum", "is_holiday", "season"]
values = [1, 2, 3]
filter_feature = "season"

calc_for = ["season", "is_holiday", "All"]



def load_data(path):
    df = pd.read_csv(path)
    fea_dic = df[features]
    data = fea_dic.to_dict(orient='list')
    return(data)



def filter_by_feature(data, feature, values):
    m = 0
    len_of_dic = len(data)
    data1 = [None] * len_of_dic
    data2 = [None] * len_of_dic
    for i in data:
        is_in_val = 0
        for j in values:
            if int(i) == int(j):
                is_in_val = 1
            else:
                continue
        if is_in_val == 1:
            data1[m] = data[m]
        else:
            data2[m] = data[m]
        m = m + 1
    return (data1, data2)

#def print_details(data, features, statistic_functions):


def print_values_from_file(features_q1,calc_for,path):
    """
       This function prints the sum, mean and median of given features from a given file
       according to the values of another features.
       :parameters: features q1, calc_for, path
       :type: List,List and string
       :returns: None
       :type: NoneType
       """
    df = pd.read_csv(path)
    #code for calculations on columns:

    print("Question 1:")
    for i in calc_for:
        print_title=0
        if (i == "All"):
            continue
        for j in features_q1:
            if(i=="season" and print_title==0):
                print("Summer:")
            elif(i=="is_holiday" and print_title==0):
                print("Holiday:")
            total_sum = sum(df[df[i] == 1][j])
            total_mean = mean(df[df[i] == 1][j])
            total_median = median(df[df[i] == 1][j])
            print(j+": "+str(total_sum)+", "+str(total_mean)+", "+str(total_median))
            print_title=1

    print("All:")
    for j in features_q1:
        total_sum=sum(df[j])
        total_mean=mean(df[j])
        total_median=median(df[j])
        print(j+": "+str(total_sum)+", "+str(total_mean)+", "+str(total_median))



def calcu_popu_stati(SEASON_REQ, path, threshold):
    """
       This function prints the mean and median of given feature from a given file
       according to the values of holidays and temperature request.
       :parameters: feature, holidays, season_req, temperature_request, path
       :type: String, List, Int, Int, Int, String
       :returns: None
       :type: NoneType
       """
    treatment = 't1'
    target = 'cnt'
    is_holiday = ['weekday', 'holiday']
    df = pd.read_csv(path)
    new_data = df.loc[df['season'] == SEASON_REQ]
    print("Question 2:")
    for i in range(2):
        if (i == 0): #temp <= 13
            is_above = False
            print("If t1<=13.0, then:")
            for j in range(1, -1, -1):
                population_statistics(is_holiday[j], new_data, treatment, target, threshold, is_above, choose_func)
        else: #temp > 13
            print("If t1>13.0, then: ")
            is_above = True
            for k in range(1, -1, -1):
                population_statistics(is_holiday[k], new_data, treatment, target, threshold, is_above, choose_func)







def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    if feature_description == 'holiday':
        holy_or_not = 1
    else:
        holy_or_not = 0
    if(is_above == True):
        mean_of_target = mean(data.loc[(data['is_holiday'] == holy_or_not) & (data[treatment] > threshold), target])
        median_of_target = median(data.loc[(data['is_holiday'] == holy_or_not) & (data[treatment] > threshold), target])
    else:
        mean_of_target = mean(data.loc[(data['is_holiday'] == holy_or_not) & (data[treatment] <= threshold), target])
        median_of_target = median(data.loc[(data['is_holiday'] == holy_or_not) & (data[treatment] <= threshold), target])
        #median_of_target= median(df[df[treatment] <= threshold][target])
    print("Winter " + feature_description + " records:\ncnt: " + str(mean_of_target) + ", " + str(median_of_target))


def main(argv):
    path = argv[1]
    dictionary_data = load_data(path)
    file = open("data.py", "w")
    file.write(str(dictionary_data))
    file.close()
    features = argv[2].split(", ")
    features_q1 = features[:3]
    print_values_from_file(features_q1, calc_for, path)
    calcu_popu_stati(SEASON_REQ, path, THRESHOLD)

if __name__ == '__main__':
    main(sys.argv)






