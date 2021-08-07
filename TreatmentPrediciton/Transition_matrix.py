

infected_initial_rate = [0.923, 0.037, 0.04]
healthy_initial_rate = [0.0001, 0.9999 , 0]
Fvar = 1 
Vvar = 1 
Hvar = 0 
Avar = 18 

def F(num, l):
    l[0] = l[0]*1.1/(1+num)
    l[2] = l[2]*1.1/(1+num)
    l[1] = 1 -l[0]-l[2]

    return l 

print(F(Fvar, infected_initial_rate))

    