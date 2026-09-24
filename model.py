from sklearn.linear_model import LinearRegression

import numpy as np

## Training 
def train():
    ## Realtionship will follow this equation y=2x+3
    #   Data Creation

    x=np.array([[1],[2],[3],[4],[5]]) ## 2D array as sklearn expects the input to be a 2D array(n_samples, b_features)
    y=np.array([5, 7, 9, 11, 13])


    model= LinearRegression() ## Model Creation
    model.fit(x,y)
    
    return model