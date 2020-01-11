import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import state_union

def tokenizedText(text):
    return word_tokenize(text)

def setStopWord(text):
    stop_words = set(stopwords.words( 'english' ))
    word_tokens = tokenizedText(text)
    filtered_sentence = [word for word in word_tokens if not word in stop_words]
    filtered_sentence = []
    for word in word_tokens:
        if word not in stop_words:
            filtered_sentence.append(word)
    return filtered_sentence

def steamExtraction(text):
    steammer = []
    for word in setStopWord(text):
        steammer.append(PorterStemmer().stem(word))
    return steammer

def taggingText(text):
    tokenized = steamExtraction(text)
    return nltk.pos_tag(tokenized)

def chunking(text):
    chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(taggingText(text))
    #chunked.draw()
    return chunked