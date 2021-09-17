import requests
import json
import time

def push(data):
  headers = {"Content-Type":"application/json"}
  url = '钉钉webhook地址'
  r=requests.post(url, data=json.dumps(data), headers=headers).text
  r=json.loads(r)
  if r['errcode']==0:
    print('INFO[6666] [WEBHOOK] 推送成功.   ')
  if 'status' in r.keys():
    time.sleep(60)
    push(data)
  print('ERRO[9999] [WEBHOOK] 推送失败'+str(r))
