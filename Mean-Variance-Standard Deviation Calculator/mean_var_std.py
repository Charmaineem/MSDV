import numpy as np

def calculate(list):
    if (len(list) != 9):
        raise ValueError('List must contain nine numbers.')
    
    array = np.array(list).reshape(3,3)
    
    #mean
    rows_mean = array.mean(axis=1).tolist()
    columns_mean = array.mean(axis=0).tolist()
    total_mean= array.mean().tolist()
    mean = [columns_mean,rows_mean,total_mean]
    
    #variance
    rows_variance = array.var(axis=1).tolist()
    columns_variance = array.var(axis=0).tolist()
    total_variance = array.var().tolist()
    variance = [columns_variance,rows_variance,total_variance]
    
    #standard deviation
    rows_std = array.std(axis=1).tolist()
    columns_std= array.std(axis=0).tolist()
    total_std = array.std().tolist()
    std = [columns_std,rows_std,total_std]
    
    #max
    rows_max = array.max(axis=1).tolist()
    columns_max = array.max(axis=0).tolist()
    total_max = array.max().tolist()
    max = [columns_max,rows_max, total_max]
    
    #min
    rows_min = array.min(axis=1).tolist()
    columns_min = array.min(axis=0).tolist()
    total_min = array.min().tolist()
    min= [columns_min,rows_min, total_min]
    
    #sum
    rows_sum = array.sum(axis=1).tolist()
    columns_sum = array.sum(axis=0).tolist()
    total_sum = array.sum().tolist()
    sum = [columns_sum,rows_sum, total_sum]
    
    calculations = {}
    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std,
        'max': max,
        'min':min,
        'sum': sum
    }
    
    return calculations