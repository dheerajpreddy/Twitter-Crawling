"""Bonus question."""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Applications/Google Chrome.app')
username = "iiit_hyderabad"
driver.get("https://twitter.com/" + username)
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source

driver.execute_script("var myVar=setInterval(function(){myTimer()},1000); function myTimer() { window.scrollTo(0,document.body.scrollHeight);console.log(document.documentElement.scrollHeight)}")

# driver.close()
