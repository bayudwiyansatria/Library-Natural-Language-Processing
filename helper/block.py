import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentence
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer
train_text = state_union.raw( "2005-GWBush.txt" )
sample_text = state_union.raw( "2006-GWBush.txt" )
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content () :
    try :
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()         
    except Exception as e:
        print(str(e)) 
        process_content()
        for subtree in chunked.subtrees():
            print (subtree)
        for subtree in chunked.subtrees(filter= lambda t: t.label() == 'Chunk' ):
            print(subtree)

#NLTK named entity recognition
Custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)
def process_content () :
    try :
        for i in tokenized[ 5 :]:
            Words = nltk.word_tokenize(i)
            Tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary= True )
            namedEnt.draw()
    except Exception as e:
        print(str(e))

process_content()

# NLTK morphological restoration
lemmatizer = WordNetLemmatizer() 
print(lemmatizer.lemmatize( "cats" ))
print(lemmatizer.lemmatize( "cacti" ))
print(lemmatizer.lemmatize( "geese" ))
print(lemmatizer.lemmatize( "rocks" ))
print(lemmatizer.lemmatize( "python" ))
print(lemmatizer.lemmatize( "better" , pos= "a" ))
print(lemmatizer.lemmatize( "best" , pos= "a" ))
print(lemmatizer.lemmatize( "run" ))
print(lemmatizer.lemmatize( "run" , 'v' ))