import requests
from bs4 import BeautifulSoup
# pip install pillow でインストールした
from PIL import Image
import io

# 画像の単体取得と保存

url = 'https://scraping-for-beginner.herokuapp.com/image'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

img_tag = soup.find('img')

root_url = 'https://scraping-for-beginner.herokuapp.com'
# img_tag['src']でsrcを取得可能
img_tag = root_url + img_tag['src']

# 画像の形式を変換するために、io.BytesIOを使用している
img = Image.open(io.BytesIO(requests.get(img_tag).content))
img.save('2023_coding/scraping/img/sample.jpg')