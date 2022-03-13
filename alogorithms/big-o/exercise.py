# Find 1st and last element from the input

tweets = [
    {"tweet": "I love my dog", "date": "2020"},
    {"tweet": "I hate dogs", "date": "2019"},
    {"tweet": "Iam gonna be succesful", "date": "2022"},
]

first_tweet = tweets[0]  # O(1)
last_tweet = tweets[-1] or tweets[len(tweets) - 1]  # O(1)


print("first tweet:",first_tweet)
print("last tweet:",last_tweet)

str = 'Gunalan'
print(str.__len__()) # O(1)