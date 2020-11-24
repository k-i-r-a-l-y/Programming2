import csv
import string
import nltk
from nltk.corpus import stopwords

class MyNLP:

    def __init__(self, file_name):
        self.csv_file = csv.reader(open(file_name, 'r', encoding = 'utf8'), delimiter = ';')
        self.tweets = []

    def preprocessing(self):
        i = 0
        for tweet in self.csv_file:
            tmp = tweet[4].lower()
            tmp = self.eliminate_tags(tmp, 'http')
            tmp = self.eliminate_tags(tmp, 'pic.')
            tmp = self.eliminate_tags(tmp, '# ')
            tmp = self.eliminate_tags(tmp, '@ ')
            tmp = self.remove_punctuation(tmp)
            self.tweets.append(tmp)
            # i += 1
            # if i % 500 == 0:
            #     print("Eredeti:{}\nKitakaritott: {}".format(tweet[4],tmp))


    def eliminate_tags(self, tweet, tag):
        ind = tweet.find(tag)
        while ind != -1:
            ind_end = tweet.find(' ', ind + len(tag))
            if ind_end == -1:
                tweet = tweet[:ind]
            else:
                tweet = tweet[:ind] + tweet[ind_end:]
            ind = tweet.find(tag)
        return tweet

    def remove_punctuation(self, tweet):
        res_tweet = ''
        for ch in tweet:
            if ch not in string.punctuation:
                res_tweet += ch
        return res_tweet

    def bag_of_words(self):
        self.bow = []
        for tweet in self.tweets:
            tweet = tweet.split(' ')
            for word in tweet:
                if word != '':
                    self.bow.append(word)
        return self.bow

    def remove_stopwords(self):
        #nltk.download('stopwords-english')
        stopwords_list = stopwords.words('english')
        new_bow = []
        for word in self.bow:
            if word not in stopwords_list:
                new_bow.append(word)
        self.bow = new_bow

#print(string.punctuation)
nlp = MyNLP("TrumpTweets.csv")
nlp.preprocessing()
bow = len(nlp.bag_of_words())
unique_bow = len(set(nlp.bag_of_words()))
print("{}% egyedi szó a teljes szövegben.".format(unique_bow / bow * 100))
nlp.remove_stopwords()
bow = len(nlp.bow)
unique = len(set(nlp.bow))
print("{}% egyedi szó a teljes szövegben.".format(unique_bow / bow * 100))