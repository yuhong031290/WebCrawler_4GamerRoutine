from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = None


def detect():

    try:
        ad = WebDriverWait(driver, 0.1)
        ad = ad.until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div/div/div[2]/div/div/div[2]/button[1]")))
        if (ad != None):
            ad.click()
        else:
            ad = WebDriverWait(driver, 0.1)
            ad = ad.until(EC.visibility_of_element_located(
                (By.XPATH, " /html/body/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[1]")))
            if (ad != None):
                ad.click()
    except:
        pass


def news(Driver):
    sleep(0.3)
    driver = Driver
    try:
        newstitle = driver.find_element(By.LINK_TEXT, "新聞")
        newstitle.click()
    except:
        newstitle = WebDriverWait(driver, 3)
        newstitle = newstitle.until(EC.visibility_of_element_located(
            (By.LINK_TEXT, "新聞"))).click()  # 新聞
        # pass

    # page2 = WebDriverWait(driver, 10)
    # page2 = page2.until(EC.visibility_of_element_located(
    #     (By.XPATH, "/html/body/div/div/div[3]/div/div[3]/div/div[2]/div/nav/ul/li[]/a"))).click()

    sleep(1)
    for i in range(1,6):
        news = WebDriverWait(driver, 10)
        news = news.until(EC.visibility_of_element_located(
            (By.XPATH, f"/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/main/div/div[{i}]"))).click()

        detect()

        body = WebDriverWait(driver, 10)
        body = body.until(EC.visibility_of_element_located(
            (By.TAG_NAME, "body")))
        body = driver.find_element(By.TAG_NAME, "body")
        print("往下滾")
        detect()

        # while True:
        #     commonded = WebDriverWait(driver, 0.004)
        #     body.send_keys(Keys.PAGE_DOWN)

        #     detect()
        #     commonded = commonded.until(EC.visibility_of_element_located(
        #         (By.XPATH, "//div[@class='d-flex align-items-center justify-content-between']//a[@class='flex-grow-1 text-black text-base mb-0']")))

        #     if commonded != None:
        #         commonded = driver.find_element(
        #             By.XPATH, "//div[@class='d-flex align-items-center justify-content-between']//a[@class='flex-grow-1 text-black text-base mb-0']")
        #         driver.execute_script("arguments[0].click();", commonded)
        #         break
        # print("點開所有留言")

        # try:
        #     theNewestCommond = WebDriverWait(driver, 1)
        #     theNewestCommond = theNewestCommond.until(EC.visibility_of_element_located(
        #         (By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div/div/div/div/div/div[3]/div/div/div[1]/div/div/button[1]"))).click()
        #     theNewestCommond = driver.find_element(
        #         By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div/div/div/div/div/div[3]/div/div/div[1]/div/div/button[1]")
        #     driver.execute_script("arguments[0].click();", theNewestCommond)
        # except:
        #     theNewestCommond = driver.find_element(By.LINK_TEXT, "最新")
        #     driver.execute_script("arguments[0].click();", theNewestCommond)

        # sleep(1)
        # firstCommond = WebDriverWait(driver, 10)
        # firstCommond = firstCommond.until(EC.visibility_of_element_located(
        #     (By.XPATH, '/html/body/div/div/div[3]/div/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/section/ul/li[1]/div/div/div[2]/div[2]/div[1]')))
        # firstCommond = firstCommond.text
        # print("找到第一則留言:"+firstCommond)

        # sendMessage = WebDriverWait(driver, 10)
        # sendMessage = sendMessage.until(EC.visibility_of_element_located(
        #     (By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div/span/form/div/div/textarea")))
        # sendMessage.send_keys(firstCommond)
        # print("點下輸入框 並傳送訊息")

        # submitButton = WebDriverWait(driver, 10)
        # submitButton = submitButton.until(EC.visibility_of_element_located(
        #     (By.XPATH, '/html/body/div/div/div[3]/div/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div/span/form/div/button'))).submit()
        # print("按下傳送")
        driver.back()
        sleep(0.2)
