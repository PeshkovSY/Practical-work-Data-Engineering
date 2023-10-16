with open("text_2_var_26", "r") as f:
    linses = f.readlines()

num_sum = []

for line in linses:
    row_line = (line.strip()
                .replace('.',' ')
                .strip())
    
    numbers = row_line.split(' ')
    numbers = list(map(int, numbers))
    num_sum.append(sum(numbers))


with open("r_text_2_var_26", "w") as r:
    for s in num_sum:
        r.write(str(s)  + '\n')