
# coding: utf-8

# Twython is a python wrapper for twitter API. For further infomation refer "https://twython.readthedocs.io/en/latest/". Run the below cell if twython is not installed.

# In[ ]:

get_ipython().system(u'pip install twython # or run !easy_install twython depends on you')
# If wish to install using source code clone the repository "git clone git://github.com/ryanmcgrath/twython.git"


# You can check whether Twython has successfully installed or not by going to Python cli and  typing import
# Twython.  If  it  has  been  successfully  installed,  then  you  will  be  able import Twython. Now, let us exit the
# Python cli.

# Let's start by importing library and creating the Twython object. We'll be using this object for all interactions with Twitter.

# In[11]:

from twython import Twython


# You must have a twitter account beforehand so that you can handle twitter API successfully. To create twitter application go to apps.twitter.com and click on create new app.
# Enter  a  name  for  your  application. And  add  a  description.  In  the  website  add  any  URL with http in front. Here we use http www.google.com, and leave the callback URL blank. Scroll down and accept terms and conditions and click on create your twitter application.
# After registering your app, get hold of access keys and tokens to use their application to gather data.
# Click on the keys and access token tab. And  you will be able to see  your consumer key and your consumer secret.
# For a successful data collection,  you need a set of two more keys which is called token actions. Click on create my access token which  will  result  in  generation  of  two  more  keys  called  access  token  and  access  token
# secret. Now this set of four keys will help us in retrieving data.

# In[12]:

APP_KEY = "qiOaRLVPldazXmYmF3IaIQw4L" #Consumer key
APP_SECRET = "FAzcCMF1UUyuNuSeddAA1nDJYPeXm6OhaCD084k1t3BZ0HleCY" #Consumer secret
OAUTH_TOKEN = "717220472623071233-oeDgXLyYdqT92Mi06aaAGV7EtSExfKS" # Access token
OAUTH_TOKEN_SECRET = "tVh6WAqVqJ5Pekb3skPON4OD46dyyBAIGOiWjPkZrtglC" #Access token secret


# Twitter rest API gives us hold on to access  data  specific  to  a user,  or  public tweets  or  you  can  even  get  the  follower  and  following  information  of  users  who  have authenticated your app or of any particular user whose such data is public. Apart  from  using  search API,  we  will  also  be  using  the  streaming API.  The  streaming API  gives  you  the  functionality  to  monitor  and  process  twitter  data  in  real  time. To  use twitter API we will be using Twython.

# Now next line is just an initiator, which connects you to the twitter API. In this particular case,  we  are  going  to  fit  the  twitter  timeline  of  the  authenticated  user  that  is  your  own account.  Timeline  equal  to  twitter  dot  get  home  timeline  will  get  you  all  the  tweets, which appear in your timeline which we will print.

# In[13]:

twitter = Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
timeline = twitter.get_home_timeline()
print timeline


# On executing the above cell, there is a bunch of texts which is pretty unreadable. And it is also not encoded in Unicode. We will import json library which lets you format  the  json  data;  and  we  are  going  to  print  this  data  in  string  format  by  using  the command json dot dumps.

# In[14]:

import json
print json.dumps(timeline)


# To view the result in readable format copy the text and paste in the viewer tab of json.viewer.stack.hu which converts json format to readable format.

# What if we had to print only the text of the tweets which the user has posted so far, to do that, we are going to iterate over timeline data one by one and print the text available in each tweet data. We will start a loop and then access the json object which is returned by the twitter API.  Note  that  each  tweet  is  basically  a  dictionary  with  a  set  of  keys,  in  this case we want to access the text.

# In[15]:

for tweet_data in timeline:
    print tweet_data['text']


# Collect  data  from  twitter  search  end  point  based  on  a specific key word, in this case IIIT Hyderabad. And the result type is mixed which means that it will be a mix of popular and recent tweets. We also have count equal to
# 100, which means that this will be the number of tweets, which will be returned. In this case, we will print the amount of tweets, which are returned to us by the twitter API.

# In[16]:

data = twitter.search(q='IIIT Hyderabad',result_type='mixed',count = 100)
print len(data['statuses'])


# We can use statuses equal to data statuses to access the list of tweets which Twitter API  has  returned  through  this  method. And  let  us  try  to  print  the  text  of each tweet along with the tweet id.

# In[17]:

statuses = data['statuses']
for post in statuses:
    print post['id_str'] + ':' + post['text']


