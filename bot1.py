#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time

CONSUMER_KEY = 'xxxx'
CONSUMER_SECRET = 'xxxx'
ACCESS_KEY = 'xxxx'
ACCESS_SECRET = 'xxxx'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

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
        if 'ici' in mention.full_text.lower():
            print('found mention')
            print('responding back...')
            api.update_status('effectivement @' + mention.user.screen_name +
                    ', il faut fermer les ecoles !', mention.id)
        
        elif 'israel' in mention.full_text.lower():
            print('found mention')
            print('responding back...')
            api.update_status('erreur 404 @' + mention.user.screen_name +
                    ', voulez-vous dire la Palestine?', mention.id)
            
        elif 'cuisine' in mention.full_text.lower():
            print('found mention')
            print('responding back...')
            api.update_status('oui @' + mention.user.screen_name +
                    ', elle doit revenir a sa cuisine !', mention.id)
            
        elif 'grenouille' in mention.full_text.lower():
            print('found mention')
            print('responding back with image...')
            api.update_with_media('DeGrenouille.jpg', in_reply_to_status_id=mention.id,
                                     auto_populate_reply_metadata=True)
            
        elif 'mediavenir' in mention.full_text.lower():
            print('found mention')
            print('responding back...')
            api.update_status('absolument @' + mention.user.screen_name +
                    ', #liberezmediavenir ', mention.id)
            
        elif 'demission' in mention.full_text.lower():
            print('found mention')
            print('responding back...')
            api.update_status('oui @' + mention.user.screen_name +
                    ', Jean Michel Blanquer doit demissioner de son poste le plus tot possible. ', mention.id)
            
while True:
    reply_to_tweets()
    time.sleep(45)
