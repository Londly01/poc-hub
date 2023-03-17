
##  0x00 原理介绍
     
         去年有个项目，有WAF，然后进行了绕过，成功反弹，现在在回忆记录一下。
     
     log4j2输出日志的时候除了常见的变量替换，还支持远程获取相应的内容，获取远程内容是通过lookup功能提供，
     
     ## 变量替换如下
     
     logger.info("user name: {}, alias name: {}", userName, aliasName)
     
     获取远程内容支持jndi
