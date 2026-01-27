import requests,os;

import datetime

from time import sleep;

from datetime import datetime, timedelta, timezone

os.system('clear')

#aut=input('Author: ')

aut='Bearer f5e431f5-4b88-49ef-b51f-b06c389251d9'
# tạo múi giờ Việt Nam 
vietnam_tz = timezone(timedelta(hours=7)) 
now_vn = datetime.now(vietnam_tz)

# định dạng yyyy-mm-dd 
today = now_vn.strftime("%Y-%m-%d")

def info():

# tự động lấy ngày hiện tại

 begin_dt = now_vn.replace(hour=17, minute=0, second=0, microsecond=0)

 end_dt   = now_vn.replace(hour=22, minute=30, second=0, microsecond=0)



 js = {

    "pageSize": 20,

    "pageNo": 1,

    "guaranteed": -1,

    "leagueHot": "",

    "searchBeginTime": begin_dt.strftime("%Y-%m-%d %H:%M:%S"),

    "searchEndTime":   end_dt.strftime("%Y-%m-%d %H:%M:%S"),

    "leagueId": []

}


 headersinfo={

  "method": "POST",

  "authority": "90trades.com",

  "path": "/soccer/game/page",

  "scheme": "https",

  "content-length": "149",

  "sec-ch-ua-platform": "\"Android\"",

  "authorization": aut,

  "lang": "vi_VN",

  "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",

  "deviceplatform": "2",

  "sec-ch-ua-mobile": "?1",

  "appver": "1.23.60255",

  "x-requested-with": "XMLHttpRequest",

  "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",

  "accept": "application/json, text/plain, */*",

  "origin": "https://90trades.com",

  "referer": "https://90trades.com/",

  "sec-fetch-site": "same-origin",

  "sec-fetch-mode": "cors",

  "sec-fetch-dest": "empty",

  "referer": "https://90trades.com/",

  "accept-encoding": "gzip, deflate, br, zstd",

  "accept-language": "vi-VN,vi;q=0.9,id-ID;q=0.8,id;q=0.7,my-MM;q=0.6,my;q=0.5,en-GB;q=0.4,en;q=0.3,fr-FR;q=0.2,fr;q=0.1,en-US;q=0.1",

  "cookie": "heauacea=d7cb1422da0f88319019df84c25b16f5",

  "priority": "u=1, i"

}

 return requests.post('https://90trades.com/soccer/game/page',headers=headersinfo,json=js)



kA=input('0 to keep alive: ')

log=info()

for records in log.json()['data']['records']:

    print(f"{records['homeTeam']} vs {records['awayTeam']} - {records['date']} ID: {records['gameId']}")

    print('  ')
def balance():
  jsbl={}
  hdbl={
  "method": "GET",
  "authority": "90trades.com",
  "path": "/soccer/member/credit",
  "scheme": "https",
  "sec-ch-ua-platform": "\"Android\"",
  "authorization": aut,
  "lang": "vi_VN",
  "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
  "deviceplatform": "2",
  "sec-ch-ua-mobile": "?1",
  "appver": "1.23.35821",
  "x-requested-with": "XMLHttpRequest",
  "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36",
  "accept": "*/*",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://90trades.com/",
  "accept-encoding": "gzip, deflate, br, zstd",
  "accept-language": "vi-VN,vi;q=0.9,id-ID;q=0.8,id;q=0.7,my-MM;q=0.6,my;q=0.5,en-GB;q=0.4,en;q=0.3,fr-FR;q=0.2,fr;q=0.1,en-US;q=0.1",
  "cookie": "heauacea=e47b1922e5f8d721905ecc2683b63cfa",
  "priority": "u=1, i"
  }
  return requests.get('https://90trades.com/soccer/member/credit',json=jsbl,headers=hdbl)

print('So du: ',balance().json()['data']['balance'])
gameId=input('gameId: ')

money=input('Money: ')



def stake():

 jsst={

  "betType": 1,

  "gameId": gameId,

  "item1": 4,

  "item2": 4,

  "odds": 0.005,

  "gameType": 1,

  "walletType": "CASH",

  "stake": money

}

 hdst={

  "method": "POST",

  "authority": "90trades.com",

  "path": "/soccer/game/stake/create",

  "scheme": "https",

  "content-length": "149",

  "sec-ch-ua-platform": "\"Android\"",

  "authorization": aut,

  "lang": "vi_VN",

  "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",

  "deviceplatform": "2",

  "sec-ch-ua-mobile": "?1",

  "appver": "1.23.35821",

  "x-requested-with": "XMLHttpRequest",

  "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36",

  "content-type": "application/json",

  "accept": "application/json",

  "origin": "https://90trades.com",

  "sec-fetch-site": "same-origin",

  "sec-fetch-mode": "cors",

  "sec-fetch-dest": "empty",

  "referer": "https://90trades.com/",

  "accept-encoding": "identity",

  "accept-language": "vi-VN,vi;q=0.9,id-ID;q=0.8,id;q=0.7,my-MM;q=0.6,my;q=0.5,en-GB;q=0.4,en;q=0.3,fr-FR;q=0.2,fr;q=0.1,en-US;q=0.1",

  "cookie": "heauacea=d7cb1422da0f88319019df84c25b16f5",

  "priority": "u=1, i"

}

 return requests.post('https://90trades.com//soccer/game/stake/create',headers=hdst,json=jsst)


st=stake()

print(st.status_code)

#print(st.headers)

print(st.text[:300])

print(st.json()['message'])

while (st.json()['success']==0):

  st=stake()

  print(st.json()['message'])

  if (kA=='0'): 
   for i in range(3000,0,-1):
     print('keeping alive: ',i,end=' \r');
     i=i+1;
     sleep(1);
  else:
   sleep(1.5)




























































































































