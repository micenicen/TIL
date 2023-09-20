# 판다스 7일차
## 정보 가져오기 - 인스타그램
### 1. 개요
만들려는 프로그램이 인스타그램에 자동으로 로그인을 한 다음 특정 키워드에 해당하는 페이지를 검색하고 그 결과를 스크래핑하는 것이다. 

로그인 - 키워드 검색 - 게시물 클릭 - 글 가져오기 - 다음 페이지 - 글 가져오기 순으로 작업이 이루어질 것이다. 

문제는 다음 페이지를 누를 때 주소에 규칙이 존재하지 않는다. 규칙을 기반으로 페이지를 읽어오기 어렵다. 그래서 화살표에 대한 주소를 알고 있어야 한다. 즉 **셀렉터를 알고 있어야만 텍스트 데이터를 긁어올 수 있다.**

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

### 3. 키워드 탐색
이제 키워드를 탐색해보자. 교육예시로 울릉도 맛집이라는 키워드를 검색한 결과페이지를 사용해보자.

```python
# https://www.instagram.com/explore/tags/%EC%9A%B8%EB%A6%89%EB%8F%84%EB%A7%9B%EC%A7%91/
```
현재와 같은 방식으로 나타난다. 퍼센트글자는 한글문자를 풀어서 유니코드로 변환한 결과를 나타낸 것이다.

이제 드라이버에 주소를 대입해서 가동해보자.
```python
driver.get("https://www.instagram.com/explore/tags/%EC%9A%B8%EB%A6%89%EB%8F%84%EB%A7%9B%EC%A7%91/")
time.sleep(1)
```
### 3.1 키워드 탐색 - 또 다른 방법
워드를 태그 앞에 대입해도 같은 방법으로 결과가 도출된다.

```python
word = "울릉도맛집"
driver.get("https://www.instagram.com/explore/tags/"+word)
time.sleep(1)
```

### 4. 피드 살펴보기
먼저 첫번째 게시글을 클릭해야 한다. 그리고 두 번째 게시글과 주소를 비교하여 차이를 살펴본다.
문제는 인스타그램은 피드를 넘길 경우 주소가 불규칙한 패턴으로 변경되는 것을 볼 수 있다. 

또 다른 방법으로는 게시판의 클래스를 보고 다른 게시글과 연관성이 있는지 확인하는 것이다. 재밌는 점은 인스타 게시글은 모든 클래스 이름이 동일하다는 것이다. 

```python
driver.find_elements("css selector","#mount_0_0_2h > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > article > div > div > div > div:nth-child(1) > div:nth-child(1) > a > div._aagu > div._aagw")[0]
```
셀렉터 링크가 너무 길다. 이럴때는 클래스명을 가져와서 표시하는 것도 하나의 방법이다. 
```python
driver.find_elements("css selector","div._aagw")
```
인스타그램의 게시물 28개가 상당히 깔끔하게 나온다. 
```python
first = driver.find_elements("css selector","div._aagw")[0]
first.click()
```
코드를 작동시켜보자.

### 5. 피드 내부 버튼 조작하기
```python
btn1 = driver.find_elements("css selector", "button> div > span > svg.x1lliihq.x1n2onr6")
btn1[button_count].click()
if button_count == 0:
    button_count += 1
```
인스타그램의 클릭 매커니즘은 다음과 같다.
1. 버튼클릭 요소는 상황에 따라 다르다. 
    - 맨 처음칸에서는 btn1[0]이 다음 칸이다. 두번째 칸부터 btn1[1]이 다음 칸으로 변경된다.
    - 그렇기에 if문을 사용하여 1을 증가시켰다.
2. 버튼은 특정 클래스를 사용해야 한다.
    - 또 다른 버튼 클래스는 댓글보기 버튼이다. 
3. 타임슬립이 어느정도 필요하다.
    - 댓글로딩으로 인해서 바로 작동시키는 것은 권장하지 않는다.

### 6. 해시태그 가져오기
```python
from bs4 import BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
content = soup.select("div._ae5q._akdn._ae5r._ae5s > ul > div > li > div > div > div._a9zr")[0].text
content
```
해시태그를 끌어온다면 샾 기호가 먼저 나오고 단어가 나온다. 이는 정규표현식을 통해서 끌어오는 것이 가능하다. 
```python
import re
re.findall("#[ㄱ-ㅎ가-핳]+",content)
```
>['#냥꼬네게스트하우스','#관음도'... '#함스타']

태그에 달려있는 그림이나 이모티콘을 가져오고 싶다면 다음과 같이 작성해보자. 
```python
re.findall("#[^[\s]+",content)
```
>['#냥꼬네게스트하우스','#관음도🏷️','#나리분지🏷️'#함스타']

### 7. 좋아요 가져오기



## 판다스 조작 노하우
### 1. 오류 예외처리하는 요령
코드가 제대로 수행되어질 수 없는 상황이 생기면 자동으로 오류가 발생한다. 오류 메세지가 나올 것을 대비해서 어떤 식으로 처리하라고 지시할 수 있다.

예를 들어 다음과 같은 함수가 있다고 가정해보자.
```python
def trycatch(x):
    return 1/x
trycatch(2)
```
2를 인풋값으로 입력했기에 정상적으로 출력될 것이다.
```python
def trycatch(x):
    return 1/x
trycatch(0)
```
이럴 경우 "ZeroDivisionError"가 발생할 것이다. 이러한 예외가 발생할 경우 예외처리를 하는 방법은 다음과 같다.

```python
try:
    # 실행 코드
    x = int(input("숫자 입력 : "))
    y = 1/x
    print(y)
except:
    #예외 발생시 실행됨
    print("0으로 나누면 안됩니다.")
```
숫자를 0으로 입력하더라도 "0으로 나누면 안됩니다."가 출력되고 별도의 오류가 뜨지 않게된다. 예외가 발생하는 경우에 except에서 처리하는 것이다.
```python
y = [10, 20, 30]
 
try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
except:
    print("애러가 발생했습니다.")
```
애러의 종류와 상관없이 예외처리를 하고자 하면 그냥 except를 실행시키면 된다. 