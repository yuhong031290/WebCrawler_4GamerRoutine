from zgetMoney import earnMoney  # 收錢
import zVote as vote
import zGacha as gacha
import ztalkComments as talkC
import ztalkPost as post
import zTalkDonate as donate  # 斗內
import zBigMasterComments as bmc  # 大賢者留言
# import zgetMoney as earnmoney  # 領錢
# from zgetMoney import earnMoney
import zBigMasterbrowse as bmb  # 案讚大賢者
import znewsComments as news  # 看新聞
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import pyautogui
from time import sleep
import pickle
# 設定時間 自動開始
# from datetime import datetime

# 設定google driver的路徑檔案2
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {
                                "profile.password_manager_enabled": False, "credentials_enable_service": False})
driver = webdriver.Chrome(
    options=options, service=Service("./chromedriver.exe"))
driver.maximize_window()


def gohome():
    sleep(0.2)
    body = WebDriverWait(driver, 5)
    body = body.until(
        EC.visibility_of_element_located((By.TAG_NAME, "body")))
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.PAGE_UP)
    body.send_keys(Keys.PAGE_UP)
    gohome = WebDriverWait(driver, 10)
    gohome = gohome.until(EC.visibility_of_element_located(
        (By.XPATH, " /html/body/div/div/header/nav/a/img"))).click()
    sleep(0.5)


# 執行要做的事情
# fb
driver.get("https://www.facebook.com/")
# ac = driver.find_element(By.ID, "email")
# ac.send_keys("")
# pas = driver.find_element(By.NAME, "pass")
# pas.send_keys("")
# login = driver.find_element(By.NAME, "login")
# login.click()
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()
sleep(1.5)
driver.get(
    "https://www.4gamers.com.tw/")

head_picture = WebDriverWait(driver, 15)
head_picture = head_picture.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "li.nav-item.d-none.d-lg-block.mDr-lg-4"))).click()

# -----------------------------------------facebook login-------------------------
facebookBTN = driver.find_element(
    By.CSS_SELECTOR, "button.btn.base-btn.d-flex.align-items-center.justify-content-center.w-100.mDb-2.btn-facebook-blue")
facebookBTN.click()
# -----------------------------------------account login ---------------------------
# account = driver.find_element(By.XPATH, "//input[@name='username']")
# account.send_keys("b976431")
# password = driver.find_element(By.XPATH, "//input[@name='password']")
# password.send_keys("5292mg6p")
# sub = WebDriverWait(driver, 10)
# sub = sub.until(EC.visibility_of_element_located(
#     (By.XPATH, "//button[@class='btn base-btn mb-3 mb-xl-2 w-100 btn-primary']"))).click()


# LoginConfirmBtn = WebDriverWait(driver, 10)
# LoginConfirmBtn = LoginConfirmBtn.until(EC.visibility_of_element_located(
#     (By.XPATH, '/html/body/div[2]/div[1]/div/div/header/button'))).click()
print(" refresh !")
sleep(2)
driver.refresh()
sleep(1)
# -------------------------------mission-----------------------------
# def callMission():
#     openMission = WebDriverWait(driver, 10)
#     openMission = openMission.until(EC.visibility_of_element_located(
#         (By.XPATH, "/html/body/div[1]/div/header/nav/ul/li[6]/a"))).click()

#     myMission = WebDriverWait(driver, 10)
#     myMission = myMission.until(EC.visibility_of_element_located(
#         (By.XPATH, "/html/body/div[1]/div/header/nav/ul/li[6]/a/div/div[2]/div/ul/li[3]/a"))).click()
# -------------------------------mission-----------------------------


# 匿名聊發文
# post.Post(driver)
# gohome()

# talkC.comments(driver)  # 匿名聊留言
# gohome()

# news.news(driver)  # 新聞
# gohome()

# bmb.bigMaster(driver)  # 大賢者閱讀案讚
# gohome()

# bmc.bigMaster(driver)  # 大賢者留言
# gohome()

# donate.talkDonate(driver)  # 匿名聊天斗內
# gohome()


gacha.Gacha(driver)  # 一次扭蛋
gohome()

vote.vote(driver)  # 投票
gohome()

earnMoney(driver)
gohome()
