import nltk
from nltk.corpus import stopwords
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english')) 

#read text file
with open('paragraphs.txt', 'r') as file: 
    text = file.read()

words = nltk.word_tokenize(text)

#remove stop words 
filtered_words = [word for word in words if word.lower() not in stop_words]

#count the frequency of each word 
word_frequency = Counter(filtered_words)
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")





