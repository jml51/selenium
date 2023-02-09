from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import pickle

if __name__ == '__main__':
    

    browser = uc.Chrome()
    browser.get('https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&ifkv=AWnogHcLMSXDQ5lvUiDJ6F1tpAvqdB-ZGne6UV9JtbRZVMWP4ROzFS83_Y5-C20rloMb-2SJxubs&flowName=GlifWebSignIn&flowEntry=ServiceLogin')


    cookies = pickle.load(open("cookies.pkl", "rb"))

    for cookie in  cookies:
        cookie['domain'] = ".google.com"

        try:
            browser.add_cookie(cookie)
        except Exception as e:
            print(e)
    
    browser.get("https://mail.google.com/mail/u/0/#inbox")

    time.sleep(120)



