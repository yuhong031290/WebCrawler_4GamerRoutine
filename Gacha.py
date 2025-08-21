from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = None

def Gacha(Driver):
    driver=Driver

    sleep(0.4)
    # gacha = WebDriverWait(driver, 10)
    # gacha = gacha.until(EC.visibility_of_element_located(
    #     (By.XPATH, "/html/body/div[1]/div/nav/div/div/ul/li[5]/a"))).click()
    gacha = WebDriverWait(driver, 10)
    gacha = gacha.until(EC.visibility_of_element_located(
        (By.LINK_TEXT,   "會員福利"))).click()
    sleep(0.3)
    selectGacha = WebDriverWait(driver, 10)
    selectGacha = selectGacha.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div/a[3]"))).click()
    sleep(0.3)
    level1 = WebDriverWait(driver, 10)
    level1 = level1.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div[1]/div[2]/div/section/a[1]/div[1]"))).click()
    sleep(0.3)

    getball = WebDriverWait(driver, 10)
    getball = getball.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/section[1]/button[1]")))
    getball = driver.find_element(
        By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/section[1]/button[1]")
    driver.execute_script("arguments[0].click();", getball)
    sleep(0.3)

    driver.refresh()
    sleep(0.2)
    