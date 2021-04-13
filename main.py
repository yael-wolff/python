import sys
import pandas as pd
from statistics import mean, median, sum



features = ["cnt", "t1", "hum", "is_holiday", "season"]
values = ["1", "2"]
filter_feature = "season"
features_q1 = ["hum", "t1", "cnt"]
calc_for = ["season", "is_holiday", "All"]

path = 'C:\\Users\Yael\Documents\python\london.csv'

def load_data(path):
    df = pd.read_csv(path)
    fea_dic = df[features]
    data = fea_dic.to_dict(orient='list')
    return(data)

dictionary_data = load_data(path)

file = open("data.py","w")
file.write(str(dictionary_data))
file.close()

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


def q1(features_q1,calc_for,path):
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
    #total_mean_cnt_summer=mean(df[df['season'] == 1]['cnt'])

    print("Question 1:")
    for i in calc_for:
        print_title=0
        if (i == "All"):
            continue
        for j in features_q1:
            if(i=="season" and print_title==0):
                print("Summer")
            elif(i=="is_holiday" and print_title==0):
                print("Holiday")
            total_sum = sum(df[df[i] == 1][j])
            total_mean = mean(df[df[i] == 1][j])
            #total_median = median(df(df[i] == 1][j])
            print(j+": "+str(total_sum)+", "+str(total_mean))
            #print(j+": "+str(total_sum)+", "+str(total_mean)+", "+str(total_median))
            print_title=1

    print("All")
    for j in features_q1:
        total_sum=sum(df[j])
        total_mean=mean(df[j])
        #total_median=median(df[j])
        print(j + ": " + str(total_sum) + ", " + str(total_mean))
        #print(j+": "+str(total_sum)+", "+str(total_mean)+", "+str(total_median))

feature="cnt"
season_req=3
temperature_req=13
holidays=[0,1]
def q2(feature,holidays,season_req,temp_req,path):
    """
       This function prints the mean and median of given feature from a given file
       according to the values of holidays and temperature request.
       :parameters: feature, holidays, season_req, temperature_request, path
       :type: String, List, Int, Int, Int, String
       :returns: None
       :type: NoneType
       """

    df = pd.read_csv(path)
    for i in holidays:
        print("If t1<=13.0, then:")

        if(i==1):
            print("Winter holiday records: ")
        else:
            print("Winter weedays records: ")

        mean_calc=mean(df.loc[(df['season'] == season_req) & (df['is_holiday'] == i) & (df['t1']<=temperature_req), 'cnt'])
        median_calc = median(df.loc[(df['season'] == season_req) & (df['is_holiday'] == i) & (df['t1'] <= temperature_req), 'cnt'])
        print("cnt: "+str(mean_calc)+", "+str(median_calc))

        print("If t1>13.0, then: ")

        if(i==1):
            print("Winter holiday records: ")
        else:
            print("Winter weedays records: ")

        mean_calc = mean(df.loc[(df['season'] == season_req) & (df['is_holiday'] == i) & (df['t1'] > temperature_req), 'cnt'])
        median_calc = median(df.loc[(df['season'] == season_req) & (df['is_holiday'] == i) & (df['t1'] > temperature_req), 'cnt'])
        print("cnt: " + str(mean_calc) + ", " + str(median_calc))



#q2(feature,holidays,season_req,temperature_req,path)

"""
def population_statistics(feature_description, data, treatment, target, threshold, is_above,
statistic_functions):

    path = 'C:\\Users\Yael\Documents\python\london.csv'
    df = pd.read_csv(path)
    if(is_above==True):
        sum_of_target = sum(df[df[treatment] > threshold][target])
        mean_of_target = mean(df[df[treatment] > threshold][target])
        median_of_target= median(df[df[treatment] > threshold][target])
    else:
        sum_of_target = sum(df[df[treatment] <= threshold][target])
        mean_of_target = mean(df[df[treatment] <= threshold][target])
        median_of_target= median(df[df[treatment] <= threshold][target])

    print(feature_description+" "+str(sum_of_target)+", "+str(mean_of_target)+", "+str(median_of_target))
    """



df = pd.read_csv(path)
#fea_dic = df[filter_feature]
#filter_by_feature(fea_dic, filter_feature, values)

q1(features_q1,calc_for,path)

