import numpy as np

numbers=[1,2,3,4,5,6,7,8,9,10]
nparr=np.array(numbers)

for i in range(0,len(numbers)):
    j=numbers[0]*2
    numbers.append(j)
    numbers.pop(0)
print(numbers)

nparrx2=nparr*2
print(nparrx2)

numbers2=[11,12,13,24,15,16,17,18,19,20]

numbersttl=[]
for i in range(0,len(numbers)):
    print(numbers[0])
    print(numbers2[0])
    numbersttl.append(numbers[0]+numbers2[0])
    numbers.remove(numbers[0])
    numbers2.remove(numbers2[0])
nparrttl=nparr+nparrx2

print(numbersttl)
print(nparrttl)