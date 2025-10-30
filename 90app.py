import requests,os;

import datetime

from time import sleep;

from datetime import timedelta

os.system('clear')

#aut=input('Author: ')

aut='Bearer 297f224d-c411-4231-9e9c-396762d5ed90'

#login

def info():

 js={
  "pageSize": 20,
  "pageNo": 1,
  "guaranteed": -1,
  "leagueHot": "",
  "searchBeginTime": "2025-10-30 16:00:00",
  "searchEndTime": "2025-10-30 20:00:59",
  "leagueId": []
}

 headersinfo={
  "DevicePlatform": "3",
  "Authorization": aut,
  "X-Requested-With": "XMLHttpRequest",
  "appver": "2.4.0",
  "lang": "vi_VN",
  "user-agent": "Mozilla/5.0 (Linux; Android 12; A202SH Build/SC263; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/141.0.7390.122 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/30.0)",
  "Content-Type": "application/json",
  "Content-Length": "149",
  "Host": "90trade.app",
  "Connection": "Keep-Alive",
  "Accept-Encoding": "gzip",
  "Cookie": "heauacea=4cd28f4ded8d72f91d3cd0acb3b73740"
}

 return requests.post('https://90trade.app/soccer/game/page',headers=headersinfo,json=js)





log=info()

for records in log.json()['data']['records']:

    print(f"{records['homeTeam']} vs {records['awayTeam']} - {records['date']} ID: {records['gameId']}")

    print('  ')
    
def balance():
  jsbl={}
  hdbl={
  "DevicePlatform": "3",
  "Authorization":aut,
  "X-Requested-With": "XMLHttpRequest",
  "appver": "2.4.0",
  "lang": "vi_VN",
  "user-agent": "Mozilla/5.0 (Linux; Android 12; A202SH Build/SC263; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/141.0.7390.122 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/30.0)",
  "Host": "90trade.app",
  "Connection": "Keep-Alive",
  "Accept-Encoding": "gzip",
  "Cookie": "heauacea=4cd28f4ded8d72f91d3cd0acb3b73740"
}
  return requests.get('https://90trade.app/soccer/member/credit',json=jsbl,headers=hdbl)

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
  "DevicePlatform": "3",
  "Authorization": aut,
  "X-Requested-With": "XMLHttpRequest",
  "appver": "2.4.0",
  "lang": "vi_VN",
  "user-agent": "Mozilla/5.0 (Linux; Android 12; A202SH Build/SC263; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/141.0.7390.122 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/30.0)",
  "Content-Type": "application/json",
  "Content-Length": "112",
  "Host": "90trade.app",
  "Connection": "Keep-Alive",
  "Accept-Encoding": "gzip",
  "Cookie": "heauacea=4cd28f4ded8d72f91d3cd0acb3b73740"
}

 return requests.post('https://90trade.app/soccer/game/stake/create',headers=hdst,json=jsst)





st=stake()

print(st.status_code)

#print(st.headers)

print(st.text[:300])

print(st.json()['message'])

while (st.json()['success']==0):

  st=stake()

  print(st.json()['message'])


  sleep(1.5)
