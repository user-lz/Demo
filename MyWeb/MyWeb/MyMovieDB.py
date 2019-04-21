import requests
from lxml import etree
import MySQLdb

conn=MySQLdb.connect(host='localhost',user='root',passwd='lizuan..7456',db='test',charset="utf8")
cur=conn.cursor()

def get_page(start_num):
    url="https://movie.douban.com/top250?start=%s&filter=" %start_num
    res=requests.get(url)
    tree=etree.HTML(res.text)
    title=tree.xpath('//span[@class="title"][1]/text()')

    return title

result=[]

def get_all_page(start,end):
    result=[]
    for i in range(start,end-start):
        title_list=get_page(i*25)
        result+=title_list
        

    return result

if __name__=="__main__":
    result=get_all_page(0,10)
    for i in range(0,250):
        cur.execute("insert into testmodel_test(movie_id,movie_name) values(%s,%s)",(i+1,result[i]))
    cur.close()
    conn.commit()
    conn.close() 

