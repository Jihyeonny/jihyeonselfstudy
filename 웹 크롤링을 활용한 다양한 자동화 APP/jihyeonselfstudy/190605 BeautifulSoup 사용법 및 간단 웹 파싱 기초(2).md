# BeautifulSoup 사용법 및 간단 웹 파싱 기초(2)

##### 정규표현식 

* [http://pythonstudy.xyz/python/article/401-%EC%A0%95%EA%B7%9C-%ED%91%9C%ED%98%84%EC%8B%9D-Regex](http://pythonstudy.xyz/python/article/401-정규-표현식-Regex)  

```python
from bs4 import BeautifulSoup
import sys
import io
import re #regex
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
  <ul>
    <li><a id="naver" href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
print(soup.find(id="naver").string)

#li = soup.find_all(href=re.compile(r"^https://")) # 시작은 https 로한다.
li = soup.find_all(href=re.compile(r"da")) # da가 들어가는 거 

for e in li:
    print(e.attrs['href']) 
```



##### 선택자(1)

```python
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("food-list.html",encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

print(soup)

print("1", soup.select("li:nth-of-type(4)")[1].string) #각 li 태그 그룹의 4번째 요소 선택
print("2", soup.select_one("#ac-list > li:nth-of-type(4)").string)
print("3", soup.select("#ac-list > li[data-lo='cn']")[0].string)
print("4", soup.select("#ac-list > li.alcohol.high")[0].string)

param = {"data-lo": "cn", "class": "alcohol"}
print("5", soup.find("li", param).string)
print("6", soup.find(id="ac-list").find("li",param).string)

for ac in soup.find_all("li"):
    if ac['data-lo'] == 'us':
        print('data-lo == us', ac.string)
```

##### 선택자(2) 

```python
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("cars.html",encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

#function 만들기
def car_func(selector):
    print("car_func", soup.select_one(selector).string)

#여러가지 방법
#1. 람다식
car_lambda = lambda q : print("car_lambda", soup.select_one(q).string)

#2. 함수(6개 다 똑같은 출력)
car_func("#gr")
car_func("li#gr")
car_func("ul > li#gr")
car_func("#cars #gr")
car_func("#cars > #gr")
car_func("li[id='gr']")


print("car_func", soup.select("li")[3].string)
print("car_func", soup.find_all("li")[3].string)

```

