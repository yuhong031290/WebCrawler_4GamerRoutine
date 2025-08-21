from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pyautogui
import pyperclip

driver = None


def callMission(Driver):
    driver=Driver
    openMission = WebDriverWait(driver, 10)
    openMission = openMission.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/header/nav/ul/li[6]/a"))).click()
    
    myMission = WebDriverWait(driver, 10)
    myMission = myMission.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/header/nav/ul/li[6]/a/div/div[2]/div/ul/li[3]/a"))).click()
def delete(Driver):
    driver=Driver

    # -----------delete poster
    sleep(0.2)
    my = WebDriverWait(driver, 10)
    my = my.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div[1]/a[1]"))).click()
    sleep(0.2)
    nonametalk = WebDriverWait(driver, 10)
    nonametalk = nonametalk.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div[2]/div[2]/ul/li[3]/a"))).click()
    sleep(0.2)
    seleteNo1 = WebDriverWait(driver, 10)
    seleteNo1 = seleteNo1.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/a[1]/div"))).click()
    sleep(0.2)
    threeDot = WebDriverWait(driver, 10)
    threeDot = threeDot.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/main/div[2]/button/i"))).click()
    sleep(0.1)
    pyautogui.moveTo(1035, 565)
    pyautogui.click()
    # sleep(2)
    pyautogui.moveTo(1178, 610)
    pyautogui.click()
    sleep(2)

def Post(Driver):
    driver = Driver
    
    poster = WebDriverWait(driver, 10)
    poster = poster.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div/div/header/nav/ul/li[7]/a/button"))).click()
    noname = WebDriverWait(driver, 10)
    noname = noname.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div/div/header/nav/ul/li[7]/a/div/div[2]/a[2]"))).click()
    # print(pyautogui.position())
    sleep(1)
    pyautogui.moveTo(951, 692)
    pyautogui.click()
    sleep(0.2)
    pyautogui.moveTo(951, 592)
    pyautogui.click()

    pyautogui.press("a")
    pyautogui.moveTo(951, 822)
    pyautogui.click()
    sleep(0.2)
    callMission(Driver)

    delete(Driver)

    
    poster = WebDriverWait(driver, 10)
    poster = poster.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div/div/header/nav/ul/li[7]/a/button"))).click()
    noname = WebDriverWait(driver, 10)
    noname = noname.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div/div/header/nav/ul/li[7]/a/div/div[2]/a[2]"))).click()
    # print(pyautogui.position())
    sleep(1)
    pyautogui.moveTo(951, 692)
    pyautogui.click()
    sleep(0.2)
    pyautogui.moveTo(951, 592)
    pyautogui.click()


    pyperclip.copy('晚安')  # 先复制
    pyautogui.hotkey('ctrl', 'v')  # 再貼上
    
    pyautogui.moveTo(951, 822)
    pyautogui.click()
    sleep(0.2)
