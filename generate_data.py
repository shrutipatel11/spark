import random

f = open("kmeans_data.txt", "a")

for i in range(6000000):
    x = random.uniform(1,1000)
    y = random.uniform(1,1000)
    z = random.uniform(1,1000)
    f.write(str(i) + " 1:" + str(x) + " 2:" + str(y) + " 3:"+ str(z) +'\n' )

f.close()
    