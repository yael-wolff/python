import sys
import pandas as pd



def load_data():
    df = pd.read_csv("C:\\Users\Yael\Documents\python\london.csv")
    data = df.to_dict()
    print(data)


load_data()