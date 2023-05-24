import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.stem import WordNetLemmatizer
import string
from datetime import datetime
from nltk.tokenize import word_tokenize
import json
import re
import nltk
from nltk.corpus import stopwords
from collections import Counter
nltk.download('stopwords')


def chmura (values_before): 
    text = ' '.join(values_before)

    cleaned_text = re.sub(r'[^\w\s]', '', text)

    words = cleaned_text.lower().split()

    filtered_text = ' '.join(words)

    lemmatizer = WordNetLemmatizer()

    tokens = word_tokenize(filtered_text)

    tokens = [token for token in tokens if token not in string.punctuation]

    custom_stop_words = ['https','brexit', "http", 'uk', 'amp', 'nt', 'u', 'nn','n','de','eu']

    stop_words = set(stopwords.words("english"))

    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

    filtered_tokes2 = [token for token in filtered_tokens if token not in custom_stop_words]

    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokes2]
    
    word_counts = Counter(lemmatized_tokens)
    most_common = word_counts.most_common(10)
    labels, values = zip(*most_common)
    plt.bar(labels, values)
    plt.xticks(rotation=45)
    plt.show()

    wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(word_counts)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

values_before=[]
positive=[]
neutral =[]
negative =[]
arrays = {'Happy': [], 'Angry': [], 'Surprise': [], 'Sad':[], "Fear":[]}

with open("./data/durring.txt", 'r') as file:
    for line in file:
        parsed_data = json.loads(line)
        cleaned_tweet = parsed_data['tweet'].strip("\"")
        data_obiekt = datetime.fromisoformat(parsed_data['date'].strip('"'))
        if(parsed_data['nltk']['compound'] > 0 ):
            positive.append(cleaned_tweet)
        elif(parsed_data['nltk']['compound'] < 0 ):
            negative.append(cleaned_tweet)
        else:
            neutral.append(cleaned_tweet)
        max_value = max(parsed_data['t2e'], key=parsed_data['t2e'].get)
        arrays[max_value].append(cleaned_tweet)
        values_before.append(cleaned_tweet)

# chmura(values_before)
# chmura(arrays["Fear"])
print(len(values_before))
for i in arrays:
    print(i)
    print(len(arrays[i]))
    print(len(arrays[i])/len(values_before)*100)
# chmura(negative)
# chmura(positive)
print("positive:")
print(len(positive))
print(len(positive)/len(values_before)*100)

print("negative:")
print(len(negative))
print(len(negative)/len(values_before) *100)

print("neutral:")
print(len(neutral))
print(len(neutral)/len(values_before) *100)

