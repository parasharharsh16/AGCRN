# This README file is modified to submit the code for assignment.
# This code credit goes to Authors of Model AGCRN

# This code is modified to run on METR-LA datset

## Requirements

Python 3.6.5, Pytorch 1.1.0, Numpy 1.16.3, argparse and configparser

## Link to METR-LA dataset

https://www.kaggle.com/datasets/annnnguyen/metr-la-dataset

- This dataset is in diffrent format (npy files for nodes and adjacency matrix), you need to change this dataset format by putting these downloaded files in data/METR-LA folder.
- Then run the code in lib/convertMETRtoPEMSfromat.py by uncommenting last line.
- For this experiment, i have already added converted NPZ file for METR-LA (which is in data/METR-LA folder), user do not need to redownload and process it.

## How to run
# Run locally on METR-LA dataset 
- (if you want to change the dataset, either pass the argument to run.py or change the dataset name in the code in run.py)
- move to model folder
- python run.py

## Run code on Google Colab on METR-LA dataset 

- Clone the repo to your colab instance by following code
!git clone https://github.com/parasharharsh16/AGCRN.git

- Move to model folder
%cd /content/AGCRN/model

- Run python code
!python Run.py


References:
The credits of this code goes to https://arxiv.org/pdf/2007.02842.pdf



