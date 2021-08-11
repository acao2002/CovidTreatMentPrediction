import numpy as np 
from Transition_matrix_class import transition_matrix

class model: 
    matrix = np.array([[0],[0],[0]],np.float32)

    def __init__(self, Pmatrix):
        self.Pmatrix = np.array([Pmatrix[0], Pmatrix[1], Pmatrix[2]], np.float32)
        

    def predict(self, state, days):
        self.matrix[state] = 1
        for i in range(days-1):
            self.Pmatrix = np.matmul(self.Pmatrix, self.Pmatrix)
        prediction = np.matmul(self.Pmatrix, self.matrix)
        return prediction
    

transition_matrix = transition_matrix(0, 0 ,1,18)

Pmatrix = transition_matrix.create_matrix()
print(Pmatrix)
state = 0
days = 1
model = model(Pmatrix)
print(model.predict(state, days))