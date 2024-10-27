import torch
import torch.nn as nn
import numpy as np
from src.model import MalConv

class Lamb():
    def __init__(self):
        self.model_path = 'model/'
        self.file_path = 'tmp/check/'
        self.first_n_byte = 2000000
        self.window_size = 500
        
        self.result = {}
        self.result['success'] = {}
        self.result['fail'] = []

        self.sigmoid = nn.Sigmoid()

    def exe_data(self, filename):
        try:
            with open(self.file_path+filename, 'rb') as f:
                tmp = [i+1 for i in f.read()[:self.first_n_byte]]
                tmp = tmp + [0]*(self.first_n_byte-len(tmp))
        except:
            with open(self.file_path+filename.lower(), 'rb') as f:
                tmp = [i+1 for i in f.read()[:self.first_n_byte]]
                tmp = tmp + [0]*(self.first_n_byte-len(tmp))

        return np.array(tmp)

    def predict(self, filename):
        model = torch.load(self.model_path+'test_case_1_sd_1.model', map_location=torch.device('cpu'), weights_only=False)
        model.eval()

        input_data = self.exe_data(filename)
        input_data = torch.tensor(input_data)

        with torch.no_grad():
            pred = model(input_data)

        result = list(self.sigmoid(pred).cpu().numpy())
        print(result[0][0])
