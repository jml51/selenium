from seleniumwire import webdriver  # Import from seleniumwire
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire.utils import decode
import time
import json

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
    

def intercept(request):
    if request.url.startswith("https://encrypted-tbn0.gstatic.com/images?q="):
        #request.abort()
        request.create_response(
            status_code=200,
            headers={'Content-Type': 'image/jpeg'},
            body=open("transferir.jpeg", 'rb').read()
        )





driver.request_interceptor = intercept
# Go to the Google home page
driver.get('https://www.google.com/search?q=mountains&sxsrf=AJOqlzUktuRorKC4mEWr42XlgmZ8RSckKw:1675795329758&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiyvuKKiIT9AhVTTaQEHRnaAsEQ_AUoAXoECAIQAw&biw=1536&bih=726&dpr=1.25')


WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#yDmH0d > c-wiz > div > div > div > div.NIoIEf > div.G4njw > div.AIC7ge > div.CxJub > div.VtwTSb > form:nth-child(1) > div > div > button > span"))
    )



driver.find_element(By.CSS_SELECTOR, "#yDmH0d > c-wiz > div > div > div > div.NIoIEf > div.G4njw > div.AIC7ge > div.CxJub > div.VtwTSb > form:nth-child(1) > div > div > button > span").click()


"""
# Access requests via the `requests` attribute
for request in driver.requests:
    if request.response:
        if request.url.startswith("https://play.google.com/log?format=json"):
            response = request.response
            body = decode(response.body, response.headers.get('Content-Encoding', 'identity'))
            decoded_body = body.decode('utf-8')
            json_data = json.loads(decoded_body)
"""

