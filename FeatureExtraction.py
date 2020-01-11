import nltk;
from nltk.corpus import movie_reviews;

def find_features(document) :
    all_words = []
    for word in movie_reviews.words():
        all_words.append(word.lower())

    all_words = nltk.FreqDist(all_words)


    # Convert words into features
    word_features = list(all_words. keys ())[: 3000 ]
    print("")
    print("============================================================== Most Common Word ====================================================================")
    print("")
    print(all_words.most_common(15))
    print("")

    print("===================================================== Number Of Negative Word e.g stupid ===========================================================")
    print("")
    print("Number of 'stupid' word : " + all_words[ "stupid" ])
    print("")

    words_set = document
    features = {}
    for w in word_features:
        features[w] = (w in words_set)    
    return features;