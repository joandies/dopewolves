from os import listdir
import os
from tqdm import tqdm

path=r'C:\Users\joand\OneDrive\Escritorio\NFT\nft-gen\DWresults/'

for filename in tqdm(listdir(path)):
    if filename.endswith('.json'):
        print(filename)
        os.remove(path+filename)