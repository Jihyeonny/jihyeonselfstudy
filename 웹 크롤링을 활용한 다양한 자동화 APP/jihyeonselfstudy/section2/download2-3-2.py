import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

API = "https://api6.ipify.org"

values = {
    'format': 'json'
}
print("before", values) # =>{'format': 'json'}
params = urlencode(values) # 동적활용 위해
print("after", params) # =>format=json

url = API + "?" + params
print("요청 url", url)

reqData = req.urlopen(url).read().decode('utf-8')
print("출력", reqData) # =>{"ip":"14.46.141.54"}
