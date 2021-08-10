

#F function
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
        y = (1-x-z)*0.9
        z = 1 -x -y

    else: 
        x = x*0.5
        z = (1 - x - y)*0.9
        y = 1-x-z
    
    return [x,y,z]

def A(num, l): 

    x = l[0]
    y = l[1]
    z = l[2]
    x = x + (1-x)*(num - 20)/500
    z = (1-x-y) + (1-z)*(num - 20)/1000
    y = 1-x-z

    return[x,y,z]    

def create_transition_matrix(il, hl, Fvar, Vvar, Hvar, Avar):
    
    il = F(Fvar,il, 0)
    il = V(Vvar,il)
    il = H(Hvar,il)
    il = A(Avar,il)

    hl = F(Fvar, hl, 1)
    hl = V(Vvar, hl)
    hl = H(Hvar,hl)
    hl = A(Avar, hl)
   

    return [il[0], hl[0], 0], [il[1], hl[1], 0], [il[2], hl[2], 1] 

class transition_matrix:

    il = [0.923, 0.037, 0.04] #initial vector for infected patients
    hl = [0.0001, 0.9999 , 0] #intial vector for healthy patients
    Fvar = 0 
    Vvar = 0
    Hvar = 0 
    Avar = 0

    def __init__(self, Fvar, Vvar, Hvar, Avar):
        self.Fvar = Fvar
        self.Vvar = Vvar
        self.Hvar = Hvar
        self.Avar = Avar
    
    def create_matrix(self):
        return create_transition_matrix(self.il, self.hl, self.Fvar, self.Vvar, self.Hvar,self.Avar)


#transition_matrix = transition_matrix(1,1,0,18)

#print(transition_matrix.create_matrix())