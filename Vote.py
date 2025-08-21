from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = None
def vote(Driver):
    driver = Driver
    
    page = 2
    driver.get(f"https://www.4gamers.com.tw/vote/latest?page={page}")
    sleep(2)
    body = WebDriverWait(driver, 6)
    body = body.until(
        EC.visibility_of_element_located((By.TAG_NAME, "body")))
    body = driver.find_element(By.TAG_NAME, "body")
    i = 20
    flag = 0
    while flag == 0:
        try:
            sleep(0.4)
            lastone = WebDriverWait(driver, 2)
            lastone = lastone.until(EC.visibility_of_element_located(
                (By.XPATH, f'/html/body/div/div/div[3]/div/div/main/div/div[{i}]/a/div/div[2]/button')))
            if lastone != None:
                lastone.click()
                sleep(1)
                try:
                    sleep(0.1)
                    notyet = WebDriverWait(driver, 2)
                    notyet = notyet.until(EC.visibility_of_element_located(
                        (By.XPATH, '//button[@class="btn vote-radio-result-btn w-100 position-relative overflow-hidden text-left text-small text-lg-base pDx-4 pDx-lg-5 py-2 pDy-lg-1 vote-form-radio-buttons btn-secondary vote-radio-result-btn-single"]')))
                    if notyet != None:
                        notyet.click()
                        print("投票~")
                        break
                    if notyet == None:
                        i-=1
                        driver.back()
                except:
                    i-=1
                    driver.back()
                    sleep(0.5)
                    
            else:
                print("3")
                body.send_keys(Keys.PAGE_UP)
                sleep(0.4)
                if i == 0:
                    page -= 1
                    driver.get(
                        f"https://www.4gamers.com.tw/vote/latest?page={page}")
                    i = 20
                    sleep(1)

        except:
            print("4")
            sleep(0.4)
            body.send_keys(Keys.PAGE_UP)