# 필요한 모듈 import
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 아이디와 비밀번호 지정하기
USER = "ID"
PW = "PASSWORD"

# 세션 적용
session = requests.session()

# 로그인
login_info = {
    "m_id":"id", # 아이디 지정
    "m_passwd":"pw" # 비밀번호 지정
}

url_join = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_join, data = login_info)
res.raise_for_status() # 오류가 발생하면 예외 발생

# 한빛미디어 마이페이지 접근
url_mypage = "http://www.hanbit.co.kr/myhanbit/"
res = session.get(url_mypage)
res.raise_for_status() # 오류가 발생하면 예외 발생

# 마일리지와 이코인 가져오기
soup = BeautifulSoup(res.text, 'html.parser')

mileage = soup.select_one(".mileage_section1 span").get_text()
ecoin = soup.select_one(".mileage_section2 span").get_text()

print("마일리지:", mileage)
print("ecoin:", ecoin)
