### 190531

# BeautifulSoup 사용법 및 간단 웹 파싱 기초

* 웹 파싱: 궁극적으로 어떤 html파일(태그, 요소, 속성 등으로 구성) 잘 분석해서 내가 원하는 데이터의 위치를 찾는 것.

  ex) 이미지 경로, 동영상 경로, 문자, 숫자 등

* BeautifulSoup이용하면 손쉽게 파싱 가능. 
  * anaconda prompt에서 beautifulSoup 설치

    ```cmd
    pip install beautifulsoup4
    conda list #설치완료 확인
    ```



*  urljoin

  ```python
  from urllib.parse import urljoin
  
  baseUrl="http://test.com/html/a.html"
  print(">>",urljoin(baseUrl,"b.html"))
  # >> http://test.com/html/b.html 치환되어서 나옴.
  print(">>",urljoin(baseUrl,"sub/b.html"))
  # >> http://test.com/html/sub/b.html
  print(">>",urljoin(baseUrl,"../index.html"))
  # >> http://test.com/index.html 상위로 가서 치환되어서 나옴.
  print(">>",urljoin(baseUrl,"../img/img.jpg"))
  # >> http://test.com/img/img.jpg
  print(">>",urljoin(baseUrl,"../css/img.css"))
  # >> http://test.com/css/img.css
  ```

  

* """ """

  줄 바꿈이 포함되어 있는 문자열

  ```python
  html="""
  <html>
  <body>
  <h1>파이썬 BeautifulSoup 공부</h1>
  <p>태그 선택자</p>
  <p>CSS 선택자</p>
  </body>
  </html>
  """
  ```

  

* beautifulsoup 기초

  ```python
  soup=BeautifulSoup(html, 'html.parser')
  #soup에 이 내용이 객체로 만들어져서 할당 됨.
  print('soup',type(soup))
  print('prettify',soup.prettify())
  h1=soup.html.body.h1
  print('h1',h1)
  # h1 <h1>파이썬 BeautifulSoup 공부</h1>
  print('h1',type(h1))
  # h1 <class 'bs4.element.Tag'>
  print(h1.string)
  
  p1=soup.html.body.p
  print(p1)
  p2=p1.next_sibling
  print('p2',p2)
  p2=p1.next_sibling.next_sibling
  print('p2',p2)
  p3=p1.previous_sibling.previous_sibling
  print('p3',p3)
  ```

  * prettify() : html 자동 들여쓰기해서 출력.

  * soup.html.body.h1: soup 객체 html태그 안의 body 태그 안의 h1태그 선택

  * h1.string: 문자열만 출력

  * p 태그는 여러 개 있으므로 soup.html.body.p의 경우 첫번째 노드만 가져옴.

    따라서, next_sibling을 이용해 다음 p태그에 접근.

    `""" """`의 경우, 각 줄 마지막에 \n이 포함되어 있기 때문에 next_sibling을 하면 \n가 선택됨.

    따라서, next_sibling.next_sibling을 해주어야 다음 태그가 출력됨. 물론 한 줄 쓰기 경우엔 그럴 필요 없음.

  * previous_sibling의 경우도 next_sibling과 마찬가지이나 이전 태그로 이동.



* 태그 선택자 이용해 한번에 가져오기

  ```python
  html="""
  <html><body>
      <ul>
          <li><a href="http://www.naver.com">naver</a></li>
          <li><a href="http://www.daum.net">daum</a></li>
          <li><a href="http://www.daum.com">daum</a></li>
          <li><a href="http://www.google.com">google</a></li>
          <li><a href="http://www.tistory.com">tistory</a></li>
      </ul>
  </body></html>
  """
  soup=BeautifulSoup(html,'html.parser')
  
  links=soup.find_all("a")
  print('links',type(links))
  a=soup.find_all("a",string="daum")
  print('a',a)
  b=soup.find("a")
  print('b',b)
  c=soup.find_all("a",limit=3)
  print('c',c)
  d=soup.find_all(string=["naver","google"])
  print('d',d)
  print('d',type(d))
  # d <class 'bs4.element.ResultSet'>
  
  for a in links:
      print('a',type(a),a)
      href=a.attrs['href']
      # attrs: 속성. 
      txt=a.string
      print('txt >> ',txt,'href >> ',href)
  ```

  * .find_all("a"): 모든 a태그 가져옴.
  * .find_all("a",string="daum"): a 태그 중 string이 조건에 맞는 것만 가져옴.

  * .find("a"): a태그 상위 1개만 가져옴.

  * .find_all("a",limit=3): "a" 태그 중 상위 3개만 가져옴.

  * .find_all(string=["naver","google"]): string에 해당하는 string만 가져옴. 보통 쓸일 x.

  * type이 resultset의 경우 for문 이용해서 출력해야함.

  * .attrs[key 값]: key 속성의 value 출력

    href=""에서 href가 key ""가 value



* css 선택자 이용해서 조건에 맞는 element 가져오기

  ```python
  html="""
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
  
  soup=BeautifulSoup(html,'html.parser')
  h1=soup.select("div#main > h1")
  print('h1',h1)
  print('h1',type(h1))
  for z in h1:
      print(z.string)
  h1=soup.select_one("div#main > h1")
  print('h1',h1)
  print('h1',h1.string
  
  list_li=soup.select("div#main > ul.lecs > li")
  for li in list_li:
      print("li >>> ",li.string)
  ```

  * .select("div#main > h1"): div태그에서 id가 main인 것의 하위의 h1

  * print('h1',h1.string)
    에러남. 왜냐하면 h1의 type이 list이기 때문에 바로 리스트의 속성에 접근 불가능.

     따라서 하나라도 반복문을 돌려야 함.

  * 하지만 번거로움 피하기 위해 .select_one 사용하면 됨. 하나인 경우!

























