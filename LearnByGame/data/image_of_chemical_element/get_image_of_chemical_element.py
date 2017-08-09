#coding = utf-8
import re
import urllib.request

url_home = 'http://images-of-elements.com/'
url_s = 'http://images-of-elements.com/s/'
php =[]
urls = []
urlh = []
for u in range(121):
    urlh.append(url_home)
    urls.append(url_s)
    php.append('.php')

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getName(html):
    reg = r'title="(.+?)" class='
    elename = re.compile(reg)
    html = html.decode('utf-8')
    namelist = re.findall(reg,html)
    return namelist

def getImage(html):
    reg = r'src="s/(.+?\.jpg)"'
    imgre = re.compile(reg)
    html = html.decode('utf-8')
    imglist = re.findall(imgre,html)
    x = 0
    for postfix in imglist:
        post = urls[x] + postfix
        x+=1
        reponse = getHtml(post)
        with open(postfix,'wb') as f:
            f.write(reponse)
            


html = getHtml(url_home)

for u in range(121):
    print(u)
    if u == 0:
        urlh[u] = urlh[u] + 'hydrogen' + php[u]
    else:
        urlh[u] = urlh[u] + getName(html)[u].lower() + php[u]
    html = getHtml(urlh[u])
   


