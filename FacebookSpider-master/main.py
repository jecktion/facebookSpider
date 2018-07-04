
from scrapy import cmdline
import os
# os.chdir("facebook_spider")
cmdline.execute('scrapy crawl facebook'.split())