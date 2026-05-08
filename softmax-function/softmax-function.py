import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.array(x)
    
    if x.ndim == 1:
        max = np.max(x)
        sum = np.sum(np.exp(x - max))
        result = np.exp(x - max) / sum
        return result
    else:
        max = np.max(x, axis=1, keepdims=True)
        sum = np.sum(np.exp(x - max), axis=1, keepdims=True)
        result = np.exp(x - max) / sum
        return result
    pass