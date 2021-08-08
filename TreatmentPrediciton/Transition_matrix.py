

il = [0.923, 0.037, 0.04]
hl = [0.0001, 0.9999 , 0]
Fvar = 1 
Vvar = 1 
Hvar = 0 
Avar = 18 

#F number function
def F(num, l, state):  #state = 0(sick) or 1(healthy)
    x = l[0]
    y = l[1]
    z = l[2]
    if state == 0:
        x = x*1.1/(1+num)
        z = y*1.1/(1+num)
        y = 1 -x-z
    else: 
        x = x*9000/(1+num)
        z = y*4/(1+num)
        y = 1 -x-z
    return [x,y,z]

#Vaccine function
def V(num,l):
    x = l[0]
    y = l[1]
    z = l[2]
    if num == 1:
        x/=10
        z/=10
        y = 1 -x- z
    return [x,y,z]

#Hospital availability function
def H(num, l):
    x = l[0]
    y = l[1]
    z = l[2]

    if num ==0:
        x*= 1.2
        z*= 1.2
        y = 1-x-z

    else: 
        x*= 0.7
        z*= 0.3
        y = 1-x-z
    
    return [x,y,z]

def A(num, l): 
    x = l[0]
    y = l[1]
    z = l[2]
    x = x*(1+ (num - 20)/1000)
    z = z*(1+ (num - 20)/1000)
    y = 1-x-z

    return[x,y,z]    

def create_transition_matrix(Fvar, Vvar, Hvar, Avar):
    il = F(Fvar,il,0)
    il = V(Vvar,il)
    il = H(Hvar,il)
    il = A(Avar,il)

