import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords

en_stops = set(stopwords.words('english'))

all_words = ['There', 'is', 'a', 'tree', 'near', 'the', 'river']

for word in all_words:
    if word not in en_stops:
        print(word)