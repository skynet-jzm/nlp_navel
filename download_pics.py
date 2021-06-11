import requests
import re

url = 'http://www.nipic.com/photo/jingguan/ziran/index.html'
response = requests.get(url).text
# print(response)
img = re.compile('data-src="(.*?).jpg"')
imgs = re.findall(img,response)

i = 1
for imgurl in imgs:
    i +=1
    image= requests.get(imgurl).content
    print(str(i)+ '.jpg 正在保存...')
    with open('./img/' + str(i)+'.jpg', 'wb')as fp:
        fp.write(image)
