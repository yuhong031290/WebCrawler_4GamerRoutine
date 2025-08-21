from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


driver = None


def comments(Driver):
    driver = Driver

    sleep(0.1)
    nonametalk = WebDriverWait(driver, 10)
    nonametalk = nonametalk.until(EC.visibility_of_element_located(
        (By.LINK_TEXT, "匿名聊"))).click()
    sleep(0.2)
    body = WebDriverWait(driver, 5)
    body = body.until(
        EC.visibility_of_element_located((By.TAG_NAME, "body")))
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.PAGE_DOWN)
    sleep(0.2)
    for i in range(1, 11):

        nonametalk = WebDriverWait(driver, 2)
        nonametalk = nonametalk.until(EC.visibility_of_element_located(
            (By.XPATH, f"/html/body/div[1]/div/div[3]/div/div[3]/div/main/section[3]/div/div/div/div/div/div[{i}]/a[1]/div/div[1]"))).click()
            # (By.XPATH, f"/html/body/div/div/div[3]/div/div[3]/div/main/section[2]/div/div/div/div/div/div[{i}]/a[1]/div/div[1]"))).click()
                        #  /html/body/div/div/div[3]/div/div[3]/div/main/section[2]/div/div/div/div/div/div[2]/a[1]/div/div[1]
                        # /html/body/div[1]/div/div[3]/div/div[3]/div/main/section[3]/div/div/div/div/div/div[1]/a[1]/div/div[1]
                        # /html/body/div[1]/div/div[3]/div/div[3]/div/main/section[3]/div/div/div/div/div/div[2]/a[1]/div/div[1]
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(Keys.PAGE_DOWN)
        sleep(0.1)

        # 尋找笑臉
        happyface = WebDriverWait(driver, 2)
        happyface = happyface.until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/section[1]/div/a[1]/img"))).click()

        # 尋找留言
        # firstComment = ""
        # try:
        #     findComment = WebDriverWait(driver, 1)
        #     findComment = findComment.until(EC.visibility_of_element_located(
        #         (By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]/section/ul/li/div/div/div[2]/div[2]/div[1]")))
        #     firstComment = findComment.text
        #     sleep(0.1)
        # except:
        #     pass
        # sendtext = driver.find_element(
        #     By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div/span/form/div/div/textarea")
        # if firstComment != "":
        #     try:
        #         sendtext.send_keys(firstComment)
        #     except:
        #         sendtext.send_keys("nice~~")

        # else:
        #     sendtext.send_keys("nice~~")
        # sleep(0.1)

        # submit = WebDriverWait(driver, 10)
        # submit = submit.until(EC.visibility_of_element_located(
        #     (By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div/span/form/div/button"))).click()
        # sleep(0.1)

        driver.back()
        sleep(0.1)

        if i > 3:
            for _ in range(i-3):
                try:
                    next = WebDriverWait(driver, 0.6)
                    next = next.until(EC.visibility_of_element_located(
                        (By.XPATH, "/html/body/div[1]/div/div[3]/div/div[3]/div/main/section[3]/div/div/div/a[1]"))).click()
                        # (By.XPATH, "/html/body/div/div/div[3]/div/div[3]/div/main/section[2]/div/div/div/a[1]/i"))).click()
                                    # /html/body/div[1]/div/div[3]/div/div[3]/div/main/section[3]/div/div/div/a[1]
                    sleep(0.1)
                except:
                    pass
