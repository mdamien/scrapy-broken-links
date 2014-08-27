# -*- coding: utf-8 -*-

# Scrapy settings for broken_links project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'broken_links'

SPIDER_MODULES = ['broken_links.spiders']
NEWSPIDER_MODULE = 'broken_links.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'broken_links (+http://www.yourdomain.com)'

# limit crawling to allowed domains only
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html#scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware
SPIDER_MIDDLEWARES = {
    'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': 999,
}