import requests
import re
from lxml import html
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
print "Enter the website adress/IP(Without http/s begining"
web = raw_input()
data = {'server': web}
with requests.Session() as s:
    url = 'http://browserspy.dk/webserver.php'
    r = s.get(url, headers = headers)
    r = s.post(url, data = data, headers = headers)

tree = html.fromstring(r.content)
webserver = tree.xpath('//td[@class="value"]/text()')
webserver = webserver[0]

if("Specified web server <" in webserver or 'Unknown' in webserver):
    print "Invalid adress/ web server is Unknown"
else:
    print ("The Web Server of the Website is: " + webserver)
    print ("The info was collected from http://browserspy.dk")
print ("See ya")





