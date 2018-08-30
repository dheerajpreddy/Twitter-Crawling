"""Bonus question."""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions() # Simulate Google Chrome
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary' # Location of Chrome
options.add_argument('window-size=800x841')
options.add_argument('headless') # Hides chrome from being shown, runs in background

driver = webdriver.Chrome(chrome_options=options) # Open browser
username = "ponguru"
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
driver2 = webdriver.Chrome()
driver2.get("https://twitter.com/" + username + "/status/" + all_tweets[-1]) # display the first ever tweet
