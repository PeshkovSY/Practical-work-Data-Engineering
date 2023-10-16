import csv

aver_salary = 0
items = []

with open("text_4_var_26", newline='\n', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        item = {
            'number': int(row[0]),
            'name': row[2] + ' ' + row[1],
            'age': int(row[3]),
            'salary': int(row[4][:-1])
        }
        
        aver_salary += item['salary']
        items.append(item)



aver_salary /= len(items)

filtered = []

filtered = list(filter(lambda item: (item['salary'] > aver_salary and item['age'] > (25 + 26%10)), items))

filtered = sorted(filtered, key=lambda i: i['number'])

with open("r_text_4_var_26", 'w', encoding='utf-8', newline='') as r:
    writer = csv.writer(r, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for item in filtered:
        writer.writerow(item.values())