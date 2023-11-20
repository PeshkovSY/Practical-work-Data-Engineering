import numpy as np
import json

mtr = np.load("Task files/matrix_26.npy")

sum = np.sum(mtr)
avr = np.average(mtr)
sumMD = np.trace(mtr)
avrMD = np.average(np.diagonal(mtr))
sumSD = np.fliplr(mtr).diagonal().sum()
avrSD = np.average(np.fliplr(mtr).diagonal())
max = np.max(mtr)
min = np.min(mtr)

mtr_char = {
    "sum": str(sum),
    "avr": str(avr),
    "sumMD": str(sumMD),
    "avrMD": str(avrMD),
    "sumSD": str(sumSD),
    "avrSD": str(avrSD),
    "max": str(max),
    "min": str(min)
}

with open("Program files/mtr_char.json", "w") as json_file:
    json.dump(mtr_char, json_file)