import requests
import json
from bs4 import BeautifulSoup


text = ''
linse = ''

url = "http://httpbin.org/get"
response = requests.get(url)

json_data = response.json()
data = json_data['headers']

print(json_data)

for line in data:
    linse += '<li>' + line + ' : ' + data[line] + '</li>'

text = '<!DOCTYPE html><html><ul>' + linse + '</ul></html>'

soup = BeautifulSoup(text, "html.parser")

table = soup.prettify()

with open("r_text_6_var_26.html", "w") as r:
    for line in table:
        r.write(str(line))