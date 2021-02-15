#import bs4 as bs
#import urllib.request
import pandas as pd
import re
import nltk
import csv

#scraped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')
#article = scraped_data.read()

#parsed_article = bs.BeautifulSoup(article,'lxml')

#paragraphs = parsed_article.find_all('p')
#print(type(paragraphs))
def summerize():
    word_frequencies = {}
    text = ''
    tweets = pd.read_csv('file.csv', header = None)
    emails = pd.read_csv('file1.csv', header = None)
    #tweets.head()
    with open('file.csv', 'r', encoding= 'utf-8') as file:
        reader = csv.reader(file)
        for each in reader:
            if each:
                text += each[0]
    with open('file1.csv', 'r', encoding= 'utf-8') as file:
        reader = csv.reader(file)
        for each in reader:
            if each:
                text += each[1]
    '''
    for p in tweets.columns[0]:
        #print(tweets[p])
        article_text += str(tweets[p])
    for p in emails[1]:
        article_text += str(emails[p])
'''

    cleanedText = re.sub('[^a-zA-Z]', ' ', text )
    cleanedText = re.sub(r'\s+', ' ', text)

    sentence_list = nltk.sent_tokenize(text)

    stopwords = nltk.corpus.stopwords.words('english')

    for word in nltk.word_tokenize(cleanedText):
        if word not in stopwords:
            if word not in word_frequencies:
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
    max_frequncy = 0
    for each in word_frequencies:
        if max_frequncy < word_frequencies[each]:
            max_frequncy = word_frequencies[each]
    #print(maximum_frequncy)

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/max_frequncy)


    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies:
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores:
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    import heapq
    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)

    return summary
