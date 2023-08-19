from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# ウェブブラウザに適した、ウェブドライバをインストールした上で起動する。
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = 'https://scraping-for-beginner.herokuapp.com/login_page'
browser.get(url)

sleep(1)

# ログイン画面の要素の場所の取得
eleme_username = browser.find_element(By.ID, 'username')
# 要素の場所に値を入力する。
eleme_username.send_keys('imanishi')

eleme_userpass = browser.find_element(By.ID, 'password')
eleme_userpass.send_keys('kohei')

# 要素を指定して、クリックをする
eleme_login_btn = browser.find_element(By.ID, 'login-btn')
eleme_login_btn.click()

# スクレイピング機能　個別指定
element_name = browser.find_element(By.ID, 'name')
name = element_name.text
element_company = browser.find_element(By.ID, 'company')
company = element_company.text
element_hobby = browser.find_element(By.ID, 'hobby')
hobby = element_hobby.text
hobby.replace('¥n', ',')

print(name)
print(company)
print(hobby)

sleep(2)

browser.quit()