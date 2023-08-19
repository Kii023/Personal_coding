from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

# Chromeを開いて実施
# browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Chromeを開かずに実施
options = Options()
# 開かないことを設定している。
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

url = 'https://scraping-for-beginner.herokuapp.com/login_page'
driver.get(url)

# ログイン
eleme_username = driver.find_element(By.ID, 'username')
eleme_username.send_keys('imanishi')
eleme_userpass = driver.find_element(By.ID, 'password')
eleme_userpass.send_keys('kohei')
eleme_login_btn = driver.find_element(By.ID, 'login-btn')
eleme_login_btn.click()

# 単体スクレイピング
# elem_th = driver.find_element(By.TAG_NAME,'th')
# elemTh = elem_th.text

# 一括スクレイピング機能

# キーの取得
elems_th = driver.find_elements(By.TAG_NAME,'th')
# キーの要素数
elems_count = len(elems_th)
keys = []
for elems_th in elems_th:
    key = elems_th.text
    # 末尾に要素を追加
    keys.append(key)

# 値の取得
elems_td = driver.find_elements(By.TAG_NAME,'td')
values = []
for elems_td in elems_td:
    value = elems_td.text
    values.append(value)

# DataFrame()二次元の表形式のデータ
df = pd.DataFrame()
df['項目'] = keys
df['値'] = values

# ファイル出力、※インデックス不要の場合index=False
df.to_csv('2023_coding/scraping/data/講師情報.csv', index=False)

# print(keys)
# print(values)
print(elems_count)

driver.quit()