import numpy as np
import json
import msgpack

with open("Task files/products_26.json") as file:
    product_dict = json.load(file)


dict_len = len(product_dict)

dict_set = set()
dict_list = []
prod = []


for i in range(dict_len):
    dict_set.add(product_dict[i].get("name"))
    k, v = product_dict[i].items()
    dict_list.append([k[1],v[1]])

mtr = np.array(dict_list)

for s in range(len(dict_set)):
    p = dict_set.pop()
    index = np.where(mtr == p)

    m1, m2 = np.hsplit(mtr,2)

    price =  m2[index[0]].astype(float)

    avr = np.average(price)
    max = np.max(price)
    min = np.min(price)

    prod_char = {
        "product" : p,
        "avr": str(avr),
        "max": str(max),
        "min": str(min)
    }

    prod.append(prod_char)

    print(p, avr, max, min)



with open("Program files/prod_char.json", "w") as json_file:
    json.dump(prod, json_file, indent=4)

with open("Program files/prod_char_msg", "bw") as file:
    msgpack.dump(prod, file)