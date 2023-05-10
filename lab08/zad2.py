

opinion1=" I needed a studio in London because I was travelling for work and I booked this one. I don't regret. It's the best choice I could do. Amazing location, well equipped kitchen, confortable bed.Everything was provided from towels, linens, soap, conditionner to Wifi.An excellent team and a very easy check in and check out process.Hopefully I didnt book a hotel room and I booked this one. Thanks! "
opinion2 = " The hotel said  When you arrive at the hotel after 22:00  you have to go to check in at the cromwell hotel, but when I arrive the cromwell at 22.30 The staff informed me that I had to check in at Earl'court garden hotel so wasting a lot of time and the room Upstairs, walking loudly, can't sleep"

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

positive_scores = sid.polarity_scores(opinion1)
negative_scores = sid.polarity_scores(opinion2)

print("Score for positive: ", positive_scores)
print("Score for negative: ", negative_scores)


import text2emotion as t2e

positive_emotion = t2e.get_emotion(opinion1)
negative_emotion = t2e.get_emotion(opinion2)

print("Score for positive: ", positive_emotion)
print("Score for negative: ", negative_emotion)



opinion1 += " Spacious, bright, and veeeeery cosy! The view from the balcony was stunning and the bed was extremely comfortable! The greatest time in my life!"
opinion2 += " The bathroom was disgusting and the sheets were covered in stains. Could not sleep whole night, it was the worst night in my life."


positive_scores = sid.polarity_scores(opinion1)
negative_scores = sid.polarity_scores(opinion2)

print("Score for positive: ", positive_scores)
print("Score for negative: ", negative_scores)


positive_emotion = t2e.get_emotion(opinion1)
negative_emotion = t2e.get_emotion(opinion2)

print("Score for positive: ", positive_emotion)
print("Score for negative: ", negative_emotion)


