"""Bonus question."""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
options.add_argument('window-size=800x841')
options.add_argument('headless')

driver = webdriver.Chrome(chrome_options=options)
username = "ponguru"
driver.get("https://twitter.com/" + username)
driver.execute_script("var myVar=setInterval(function(){myTimer()},1000); function myTimer() { window.scrollTo(0,document.body.scrollHeight);console.log(document.documentElement.scrollHeight)}")
oldVal = driver.execute_script("return window.scrollY;")
sleep(5)
while oldVal != driver.execute_script("return window.scrollY;"):
    oldVal = driver.execute_script("return window.scrollY;")
    sleep(10)
page_source = driver.page_source
driver.quit()
soup = BeautifulSoup(page_source, 'html.parser')
all_tweets = [ tweet['data-tweet-id'] for tweet in soup.select("div.tweet")]
driver2 = webdriver.Chrome()
driver2.get("https://twitter.com/" + username + "/status/" + all_tweets[-1])
