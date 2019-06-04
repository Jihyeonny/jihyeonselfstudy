print('hi')
print('한글') #실행 => 한글은 깨져서 나옴

import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print('한글')
print('하이')
print('yo')

imgUrl = "http://blogfiles.naver.net/20120717_72/sunjahwang_1342512929146R1wSv_JPEG/%B5%BF%B9%B00_%28411%29.jpg"
htmlURL = "http://google.com"

savePath1 = "C:/Users/student/selfstudy/웹 크롤링을 활용한 다양한 자동화 APP/jihyeonselfstudy/section2/test1.jpg"
savePath2 = "C:/Users/student/selfstudy/웹 크롤링을 활용한 다양한 자동화 APP/jihyeonselfstudy/section2/index.html"

dw.urlretrieve(imgUrl, savePath1) # savePath 경로에 따라 이미지 저장
dw.urlretrieve(htmlURL, savePath2)
print("다운로드 완료!")
