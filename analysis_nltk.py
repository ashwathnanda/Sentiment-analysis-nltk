import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

#function to tokenise each sentence
def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})

#list to append each sentence from each file
pos = []
with open("./pos_com.txt") as f:
    for i in f: 
        pos.append([format_sentence(i), 'pos'])

neg = []
with open("./neg_com.txt") as f:
    for i in f: 
        neg.append([format_sentence(i), 'neg'])
        
#spliting the sentences for training 80% and test 20% 
training = pos[:int((.8)*len(pos))] + neg[:int((.8)*len(neg))]
test = pos[int((.8)*len(pos)):] + neg[int((.8)*len(neg)):]

#initialising count values
pos_count=0
neg_count=0
n_count=0
c=0

#naive bayes training function
classifier = NaiveBayesClassifier.train(training)

classifier.show_most_informative_features()


#running the classifier over any text file and checking its sentiment
with open("./comments.txt", encoding='utf-8') as f:
    for line in f:
        t=classifier.classify(format_sentence(line))
        c+=1
        if t=="neg":
            neg_count+=1
        elif t=="pos":
            pos_count+=1
        else:
            n_count+=1

print("accuracy of the classifier ",accuracy(classifier,test))
print('Total positive comments',pos_count)
print('total negative comments',neg_count)
