### 190604

# BeautifulSoup을 활용한 웹 파싱 실습

- 변하는 데이터들을 자동화 시켜두어, 일정한 시간에 가져와 데이터베이스에 저장하기.

- 다음 금융 시가총액 상위 종목 가져오기

  다음 금융 사이트

  ```python
  url="http://finance.daum.net/"
  res=req.urlopen(url).read()
  soup=BeautifulSoup(res,"html.parser")
  
  # print('soup',soup.prettify())
  # .prettify() 이쁘게 보여주기 위해
  
  top=soup.select("ul#topMyListNo1 > li")
  
  for i,e in enumerate(top,1):
      (top,1) 시작 인덱스 1로 지정.
      print(i,",",e.find("a").string," : ", e.find("span").string)
  ```

  

- 네이버 금융 Top4 종목 가져오기

  ```python
  url="https://finance.naver.com/"
  res=req.urlopen(url).read().decode('cp949')
  # utf-8 : 한글 깨짐, unicode_escape : 한글 깨짐
  soup=BeautifulSoup(res,"html.parser")
  
  # print(soup)
  
  top4=soup.select("tbody#_topItems1 > tr")
  
  i=1
  for e in top4:
      if e.find("a") is not None:
          print(i,e.select_one("a").string)
          i+=1
  ```

  

- 인프런 추천 강좌 10개 가져오기

  ```python
  인프런 추천강좌 Top10 가져오기
  현재 홈페이지 변경되어 이 방식으로 가져와지지 않음.
  
  base="https://www.inflearn.com/"
  quote=rep.quote_plus("추천-강좌")
  print(quote)
  
  url=base+quote
  res=req.urlopen(url).read()
  soup=BeautifulSoup(res,"html.parser")
  
  recommend=soup.select("ul.slides")[0]
  
  for i,e in enumerate(recommend,1):
      print(i,e.select_one("h4.block_title>a"))
  ```

  