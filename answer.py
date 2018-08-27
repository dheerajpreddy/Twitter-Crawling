from twython import Twython
import json



APP_KEY = "qiOaRLVPldazXmYmF3IaIQw4L" #Consumer key
APP_SECRET = "FAzcCMF1UUyuNuSeddAA1nDJYPeXm6OhaCD084k1t3BZ0HleCY" #Consumer secret
OAUTH_TOKEN = "717220472623071233-oeDgXLyYdqT92Mi06aaAGV7EtSExfKS" # Access token
OAUTH_TOKEN_SECRET = "tVh6WAqVqJ5Pekb3skPON4OD46dyyBAIGOiWjPkZrtglC" #Access token secret


twitter = Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
data = twitter.search(q='@iiit_hyderabad',result_type='mixed',count = 100)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
