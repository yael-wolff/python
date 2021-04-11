import sys
import pandas as pd

features = ["cnt", "t1", "hum", "is_holiday", "season"]
values = ["1", "2"]
filter_feature = "season"

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
    m = 0;
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




df = pd.read_csv(path)
fea_dic = df[filter_feature]
filter_by_feature(fea_dic, filter_feature, values)