import numpy as np
import pickle
import json

with open('Task files/products_26.pkl', 'rb') as pickle_in: 
    products_list = pickle.load(pickle_in) 
    
with open("Task files/price_info_26.json") as file:
    product_info = json.load(file)

prod = []
prod_info = []

for i in range(len(products_list)):
    k, v = products_list[i].items()
    prod.append([k[1],v[1]])

prod_mtr = np.array(prod)

for i in range(len(product_info)):
    k, v, p = product_info[i].items()
    prod_info.append([k[1],v[1],p[1]])

prod_info_mtr = np.array(prod_info)
new_prod_mtr = np.copy(prod_mtr)

for i in range(len(product_info)):
    index = np.where(prod_mtr == prod_info_mtr[i][0])  
    namder = index[0]
    
    method = prod_info_mtr[i][1]   
    param = prod_info_mtr[i][2].astype(float)
    price = new_prod_mtr[*namder][1].astype(float)

    match method:
        case "sum":                           
            new_prod_mtr[*namder][1] =  price + param
        case "sub":                         
            new_prod_mtr[*namder][1] =  price - param
        case "percent+":                             
            new_prod_mtr[*namder][1] =  price + (param * price)
        case "percent-":                             
            new_prod_mtr[*namder][1] =  price - (param * price)


new_prod = []

for i in range(len(products_list)):
    new_prod.append({'name': new_prod_mtr[i][0], 'price': new_prod_mtr[i][1]})

with open("Program files/products_updated.pkl", "wb") as f:
    f.write(pickle.dumps(new_prod))

