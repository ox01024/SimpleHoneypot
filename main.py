import json
import subprocess
import os
from lib.webhook import push

os.system("nohup ./fapro run -v > logs/fapro.log 2>&1 &")
cmd=["tail","-F","logs/fapro.log"]
pope=subprocess.Popen(cmd,stdout = subprocess.PIPE)


# 日志解析
def log_dt(log):
    try:
        log=json.loads(log)
        protocol=log["protocol"]
        remote_ip=log["remote_ip"]
        time=log['time']
        data='# 捕获到攻击行为'+'\n'
        data+='## 协议:'+protocol+'\n'
        data+="### 攻击ip:"+remote_ip+'\n'
        if protocol=='HTTP':
            uri=log['uri']
            data+="### path:"+uri+'\n'
        data += '#### time:' + time + '\n'
        log_data={
            "msgtype":"markdown",
            "markdown":{
                "title": "捕获到攻击行为",
                "text":data
            }
        }
        return log_data
    except:
        log_data={
            "msgtype": "text",
            "text": {
                "content":log}
        }
        print(log_data)
        return log_data




while True:
    log=pope.stdout.readline()[:-1].decode()
    if len(log)>0:
        print(log)
        data=log_dt(log)
        push(data)

