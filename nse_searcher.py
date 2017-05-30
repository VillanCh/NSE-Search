#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: NSE Search
  Created: 05/29/17
"""

import argparse
import warnings
import os
import sys
import urlparse

#
# ignore warning
#
warnings.filterwarnings("ignore")

import sqlite3

import requests
from bs4 import BeautifulSoup

banner = """
 _   _ ____  _____     ____                      _
| \ | / ___|| ____|   / ___|  ___  __ _ _ __ ___| |__   ___ _ __
|  \| \___ \|  _| ____\___ \ / _ \/ _` | '__/ __| '_ \ / _ \ '__|
| |\  |___) | |__|_____|__) |  __/ (_| | | | (__| | | |  __/ |
|_| \_|____/|_____|   |____/ \___|\__,_|_|  \___|_| |_|\___|_|     -by v1ll4n"""


NSE_INDEX_URL = 'https://nmap.org/nsedoc/index.html'
DEFAULT_DB_NAME = './nseinfos.db'


#----------------------------------------------------------------------
def build_db():
    """"""
    global NSE_INDEX_URL
    
    #
    # fetch information
    #
    try:
        _text = requests.get(NSE_INDEX_URL).text
    except:
        print('[x] Sorry! Cannot GET NSE_INDEX_PAGE:{}, the db was not changed'.format(NSE_INDEX_URL))
        exit()
        
    _soup = BeautifulSoup(_text)
    _tabletag = _soup.find('table', attrs={'class':'file_list'})
    
    _items = _tabletag.findAll('tr')
    
    #
    # build db
    #
    if os.path.exists(DEFAULT_DB_NAME):
        os.remove(DEFAULT_DB_NAME)
    
    _db = sqlite3.connect(DEFAULT_DB_NAME)
    _cursor = _db.cursor()
    
    #
    # create db
    #
    _cursor.execute('create table nse_script(name text, url text, description text)')
    
    for i in _items:
        #print "NAME:{}".format(i.a.strings.next())
        #print "URL:{}".format(i.a.attrs['href'])
        #print "DESC:{}".format(i.p.strings.next())
        
        #
        # insert db
        #
        _script_name = i.a.strings.next()
        _url = i.a.attrs['href']
        _desc = i.p.strings.next()
        
        _cursor.execute('insert into nse_script(name, url, description) ' + \
                        'values(?,?,?)', tuple([_script_name, _url, _desc]))
    
    #
    # commit and close
    #
    _db.commit()
    _db.close()
        
#----------------------------------------------------------------------
def search(keyword):
    """"""
    #
    # db conn error -> rebuild db
    #
    db = sqlite3.connect(DEFAULT_DB_NAME)
    
    _cursor = db.execute('select name, url, description from nse_script where name like "%{kw}%" or description like "%{kw}%"'.format(kw=keyword))
    _result_set = _cursor.fetchall()
    db.close()
    
    return _result_set


#----------------------------------------------------------------------
def show_result(rset, detail_flag=False):
    """"""
    for i in rset:
        _n = i[0]
        _url = urlparse.urljoin(NSE_INDEX_URL, i[1])
        _summary = i[2]
        
        print('')
        print('-'*64)
        print('Script Name: {}'.format(_n))
        print('Script Usage URL: {}'.format(_url))
        
        if detail_flag:
            print('Script Summary(Description): \n {}'.format(_summary))
        

#----------------------------------------------------------------------
def main():
    """"""
    #
    # define argparse
    #
    print(banner)
    print('')
    print('')
    
    _parser = argparse.ArgumentParser()
    _parser.add_argument('-k', '--keyword', dest='keyword')
    _parser.add_argument('--update', dest='update', action='store_true', default=False)
    _parser.add_argument('--detail', dest='detail', action='store_true', default=False)
    
    #
    # get options
    #
    _opt = _parser.parse_args()
    
    _keyword = _opt.keyword
    _update_flag = _opt.update
    _detail_flag = _opt.detail
    
    print('[*] Search Keyword: {}'.format(_keyword))
    print('[*] Details about the result? {}'.format(_detail_flag))
    
    print('')
    print('')
    
    #
    # if update flag is True, reset db from nmap.org
    #
    if _update_flag:
        print('[-] Update Flag is True, Wait for a moment to update the nse scripts information!')
        build_db()
    
    if _keyword:
        _items = search(_keyword)
    
        show_result(_items, _detail_flag)
    
    

if __name__ == '__main__':
    main()
    