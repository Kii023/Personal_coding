import requests
from bs4 import BeautifulSoup
import pandas as pd

# 一括でスクレイピングを行い、そのデータをcsvではき出すまとめ

url = 'https://scraping-for-beginner.herokuapp.com/ranking/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

data = []

spots = soup.find_all('div',attrs = {'class':'u_areaListRankingBox row'})
for spot in spots:

    spot_title = spot.find('div',attrs = {'class': 'u_title'})
    spot_title.find('span',attrs = {'class': 'badge'}).extract()
    spot_title = spot_title.text.replace('\n','')

    spot_score = soup.find('div',attrs= {'class': 'u_rankBox'}).text
    spot_score = float(spot_score.replace('\n',''))

    categoryItem = spot.find('div',attrs={'class':'u_categoryTipsItem'})
    categoryItem = categoryItem.find_all('dl')

    details = {}

    for categoryItem in categoryItem:
        category = categoryItem.dt.text
        rank = float(categoryItem.span.text)
        # 変数名['値'] = 'キー'　辞書型
        details[category] = rank

    datum = details
    datum['観光地名'] = spot_title
    datum['評点'] = spot_score

    data.append(datum)

print(data)

df = pd.DataFrame(data)
df.to_csv('2023_coding/scraping/data/観光地評点.csv', index=False)

# カラムの順番を入れ替える
df = df[['観光地名','評点','楽しさ','人混みの多さ','景色','アクセス']]
df.to_csv('2023_coding/scraping/data/観光地評点_カラム整理.csv', index=False)