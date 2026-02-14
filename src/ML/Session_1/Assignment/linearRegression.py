import numpy as np
class Linear_Regression_Nour_Eldin_Ahmed: 
    def __init__(self, learning_rate=0.01, num_iters=1000):
        self.learning_rate = learning_rate
        self.num_iters = num_iters
        self.w = 0  
        self.b = 0  

    def fit(self, X, y):
        n_samples = len(X)
        sse_values = []

        for _ in range(self.num_iters):
            y_predicted = self.w * X + self.b
            sse = np.sum((y - y_predicted) ** 2)
            sse_values.append(sse)

            dw = (-2 / n_samples) * np.sum(X * (y - y_predicted))
            db = (-2 / n_samples) * np.sum(y - y_predicted)

            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db

        return sse_values