# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3




# A demo pipeline which can create a table and store data in it
# class QuotetPipeline:
    
#     def __init__(self):
#         self.create_connection()
#         self.create_table()

#     def process_item(self, item, spider):
#         self.store_db(item)
#         return item

#     def create_connection(self):
#         self.conn = sqlite3.connect("myqutes.db")
#         self.curr = self.conn.cursor()

#     def create_table(self):
#         self.curr.execute("""
#                           DROP TABLE IF EXISTS qutes
#                           """)

#         self.curr.execute("""
#                           CREATE TABLE qutes(
#                               title text,
#                               author text,
#                               tag text)
#                           """)

#     def store_db(self,item):
#         self.curr.execute("""
#                     INSERT INTO qutes VALUES(?,?,?)""",(item['title'][0],
#                                                        item['author'][0],
#                                                         ",".join(item['tag']))
#                     )
#         self.conn.commit()