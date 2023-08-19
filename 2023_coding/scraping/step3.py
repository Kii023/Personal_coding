import requests
from bs4 import BeautifulSoup

# ライブラリRequests　と　BeautifulSoup　を使用

url = 'https://scraping-for-beginner.herokuapp.com/udemy'
# 指定したURLのHTMLを取得する
res = requests.get(url)
# ↑で取得した形式は「str」このままだと使いにくいため、BeautifulSoupを使用する

# htmlの構造を分解してわかりやすくする
soup = BeautifulSoup(res.text, 'html.parser')
# フォーマットをかけてくれる
# print(soup.prettify())

# 要素名に続いて、属性を引数で指定
# pタグを全て取得する　※複数リスト型で取得している
soup.find_all('p')

# pタグ一つを取得する
# soup.find('p')
# 簡略化
# soup.p

# リストで取得をしてきた、pタグの中の、クラスがsubscribersを指定
subscribers = soup.find_all('p',attrs = {'class': 'subscribers'})[0]

# text.splitで文字を分割して、その2番目を[1]で指定
n_subscribers = int(subscribers.text.split('：')[1])

reviews = soup.find_all('p', attrs = {'class':'reviews'})[0]
n_reviews = int(reviews.text.split('：')[1])

# view =  
print(n_subscribers)
print(n_reviews)

# CSSセレクタで指定
# css_subscribers = soup.select('.subscribers')[0] ↓と同様の取得内容
css_subscribers = soup.select_one('.subscribers')

print(css_subscribers.text)
