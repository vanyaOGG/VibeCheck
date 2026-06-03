import re
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return tokens


print("== Task 3: Testing preprocess() ==")
test_sentences = [
    "I'm SO hyped!!!!",
    "ugh... everything's going wrong",
    "I am very happy today!!!",
    "She was running and jumping in the park.",
    "The cats are playing with their toys."
]
for s in test_sentences:
    print(f"Input:  {s}")
    print(f"Tokens: {preprocess(s)}")
    print()


print("== Task 4: Dataset Exploration ==")
df = pd.read_csv('train.txt', sep=';', header=None, names=['text', 'emotion'])

print("First 10 rows:")
print(df.head(10))
print()

print("Emotion label counts:")
print(df['emotion'].value_counts())
print()

print("Average word count per sentence:")
avg = df['text'].apply(lambda x: len(x.split())).mean()
print(round(avg, 2))
print()


print("== Task 5: Sample sentences by emotion ==")
for emotion in ['joy', 'sadness', 'anger']:
    sample = df[df['emotion'] == emotion].iloc[0]['text']
    print(f"Emotion : {emotion}")
    print(f"Original: {sample}")
    print(f"Tokens  : {preprocess(sample)}")
    print()