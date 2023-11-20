import numpy as np

mtr = np.load("Task files/matrix_26_2.npy")

var = 526

index = np.where(mtr > var)

x = index[0]
y = index[1]
z = mtr[index]

np.savez("Program files/matrix_26_2.npz",x,y,z)
np.savez_compressed("Program files/matrix_26_2_com.npz",x,y,z)