# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
from scrapy.pipelines.files import FilesPipeline



# A demo pipeline which can create a table and store data in it
class LinkPipeLine:
    
    def __init__(self):
        self.create_connection()
        self.create_table()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def create_connection(self):
        self.conn = sqlite3.connect("myspiderstore.sqlite3")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""
                          DROP TABLE IF EXISTS linkT
                          """)

        self.curr.execute("""
                          CREATE TABLE linkT(
                              link text 
                              );
                          """)

        # self.curr.execute("""
        #                   CREATE TABLE linkT(
        #                       link text NOT NULL,
        #                       UNIQUE (link)
        #                       )
        #                   """)
    def store_db(self,item):
        print("-----------------------------------------------------------------")
        print(f"item: {item}")
        # print(f"item[0]: {item[0]}")
        # print(f"item.link: {item.link}")
        # print(f"item[0].link: {item[0].link}")
        # print(f"item.link[0]: {item.link[0]}")
        print("-----------------------------------------------------------------")
        for link in item['link']:
            self.curr.execute("""
                    INSERT INTO linkT VALUES(?)""",(link,))
        self.conn.commit()
        


class FiledownloadPipeline(FilesPipeline):
    
    def file_path(self, request, response=None, info=None):
        
        file_name: str = request.url.split("/")[-1]
        return file_name
