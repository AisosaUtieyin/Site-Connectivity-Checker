import urllib
from urllib . request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def is_connected(site):
    try:
         urlopen(site,timeout=1)
         return True
    except urllib.error.URLError as Error:
        print(Error)
        return False



urlSite= input('Enter http')


if is_connected(urlSite):
    print('Internet is active')
else:
    print('Internet is disconected')
