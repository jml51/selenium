from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

browser = webdriver.Chrome()
browser.get('https://intoli.com/blog/scrape-infinite-scroll/demo.html')


items = []

last_height = browser.execute_script("return document.body.scrollheight")

itemTarfetcount = 100

while itemTarfetcount > len(items):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") 

    time.sleep(1)

    new_height = browser.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break

    last_height = new_height

    elements = browser.find_elements(By.CSS_SELECTOR, "#boxes > div")
    textElements = []
    for element in elements:
        textElements.append(element.text)

        items = textElements

        """
        title = element.find_element(BY.TAG_NAME, "h2").text
        textElements.append({
            title:title
        })
        """


print(items)
print(len(items))

json.dump(items, open("itens.json", "w"))



















