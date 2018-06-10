#!/usr/bin/python3
#encodiong:utf-8

import flup.server.fcgi as flups

import json
import urllib.request as urllib

mc = memcache.Connect()

def getFromCache(key):
    return str(mc.get(key))

def setToCache(key,data):
    return mc.set(key,data)

def myapp(environ, start_response):
    start_response("200 OK",[('Content-Type','text/plain')])
    method = environ['REQUEST_METHOD']

    uri = ''
    if 'REQUEST_URI' in environ:
        uri = environ['REQUEST_URI']
    
    length = 0
    if 'CONTENT_LENGTH' in environ:
       if environ['CONTENT_LENGTH']=='':
          length = 0
       else:
          length = int(environ['CONTENT_LENGTH'])
    if method=='POST':
       content = str(environ['wsgi.input'].read(length).decode())
       source = json.loads(content)
       key = source['key']
       if uri=='/api/cache/set/':
          data = json.dumps(source['data'])
          setToCache(key,data)
          yield b'Set success!'
       elif uri=='/api/cache/get/':
          data = getFromCache(key)
          yield data.encode()

if __name__=='__main__':
   flups.WSGIServer(myapp).run()


