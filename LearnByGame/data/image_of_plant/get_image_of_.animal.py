#coding = utf-8
import urllib.request
import re

url_content = 'http://images-of-elements.com/'
url_s = 'http://images-of-elements.com/s/'
url = []
for i in range(103):
    url.append(url_content)


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImage(html):
    global url
    reg_url = r'href="(.+?)\.php">'
    imgre_url = re.compile(reg_url)
    html = html.decode('utf-8')
    imglist = re.findall(imgre_url,html)
    #return imglist
    x = 0
    for imglist[x] in imglist:
        url[x] = url[x] + imglist[x] + r'.php'
        x += 1
    return url
        #urllib.urlretrieve(imgurl)

html = getHtml(url[0])
url = getImage(html)
number = 0
for u in url:
    reg_img = r'src="s/(.+?\.jpg)"'
    html =getHtml(u)
    imgre = re.compile(reg_img)
    html = html.decode('utf-8')
    imglist = re.findall(imgre,html)
    print(number)
    print(imglist)
    count = 0
    for img in imglist:
        _img = url_s + img
        response = urllib.request.urlopen(_img)
        response_img = response.read()
        with open(img,'wb') as f:
            f.write(response_img)
        print(count)
        count+=1
    number+=1

   
    
    













