from bs4 import BeautifulSoup
import urllib.request as req
import datetime

# HTML 가져오기
url = "http://info.finance.naver.com/marketindex"
res = req.urlopen(url)

# HTML 분석
soup = BeautifulSoup(res, "html.parser")

# 원하는 데이터 추출
price = soup.select_one("div.head_info > span.value").string
print("usd/krw", price)

# 저장할 파일 이름 구하기
t = datetime.date.today()
fname = t.strftime("%Y-%m-%d") + ".txt"
with open(fname, "w", encoding = "utf-8") as f:
    f.write(price)
