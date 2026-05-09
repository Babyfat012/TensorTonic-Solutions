import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """

    y_pred = np.asarray(y_pred)
    N = len(y_true)
    rows = np.arange(len(y_true))
    cols = y_true
    log_probs = np.log(y_pred[rows, cols])
    loss = -np.mean(log_probs)
    
    return loss