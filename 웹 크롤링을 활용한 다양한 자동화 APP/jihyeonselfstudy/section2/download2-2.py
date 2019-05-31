print('hi')
print('한글') #실행 => 한글은 깨져서 나옴

import sys
import io
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print('한글')
print('하이')
print('yo')

imgUrl = "http://blogfiles.naver.net/20120717_72/sunjahwang_1342512929146R1wSv_JPEG/%B5%BF%B9%B00_%28411%29.jpg"
