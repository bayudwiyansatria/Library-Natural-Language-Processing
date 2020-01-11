from nltk.corpus import stopwords
from nltk.tokenize import word_tokenizeExample_sent = "This is a sample sentence, showing off the stop words filtration.";
from nltk.stem import porterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
# NLTK and stop words
stop_words = set(stopwords.words( 'english' ))
word_tokens = word_tokenize(example_sent)
filtered_sentence = [w for w in word_tokens if not w in stop_words]
filtered_sentence = [] for w in word_tokens:
   if w not in stop_words:
      filtered_sentence.append(w)
      print(word_tokens)
print(filtered_sentence)

# NLTK stem extraction
ps = PorterStemmer()
for w in example_words:
   print (ps.stem(w))

new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
words = word_tokenize(new_text);
for w in words :
   print(ps.stem(w));

# NLTK part-of-speech tagging
train_text = state_union.raw( "2005-GWBush.txt" );
sample_text = state_union.raw( "2006-GWBush.txt" );
Custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
Tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content () :
   try :
      for i in tokenized[: 5 ]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)   Except Exception as e:
            print(str(e))
process_content()

