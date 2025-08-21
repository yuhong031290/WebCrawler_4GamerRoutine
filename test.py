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
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from time import sleep
import pickle
# 設定時間 自動開始
from datetime import datetime

# 設定google driver的路徑檔案2
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    print(cookie)