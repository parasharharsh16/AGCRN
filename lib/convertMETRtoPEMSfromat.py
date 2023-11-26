import numpy as np
import os

def PreprocessDataset(nodefile_path = "data/METR-LA/node_values.npy", adjacency_matrix_path="data/METR-LA/adj_mat.npy", npz_file_path = "data/METR-LA/METR-LA_to_PEMS_from_adjacency.npz", file_type = "npy"):
    """
    Either you give dataset files path for node and adjacency file which are downloaded from kaggle
    or 
    you give path for npz file which is the converted dataset in PEMS format which contains three columns
    1. from
    2. to
    3. distance

    if you are giving NPY files then put file type 'npy' else put 'npz'
    """
    file_path = npz_file_path

    if file_type == "npy":
        adjacency_matrix = np.load(adjacency_matrix_path)  
        node_values = np.load(nodefile_path)  
        # Extract traffic flow data from node_data
        traffic_flow_data = node_values[:, :, 0]  # Assuming traffic flow is in the first column

        # Reshape traffic flow data to match the desired format (num_samples, num_nodes, 1)
        traffic_flow_data_reshaped = traffic_flow_data[:, :, np.newaxis]

        # Save traffic flow data in the .npz format with key 'data'
        np.savez(file_path, data=traffic_flow_data_reshaped)
    else:
        print("Dataset already in desired format")


    return file_path

#PreprocessDataset()