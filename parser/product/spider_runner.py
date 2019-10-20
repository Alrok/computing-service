import crochet
import os

from scrapy.crawler import CrawlerRunner
from scrapy.settings import Settings


class SpiderRunner:
    def __init__(self):
        crochet.setup()
        pass

    @crochet.wait_for(timeout=60.0)
    def run(self, spider, allowed_domains, start_urls):
        crawl_runner = CrawlerRunner(self._get_settings())

        eventual = crawl_runner.crawl(
            spider,
            allowed_domains=allowed_domains,
            start_urls=start_urls)

        return eventual

    def _get_settings(self):
        settings = Settings()

        os.environ['SCRAPY_SETTINGS_MODULE'] = 'parser.product.settings'
        settings_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
        settings.setmodule(settings_module_path, priority='project')

        return settings
