import requests
from bs4 import BeautifulSoup

url = 'https://scraping-for-beginner.herokuapp.com/ranking/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

# 全ての観光地情報を取得
spots = soup.find_all('div',attrs = {'class':'u_areaListRankingBox row'})
# その中の一つを取得する
spot = spots[0]

# タイトル名を取得する
spot_title = spot.find('div',attrs = {'class': 'u_title'})
# タイトル取得の際に不要なものを指摘する extract()で指定したタグを削除する
spot_title.find('span',attrs = {'class': 'badge'}).extract()
# 表記を変更する
spot_title = spot_title.text.replace('\n','')



# 評点の取得
spot_score = soup.find('div',attrs= {'class': 'u_rankBox'}).text
spot_score = float(spot_score.replace('¥n',''))

# 値の取得
# evaluateNumberは別の箇所で、class名でも使用されているため、その外側のu_categoryTipsItemから取得してくる
categoryItem = spot.find('div',attrs={'class':'u_categoryTipsItem'})
# 入れ子構造で、ひとまとまりで取得してきたものをリストで格納し直す
categoryItem = categoryItem.find_all('dl')

# categoryItem = categoryItem[0]
# # リストでそれぞれに分けて入れたものからさらに、値を指定
# category = categoryItem.dt.text
# rank = (categoryItem.span.text)

# print(category)
# print(rank)

# 辞書（dictionary）型とは、「{}」の中にkeyとvalueの組み合わせが含まれているデータ
details = {}

for categoryItem in categoryItem:
    category = categoryItem.dt.text
    rank = float(categoryItem.span.text)
    # 変数名['値'] = 'キー'　辞書型
    details[category] = rank

datum = details
datum['観光地名'] = spot_title
datum['評点'] = spot_score

print(details)