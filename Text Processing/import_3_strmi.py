import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer

print(PorterStemmer().stem('running'))
print(LancasterStemmer().stem('running'))
print(SnowballStemmer('english').stem('running'))