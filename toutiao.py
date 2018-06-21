#coding =utf -8
import requests
import json
import pymysql

"""动态页面网站"""
#连接pymql
conn = pymysql.connect(host='localhost',port = 3307, user = 'root' ,password = 'usbw',db = 'toutiao' ,charset = 'utf8')
cursor = conn.cursor()

url = 'https://www.toutiao.com/api/pc/realtime_news/'
webdata = requests.get(url).text

data = json.loads(webdata)
realtime_news = data['data']

for n in realtime_news:
    title = n['title']
    img_url = 'http://www.'+ n['image_url']
    url = n ['open_url']
    print(url,title,img_url)
    cursor.execute("INSERT INTO data3(title,img_url,url)VALUES('{0}','{1}','{2}');".format(title,img_url,url))
    conn.commit()
cursor.close()
conn.close()