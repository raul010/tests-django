from django.core.management.base import BaseCommand
import urllib2
import os
from lxml import etree

class Command(BaseCommand):



    def handle(self, *args, **options):
        global urls_resolved
        global links_resolved
        global url
        urls_resolved = set()
        links_resolved = set()

        url = 'http://localhost:8000/index/'

        request = urllib2.urlopen(url)

        print(request.code == 200)

        htmlparser = etree.HTMLParser()
        tree = etree.parse(request, htmlparser)

        self.take_elements(tree)


    def elements_navigation(self, links, xpath, info):
        tag_name = links[0].tag

        for i in links:
            link = i.xpath(xpath)[0]
            if 'a' == tag_name:
                if link not in urls_resolved:
                    urls_resolved.add(link)
                    self.url_open(link)
                    continue
            else:
                if link not in links_resolved:
                    links_resolved.add(link)
                    self.url_open(link)
                    continue

    def take_elements(self, tree):
        css_links = tree.xpath('//link[@href]')
        self.elements_navigation(css_links, '@href', 'CSS')

        js_links = tree.xpath('//script')
        self.elements_navigation(js_links, '@src', 'JS')

        js_links = tree.xpath('//a')
        self.elements_navigation(js_links, '@href', 'Html')

    def url_open(self, url_path):

        url_result = self.normalize_url(url_path)

        request = urllib2.urlopen(url_result)
        print(request.code == 200)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(request, htmlparser)
        self.take_elements(tree);

    def normalize_url(self, url_path):

        index_in_url = url_path == 'index' or url_path == '/index';
        url_result = '';

        if index_in_url:
            if url_path.startswith('/'):
                url_result = '%s%s'%(url, url_path.replace('/index', ""))
            else:
                url_result = '%s%s'%(url, url_path.replace('index', ""))
        else:
            if url_path.startswith('/'):
                url_result = '%s%s'%(url, url_path.replace('/', '', 1))
            else:
                url_result = '%s%s'%(url, url_path)

        print(url_result)
        return url_result









# url =  "http://www.example.com/servlet/av/ResultTemplate=AVResult.html"
# response = urllib2.urlopen(url)
# htmlparser = etree.HTMLParser()
# tree = etree.parse(response, htmlparser)
# tree.xpath(xpathselector)

# Example Selenium works
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("http://localhost:8000/index/")
# links_el = driver.find_elements_by_xpath('//link[@href]')
#
# for e in links_el:
#     link_name = e.get_attribute("href")
#     # e.click()
#
#     print('Link a: %s'%(link_name))
#
# driver.quit()