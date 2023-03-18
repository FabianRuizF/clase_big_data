import nltk
nltk.download('words')
nltk.download('brown')

from nltk.corpus import brown
from random import sample
list_of_words = list(brown.words())

n = 1000000
rand_words = sample(list_of_words, n)
df = pd.DataFrame(rand_words,columns=["word"])
BAN_LIST = ["He","She","It"]