# In this case, we have a class My Streamer which has basically two  functions  which  define  what  we  will  do,  when  we  get  the  data  successfully,  and when  we  fail.  In  case  we  get  the  data  successfully,  we  are  going  to  print  the  text  of  it after encoding it into utf-8. And in case, it shows an error we are going to print this status
# code  and  pass.  We  will  use  the  'Monday morning'  keyword. In this case we are going to do the same in real time.

# In[19]:

from twython import TwythonStreamer

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text']).encode('utf-8')

    def on_error(self, status_code, data):
        print(status_code)
        pass

stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.filter(track='Monday morning')


# Now remember since is this data is being collected in real time,  you  will  not  see  the  results  immediately,  depending  on  when  the  tweets  are  being posted.  You  will  notice  that  tweets  will  start  coming  if
# the  particular  keyword  is  still actively being used. So, the tweets, which you see now, are being generated in real time.

# In[21]:

stream.statuses.filter(follow='1028642661765459969')


# Tweepy also is a python wrapper for twitter, which helps in holding twitter data.Tweepy provides access to the well documented Twitter API. With tweepy, it's possible to get any object and use any method that the official Twitter API offers. For example, a User object has its documentation at https://dev.twitter.com/docs/platform-objects/users and following those guidelines, tweepy can get the appropriate information. If not installed in your system, then execute the following command 'pip install tweepy' or 'easy_install tweepy'. If interested in using source code then undergo following steps:
# 1. Clone it from github repository by running 'git clone https://github.com/tweepy/tweepy.git'
# 2. Run 'python setup.py install'
#
# Tweepy supports accessing Twitter via Basic Authentication and the newer method, OAuth. Twitter has stopped accepting Basic Authentication so OAuth is now the only way to use the Twitter API.

# In[23]:

import tweepy
consumer_key = APP_KEY
consumer_secret = APP_SECRET
access_token = OAUTH_TOKEN
access_token_secret = OAUTH_TOKEN_SECRET
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text


# This example will download your home timeline tweets and print each one of their texts to the console.

# In[24]:

from tweepy import OAuthHandler

def load_api():
    ''' Function that loads the twitter API after authorizing the user. '''

    consumer_key = 'qiOaRLVPldazXmYmF3IaIQw4L'
    consumer_secret = 'FAzcCMF1UUyuNuSeddAA1nDJYPeXm6OhaCD084k1t3BZ0HleCY'
    access_token = '717220472623071233-oeDgXLyYdqT92Mi06aaAGV7EtSExfKS'
    access_secret = 'tVh6WAqVqJ5Pekb3skPON4OD46dyyBAIGOiWjPkZrtglC'
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    # load the twitter API via tweepy
    return tweepy.API(auth)


# The below cell on execution returns the set of tweets based on search hashtags within specified time.

# In[25]:

tweets_data = []
api = load_api()
search_phrases = ['#edpolicy','#edreform',
                     '#edreformtribe', '#edgap',
                     '#literacy', '#teacherquality',
                     '#urbaned', 'edadmin',
                     '#edpolitics']
maxtweets = 100


# In[26]:

for search_phrase in search_phrases:
    for tweets in tweepy.Cursor(api.search,search_phrase,                           lang="en",                           since='2017-08-06',until='2017-08-12').items(maxtweets):
        #print tweet.created_at, tweet.text
    #print type(tweets)
        tweets_data.append(tweets)
    #csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])


# In[27]:

print len(tweets_data)


# In[28]:

# Creates the user object. The me() method returns the user whose authentication keys were used.
user = api.me()

print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))



# All of the API methods are documented here: http://packages.python.org/tweepy/html/api.html

# One of the main usage cases of tweepy is monitoring for tweets and doing actions when some event happens. Key component of that is the StreamListener object, which monitors tweets in real time and catches them.The Twitter streaming API is used to download twitter messages in real time. It is useful for obtaining a high volume of tweets, or for creating a live feed using a site stream or user stream.
# The streaming api is quite different from the REST api because the REST api is used to pull data from twitter but the streaming api pushes messages to a persistent session. This allows the streaming api to download more data in real time than could be done using the REST API.
#
# In Tweepy, an instance of tweepy.Stream establishes a streaming session and routes messages to StreamListener instance. The on_data method of a stream listener receives all messages and calls functions according to the message type. The default StreamListener can classify most common twitter messages and routes them to appropriately named methods, but these methods are only stubs.
# StreamListener has several methods, with on_data() and on_status() being the most useful ones.
# Therefore using the streaming api has three steps.
#
# 1.Create a class inheriting from StreamListener
# 2.Using that class create a Stream object
# 3.Connect to the Twitter API using the Stream.
#

# In[35]:

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['python'])


# In this example we will use filter to stream all tweets containing the word python. The track parameter is an array of search terms to stream.
