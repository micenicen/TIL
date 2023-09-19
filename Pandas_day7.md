# 판다스 7일차
## 정보 가져오기 - 인스타그램
### 1. 개요
만들려는 프로그램이 인스타그램에 자동으로 로그인을 한 다음 특정 키워드에 해당하는 페이지를 검색하고 그 결과를 스크래핑하는 것이다. 

로그인 - 키워드 검색 - 게시물 클릭 - 글 가져오기 - 다음 페이지 - 글 가져오기 순으로 작업이 이루어질 것이다. 

문제는 다음 페이지를 누를 때 주소에 규칙이 존재하지 않는다. 규칙을 기반으로 페이지를 읽어오기 어렵다. 그래서 화살표에 대한 주소를 알고 있어야 한다. 즉 셀렉터를 알고 있어야만 텍스트 데이터를 긁어올 수 있다.

이벤트가 발생했을 때 (사용자가 어느 동작을 할 경우) 텍스트를 스크래핑할 수 있도록 코드를 작성하는 법을 배워보자.

참고 : 다른 sns도 동작방식이 거의 유사하다. 


### 2. 접속절차
```python
from selenium import webdriver
import time
```
셀레늄으로부터 웹드라이버를 가져오는 작업을 먼저 시작하자.
염두에 두어야 하는 점은 코드의 실행속도는 매우 빠르나 페이지 실행속도가 매우 느리다는 것이다.

```python
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(1)
```

동작은 천천히 수행하거나 Time.sleep를 이용하는 방법이 존재한다.
웹사이트로부터 읽어들이는 시간이 있는 것은 항상 염두에 두어야 한다.

이제 아이디와 비밀번호를 입력해야 할 것이다. 아이디/비밀번호를 입력할 수 있는 박스가 무엇인지 알아야 한다.

```python
#loginForm > div > div:nth-child(1) > div > label > input -> 아이디 입력가능
#loginForm > div > div:nth-child(2) > div > label > input -> 비밀번호 입력가능
```

이제 이와 같은 방법으로 입력이 가능하다. 
```python
input_id.send_keys("userid")
input_pw.send_keys("userpw")
```
이렇게 해서 내부에 아이디를 입력하는 것이 가능하다.
만약 안된다면 아이디 내부칸의 정보를 input_id.clear()로 지우고 시작할 수도 있다.
```python
input_pw.submit()
time.sleep(2)
```
다음과 같은 명령어를 입력하여 로그인을 실행할 수 있다.

### 2. 1 접속절차 - 또 다른 방법
다음과 같은 방법으로도 로그인이 가능하다. 클래스를 따로 가져와서 로그인을 하는 것이다.

```python
input_id = driver.find_elements("css selector", "input._aa4b._add6._ac4d")[0]
input_pw = driver.find_elements("css selector", "input._aa4b._add6._ac4d")[1]
```
현재와 같이 클래스 이름을 주면서 로그인을 할 수 있다.

