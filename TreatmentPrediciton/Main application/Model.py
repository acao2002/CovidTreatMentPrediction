import numpy as np 

class model: 

    def __init__(self, Pmatrix, matrix):
        self.Pmatrix = np.array(Pmatrix[0], Pmatrix[1], Pmatrix[2], np.float32)
        self.matrix = np.array([[0],[0],[0]],np.float32)

    def predict(self, state, days):
        self.matrix[state] = 1
        for i in range(days-1):
            self.Pmatrix = np.mathmul(self.Pmatrix, self.Pmatrix)
        prediction = np.matmul(self.Pmatrix, self.matrix)
        return prediction
    
