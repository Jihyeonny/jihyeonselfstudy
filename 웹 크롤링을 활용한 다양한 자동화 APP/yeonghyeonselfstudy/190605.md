### 190605

# BeautifulSoup을 활용한 웹 파싱 실습

###### 실습: 다음 실시간 인기 검색어 + link 스크랩핑 해보기

```python
# 다음 실시간 이슈 검색어 Top10가져오기
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

url="https://www.daum.net/"
res=req.urlopen(url).read()
soup=BeautifulSoup(res,"html.parser")
# print(soup.prettify())

top10=soup.select("div.realtime_part>ol.list_hotissue>li>div>div:nth-of-type(1)>span.txt_issue>a")
for i,e in enumerate(top10,1):
    print(i,e.string,e["href"])
```



- **3Vs**

  Volume: 데이터의 양

  Variety: 데이터의 다양성

  Velocity: 데이터의 속도

- 네이버에서 원하는 사진 한 번에 다운로드 받기

  ```python
  from bs4 import BeautifulSoup
  import urllib.request as req
  import urllib.parse as rep
  import sys
  import io
  import os
  
  sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
  sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')
  
  base="https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
  quote=rep.quote_plus("박보영")
  url=base+quote
  print(url)
  
  res=req.urlopen(url)
  savePath="C:\\imagedown\\" # c:\imagedown\
  
  try:
      if not (os.path.isdir(savePath)):
          os.makedirs(os.path.join(savePath))
  # 권한이 없어서 폴더 만드는 것 실패한 경우
  except OSError as e:
      if e.errno != errno.EEXIST:
          print("폴더 만들기 실패!")
          raise #에러 강제로 실행 시킴
  
  soup=BeautifulSoup(res,"html.parser")
  
  img_list=soup.select("div.img_area._item >a.thumb._thumb>img")
  
  for i,img_list in enumerate(img_list,1):
      # print(img_list['data-source'])
      fullFileName=os.path.join(savePath,savePath+str(i)+'.jpg')
      # 폴더에 저장될 이름
      req.urlretrieve(img_list['data-source'],fullFileName)
  
  print("다운로드 완료")
  ```

  

  - 브라우저를 이용해서 접속한 경우, user-agent 값이 브라우저로 request로 날아감.

    네이버에서 이 값을 보고 response를 해줄 때(브라우저에서 최종적으로 rendering될 때), jquery라던지 그 프레임워크에 따라 화면이 만들어짐.

    but, 실습 시, 브라우저를 사용한 것이 아니라 http 통신으로 값을 날렸기 때문에 태그 요소와 브라우저에서 보는 것이 다를 수 있다.

    src값이 아니라 data-source값이 이미지 소스 값이 들어 있음!

    

- 인프런 추천 강좌 이미지 한 번에 다운로드 & 제목 텍스트파일 출력하기

  ##### 홈페이지 변경으로 오류나는 코드입니다.

  ```python
  from bs4 import BeautifulSoup
  import urllib.request as req
  import urllib.parse as rep
  import sys
  import io
  import os
  
  sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
  sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')
  
  base="https://www.inflearn.com/"
  quote=rep.quote_plus("")
  url=base+quote
  print(url)
  
  res=req.urlopen(url)
  savePath="C:\\imagedown\\" # c:\imagedown\
  
  try:
      if not (os.path.isdir(savePath)):
          os.makedirs(os.path.join(savePath))
  # 권한이 없어서 폴더 만드는 것 실패한 경우
  except OSError as e:
      if e.errno != errno.EEXIST:
          print("폴더 만들기 실패!")
          raise #에러 강제로 실행 시킴
  
  soup=BeautifulSoup(res,"html.parser")
  
  img_list=soup.select("ul.slides")[0]
  
  for i,img_list in enumerate(img_list,1):
      with open(savePath+"text_"+str(i)+".txt","wt") as f:
      # wt:text형태로 write하겠다.
          f.write(e.select_one("h4.block_title>a").string)
      fullFileName=os.path.join(savePath,savePath+str(i)+'.png')
      # .png, .jpg 상관 없음.
      req.urlretrieve(e.select_one("div.block_media>a>img")['src'],fullFileName)
  
  print("다운로드 완료")
  ```

  