# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class TutorialPipeline(object):
    def process_item(self, item, spider):
        self.insertDB(item)
        return item
    def insertDB(self,item):
        conn=MySQLdb.connect(host='localhost',user='root',passwd='lizuan..7456',db='test', charset="utf8")
        cur=conn.cursor()
        sql="insert into movie (id,name)values(%s,'%s')" %(item['id'],item['name'])
        cur.execute(sql)
        cur.close()
        conn.commit()
        conn.close()