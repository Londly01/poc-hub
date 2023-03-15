## 参考二篇文章
1.https://gv7.me/articles/2021/java-deserialized-data-bypasses-waf-through-sleep-chunked/

2.https://www.anquanke.com/post/id/169738


## 自测有些坑

    只有HTTP/1.1支持分块传输
    POST包都支持分块，不局限仅仅于反序列化和上传包
    Transfer-Encoding: chunked大小写不敏感

