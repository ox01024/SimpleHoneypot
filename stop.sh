ps -ef |grep fapro  |awk '{print $2}'|xargs kill -9
ps -ef |grep main.py |awk '{print $2}'|xargs kill -9
echo "已停止运行"