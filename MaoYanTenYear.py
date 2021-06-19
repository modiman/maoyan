import requests
from pandas._libs import json
from main.csv_process import write_list
url = 'https://piaofang.maoyan.com/mdb/rank'
selectStr = '#app > div > div.home-content > div > div.rank-list > div.tiny-table.tiny-table-no-border.tiny-table-middle > div > table > tbody > tr'
##app > div > div.home-content > div > div.rank-list > div.tiny-table.tiny-table-no-border.tiny-table-middle > div > table > tbody > tr> td > div > div > div
html = requests.get(url='https://piaofang.maoyan.com/mdb/rank/query?type=0&id=2016', headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'})
url_time = 'https://piaofang.maoyan.com/mdb/rank/query?type=0&id=20'
url_list = []

for i in range(1,12):
    url_list.append(url_time+str(22-i))
for u in url_list:
    html = requests.get(url=u, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'})

    js = json.loads(html.text)
    ans = []
    index = 1
    for i in js['data']['list']:
        info = []
        info.append(str(index))
        index+=1
        info.append(i['movieId'])
        info.append(i['movieName'])
        info.append(i['releaseInfo'])
        info.append(i['boxDesc'])
        info.append(i['avgViewBoxDesc'])
        info.append(i['avgShowViewDesc'])
        ans.append(info)
        print(info)

    write_list('idandname.csv',ans)
