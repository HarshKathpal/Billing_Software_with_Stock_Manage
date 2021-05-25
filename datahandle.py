import pandas as pd
import ast

def datahandle_first():
    data1 = pd.read_excel("data.xlsx",usecols=["com_item","com_combo","com_stock"])
    data1 = data1[~data1['com_item'].isna()] 
    data1 = data1[data1['com_stock']!=0]
    d1 = len(data1['com_item'])
    print(d1)
    data_item = list(data1['com_item'])
    data_combo = list(data1['com_combo'])
    data_stock = list(data1['com_stock'])
    new_data1 = pd.DataFrame()

    com_item = []
    x = []
    com_combo = []
    com_stock = []

    for i in range(len(data_item)):
        if data_item[i] not in com_item:
            com_item.append(data_item[i])
            x.append(data_combo[i])
            com_combo.append(x)
            x = []
            x.append(data_stock[i])
            com_stock.append(x)
            x = []
        else:
            ind = com_item.index(data_item[i])
            if data_combo[i] in com_combo[ind]:
                _ind = com_combo[ind].index(data_combo[i])
                com_stock[ind][_ind] = com_stock[ind][_ind]+data_stock[i]
            else:
                com_combo[ind].append(data_combo[i])
                com_stock[ind].append(data_stock[i])

    new_data1['com_item'] = com_item
    new_data1['com_combo'] = com_combo
    new_data1['com_stock'] = com_stock
    new_data1.to_excel("main_data.xlsx")

def datahandle_last():
    data1 = pd.read_excel("main_data.xlsx",usecols=["com_item","com_combo","com_stock"])
    data1 = data1[~data1['com_item'].isna()] 
    # d1 = len(data1['item'])
    com_item = list(data1['com_item'])
    combo = list(data1.com_combo)
    com_combo=[]
    for i in combo:
        res = ast.literal_eval(i)
        com_combo.append(res)
    stock = list(data1.com_stock)
    # sto1 = list(data2.com_stock)
    com_stock=[]
    for i in stock:
        res = ast.literal_eval(i)
        com_stock.append(res)
    # print(com_item)
    # print(com_combo)
    # print(com_stock)
    new_data = pd.DataFrame()
    x = []
    y = []
    z = []
    # print(len(com_item))
    for i in range(len(com_item)):
        for j in range(len(com_combo[i])):
            x.append(com_item[i])
            y.append(com_combo[i][j])
            z.append(com_stock[i][j])
    # print(x)
    # print(y)
    # print(z)
    new_data['com_item']=x
    new_data['com_combo']=y
    new_data['com_stock']=z
    new_data.to_excel("data.xlsx")

# datahandle_first()