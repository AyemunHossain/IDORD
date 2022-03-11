from django.core.management.base import BaseCommand
from django.conf import settings
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import data_path, get_project_settings
import os
from pathlib import Path

class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        django_path = Path(__file__).resolve().parent.parent.parent.parent
        os.system("python3 IDORD.py")