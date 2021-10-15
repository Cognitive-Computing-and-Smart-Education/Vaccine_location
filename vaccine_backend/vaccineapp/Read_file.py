import pandas as pd
import os

dir_name = os.path.dirname(os.path.abspath('__file__'))

def read_file(file_name):
    if file_name.endswith('.csv'):
        return pd.read_csv(os.path.join(dir_name,'vaccineapp\\data\\' + file_name))
