import nltk
from nltk.stem import PorterStemmer

ws = PorterStemmer()

print(ws.stem('eating'))
print(ws.stem('running'))