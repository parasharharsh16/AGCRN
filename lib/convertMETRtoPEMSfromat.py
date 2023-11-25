import numpy as np
import os
# Function to create 'from', 'to', and 'distance' columns based on adjacency matrix
def generate_pems_format_from_adjacency(adj_matrix, node_vals, file_path):
    # check if npz alrady exists
    if os.path.exists(file_path):
        os.remove(file_path)

    num_nodes = adj_matrix.shape[0]
    from_ids = []
    to_ids = []
    distance = []
    
    # Generate 'from', 'to', and 'distance' based on adjacency matrix
    for i in range(num_nodes):
        for j in range(num_nodes):
            if adj_matrix[i, j] != 0:  # Assuming non-zero elements represent connections
                from_ids.append(i)
                to_ids.append(j)
                # Calculate 'distance' based on node values or a placeholder value
                distance.append(node_vals[i] + node_vals[j])  # Replace with actual distance calculation
    
    return np.array(from_ids), np.array(to_ids), np.array(distance)


def PreprocessDataset(nodefile_path, adjacency_matrix_path, npz_file_path = "data/METR-LA/METR-LA_to_PEMS_from_adjacency.npz", file_type = "npy"):
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
        #file_path = "data/METR-LA/METR-LA_to_PEMS_from_adjacency.npz"
        # Generate 'from', 'to', 'distance' columns based on adjacency matrix and node values
        from_columns, to_columns, distance_columns = generate_pems_format_from_adjacency(adjacency_matrix, node_values,file_path)

        # Create a dictionary to save the PEMS format data
        pems_data = {
            'from': from_columns,
            'to': to_columns,
            'distance': distance_columns
        }

        # Save the data in NPZ format (PEMS format)
        np.savez(file_path, **pems_data)
    else:
        print("Dataset already in desired format")

    return file_path
PreprocessDataset()