import numpy as np

def calculate(list):
    if len(list)<9:
        raise ValueError("List must contain nine numbers.")
    a=np.array(list)
    b=a.reshape(3,3)
    
    calculations={}
    calculations["mean"]=[b.mean(axis=0).tolist(),b.mean(axis=1).tolist(),b.mean()]
    calculations["variance"]=[b.var(axis=0).tolist(),b.var(axis=1).tolist(),b.var()]
    calculations["standard deviation"]=[b.std(axis=0).tolist(),b.std(axis=1).tolist(),b.std()]
    calculations["max"]=[b.max(axis=0).tolist(),b.max(axis=1).tolist(),b.max()]
    calculations["min"]=[b.min(axis=0).tolist(),b.min(axis=1).tolist(),b.min()]
    calculations["sum"]=[b.sum(axis=0).tolist(),b.sum(axis=1).tolist(),b.sum()]


    return calculations