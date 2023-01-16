import os
import re
import numpy as np
import nltk
import pandas as pd
from nltk.stem import PorterStemmer
from scipy.io import loadmat
# from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.datasets import load


def get_sample(fn1):
    with open(fn1, 'r') as f:
        content1 = f.read()
    return content1


def word_tokenize(content1):
    """
    content: str - body of mail
    return: list of tokens (str) e.g. ['>', 'Anyone', 'knows', 'how', 'much', 'it', 'costs', 'to', 'host', 'a']
    """
    # YOUR_CODE.  Split the content to tokens. You may need re.split()
    # START_CODE
    token = np.array(nltk.casual_tokenize(content1))
    # END_CODE

    return token


def lower_case(token):
    """
    tokens: ndarry of str
    return: ndarry of tokens in lower case (str)
    """
    # YOUR_CODE.  Make all tokens in lower case
    # START_CODE
    token = np.char.lower(token)
    # END_CODE

    return token


def normalize_tokens(token):
    """
    tokens: ndarry of str
    return: ndarry of tokens replaced with corresponding unified words

    # YOUR_CODE.
    # Remove html and other tags
    # mark all numbers "number"
    # mark all  urls as "httpaddr"
    # mark all emails as "emailaddr"
    # replace $ as "dollar"
    # get rid of any punctuation
    # Remove any non-alphanumeric characters
    #  You may  need re.sub()
    """
    # START_CODE
    token = np.array(list(map(lambda v: re.sub(r'[>:.,?]', '', v), token)))
    token = np.array(list(map(lambda v: re.sub(r'\d', 'number', v), token)))
    token = np.array(list(map(lambda v: re.sub(r'http\S+', 'httpaddr', v), token)))
    token = np.array(list(map(lambda v: re.sub(r'\S+@\S+', 'emailaddr', v), token)))
    token = np.array(list(map(lambda v: re.sub(r'\$', 'dollar', v), token)))
    # END_CODE
    return token


def filter_short_tokens(token):
    """
    tokens: ndarry of str
    return: ndarry of filtered tokens (str)
    """
    original_tokens_len = len(token)
    # YOUR_CODE. Keep only tokens that length >0
    # START_CODE
    token = token[token != '']
    # END_CODE

    print('Original len= {}\nRemaining len= {}'.format(original_tokens_len, len(token)))

    return token


def stem_tokens(token):
    """
    tokens: ndarry of str
    return: ndarry of stemmed tokens e.g. array(['anyon', 'know', 'how', 'much', 'it', 'cost', 'to', 'host', 'a',
       'web', 'portal', 'well', 'it', 'depend', 'on', 'how', 'mani']...
    """
    # YOUR_CODE. replace the tokens by stemmed form. You may need PorterStemmer.stem()
    # START_CODE
    ps = PorterStemmer()
    token = np.array(list(map(lambda word: ps.stem(word), token)))
    # END_CODE

    return token


def get_vocabulary(fn1):
    """
    fn: str - full path to file
    return: ndarray of str e.g. array(['aa', 'ab', 'abil', ..., 'zdnet', 'zero', 'zip'], dtype=object)
    """
    vocab_list = pd.read_table(fn1, header=None)
    vocabl = np.array(vocab_list)[:, 1]  # first columns is index, select only words column
    print('len(vocab)= {:,}'.format(len(vocabl)))
    return vocabl


def represent_features(token, vocabulary):
    """
    tokens: ndarry of str
    return: ndarry of binary values 1 if word from vocabulary is in mail 0 otherwise
    """
    # YOUR_CODE. Compute the array with 1/0 corresponding to is word from vocabulary in mail
    # START_CODE
    tokens_represented = np.zeros(len(vocabulary))
    for i in vocabulary:
        if i in token:
            tokens_represented[np.where(vocabulary == i)[0]] = 1
    # END_CODE

    print('{} word(s) from vocab are in the tokens.'.format(np.sum(tokens_represented)))

    return tokens_represented


def preprocess(_content, _vocab):
    """
    content: str - body of mail
    vocab: ndarray of str - list of considered words
    """
    # YOUR_CODE. Compute the array with 1/0 corresponding to is word from vocabulary in mail
    # START_CODE

    # tokenize content
    token = word_tokenize(_content)

    # make lower case
    token = lower_case(token)

    # normalize tokens
    token = normalize_tokens(token)

    # remove zero words
    token = filter_short_tokens(token)

    # stem words
    token = stem_tokens(token)

    # convert to binary array of features
    tokens_represented = represent_features(token, _vocab)
    # END_CODE

    return tokens_represented


def check_spam():  # arr_binary):
    fn1 = os.path.join(os.getcwd(), 'data/spamTrain.mat')

    mat = loadmat(fn1)
    X_train = mat['X']
    y_train = mat['y'].ravel()

    print('X_train.shape= ', X_train.shape)
    print('y_train.shape= ', y_train.shape)

    fn1 = os.path.join(os.getcwd(), 'data/spamTest.mat')
    mat = loadmat(fn1)
    X_test = mat['Xtest']
    y_test = mat['ytest'].ravel()

    print('X_test.shape= {}', X_test.shape)
    print('y_test.shape= {}', y_test.shape)
    index = 0
    print('Sample with index  ={}: \n{}'.format(index, X_train[index]))

    clf = LinearSVC(C=1)
    clf.fit(X_train, y_train)
    print('Score train= {}'.format(clf.score(X_train, y_train)))
    print('Score test= {}'.format(clf.score(X_test, y_test)))

    return clf


if __name__ == '__main__':
    """
    tokens = '''> Anyone knows how much it costs to host a web portal ?\n>\nWell, it depends on how many visitors 
    you're expecting.\nThis can be anywhere from less than 10 bucks a month to a couple of $100. \nYou should 
    checkout http://www.rackspace.com/ or perhaps Amazon EC2 \nif youre running something big..\n\nTo unsubscribe 
    yourself from this mailing list, send an email to:\ngroupname-unsubscribe@egroups.com\n\n'''
    """
    fn = os.path.join(os.getcwd(), 'data/vocab.txt')
    vocab = get_vocabulary(fn)

    for sfn in ['data/emailSample1.txt', 'data/emailSample2.txt', 'data/spamSample1.txt', 'data/spamSample2.txt']:
        fn = os.path.join(os.getcwd(), sfn)
        content = get_sample(fn)

        # YOUR_CODE.  Preprocess the sample and get prediction 0 or 1 (1 is spam)
        # START_CODE
        tokens = preprocess(content, vocab)
        prediction = check_spam().predict([tokens])
        # END_CODE

        print('{} is {}\n'.format(sfn, ('Not Spam', 'Spam')[prediction[0]]))

    print('Latter sample:\n{1}\n{0}\n{1}'.format(content, '=' * 50))
