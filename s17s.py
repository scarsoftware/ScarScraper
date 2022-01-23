import requests
from colorama import init, Fore, Back, Style
import os
init(convert=True, autoreset=True)
log_html = "false"
from bs4 import BeautifulSoup
os.system("cls")
print("""
                    _ _____
 ___  ___ __ _ _ __/ |___  |__  ___ _ __ __ _ _ __   ___ _ __
/ __|/ __/ _` | '__| |  / / __|/ __| '__/ _` | '_ \\ / _ \\ '__|
\\__ \\ (_| (_| | |  | | / /\\__ \\ (__| | | (_| | |_) |  __/ |
|___/\\___\\__,_|_|  |_|/_/ |___/\\___|_|  \\__,_| .__/ \\___|_|
                                             |_|
""")
username = input("Enter username.\n")
agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
def check(name, url):
    request = requests.get('{0}'.format(url)+username)
    html = str(BeautifulSoup(request.text, 'lxml'))
    result = str(request.status_code)
    if result == "200":
        if name == "Github":
            status[0] = "account detected."
            update()
        if name == "Ask.FM":
            status[1] = "account detected."
            update()
        if name == "Instagram":
            status[2] = "account detected."
            update()
        result = Fore.GREEN+"account detected."
    if result == "404":
        result = Fore.RED+"account not detected."
    if result == "410":
        result = Fore.YELLOW+"account deleted."
    print("{0} | {1}{2} | {3}".format(name, url, username, result))
    if log_html == "true":
        with open(name+".html", "w", encoding="utf-8") as html_file:
            html_file.write(str(html))

check("Github", "https://github.com/")
check("Ask.FM", "https://ask.fm/")
check("Instagram", "https://instagram.com/")
check("Facebook", "https://facebook.com/")
check("Repl.it", "https://replit.com/@")
check("Pastebin", "https://pastebin.com/u/")
check("YouTube", "https://www.youtube.com/user/")
