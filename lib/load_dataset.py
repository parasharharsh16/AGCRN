import os
import numpy as np
from lib.convertMETRtoPEMSfromat import PreprocessDataset

def load_st_dataset(dataset):
    #output B, N, D
    if dataset == 'PEMSD4':
        data_path = os.path.join('../data/PEMS04/PEMS04.npz')
        data = np.load(data_path)['data'][:, :, 0]  #onley the first dimension, traffic flow data
    elif dataset == 'PEMSD8':
        data_path = os.path.join('../data/PEMS08/PEMS08.npz')
        data = np.load(data_path)['data'][:, :, 0]  #onley the first dimension, traffic flow data
    elif dataset == 'PEMSD7':
        data_path = os.path.join('../data/PEMS07/PEMS07.npz')
        data = np.load(data_path)['data'][:, :, 0]  #code added to test on diffrent dataset
    elif dataset == 'METR-LA':
        """
        Either you give dataset files path for node and adjacency file which are downloaded from kaggle
        or 
        you give path for npz file which is the converted dataset in PEMS format which contains three columns
        1. from
        2. to
        3. distance

        if you are giving NPY files then put file type 'npy' else put 'npz'
        """
        data_path = os.path.join(PreprocessDataset(file_type="npz",npz_file_path="../data/METR-LA/METR-LA_to_PEMS_from_adjacency.npz"))
        data = np.load(data_path)['data'][:, :, 0] 
    else:
        raise ValueError
    if len(data.shape) == 2:
        data = np.expand_dims(data, axis=-1)
    print('Load %s Dataset shaped: ' % dataset, data.shape, data.max(), data.min(), data.mean(), np.median(data))
    return data


# np.load('data/METR-LA/adj_mat.npy')  
# node_values = np.load('data/METR-LA/node_values.npy')  