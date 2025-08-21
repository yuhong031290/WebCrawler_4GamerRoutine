from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = None


def bigMaster(Driver):  # 瀏覽 案其中一條 發問/回答 的 good
    sleep(0.1)
    count = 0
    driver = Driver
    for i in range(1, 11):
        
        bigmaster = driver.find_element(By.LINK_TEXT, "大賢者")
        bigmaster.click()
        try:
            saearch = WebDriverWait(driver, 10)
            saearch.until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div/a[1]"))).click()
        except:pass
        try:
            alreadyDone = WebDriverWait(driver, 1)
            alreadyDone = alreadyDone.until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/div[1]/div[3]/ul/li[2]/button'))).click()
        except:pass
        discuss = WebDriverWait(driver, 10)
        discuss.until(EC.visibility_of_element_located(
            (By.XPATH, f"/html/body/div/div/div[3]/div/div[2]/div/div[1]/section/div/div[1]/a[{i}]"))).click()
        sleep(0.2)
        if count == 1:
            sayGood = WebDriverWait(driver, 10)
            sayGood.until(EC.visibility_of_element_located(
                (By.XPATH, f"/html/body/div/div/div[3]/div/div[2]/div/div[1]/main/div[6]/div[1]/a/img"))).click()
            

            sayMessageGood = WebDriverWait(driver, 10)
            sayMessageGood.until(EC.visibility_of_element_located(
                (By.XPATH, " /html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/section/section/div[2]/span/div[1]/div[2]/div[3]/div/div[1]/a/img"))).click()
        count+=1
        print("到此一遊")
        driver.back()
        sleep(0.1)
