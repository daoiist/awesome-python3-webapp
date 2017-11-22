' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

@get('/')
def index(request):
    return {
        '__template__': 'test.html'
    }