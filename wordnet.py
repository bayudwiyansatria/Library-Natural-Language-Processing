import nltk;
nltk.download('wordnet');
from nltk.corpus import wordnet;
syns = wordnet.synsets( "program" )

synonyms = []
antonyms = [] 
for syn in wordnet.synsets( "good" ):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[ 0 ].name()) 

print( set (synonyms))
print( set (antonyms))

w1 = wordnet.synset( 'ship.n.01' )
w2 = wordnet.synset( 'boat.n.01' )
print (w1.wup_similarity(w2))

# 0.9090909090909091
w1 = wordnet.synset( 'ship.n.01' )
w2 = wordnet.synset( 'car.n.01' )
print (w1.wup_similarity(w2))

# 0.6956521739130435

w1 = wordnet.synset( 'ship.n.01' )
w2 = wordnet.synset( 'cat.n.01' )
print (w1.wup_similarity(w2))

# 0.38095238095238093