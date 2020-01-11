import nltk;
import TextProcessing;

textToProcess = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard.";
    
filtered = TextProcessing.setStopWord(textToProcess);
print ("Tokenizing Process : ");
print ("");
print(filtered);
print("");

steam = TextProcessing.steamExtraction(textToProcess);

print ("Steam Process : ");
print ("");
print(steam);
print("");

tagging = TextProcessing.taggingText(textToProcess);

print ("Tagging Process : ");
print ("");
print(tagging);
print("");

chunk = TextProcessing.chunking(textToProcess);
#print ("Chunk Process : ");
print ("");
#print(chunk);
print("");
