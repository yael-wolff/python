import sys
import pandas as pd

features = ["cnt", "t1", "hum", "is_holiday", "season"]

path = 'C:\\Users\Yael\Documents\python\london.csv'

def load_data(path):
    df = pd.read_csv(path)
    fea_dic = df[features]
    data = fea_dic.to_dict(orient='list')
    print(data)

load_data(path)