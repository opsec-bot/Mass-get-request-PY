import random
import threading
import colorama
import requests


# Proxy format is http://NAME:PASS@IP:PORT
__PROXIES = [
    "PROXIES", 
]
__SITE = "SITE" # Must have https before site domain (example: https://google.com/ )

__ITER = 1000
def get(site: str):
    proxy = random.choice(__PROXIES)
    r = requests.get(site, proxies={"http": proxy, "https": proxy})

    if r.status_code == 200:
        print(f"{colorama.Fore.GREEN}[+] {site} [{r.status_code}]")
    else:
        print(f"{colorama.Fore.RED}[-] {site} [{r.status_code}]")

def main():
    colorama.init()

    threads = []
    for _ in range(__ITER):
        t = threading.Thread(target=get, args=(__SITE,))
        threads.append(t)
        t.start()
        
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()