import codecs

import numpy as np


def filter_not_empty(a):
    return list(filter(lambda x: len(x) > 0, a))


def trim_sentence(s):
    return " ".join(filter_not_empty(s.split()))


def read(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write(filename, string):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(string)


def is_num(c):
    return c in [str(i) for i in range(10)]

def map_number_and_punct(word):
    if any(char.isdigit() for char in word):
        word = u'<number>'
    elif word in [u',', u'<', u'.', u'>', u'/', u'?', u'..', u'...', u'....', u':', u';', u'"', u"'", u'[', u'{', u']',
                  u'}', u'|', u'\\', u'`', u'~', u'!', u'@', u'#', u'$', u'%', u'^', u'&', u'*', u'(', u')', u'-', u'+',
                  u'=']:
        word = u'<punct>'
    return word

def read_conll_format(input_file):
    with codecs.open(input_file, 'r', 'utf-8') as f:
        word_list = []
        chunk_list = []
        pos_list = []
        tag_list = []
        words = []
        chunks = []
        poss = []
        tags = []
        len_sents = []
        num_sent = 0
        max_length = 0
        num_word = 0
        num_loc = 0
        num_per = 0
        num_org = 0
        for line in f:
            line = line.split()
            if len(line) > 0:
                words.append(map_number_and_punct(line[0].lower()))
                poss.append(line[1])
                chunks.append(line[2])
                tags.append(line[3])
            else:
                word_list.append(words)
                pos_list.append(poss)
                chunk_list.append(chunks)
                tag_list.append(tags)
                sent_length = len(words)
                len_sents.append(sent_length)
                num_word += sent_length
                words = []
                chunks = []
                poss = []
                tags = []
                num_sent += 1
                max_length = max(max_length, sent_length)
        average_sent_length = max(len_sents)/len(len_sents)
        for array in tag_list:
            for tag in array:
                if(tag == "B-LOC"):
                    num_loc += 1
                elif(tag == "B-ORG"):
                    num_org += 1
                elif(tag == "B-PER"):
                    num_org +=1
        return word_list, pos_list, chunk_list, tag_list, num_sent, max_length, num_word, average_sent_length, num_org, num_loc, num_per

def concatArray(A):
    A = np.unique(A)
    return A

def get_new_Nertag(ners):
    ners = concatArray(ners)
    print(ners)
    # for ner in ners:
    #     ner = ner.replace("I-", "").replace("B-", "")
    return ners

def getTag(words, ners):
    words = concatArray(words)
    ners = get_new_Nertag(ners)
    data = []
    for token, ner in zip(words, ners):
        if ner not in data:
            data[ner] = [token]
        elif token not in data[ner]:
            data[ner].append(token)
    return data['LOC'], data['PER'], data['ORG']

def countMutualEntity(a,b):
    count = 0
    # for
    return count

def caculateOutOfVocab(A, B):
    vocab = 0
    vocab = [x for x in A if x not in B]
    return vocab