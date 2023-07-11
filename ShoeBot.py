from bs4 import BeautifulSoup
import urllib
import requests
from requests_html import HTMLSession


session = HTMLSession()

#results = session.get("https://www.nike.com/")
results = session.get("https://accounts.nike.com/lookup?client_id=4fd2d5e7db76e0f85a6bb56721bd51df&redirect_uri=https://www.nike.com/auth/login&response_type=code&scope=openid%20nike.digital%20profile%20email%20phone%20flow%20country&state=e6494308368a42319f3e7a3e06264111&code_challenge=kqT7PsWQ3DctWwhPbM3EESS2aiO3PCLgR8gj2sND6qI&code_challenge_method=S256")

print(results.html.links)
print(results.html.absolute_links)


'''''
longUrl = "https://accounts.nike.com/lookup?client_id=4fd2d5e7db76e0f85a6bb56721bd51df&redirect_uri=https://www.nike.com/auth/login&response_type=code&scope=openid%20nike.digital%20profile%20email%20phone%20flow%20country&state=48ab1a5be76e4dfe8c9884a893273653&code_challenge=-I2OPvteh9m8_rXcE_k8gL0KusOObTvBmVNUa4SJPhE&code_challenge_method=S256"
url = "https://www.nike.com/"
page = requests.get(url)

print(page.text)


loginUsername = ""
loginPassword = ""

post_params = {
    username : loginUsername,
    password : loginPassword,
        }
post_args = urllib.urlencode(post_params)

url = 'https://www.nike.com/'
fp = urllib.urlopen(url, post_args)
soup = BeautifulSoup(fp)
'''''