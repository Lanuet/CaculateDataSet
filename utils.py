import codecs

import numpy as np

import traceback

def make_dict(*expr):
    (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
    begin=text.find('make_dict(')+len('make_dict(')
    end=text.find(')',begin)
    text=[name.strip() for name in text[begin:end].split(',')]
    return dict(zip(text,expr))


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
        loc_list = []
        org_list = []
        per_list = []
        len_sents = []
        num_sent = 0
        max_length = 0
        num_word = 0
        num_loc = 0
        num_per = 0
        num_org = 0
        for line in f:
            line = line.strip().split()
            if len(line) > 0:
                word, pos, chunk, tag = line
                word = map_number_and_punct(word.lower())
                words.append(word)
                poss.append(pos)
                chunks.append(chunk)
                tags.append(tag)
                if tag.endswith("LOC"):
                    if tag == "B-LOC": num_loc += 1
                    if word not in loc_list: loc_list.append(word)
                elif tag.endswith("ORG"):
                    if tag == "B-ORG": num_org += 1
                    if word not in org_list: org_list.append(word)
                elif tag.endswith("PER"):
                    if tag == "B-PER": num_per += 1
                    if word not in per_list: per_list.append(word)
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
        return make_dict(word_list, pos_list, chunk_list, tag_list, num_sent, max_length, num_word, average_sent_length, num_org, num_loc, num_per, loc_list, org_list, per_list)


# def concatArray(A):
#     A = np.concatenate(A)
#     A = np.unique(A)
#     return A
#
# def get_new_Nertag(ners):
#     ners = concatArray(ners)
#     print(ners)
#     for ner in ners:
#         ner = ner.replace("I-", "").replace("B-", "")
#     return ners
#
# def getTag(words, ners):
#     words = concatArray(words)
#     ners = concatArray(ners)
#     loc_list = []
#     per_list = []
#     org_list = []
#     for token, ner in zip(words, ners):
#         if ner in ["B-LOC", "I-LOC"]:
#             loc_list.append(token)
#         elif ner in ["B-PER", "I-PER"]:
#             per_list.append(token)
#         elif ner in ["B-ORG", "I-ORG"]:
#             org_list.append(token)
#     return loc_list, per_list, org_list

def countMutualEntity(a,b):
    count = 0
    # for
    return count

def caculateOutOfVocab(A, B):
    vocab = 0
    vocab = [x for x in A if x not in B]
    return vocab