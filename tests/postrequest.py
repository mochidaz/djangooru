import requests
from requests.auth import HTTPBasicAuth

url = 'http://localhost:8000/api/posts/'
myobj = {"tags":["touhou","mystia_lorelei","touhou_project"], "artist":"-", "source":"https://danbooru.donmai.us"} 

x = requests.post(url, json = myobj, files={"image":"/home/rahman/Pictures/Test/__mystia_lorelei_touhou_drawn_by_rin_falcon__sample-32465035f10c5389d9baf866b3141b99.jpg"}, auth=HTTPBasicAuth('rahman','AlMulk78'))

print(x.json())
