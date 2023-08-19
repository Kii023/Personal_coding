import requests
from bs4 import BeautifulSoup
# pip install pillow でインストールした
from PIL import Image
import io

# 画像の複数取得と保存

url = 'https://scraping-for-beginner.herokuapp.com/image'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

img_tags = soup.find_all('img')
# 画像の命名の際に、インデントが必要のため、enumerate
for i, img_tag in enumerate(img_tags):

    root_url = 'https://scraping-for-beginner.herokuapp.com'
    img_tag = root_url + img_tag['src']

    img = Image.open(io.BytesIO(requests.get(img_tag).content))
    # 文字列に変数を入れる場合：文字列の前にfをいれ、入れる変数を{}で囲む必要がある
    img.save(f'2023_coding/scraping/img/sample{i}.jpg')