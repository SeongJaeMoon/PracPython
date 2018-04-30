# 필요한 모듈 import
from selenium import webdriver
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

USER = "USER"
PW = "PASSWORD"

driver = webdriver.Chrome("크롬 드라이버 주소")
driver.implicitly_wait(3)

url_join = "https://nid.naver.com/nidlogin.login"
driver.get(url_join)
print("로그인 페이지에 접근")

# 텍스트 박스에 아이디와 비밀번호 입력
e = driver.find_element_by_id("id")
e.clear()
e.send_keys(USER)
e = driver.find_element_by_id("pw")
e.clear()
e.send_keys(PW)

# 입력 양식 전송해서 로그인
form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()
print("로그인 버튼을 클릭")

# 쇼핑 페이지의 데이터 get
driver.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")

# 쇼핑 목록 출력
products = driver.find_element_by_css_selector(".p_info span")
print(products)
for product in products:
    print("-", product.text)
    
