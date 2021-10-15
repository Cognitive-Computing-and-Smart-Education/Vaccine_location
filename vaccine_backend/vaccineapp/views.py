from django.shortcuts import render
from django.shortcuts import HttpResponse

import json
from vaccineapp import Read_file
from vaccineapp import modle

# Create your views here.
distence_file = 'distence_matrix.csv'
people_data_file = 'people_age_data.csv'
demand_point_file = 'demand_point.csv'
vaccine_sits_file = 'vaccine candidate sits.csv'


dis_data = Read_file.read_file(distence_file)
people_data = Read_file.read_file(people_data_file)
demand_ldata = Read_file.read_file(demand_point_file)
vaccine_ldata = Read_file.read_file(vaccine_sits_file)
dis_data = dis_data.set_index(['Unnamed: 0'],drop=True)
# print(dis_data)


def get_result(request):
    print(type(vaccine_ldata))
    Object_value, solution = modle.main_model(dis_data.values.tolist(),people_data['valid_data'].tolist(),
                                              demand_ldata.values.tolist(), vaccine_ldata.values.tolist())
    return HttpResponse(json.dumps({'object':Object_value,'Paths':solution}))
