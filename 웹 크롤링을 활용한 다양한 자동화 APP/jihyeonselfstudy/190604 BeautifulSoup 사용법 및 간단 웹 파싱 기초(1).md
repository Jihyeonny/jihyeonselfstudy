# BeautifulSoup 사용법 및 간단 웹 파싱 기초(1)

##### beautifulsoup 설치

* anaconda prompt -> activate section2 -> pip install beautifulsoup4 -> atom 

   

##### beautifulsoup 사용법

```python
from urllib.parse import urljoin

baseUrl = "http://test.com/html/a.html"
print(">>", urljoin(baseUrl, "b.html"))
print(">>", urljoin(baseUrl, "sub/b.html"))
print(">>", urljoin(baseUrl, "../index.html"))
print(">>", urljoin(baseUrl, "../img/img.jpg"))
print(">>", urljoin(baseUrl, "../css/img.css"))

# => 출력
# >> http://test.com/html/b.html
# >> http://test.com/html/sub/b.html
# >> http://test.com/index.html
# >> http://test.com/img/img.jpg
# >> http://test.com/css/img.css 
```



```python
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# """ 을 쓰면 줄바꿈이 포함되어있는 문자열 """
html = """
<html>
<body>
<h1>파이썬 BeautifulSoup 공부</h1>
<p>태그 선택자</p>
<p>CSS 선택자</p>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
# print('soup', type(soup))
print('prettify', soup.prettify())


# => 출력
# prettify <html>
#  <body>
#   <h1>
#    파이썬 BeautifulSoup 공부
#   </h1>
#   <p>
#    태그 선택자
#   </p>
#   <p>
#    CSS 선택자
#   </p>
#  </body>
# </html>

h1 = soup.html.body.h1
print('h1', type(h1))
print(h1.string) # 내용 출력위해서
p1 = soup.html.body.p
print('p1', p1)
p2 = p1.next_sibling.next_sibling # 줄바꿈이 있었으니까 2번
print('p2', p2)
p3 = p1.previous_sibling.previous_sibling
print('p3', p3)

print("h1 >> ", h1.string)
print("p >> ", p1.string)
print("h2 >> ", p2.string)

# => 출력
# h1 <class 'bs4.element.Tag'>
# 파이썬 BeautifulSoup 공부
# p1 <p>태그 선택자</p>
# p2 <p>CSS 선택자</p>
# p3 <h1>파이썬 BeautifulSoup 공부</h1>
# h1 >>  파이썬 BeautifulSoup 공부
# p >>  태그 선택자
# h2 >>  CSS 선택자
```



```python
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")
# print('links', type(links))

for a in links:
    print('a', type(a), a)

# => 출력
# a <class 'bs4.element.Tag'> <a href="http://www.naver.com">naver</a>
# a <class 'bs4.element.Tag'> <a href="http://www.daum.net">daum</a>
# a <class 'bs4.element.Tag'> <a href="https://www.google.com">google</a>
# a <class 'bs4.element.Tag'> <a href="https://www.tistory.com">tistory</a>
```



```python
for a in links:
    # print('a', type(a), a)
    href = a.attrs['href']
    txt = a.string
    print('txt >> ', txt, 'href >> ', href)

# => 출력
# txt >>  naver href >>  http://www.naver.com
# txt >>  daum href >>  http://www.daum.net
# txt >>  google href >>  https://www.google.com
# txt >>  tistory href >>  https://www.tistory.com
```

```python
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a") # find메소드를 사용해서 bsf제공하는 태그요소로 원하는 요소로 파싱
# print('links', type(links))

a = soup.find_all("a", string="daum")
print('a', a)
b = soup.find_all("a", limit=2)
print('b', b)
c = soup.find_all(string=["naver", "google"])
print('c', c)

for a in links:
    # print('a', type(a), a)
    href = a.attrs['href']
    txt = a.string
    # print('txt >> ', txt, 'href >> ', href)

# => 출력
# a [<a href="http://www.daum.net">daum</a>, <a href="http://www.daum.net">daum</a>]
# b [<a href="http://www.naver.com">naver</a>, <a href="http://www.daum.net">daum</a>]
# c ['naver', 'google']
```



##### 선택자

* <https://www.w3schools.com/cssref/trysel.asp> 

```python
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


html = """
<html><body>
<div id="main">
  <h1>강의목록</h1>
  <ul class="lecs">
    <li>Java 초고수 되기</li>
    <li>파이썬 기초 프로그래밍</li>
    <li>파이썬 머신러닝 프로그래밍</li>
    <li>안드로이드 블루투스 프로그래밍</li>
  </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

h1 = soup.select("div#main > h1")
print('h1', h1)
print(h1.string)


# => 출력
# Traceback (most recent call last):
#   File "C:\Users\student\selfstudy\웹 크롤링을 활용한 다양한 자동화 APP\jihyeonselfstudy\section2\download2-5-4.py", line 27, in <module>
#     print(h1.string)
# AttributeError: 'list' object has no attribute 'string'
# => 에러메세지: h1타입은 list 이기 때문에 string 속성 접근 x 
```



```python
soup = BeautifulSoup(html, 'html.parser')

h1 = soup.select("div#main > h1")
print('h1', h1)
print(h1.string)

for z in h1:
    print(z.string) # 이렇게 하면 번거로움  

# => 해결방안
soup = BeautifulSoup(html, 'html.parser')

h1 = soup.select_one("div#main > h1")
print(h1.string)
```



```python
# li가져오기 

from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


html = """
<html><body>
<div id="main">
  <h1>강의목록</h1>
  <ul class="lecs">
    <li>Java 초고수 되기</li>
    <li>파이썬 기초 프로그래밍</li>
    <li>파이썬 머신러닝 프로그래밍</li>
    <li>안드로이드 블루투스 프로그래밍</li>
  </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

h1 = soup.select_one("div#main > h1")
# h1 = soup.select_one("#main > h1") 같은 말
print(h1.string)
list_li = soup.select("div#main > ul.lecs > li")
# list_li = soup.select("#main > .lecs >li") 같은 말 
for l in list_li:
    print("li >>>", li.string)

```

