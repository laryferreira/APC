tweet = input()  
word = input()   

if word in tweet:
    censored_tweet = tweet.replace(word, "*") 
    print(censored_tweet)
else:
    print("tudo certo :)")
