from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pyautogui

driver=None
def talkDonate(Driver):
    driver = Driver
    sleep(0.4)
    # nonametalk= WebDriverWait(driver, 5)
    # nonametalk = nonametalk.until(EC.visibility_of_element_located(
    #     (By.XPATH, "/html/body/div/div/nav/div/div/ul/li[3]/a"))).click()
    nonametalk= WebDriverWait(driver, 5)
    nonametalk = nonametalk.until(EC.visibility_of_element_located(
        (By.LINK_TEXT,"匿名聊"))).click()
    sleep(0.5)
    firstTalk = WebDriverWait(driver, 5)
    firstTalk = firstTalk.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div/div/div[3]/div/div[3]/div/main/section[1]/div/div/div[1]/a/div/div[1]"))).click()
    sleep(0.5)
    body = WebDriverWait(driver, 5)
    body = body.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.PAGE_DOWN)
    # body.send_keys(Keys.PAGE_DOWN)
    sleep(0.4)


    # donate
    donate = WebDriverWait(driver, 5)
    donate = donate.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div/div/main/div[4]/a[4]"))).click()
    # confirm
    sleep(0.4)
    pyautogui.moveTo(959, 680)
    pyautogui.click()