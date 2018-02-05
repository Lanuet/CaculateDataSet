import codecs
import glob
import re
import utils

import os

import utils

def sumTokens(folder):
    files = glob.glob(os.path.join(folder, "**", "*.txt")) #file tokenized
    sum = 0
    for file in files:
        # sum += countTokens_inFile(file)
        pass
    return sum


def generateMatrix(word_list, tag_list):
    return


def main():
    folder_1 = "D:\Khoa luan\Models\Data\VLSP2018-Train"
    folder_2 = "D:\Khoa luan\Models\Data\VLSP2018-Dev"
    train_dir = "dev_sample.txt"
    data = utils.read_conll_format(train_dir)
    print(data)
    loc_list = data['loc_list']
    per_list = data['per_list']
    org_list = data['org_list']
    print (loc_list)

if __name__ == '__main__':
    main()