import torch
import torch.nn as nn
import numpy as np
import zipfile
import os
# 모델 불러올 때 필요한 듯?
from .model import MalConv

class Lamb():
    def __init__(self):
        self.model_path = 'model/'
        self.model_name = 'test_case_1_sd_1.model'
        self.file_path = '/tmp/check/'
        self.first_n_byte = 2000000
        self.window_size = 500
        
        self.filenames = []
        self.path_filenames = []
        self.path_filename = []

        self.result = {}
        self.result['success'] = {}
        self.result['fail'] = []

        self.sigmoid = nn.Sigmoid()

    def exe_data(self, filename):
        try:
            with open(filename, 'rb') as f:
                tmp = [i+1 for i in f.read()[:self.first_n_byte]]
                tmp = tmp + [0]*(self.first_n_byte-len(tmp))
        except:
            with open(filename.lower(), 'rb') as f:
                tmp = [i+1 for i in f.read()[:self.first_n_byte]]
                tmp = tmp + [0]*(self.first_n_byte-len(tmp))

        return np.array(tmp)

    def check_header(self, filename, num=0):
        with open(filename, 'rb') as f:
            header = f.read(4)
            

            if b'MZ' in header:
                self.filenames.append(filename)
                self.path_filename.append(self.path_filenames[num])
            else:            
                file_name1 = filename.split('/')
                file_name1 = file_name1[len(file_name1)-1]

                self.result['fail'].append(self.path_filenames[num])
            return

    def extract_check_header(self, zipname, extract_to="/tmp/extracted/"):
        with zipfile.ZipFile(zipname, 'r') as zip_ref:
            if not os.path.exists(extract_to):
                os.mkdir(extract_to)

            for num, file_name in enumerate(zip_ref.namelist()):
                zip_ref.extract(file_name, path=extract_to)

                extracted_file_path = os.path.join(extract_to, file_name)
                self.path_filenames.append(file_name)
                if not os.path.isdir(extracted_file_path):
                    self.check_header(extracted_file_path, num)

    def predict(self, filename):
        if '.zip' in filename:
            self.extract_check_header(self.file_path+filename)
        else:
            self.check_header(self.file_path+filename)


        model = torch.load(self.model_path+self.model_name, map_location=torch.device('cpu'), weights_only=False)
        model.eval()

        for num, file in enumerate(self.filenames):
            input_data = self.exe_data(file)
            input_data = torch.tensor(input_data)

            with torch.no_grad():
                pred = model(input_data)

            result = list(self.sigmoid(pred).cpu().numpy())

            file_name1 = file.split('/')
            file_name1 = file_name1[len(file_name1)-1]

            if file_name1 in self.path_filename[num]:
                self.result['success'][self.path_filename[num]] = result[0][0]

        return self.result
