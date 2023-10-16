with open("text_3_var_26", "r") as f:
    linses = f.readlines()

matrix = []

for line in linses:
    nums = line.strip().split(',')
    if 'NA' in nums:
        for i in range(len(nums)):
             if nums[i] == 'NA':
                    nums[i] = str((int(nums[i-1])+int(nums[i+1])) / 2)
    
    nums = list(filter(lambda x: (x > (50+26)**2), map(float, nums)))
    nums = list(map(str,nums))
    nums = ','.join(nums)
    nums = nums.replace('.0','')
    matrix.append(nums)

with open("r_text_3_var_26", "w") as r:
    for line in matrix:
        r.write(str(line) + '\n')