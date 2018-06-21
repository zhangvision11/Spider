#coding = utf -8
import requests
from bs4 import BeautifulSoup
import re
from multiprocessing import Pool
def get_zhaopin(page):
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%85%A8%E5%9B%BD&kw=python&sm=0&p=1'.format(page)
    print('第{0}页'.format(page))
    webdata = requests.get(url).content
    soup = BeautifulSoup(webdata,'lxml')
    job_name = soup.select('.zwmc > div > a')
    salarys = soup.select('td.zwyx')
    locations = soup.select('td.gzdd')
    times = soup.select(' td.gxsj > span')
    for name,salary,location,time in zip(job_name,salarys,locations,times):
        data = {
            'name': name.get_text(),
            'salary':salary.get_text(),
            'location':location.get_text(),
            'time':time .get_text()
        }
        print(data)
if __name__ == '__main__':
    pool = Pool(processes = 2)
    pool.map_async(get_zhaopin, range(1,5))
    pool.close()
    pool.join()