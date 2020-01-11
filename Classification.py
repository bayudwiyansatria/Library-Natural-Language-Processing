import nltk;
import random;
from nltk.corpus import movie_reviews;

documents = [
    (list(movie_reviews.words(fileid)), category)
    for category in movie_reviews.categories()
        for fileid in movie_reviews.fileids(category)
]

random.shuffle(documents)
print(documents[1])
                
all_words = []
for word in movie_reviews.words():
    all_words.append(word.lower())

all_words = nltk.FreqDist(all_words)

print("")
print("============================================================== Most Common Word ====================================================================")
print("")
print(all_words.most_common(15))
print("")

print("===================================================== Number Of Negative Word e.g stupid ===========================================================")
print("")
print(all_words[ "damn" ])
print("")

# Convert words into features
word_features = list(all_words. keys ())[: 3000 ]

def find_features(document) :
    words_set = document
    features = {}
    for w in word_features:
        features[w] = (w in words_set)    
    return features;

featuresets = [(find_features(rev), category) for (rev, category) in documents]

print("")
print("============================================================= Feature ==============================================================================")
print("")
#print(featuresets);

# Naive Bayes Classifier 
training_set = featuresets[: 1900 ]
testing_set = featuresets[ 1900 :]

classifier = nltk.NaiveBayesClassifier.train(training_set);
informative_feature = classifier.show_most_informative_features(10);
print("Naive Beyes Accuracy : ", (nltk.classify.accuracy(classifier, testing_set))*100, " % ");