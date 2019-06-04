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
