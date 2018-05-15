# 모듈 import
import io
import sys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import os.path, time, re
# from firebase import firebase

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# url = "https://www.instagram.com/explore/tags/%ED%95%99%EA%B5%90/"
# url = "https://www.instagram.com/explore/tags/%EC%A7%80%EB%B0%A9%EC%84%A0%EA%B1%B0/"


headers = {
'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
'''
x = 125, 446, 767 반복, y = 321씩 커짐
{'height': 293, 'width': 293, 'x': 125, 'y': 361}
{'height': 293, 'width': 293, 'x': 446, 'y': 361}
{'height': 293, 'width': 293, 'x': 767, 'y': 361}
{'height': 293, 'width': 293, 'x': 125, 'y': 682}
{'height': 293, 'width': 293, 'x': 446, 'y': 682}
{'height': 293, 'width': 293, 'x': 767, 'y': 682}
{'height': 293, 'width': 293, 'x': 125, 'y': 1003}
{'height': 293, 'width': 293, 'x': 446, 'y': 1003}
{'height': 293, 'width': 293, 'x': 767, 'y': 1003}
{'height': 293, 'width': 293, 'x': 125, 'y': 1404}
{'height': 293, 'width': 293, 'x': 446, 'y': 1404}
{'height': 293, 'width': 293, 'x': 767, 'y': 1404}
{'height': 293, 'width': 293, 'x': 125, 'y': 1725}
{'height': 293, 'width': 293, 'x': 446, 'y': 1725}
{'height': 293, 'width': 293, 'x': 767, 'y': 1725}
{'height': 293, 'width': 293, 'x': 125, 'y': 2046}
{'height': 293, 'width': 293, 'x': 446, 'y': 2046}
{'height': 293, 'width': 293, 'x': 767, 'y': 2046}
{'height': 293, 'width': 293, 'x': 125, 'y': 2367}
{'height': 293, 'width': 293, 'x': 446, 'y': 2367}
{'height': 293, 'width': 293, 'x': 767, 'y': 2367}
'''


DRIVER_DIR = '/Users/moonseongjae/chromedriver'
BASE_URL = 'https://www.instagram.com/'
IMG_PAUSE_TIME = 3

def get_detail(url):
    try:
        driver = webdriver.Chrome(DRIVER_DIR)
        driver.implicitly_wait(5)
        driver.get(url)
        time.sleep(2)
        ul_list = []
        likes_list = []
        ul = driver.find_elements_by_css_selector('ul._b0tqa li')
        likes = driver.find_elements_by_css_selector('span._nzn1h span')
        for t in ul:
            ul_list.append(t.text)
        for t in likes:
            likes_list.append(t.text)
        return ul_list, likes_list
    except:
        return None
        print('error')
    finally:
        driver.close()

def print_list(temp_list):
    for items in temp_list:
        if isinstance(items, list):
            print_list(items)
        else:
            print(items)
    # print("==============================")

# 이미지경로(가능), 내용(가능), 태그(가능), 댓글(시도), 작성자(시도), 등록일(시도), 좋아요(시도)
driver = webdriver.Chrome(DRIVER_DIR)
try:
    driver.implicitly_wait(10) # 암묵적으로 웹 자원을 (최대) 10초 기다리기
    driver.get(url)
    totalCount = driver.find_element_by_class_name('_fd86t ').text # 총 게시물 수
    print("총게시물:",totalCount)
    elem = driver.find_element_by_tag_name("body")
    no_of_pagedowns = 1
    img_list = [] # 이미지
    # alt_list = [] # 태그, 제목
    loc_list = [] # 상세보기 url
    while no_of_pagedowns < 5:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        loc = driver.find_elements_by_css_selector('div._mck9w a')
        img = driver.find_elements_by_css_selector('div._4rbun img')
        for i in img:
            if i.get_attribute('src') not in img_list:
                img_list.append(i.get_attribute('src'))
                # alt_list.append(i.get_attribute('alt'))
        for i in loc:
            if i.get_attribute('href') not in loc_list:
                loc_list.append(i.get_attribute('href'))
        no_of_pagedowns += 1

    for img in img_list:
        print(img)

    ret_ul = []
    ret_likes = []
    for i in loc_list:
        ul_list, likes_list = get_detail(i)
        if ul_list is None:
            print("Error ul")
        else:
            ret_ul.append(ul_list)
        if likes_list is not None:
            ret_likes.append(likes_list)

    print_list(ret_ul)
    print_list(ret_likes)
finally:
    driver.close()

# driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[2]/a/div/div[1]/img').send_keys(Keys.ENTER)

# test = driver.find_elements_by_css_selector('div._4rbun img') # alt = 글, 태그, src = 사진 경로
    # for i in test:
        # print(i.get_attribute('src'))
        # print(i.get_attribute('src'), i.get_attribute('alt'))
# finally:
    # driver.close()


# print(i.get_attribute('href')) # 추가 경로
# loc = driver.find_elements_by_css_selector('div._mck9w a')
# for i in loc:
#     print(i.get_attribute('src'), i.get_attribute('alt'))
#     print(i.get_attribute('href'))

# driver.implicitly_wait(3)
# driver.get(i.get_attribute('href'))
# ul = driver.find_elements_by_css_selector('ul._b0tqa li')
# for t in ul:
#     print(t.text)

# for i in loc:
#     req = requests.get(i.get_attribute('href'))
#     soup = BeautifulSoup(req.content, 'html.parser')
#     title = soup.find("title").text
#     test = soup.select("div._4a48i li")
#     print('title:',title)
#     print('test:',test)
#     print("==============================")

# def get_detail(driver, link, max_attempts = 3):
#     attempt = 1
#     while True:
#         try:
#             driver.implicitly_wait(3)
#             driver.get(link)
#             ul = driver.find_elements_by_css_selector('ul._b0tqa li')
#             # likes = driver.find_elements_by_css_selector('span._nzn1h > span.text')
#             print(ul)
#         except StaleElementReferenceException:
#             if attempt == max_attempts:
#                 raise
#             attempt += 1
# try:
