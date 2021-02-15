from datetime import date, timedelta
import tweepy
import json
import io
import csv

upto = date.today()
since = upto - timedelta(days = 30)

auth = tweepy.OAuthHandler('NRiMpFEGuGBZdYuUGqFx6jHKw', 'DyC81HQp0clndydDXwMQNXFQUEyZqxp8ISlPueBVvZiMPFtYZh')
auth.set_access_token('842279246999506945-cZMLYn5wfddox2nE8TRMvBFbAwNhMX9', '5I3l7DhAG1gnYa09Ub3NMki9VDHZP22XKp8LxEQWxTvcs')
			
api = tweepy.API(auth)
#value=User_Handle.get()
def see_tweets(handle, since):
    file = io.open('file.csv' , 'w' , encoding="utf-8")
    thewriter = csv.writer(file)
    for status in tweepy.Cursor(api.search, tweet_mode='extended' , q = handle).items():
        #print(status._json)
        if status.created_at.date() < since :
            break

        print(status.created_at.date())
        if status.full_text[:2] != 'RT':
            thewriter.writerow([status.full_text])
        else:
            thewriter.writerow([status._json['retweeted_status']['full_text']])
    file.close()
    
    #print(datetime.date(status._json['created_at'][8:10],status._json['created_at'][12:14],status._json['created_at'][8:10]))