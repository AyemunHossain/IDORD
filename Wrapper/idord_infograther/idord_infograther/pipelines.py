from itemadapter import ItemAdapter
import sqlite3
from scrapy.pipelines.files import FilesPipeline


# A demo pipeline which can create a table and store data in it
class LinkPipeLine:
    
    def process_item(self, item, spider):
        model_class = getattr(item, 'django_model')
        for link in item['link']:
            obj = model_class.objects.create(link=link)
            obj.save()
        return item

#     def __init__(self):
#         self.create_connection()
#         self.create_table()

#     def process_item(self, item, spider):
#         self.store_db(item)
#         return item

#     def create_connection(self):
#         self.conn = sqlite3.connect("myspiderstore.sqlite3")
#         self.curr = self.conn.cursor()

#     def create_table(self):
#         self.curr.execute("""
#                           DROP TABLE IF EXISTS linkT
#                           """)

#         self.curr.execute("""
#                           CREATE TABLE linkT(
#                               link text 
#                               );
#                           """)

# #                                   self.curr.execute("""
# #                           CREATE TABLE linkT (
# #                             # link_id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                             link TEXT NOT NULL);
# # );
# #                           """)

#         # self.curr.execute("""
#         #                   CREATE TABLE linkT(
#         #                       link text NOT NULL,
#         #                       UNIQUE (link)
#         #                       )
#         #                   """)
        
#     def store_db(self,item):
#         for link in item['link']:
#             self.curr.execute("""
#                     INSERT INTO linkT VALUES(?)""",(link,))
#         self.conn.commit()
        


class FiledownloadPipeline(FilesPipeline):
    
    def file_path(self, request, response=None, info=None):
        file_name: str = request.url.split("/")[-1]
        return file_name