import numpy as np
import random
from matplotlib import pyplot as plt

flag = 0
mat = np.full((6,6),1)
i=j=0
maxNum = 60
while(i<6):
    while(j<6):
        mat[i][j]=random.randint(-400,400)
        j+=1
    i+=1
    j=0
print(mat)
print("\n")
t1_norm =[]
t2_norm =[]
tInf_norm = []
i=1
while (i<maxNum):
    if flag==0:
        tempMat = np.matmul(np.identity(6),mat)
        flag=1
    else:
        tempMat = np.matmul(tempMat,mat)
    t1_norm.insert(i,((np.linalg.norm(tempMat,1)))**(1/i))
    t2_norm.insert(i,(np.linalg.norm(tempMat,2))**(1/i))
    tInf_norm.insert(i,(np.linalg.norm(tempMat,np.inf))**(1/i))
    i+=1

plt.plot(np.array(t1_norm),marker='.',color='y',linestyle='None')
plt.plot(np.array(t2_norm),marker='.',color='m',linestyle='None')
plt.plot(np.array(tInf_norm),marker='.',color='k',linestyle='None')
plt.show()
