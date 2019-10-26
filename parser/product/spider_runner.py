import crochet
import os
import logging

from threading import Thread

from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerRunner
from scrapy.settings import Settings


class SpiderRunner:
    spider = None
    allowed_domains = []
    start_urls = []
    follow_links = False

    def __init__(self, spider, allowed_domains, start_urls, follow_links=False):
        self.spider = spider
        self.allowed_domains = allowed_domains
        self.start_urls = start_urls
        self.follow_links = follow_links

        self.__configure_logging()
        crochet.setup()
        pass

    def run(self):
        # Thread(target=self.__run, daemon=True).start()
        self.__run()

    def __get_settings(self):
        settings = Settings()

        os.environ['SCRAPY_SETTINGS_MODULE'] = 'parser.product.settings'
        settings_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
        settings.setmodule(settings_module_path, priority='project')

        return settings

    def __configure_logging(self):
        configure_logging(install_root_handler=False)
        logging.basicConfig(
            filename=self.spider + '_log.txt',
            format='%(levelname)s: %(message)s',
            level=logging.INFO)

    @crochet.wait_for(timeout=3200.0)
    def __run(self):
        crawl_runner = CrawlerRunner(self.__get_settings())

        eventual = crawl_runner.crawl(
            self.spider,
            allowed_domains=self.allowed_domains,
            start_urls=self.start_urls,
            follow_links=self.follow_links)

        return eventual
