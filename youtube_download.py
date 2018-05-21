# -*- coding: utf-8 -*-

import requests
import time

def get_down_detail(url):
    s = requests.session()
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',} 

    d = {}
    d['function']=''
    d['args[serverId]']=''
    d['args[title]']=''
    d['args[keyHash]']=''
    d['args[serverUrl]']=''
    d['args[id_process]']=''
    d['args[dummy]']='1'
    d['args[urlEntryUser]']=url
    d['args[fromConvert]']='urlconverter'
    d['args[requestExt]']='flv'
    d['args[nbRetry]']='0'
    d['args[videoResolution]']='-1'
    d['args[audioBitrate]']='0'
    d['args[audioFrequency]']='0'
    d['args[channel]']='stereo'
    d['args[volume]']='0'
    d['args[startFrom]']='-1'
    d['args[endTo]']='-1'
    d['args[custom_resx]']='-1'
    d['args[custom_resy]']='-1'
    d['args[advSettings]']='false'
    d['args[aspectRatio]']='-1'

    url1 = 'https://www2.onlinevideoconverter.com/webservice'
    d['function']='validate'
    #r = requests.post(url, data=d, verify=False)
    r1 = s.post(url1, data=d, headers = header)
    r1_json = r1.json()
    print r1_json['result']['serverUrl']

    url2 = 'https://www2.onlinevideoconverter.com/webservice'
    d['function']='processVideo'
    d['args[serverId]']=r1_json['result']['serverId']
    d['args[title]']=r1_json['result']['title']
    d['args[keyHash]']=r1_json['result']['keyHash']
    d['args[serverUrl]']=r1_json['result']['serverUrl']
    d['args[id_process]']=r1_json['result']['id_process']
    r2 = s.post(url2, data=d, headers = header)
    r2_json = r2.json()
    print r2_json['result']['id_process']

    url3 = r1_json['result']['serverUrl'].replace('http', 'https')+'/webservice'
    print url3
    d['function']='getStatusVideo'
    r3 = s.post(url3, data=d, headers = header)
    r3_json = r3.json()
    print r3_json['result']['jobpc']
    while not r3_json['result']['jobpc'] != '100':
        time.sleep(3)
        r3 = s.post(url3, data=d, headers = header)
        r3_json = r3.json()
        print r3_json['result']['jobpc']
    
    url4 = 'https://www2.onlinevideoconverter.com/webservice'
    d['function']='getDownloadVideoFilename'
    r4 = s.post(url4, data=d, headers = header)
    r4_json = r4.json()
    print r4_json['result']['dPageId']
    downurl = r1_json['result']['serverUrl'].replace('http', 'https') + '/download?file=' + r1_json['result']['id_process']
    r5 = s.get(downurl)
    print r5.text




if __name__ == '__main__':
    get_down_detail('https://www.youtube.com/watch?v=lIbkHo3PTeU')
