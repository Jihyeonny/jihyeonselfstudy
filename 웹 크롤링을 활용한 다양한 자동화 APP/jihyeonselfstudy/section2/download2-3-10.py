import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://edu.ssafy.com/"

mem = req.urlopen(url) #url정보 할당됨

# print(type(mem))
# print(type({})) #dict
# print(type([])) #list
# print(type(())) #tuple

# print("geturl", mem.geturl())
# print("status", mem.status) #정상: 200, 요청페이지없음: 404, 내부망이나 외부에서 접속안됨(거절): 403, 서버자체에러: 500
# print("headers", mem.getheaders())
# print("info", mem.info())
# pirnt("code", mem.getcode())
# print("read", mem.read().decode("utf-8")) #():전체를 가져옴 (50): 정해진 만큼 가져옴 (decode권장)

print(urlparse("https://edu.ssafy.com?test=test"))
