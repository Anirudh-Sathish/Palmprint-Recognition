# Extracting from our own custom dataset for pytorch 
import torch 
import os 
import pandas as pd 
from torch.utils.data import Dataset
from skimage import io 

class PalmprintDataset(Dataset):
    def __init__(self,csv_file , root)