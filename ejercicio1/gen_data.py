import random


archi1=open("datos.txt","w") 

for i in range(99):
    archi1.write("{},{}\n".format(i, random.randint(5, 30)))
archi1.write("{},{}".format(i, random.randint(5, 30)))
archi1.close()