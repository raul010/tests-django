from django.test import TestCase
import urllib2
from lxml import etree
# models test
class WhateverTest(TestCase):

    def setUp(self):
        self.urls_resolved = set()
        self.links_resolved = set()
        self.url = 'http://localhost:8052/index/'


    def test_whatever_creation(self):
        request = urllib2.urlopen(self.url)

        self.assertEqual(request.code, 200)

        htmlparser = etree.HTMLParser()
        tree = etree.parse(request, htmlparser)

        self.take_elements(tree)


    def elements_navigation(self, links, xpath, info):
        tag_name = links[0].tag

        for i in links:
            link = i.xpath(xpath)[0]
            if 'a' == tag_name:
                if link not in self.urls_resolved:
                    self.urls_resolved.add(link)
                    self.url_open(link)
                    continue
            else:
                if link not in self.links_resolved:
                    self.links_resolved.add(link)
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
        self.assertEqual(request.code, 200)

        htmlparser = etree.HTMLParser()
        tree = etree.parse(request, htmlparser)
        self.take_elements(tree);

    def normalize_url(self, url_path):

        index_in_url = url_path == 'index' or url_path == '/index';
        url_result = '';

        if index_in_url:
            if url_path.startswith('/'):
                url_result = '%s%s'%(self.url, url_path.replace('/index', ""))
            else:
                url_result = '%s%s'%(self.url, url_path.replace('index', ""))
        else:
            if url_path.startswith('/'):
                url_result = '%s%s'%(self.url, url_path.replace('/', '', 1))
            else:
                url_result = '%s%s'%(self.url, url_path)

        return url_result

    def test_human_view_brower(self):
        from selenium import webdriver

        driver = webdriver.Chrome()
        driver.get(self.url)
        # links_el = driver.find_elements_by_xpath('//link[@href]')

        # driver.quit()
