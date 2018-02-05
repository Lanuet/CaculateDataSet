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
    word_list_train, pos_list_train, chunk_list_train, tag_list_train, num_sent_train, max_length_train, num_word, average_sent_length, num_org, num_loc, num_per  = \
        utils.read_conll_format(train_dir)
    print(num_word, num_per, num_loc, num_org)
    loc_list, per_list, org_list = utils.getTag(word_list_train, tag_list_train)
    # print (loc_list)

if __name__ == '__main__':
    main()