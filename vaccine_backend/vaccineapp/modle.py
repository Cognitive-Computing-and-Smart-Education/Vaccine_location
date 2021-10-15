from pyscipopt import Model, quicksum
c1= 1000
import copy

def discos_func(dis):
    if dis < 1:
        return 0
    if dis < 3 and dis >= 1:
        return 8
    if dis <= 18 and dis >=3:
        return 8+ 2.5*(dis -3)
    else:
        return 8 + 100000*(dis -3)

def main_model(dis_data, people_data, demand_ldata, vaccine_ldata):
    model = build_model(dis_data,people_data)
    obj,result = resolve(model,demand_ldata, vaccine_ldata)
    return obj,result

def build_model(dis_data,people_data):
    model = Model("vaccin_plan")

    x ,y= {},{}

    for i in range(len(dis_data)):
        y[i] = model.addVar(name = 'y[%s]'%(i), vtype = 'B')

    for i in range(len(dis_data)):
        for j in range(len(dis_data[0])):
            x[i, j] = model.addVar(name='x[%s][%s]' % (i, j), vtype='B')

    for j in range(len(dis_data[0])):
        model.addCons(quicksum(x[i,j] for i in range(len(dis_data))) == 1,name = 'ser%s'%(j))

    for i in range(len(dis_data)):
        model.addCons(y[i] >= quicksum(x[i,j] for j in range(len(dis_data[0])))/len(dis_data[0]))
        model.addCons(quicksum(x[i,j] * people_data[j] for j in range(len(dis_data[0]))) <= 250000, name = 'ser_limit(%s)'%(i))

    # for content in x:
    #     print(dis_data[0,0])


    model.setObjective(quicksum(x[i,j] * people_data[j] * discos_func(float(dis_data[i][j].split(' ')[0])) for (i,j) in x)
                       + c1 * (quicksum(y[i] for i in range(len(dis_data)))) ,'minimize')

    #quicksum(min(0, quicksum(x[i, j] for j in range(len(dis_data[0])))) for i in range(len(dis_data)))

    return model


def resolve(model,demand_ldata, vaccine_ldata):
    model.optimize()
    cost = model.getObjVal()
    print("Optimal Cost:", cost)

    result = []
    for v in model.getVars():
        if model.getVal(v) > 0.001:
            if v.name.startswith('x'):
                index_x = v.name.split('[')[1][:1]
                index_y = v.name.split('[')[2][:1]
                print(index_x,end= '   ')
                print(index_y)
                print(demand_ldata[int(index_y)][2:])
                print(vaccine_ldata[int(index_x)][2:])
                result.append(copy.deepcopy({'from':{'name':demand_ldata[int(index_y)][2],'location': demand_ldata[int(index_y)][4:]},
                                                     'to':{'name':vaccine_ldata[int(index_x)][2], 'location':vaccine_ldata[int(index_x)][4:]}}))
                print('------------------------------------分割线----------------------------------------')
            # print(v.name, "=", model.getVal(v))
    return model.getObjVal(),result

