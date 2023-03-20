## 0x00 背景

  最近打的几个项目，各种WAF拦截，也进行相应的绕过，基本都是http请求包进行展开，总结一些实用的绕过方式。
  
## 0x01 方法1

  添加大量的//////////////进行绕过，图片来自ABC123师傅
  
  ![图片](https://user-images.githubusercontent.com/118274389/226229355-277c9279-c324-4a8f-8f93-6cd581bbfa59.png)

## 0x02 方法2

   get请求改成其他请求方式，例如post 
   
## 0x03 方法3

   添加无用的GET请求方式
   
   添加username=xxxxx或者password=sdfewfwfeewffew等等   图片来自ABC123师傅
   
   ![图片](https://user-images.githubusercontent.com/118274389/226229693-9807197b-cec4-4579-8572-a9003e9705ef.png)
## 0x04 方法4

    为了进一步绕过waf，我们还可以对URL路径进行URL编码混淆掺杂，这里不要将整个url路径全部用URL编码，一小段一小段地进行URL编码绕waf效果更好。
   
 ![图片](https://user-images.githubusercontent.com/118274389/226230399-4b019d4e-f836-465b-8146-8101c5b5341f.png)

    
## 0x05 方法5

    我们也可以在请求数据包中添加脏数据，可以在<wsa:RelatesTo>标签中间添加脏数据，由于是POST请求数据包，这里面可以添加很长很长的脏数据， 图片来自ABC123师傅
    

![图片](https://user-images.githubusercontent.com/118274389/226230309-12b235f2-73c2-47fe-9b24-5cc90c83e128.png)


## 0x06 方法6
    
    分块传输
    
