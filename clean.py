from os import listdir
import os
from tqdm import tqdm

path=r'path-to-folder'

for filename in tqdm(listdir(path)):
    if filename.endswith('.json'):
        print(filename)
        os.remove(path+filename)
