import numpy as np
inputs = np.array([[0.5, -0.2, 0.1]])
targets = np.array([[0.4]])
test_w_i_h = np.array([[0.1, -0.2],
                       [0.4, 0.5],
                       [-0.3, 0.2]])
test_w_h_o = np.array([[0.3],
                       [-0.1]])

activation_function = lambda x : 1/1+np.exp(-x)
print(activation_function(0.5)==(1/1+np.exp(-0.5)))