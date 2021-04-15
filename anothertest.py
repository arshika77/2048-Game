from copy import deepcopy
#x = []

#x[2][3] = 1

#print(x[0][1])
temp_var = []
l = []
for i in range(4):
    temp_var.append(deepcopy(l))

print(temp_var[0][0])