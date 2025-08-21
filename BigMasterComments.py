from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = None


def bigMaster(Driver):
    driver = Driver

    for i in range(1, 11):
        try:
            bigmaster = driver.find_element(By.LINK_TEXT, "大賢者")
            bigmaster.click()
            try:
                search = WebDriverWait(driver, 10)
                search.until(EC.visibility_of_element_located(
                    (By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div/a[1]"))).click()
            finally:
                pass
        except:
            driver.get("https://www.4gamers.com.tw/saged")
            sleep(1)
        # 捲下來
        body = WebDriverWait(driver, 5)
        body = body.until(
            EC.visibility_of_element_located((By.TAG_NAME, "body")))
        body = driver.find_element(By.TAG_NAME, "body")
        sleep(0.4)
        alreadyDone = WebDriverWait(driver, 1)
        alreadyDone = alreadyDone.until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/div[1]/div[3]/ul/li[2]/button')))
        if alreadyDone == None:
            while True:

                alreadyDone = WebDriverWait(driver, 0.6)

                alreadyDone = alreadyDone.until(EC.visibility_of_element_located(
                    (By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/div[1]/div[3]/ul/li[2]/button')))

                body.send_keys(Keys.PAGE_DOWN)
                if alreadyDone != None:
                    alreadyDone.click()
                    break
        else:
            alreadyDone.click()
        # alreadyDone = WebDriverWait(driver, 10)
        # alreadyDone.until(EC.visibility_of_element_located(
        #     (By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/div[1]/div[3]/ul/li[2]/button'))).click()

        sleep(0.4)
        while True:
            discusses = WebDriverWait(driver, 1)
            discusses = discusses.until(EC.visibility_of_element_located(
                (By.XPATH, f"/html/body/div/div/div[3]/div/div[2]/div/div[1]/section/div/div[1]/a[{i}]")))
            print("我進去個人問答了")
            if discusses != None:
                discusses.click()
                break
            body.send_keys(Keys.PAGE_DOWN)
            # discusses = WebDriverWait(driver, 10)
            # discusses.until(EC.visibility_of_element_located(
            #     (By.XPATH, f"/html/body/div/div/div[3]/div/div[2]/div/div[1]/section/div/div[1]/a[{i}]"))).click()
            # print("我進去個人問答了")

        # 開啟所有留言紀錄
        count = 0
        while True:

            openMessage = WebDriverWait(driver, 0.6)
            body.send_keys(Keys.PAGE_DOWN)

            openMessage = openMessage.until(EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div[1]/section/section/div[2]/span/div[1]/div[2]/div[4]/div/div/div/a/div")))

            if openMessage != None:

                openMessage = driver.find_element(
                    By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div[1]/section/section/div[2]/span/div[1]/div[2]/div[4]/div/div/div/a/div")
                driver.execute_script("arguments[0].click();", openMessage)
                break
            count += 1
            if count == 5:
                break
        # ---------
        print("我捲下來了")

        # getfirstmsg = WebDriverWait(driver, 10)
        # getfirstmsg.until(EC.visibility_of_element_located(
        #     (By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div[1]/section/section/div[2]/span/div[1]/div[2]/div[4]/div/div/div/section/ul/li[1]/div/div/div[2]/div[2]/div[1]")))
        # getfirstmsg = driver.find_element(
        #     By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div[1]/section/section/div[2]/span/div[1]/div[2]/div[4]/div/div/div/section/ul/li[1]/div/div/div[2]/div[2]/div[1]")
        # getfirstmsg = getfirstmsg.text

        sleep(0.5)
        # textarea
        inputtext = driver.find_element(
            By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div[1]/section/section/div[2]/span/div[1]/div[2]/div[4]/div/div/div/div/span/form/div/div/textarea")
        inputtext.send_keys("讚讚讚!!")

        # submit
        sub = WebDriverWait(driver, 10)
        sub.until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div[1]/section/section/div[2]/span/div[1]/div[2]/div[4]/div/div/div/div/span/form/div/button"))).click()

        print("到此一遊")
        driver.back()
        sleep(0.15)
        # print(driver.page_source())
