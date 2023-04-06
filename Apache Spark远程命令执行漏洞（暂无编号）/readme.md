## 0x00 漏洞背景

        之前渗透时候发现了这个界面复现一下。
        
        Apache Spark存在一处命令注入，该漏洞是由于Apache Spark UI提供了通过配置选项spark.acls.enable启用ACL的可能性，
        HttpSecurityFilter中的代码路径可以通过提供任意用户名来允许某人执行模拟，恶意用户凭借访问权限检查函数最终将基于其输入构建Unix shell命令并执行它。
        
        
![图片](https://user-images.githubusercontent.com/118274389/230276100-cd56142e-4427-4da9-b425-fe1711cded27.png)

## 0x01 漏洞影响范围

       versions 3.0.3
       3.1.1 -- 3.1.2
       3.2.0 -- 3.2.1
       
       
        
