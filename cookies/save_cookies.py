from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import pickle

with open('data.json', "w") as f:
    json.dump([], f)

def write_json(new_data, filename='data.json'):
    with open(filename, "r+") as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

if __name__ == '__main__':
    
    email     = "vortexe2002@gmail.com"
    password  = "Alt9908854."

    options = webdriver.ChromeOptions()
    options.add_argument('proxy-server=106.122.8.54:3128')
    #options.add_argument(r'--user-data-dir=C:\Users\José Lopes\AppData\Local\Google\Chrome\User Data\Default')
    browser = uc.Chrome(executable_path= "C:\Program Files (x86)\chormedriver.exe", options=options)
    browser.get('https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&ifkv=AWnogHcLMSXDQ5lvUiDJ6F1tpAvqdB-ZGne6UV9JtbRZVMWP4ROzFS83_Y5-C20rloMb-2SJxubs&flowName=GlifWebSignIn&flowEntry=ServiceLogin')


    browser.find_element(By.ID, "identifierId").send_keys(email)
    browser.find_element(By.CSS_SELECTOR, "#identifierNext > div > button > span").click()


    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input'))
    )


    browser.find_element(By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input').send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "#passwordNext > div > button").click()

    time.sleep(5)

    cookies =  browser.get_cookies()



    pickle.dump((cookies), open("cookies.pkl", "wb"))

    write_json({
        "cookies": cookies           
                })






