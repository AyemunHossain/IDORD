from scrapy.pipelines.files import FilesPipeline

from core.models import LinkItem
from core.models import FormDetailsItem as FormDetailsModel


class multiperpousePipeline:
    """Persist scraped items into their backing Django models."""

    def process_item(self, item, spider):
        model_class = getattr(item, "django_model")

        if model_class is LinkItem:
            model_class.objects.create(
                link=item.get("link"),
                base_link=item.get("base_link"),
                tag=item.get("tag") or None,
            )
            return item

        if model_class is FormDetailsModel:
            try:
                model_class.objects.create(
                    link=item.get("link"),
                    page_link=item.get("page_link"),
                    type=item.get("type"),
                    is_auth_related=item.get("is_auth_related", False),
                )
            except Exception as error:
                print(f"_______________________{error}________________________________")
            return item

        return item


class FiledownloadPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None):
        return request.url.split("/")[-1]
