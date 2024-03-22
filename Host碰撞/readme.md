## 0x00 原理


      正常访问一个网站的流程是： 用户通过浏览器访问一个域名 ->
      先在本地hosts文件中查询域名对应的IP，没查到的话再通过DNS查询域名对应的IP
      -> 访问查询到的IP并以最初访问的域名作为请求头中host字段的值 -> 
      反代服务器nginx根据host字段的值转发到对应的server_name下，
      漏洞就出现在，当目标单位删除了DNS中host对应的IP，但是没有删除反代服务
      器中host对应的server，此时我们访问反代服务器的IP且host头中带有对应域名，若域名匹配反代服务器的server，则能够访问到内网业务
## 测试

// 拿来做碰撞的 ip
域名: https://sso.testmiao.com 解析的 ip: 42.xxx.xxx.xxx


// 拿来做碰撞的 host
域名: vms.testmiao.com 解析的 ip: 10.xxx.xxx.xxx
域名: a.testmiao.com 解析的 ip: 无法解析(猜的内网可能有这个域名)
域名: b.testmiao.com 解析的 ip: 无法解析(猜的内网可能有这个域名)
域名: c.testmiao.com 解析的 ip: 无法解析(猜的内网可能有这个域名)
域名: d.testmiao.com 解析的 ip: 无法解析(猜的内网可能有这个域名)
域名: scm.testmiao.com 解析的 ip: 118.xx.xxx.xxx下载地址: https://github.com/pmiaowu/HostCollision

下载测试工具：https://github.com/pmiaowu/HostCollision

第一步: 
    打开 HostCollision/dataSource 目录
    将: ipList.txt 与 hostList.txt 分别填写进对应的数据(一行一个)
第二步:
    打开 HostCollision 目录
    执行命令: java -jar HostCollision.jar
    执行完毕以后会在根目录生成一个 年-月-日_8 位随机数 csv/txt 文件
    里面会保存碰撞成功的结果
    
