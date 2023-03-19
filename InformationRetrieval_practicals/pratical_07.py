import io
from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('English'))
file1 = open("d:\\text1.txt")
line = file1.read()
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open("d:\\filteredtext.txt", "a")
        appendFile.write(" " +r)
        appendFile.close()