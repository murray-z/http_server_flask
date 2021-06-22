# 概述
> 采用flask部署http服务。

# 2种启动
1. python server.py
2. gunicorn -b 0.0.0.0:7777 -k gevent -w 3 server:app -t 120

# 测试服务
- python client.py
