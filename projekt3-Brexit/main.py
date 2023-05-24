import nltk
import json
import text2emotion as t2e
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

with open('./data/twitter19-20.jsonl', 'r') as file, open('./data/before.txt', 'w') as output_file:
    for line in file:
        parsed_data = json.loads(line)
        new_data = parsed_data["rawContent"]
        data = json.dumps(new_data)
        tokens = nltk.word_tokenize(data)
        tokens = [token.replace('#', '') for token in tokens]
        data = " ".join(tokens)
        data= json.dumps(data)
        dane={}
        dane["tweet"]=data
        dane["nltk"]=sid.polarity_scores(data)
        dane["t2e"]=t2e.get_emotion(data)
        dane["date"] = json.dumps(parsed_data["date"])
        json_data = json.dumps(dane)
        output_file.write(json_data)
        output_file.write('\n')   

with open('./data/twitter20.jsonl', 'r') as file,  open('./data/durring.txt', 'w') as output_file:
    for line in file:
        parsed_data = json.loads(line)
        new_data = parsed_data["rawContent"]
        data = json.dumps(new_data)
        tokens = nltk.word_tokenize(data)
        tokens = [token.replace('#', '') for token in tokens]
        data = " ".join(tokens)
        data= json.dumps(data)
        dane={}
        dane["tweet"]=data
        dane["nltk"]=sid.polarity_scores(data)
        dane["t2e"]=t2e.get_emotion(data)
        dane["date"] = json.dumps(parsed_data["date"])
        json_data = json.dumps(dane)
        output_file.write(json_data)
        output_file.write('\n')   
        
with open('./data/twitter23.jsonl', 'r') as file,  open('./data/now.txt', 'w') as output_file:
   for line in file:
        parsed_data = json.loads(line)
        new_data = parsed_data["rawContent"]
        data = json.dumps(new_data)
        tokens = nltk.word_tokenize(data)
        tokens = [token.replace('#', '') for token in tokens]
        data = " ".join(tokens)
        data= json.dumps(data)
        dane={}
        dane["tweet"]=data
        dane["nltk"]=sid.polarity_scores(data)
        dane["t2e"]=t2e.get_emotion(data)
        dane["date"] = json.dumps(parsed_data["date"])
        json_data = json.dumps(dane)
        output_file.write(json_data)
        output_file.write('\n')   

