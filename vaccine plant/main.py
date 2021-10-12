# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from preprocess import Read_file
import modle

dis_file_name = 'distence_matrix.csv'
people_file_name = 'people_age_data.csv'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dis_data = Read_file.read_file(dis_file_name)
    people_data = Read_file.read_file(people_file_name)
    print(dis_data.columns)
    # print(people_data)
    modle.main_model(dis_data.values.tolist(),people_data['valid_data'].tolist())
