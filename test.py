#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time

CONSUMER_KEY = 'IKZ7qH0GR3Z77assB88M7xFwX'
CONSUMER_SECRET = '5XcUcmceAC9rEHjAGaPsmeIzIGYUmSEJO5JlvHDSvfDx8J20sO'
ACCESS_KEY = '1307636786311630848-gJgal7HJLLt36cJbPLOfNhnQcTEy6d'
ACCESS_SECRET = 'eZ7YlTBgoJZ9suGQV3eveQziJpcAcHruhtZYXejfQLlTy'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

media = api.media_upload("grenouille.jpg")

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving tweets...')

    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        
        if 'grenouille' in mention.full_text.lower():
            print('found mention')
            print('responding back with image...')
            api.update_with_media('grenouille.jpg', in_reply_to_status_id=mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)






   
