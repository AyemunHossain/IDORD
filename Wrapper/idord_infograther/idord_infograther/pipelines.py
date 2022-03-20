from itemadapter import ItemAdapter
import sqlite3
from scrapy.pipelines.files import FilesPipeline
from core.models import LinkActionItem, LinkActionItemResponse, FormItem, FormDetailsItem, LinkItem

# A demo pipeline which can create a table and store data in it
class multiperpousePipeline:
    
    def process_item(self, item, spider):
        model_class = getattr(item, 'django_model')
        

        if (model_class.__dict__==LinkItem.__dict__):
            obj = model_class.objects.create(link=item['link'],tag=(item['tag'] or None))
            obj.save()
            return item

        elif(model_class.__dict__==FormDetailsItem.__dict__):
            try:
                obj = model_class.objects.create(link=item['link'], page_link=item['page_link'], type=item['type'], is_auth_related=item['is_auth_related'])
                obj.save()
            except Exception as E:
                print(f"_______________________{E}________________________________")
            return item
        

class FiledownloadPipeline(FilesPipeline):
    
    def file_path(self, request, response=None, info=None):
        file_name: str = request.url.split("/")[-1]
        return file_name