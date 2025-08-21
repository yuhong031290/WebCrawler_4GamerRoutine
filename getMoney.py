from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pickle


# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_experimental_option("prefs", {
#                                 "profile.password_manager_enabled": False, "credentials_enable_service": False})
# driver = webdriver.Chrome(
#     options=options, service=Service("./chromedriver.exe"))
# driver.maximize_window()



# driver.get("https://www.facebook.com/")
# sleep(2)
# driver.refresh()
# cookies = pickle.load(open("./cookies.pkl", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)
#     print(cookie)
# sleep(2)
# driver.refresh()
# driver.get(
#     "https://www.4gamers.com.tw/")

# head_picture = WebDriverWait(driver, 10)
# head_picture = head_picture.until(EC.visibility_of_element_located(
#     (By.CSS_SELECTOR, "li.nav-item.d-none.d-lg-block.mDr-lg-4"))).click()

# # -----------------------------------------facebook login-------------------------
# facebookBTN = driver.find_element(
#     By.CSS_SELECTOR, "button.btn.base-btn.d-flex.align-items-center.justify-content-center.w-100.mDb-2.btn-facebook-blue")
# facebookBTN.click()


# print(" refresh !")
# sleep(2)
# driver.refresh()
# sleep(1)


selfdriver = None
def earnMoney(Driver):
    sleep(0.1)
    selfdriver = Driver
    openMission = WebDriverWait(selfdriver, 5)
    openMission = openMission.until(EC.visibility_of_element_located(
        (By.XPATH, "//li[@class='nav-item d-none d-lg-block text-2x-large mDr-lg-4']/a[@class='position-relative h-100 d-flex align-items-center text-black']/img[@class='rounded-circle']"))).click()
    
    sleep(0.1)
    myMission = WebDriverWait(selfdriver, 10)
    myMission = myMission.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/header/nav/ul/li[6]/a/div/div[2]/div/ul/li[3]/a"))).click()
    sleep(0.1)
    count = ""
    while True:

        allmissions = WebDriverWait(selfdriver, 3)
        allmissions = allmissions.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "button.btn.gradient-button.text-nowrap.btn-secondary.warning.fixed-width.px-0")))
        if allmissions == None:
            count += "0"
            if count == "000":
                break
            print("count= ", count)
        else:
            allmissions.click()
        sleep(0.85)
        print(allmissions)

# earnMoney(driver)