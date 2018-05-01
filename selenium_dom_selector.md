# Selenium으로 DOM 요소를 선택하는 방법

## DOM 내부에 있는 여러 개의 요소 중 처음 찾아지는 요소를 추출

메서드명|설명
:--:|:--:
find_element_by_id(id)|id 속성으로 요소를 하나 추출
find_element_by_name(name)|name 속성으로 요소를 하나 추출
find_element_by_css_selector(query)|CSS 선택자로 요소를 하나 추출
find_element_by_xpath(query)|XPath를 지정해 요소를 하나 추출
find_element_by_tag_name(name)|태그 이름이 name에 해당하는 요소를 하나 추출
find_element_by_link_text(text)|링크 텍스트로 요소를 추출
find_element_by_partial_link_text(text)|링크의 자식 요소에 포함돼 있는 텍스트로 요소를 하나 추출
find_element_by_class_name(name)|클래스 이름이 name에 해당하는 요소를 하나 추출


## DOM 내부에 있는 모든 요소 추출

메서드명|설명
:--:|:--:
find_elements_by_css_selector(query)|CSS 선택자로 요소를 여러개 추출
find_elements_by_xpath(query)|XPath를 지정해 요소를 여러개 추출
find_elements_by_tag_name(name)|태그 이름이 name에 해당하는 요소를 여러개 추출
find_elements_by_class_name|클래스 이름이 name에 해당하는 요소를 여러 개 추출
find_elements_by_partial_link_text(text)|링크의 자식 요소에 포함돼 있는 텍스트로 요소를 여러 개 추출

> 찾지 못하면 NoSuchElementException 예외 발생.

## DOM 요소에 적용할 수 있는 메서드와 속성

메서드명|설명
:--:|:--:
clear()|글자를 입력할 수 있는 요소의 글자를 지움
click()|요소를 클릭
get_attribute(name)|요소의 속성 중 name에 해당하는 속성의 값을 추출
is_displayed()|요소가 화면에 출력되는지 확인
is_enabled()|요소가 활성화돼 있는지 확인
is_selected()|체크박스 등의 요소가 선택된 상태인지 확인
screenshot(filename)|스크린샷을 찍음
send_keys(value)|키를 입력
submit()|입력 양식을 전송
value_of_css_property(name)|name에 해당하는 CSS 속성의 값을 추출
id|요소의 id 속성
location|요소의 위치
parent|부모 요소
rect|크기와 위치 정보를 가진 딕셔너리 자료형을 반환
screenshot_as_base64|스크린샷을 Base64로 추출
size|요소의 크기
tag_name|태그 이름
text|요소 내부의 글자

> 특수 키를 사용하려면 from selenium.Webdriver.common.keys import keys 모듈 import 필요.

## Selenium 드라이버 조작 (PhantomJS 전용 드라이버의 메서드와 속성)

메서드명|설명
:--:|:--:
add_cookie(cookie_dict)|쿠키 값을 딕셔너리 형식으로 지정
back()/forward()|이전 페이지 또는 다음  페이지로 이동
close()|브라우저를 닫음
current_url|현재 URL을 추출
delete_all_cookies()|모든 쿠키를 제거
delete_cookie(name)|특정 쿠키를 제거
execute(command, params)|브라우저 고유의 명령어를 실행
execute_async_script(script, &#42;args)|비동기 처리하는 자바스크립트를 실행
execute_script(script, &#42;args)|동기 처리하는 자바스크립트를 실행
get(url)|웹 페이지를 읽어 들임
get_cookie(name)|특정 쿠키 값을 추출
get_log(type)|로그를 추출(browser/driver/client/server)
get_screenshot_as_base64()|base64 형식으로 스크린샷을 추출
get_screenshot_as_file(filename)|스크린샷을 파일로 저장
get_window_position(windowHandle='current')|브라우저의 위치를 추출
get_window_size(windowHandle='current')|브라우저의 크기를 추출
implicitly_wait(sec)|최대 대기 시간을 초 단위로 지정해서 처리가 끝날 때 까지 대기
quit()|드라이버를 종료시켜 브라우저를 닫음
save_screenshot(filename)|스크린샷을 저장
set_page_load_timeout(time_to_wait)|페이지를 읽는 타임아웃 시간을 지정
set_script_timeout(time_to_wait)|스크립트의 타임아웃 시간을 지정
set_window_position(x, y, windowHandle='current')|브라우저의 위치를 지정

- 참고문헌 : 파이썬을 이용한 머신러닝, 딥러닝 실전 개발 입문

- Selenium with 파이썬 : [URL](http://selenium-python.readthedocs.io/index.html)
- SeleniumHQ Documentation : [URL](http://docs.seleniumhq.org/docs/)
