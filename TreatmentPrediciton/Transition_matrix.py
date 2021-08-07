

infected_initial_rate = [0.923, 0.037, 0.04]
healthy_initial_rate = [0.0001, 0.9999 , 0]
Fvar = 1 
Vvar = 1 
Hvar = 0 
Avar = 18 

def F(num, l):
    x = l[0]
    y = l[1]
    z = l[2]
    x = x*1.1/(1+num)
    y = y*1.1/(1+num)
    z = 1 -x-y

    return [x,y,z]

def V(num,l):
    x = l[0]
    y = l[1]
    z = l[2]
    if num == 1:
        x/=10
        z/=10
        y = 1 -x- z
    return [x,y,z]


test = (V(Vvar, infected_initial_rate))

print(test)


