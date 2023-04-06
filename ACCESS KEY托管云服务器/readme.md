## 0x00 漏洞背景

        之前渗透碰见一次小程序泄露ACCESS KEY，所以想把相关知识总结一遍。
## 0x01 泄露途径

        1.小程序反编译后一般有个config.js里会泄露ACCESS KEY
        
        
   
   ![图片](https://user-images.githubusercontent.com/118274389/230257864-04b739f0-1a64-403b-9416-961799278efa.png)


        2.有些网站的JS文件也会泄露相关的key
        
        3.有些开发人员把源码放到git上不小心把key放上去了也会泄露
        
        4.网站的备份文件或者报错信息也会泄露
        
          fofa搜索：ErrorException
## 0x02 利用

       可以找几个工具进行接管
       
       https://github.com/mrknow001/aliyun-accesskey-Tools
       
       行云管家导入云主机，网站地址：https://yun.cloudbility.com/
       
       OSS接管：https://promotion.aliyun.com/ntms/ossedu6.html
