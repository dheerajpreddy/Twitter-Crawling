"""Bonus question."""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
from twython import Twython

options = webdriver.ChromeOptions() # Simulate Google Chrome
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary' # Location of Chrome
options.add_argument('window-size=800x841')
options.add_argument('headless') # Hides chrome from being shown, runs in background

driver = webdriver.Chrome(chrome_options=options) # Open browser
username = "iiscbangalore"
driver.get("https://twitter.com/" + username) # go to this profile website
# Scroll down forever using this piece of JS code
driver.execute_script("var myVar=setInterval(function(){myTimer()},1000); function myTimer() { window.scrollTo(0,document.body.scrollHeight);console.log(document.documentElement.scrollHeight)}")
oldVal = driver.execute_script("return window.scrollY;") # Find position of scrollbar
sleep(5)
while oldVal != driver.execute_script("return window.scrollY;"): # Keep running until scrollbar stops moving
    oldVal = driver.execute_script("return window.scrollY;")
    sleep(10)
page_source = driver.page_source
driver.quit()
soup = BeautifulSoup(page_source, 'html.parser')
all_tweets = [ tweet['data-tweet-id'] for tweet in soup.select("div.tweet")] # get all tweets present on the page
# driver2 = webdriver.Chrome()
# driver2.get("https://twitter.com/" + username + "/status/" + all_tweets[-1]) # display the first ever tweet

consumer_key = "nZSdk3QfF4SuO5I1assGAaZOm"
consumer_secret = "NmjFsFohlC0Trr34ghc1nnZc3JsPnjJUSlzCZ11nGkJ3QtIYWD"
access_token = "973951591249190912-wsvLdApA3YkcMYqvtKMZNasVa698wUT"
access_token_secret = "AbhkZ86INFeVSjzpCYVBxFjjpjfm6MEOjPuGywoIrOcKt"
twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
tweet = twitter.show_status(id=all_tweets[-1])
print(tweet['text'])
