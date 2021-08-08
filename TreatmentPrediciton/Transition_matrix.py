

il = [0.923, 0.037, 0.04]
hl = [0.0001, 0.9999 , 0]
Fvar = 0
Vvar = 0 
Hvar = 0 
Avar = 60

#F number function
def F(num, l, state):  #state = 0(sick) or 1(healthy)
    x = l[0]
    y = l[1]
    z = l[2]
    if state == 0:
        x = x*1.01/(1+num)
        z = z*1.01/(1+num)
        y = 1 -x-z
    else: 
        x = x*9000/(1+num)
        z = z+1/100*(1+num)
        y = 1 -x-z
    return [x,y,z]

#Vaccine function
def V(num,l):
    x = l[0]
    y = l[1]
    z = l[2]
    if num == 1:
        x/=10
        z/= 10
        y = 1 -x- z
    return [x,y,z]

#Hospital availability function
def H(num, l):
    x = l[0]
    y = l[1]
    z = l[2]

    if num == 0:
        x = x+(1-x)*0.5
        z = (1 - x - y)*2
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
    x = x*(1+ (num - 20)/100)
    z = z*(1+ (num - 20)/100)
    y = 1-x-z

    return[x,y,z]    

def create_transition_matrix(Fvar, Vvar, Hvar, Avar):
    global il, hl
    il = F(Fvar,il, 0)
    print(il)
    il = V(Vvar,il)
    print(il)
    il = H(Hvar,il)
    print(il)
    il = A(Avar,il)
    print("il")
    print(il)

    hl = F(Fvar, hl, 1)
    print(hl)
  
    hl = V(Vvar, hl)
    print(hl)
    hl = H(Hvar,hl)
    print(hl)
    hl = A(Avar, hl)
    print(hl)




create_transition_matrix(Fvar,Vvar,Hvar, Avar)

