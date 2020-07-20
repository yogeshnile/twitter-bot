import tweepy
import time

API_key = ""
API_secret_key = ""
access_token = ""
Access_token_secret = ""

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(access_token, Access_token_secret)
api = tweepy.API(auth)

FILE_NAME = "last_seen.txt"

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    last_seen_id = read_last_seen(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')
    for mention in reversed(mentions):
        print(str(mention.id)+ '---' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen(FILE_NAME, last_seen_id)
        #mention.
        if '@yogeshnile' in mention.full_text.lower():
            print("Boss ko tag kiya hai")
            api.update_status("@"+ mention.user.screen_name + " thank you for mention me and 'Yogesh Nile', @YogeshNile will replay soon.", in_reply_to_status_id = last_seen_id)
        else:
            print("Boss tag nahi kiya")
            api.update_status("@"+ mention.user.screen_name + " Thank you for mention me, @YogeshNile will reply soon", in_reply_to_status_id = last_seen_id)
        #mention.id.favorites()

def searchbot(hashtag):
    for tweet in api.search(q=hashtag, lang="en", rpp=10):
        try:
            tweet.retweet()
            print(hashtag)
            api.update_status("@"+ tweet.user.screen_name + " Your Tweet is helpful to the world, keep it up. 👍", in_reply_to_status_id = tweet.id)
            time.sleep(300)
        except tweepy.TweepError as e:
            print(e)
            time.sleep(300)

hashtag = ['#developer','#IoT','100DaysOfCode','python','PythonProgramming','DeepLearning','MachineLearning','AI','DataScience','DataAnalysis','#DataCleaning','BigData','#Flask','#Plotly','NLTK','#beautifulsoup','#seaborn','#numpy','#sklearn','#opencv','#scipy','tensorflow','#keras','#pygame','#tkinter','stackoverflow','github','#pypi','NeauralNetwork','#spacy','#Django']
while True:
    reply()
    time.sleep(300)
    for hash_tag in hashtag:
        searchbot(hash_tag)
