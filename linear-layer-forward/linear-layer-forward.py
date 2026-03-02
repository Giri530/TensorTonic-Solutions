def linear_layer_forward(X,W,B):
    x=np.array(X)
    w=np.array(W)
    b=np.array(B)
    return (x@w+b).tolist()