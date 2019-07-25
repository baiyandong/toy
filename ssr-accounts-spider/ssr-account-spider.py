# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import os

from PIL import Image
import pytesseract

def spider():
    '''爬取 ssr-accounts账户 https://github.com/gfw-breaker/ssr-aacounts'''
    print('Work Start')
    target = 'https://github.com/gfw-breaker/ssr-accounts'
    r = requests.get(url=target)
    html = r.text
    bf = BeautifulSoup(html, 'lxml')
    img = bf.article.table.tbody.find('img').get('src')
    img = img.replace('/raw', '')
    imgUrl = 'https://raw.githubusercontent.com%s' % img 
    print('img url: %s' % imgUrl)

    di(imgUrl)

    writeText('IP Address: %s ' % ocr_core('./images/%s' % imgUrl.split('/')[-1]))

    print(ocr_core('./images/%s' % imgUrl.split('/')[-1]))

    #contents = bf.article.table.tbody.find_all('td')
    for tr in bf.article.table.tbody.find_all('tr'):
        for td in tr.find_all('td'):
            writeText(td.getText() + '\n')

    
    print('Work End')
            
#    for child in contents:
#        print(child)

def writeText(text):
    with open('./text/port.txt', 'a+') as f:
        f.write(text)

def di(url):
    #url = 'https://raw.githubusercontent.com/gfw-breaker/ssr-accounts/master/resources/ip2.png'
    print('url is: %s' % url)
    response = requests.get(url)
    print('res: %s' % response)
    print('正在下载: %s' % url.split('/')[-1])
    with open('./images/%s' % url.split('/')[-1], 'wb') as f:
        f.write(response.content)

def ocr_core(filename):
    '''
    This function will handle the core OCR processing of images.
    '''
    text = pytesseract.image_to_string(Image.open(filename)) # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

if __name__ == '__main__':
    spider()

