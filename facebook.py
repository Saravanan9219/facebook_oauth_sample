#! /usr/bin/python2

import requests
import uuid
import sys
import urllib
import urlparse

state = uuid.uuid4().get_hex()
client_id = '738454899555573'
client_secret = '3e1fc01c4c25891e34705bb11f1076c1'

authorisation_uri = 'https://www.facebook.com/dialog/oauth'
redirect_uri = 'https://localhost/facebook/'

token_uri = 'https://graph.facebook.com/oauth/access_token'

basic_authorisation_uri = requests.Request(url=authorisation_uri, params={'client_id':client_id, 'redirect_uri':redirect_uri, 'state':state}).prepare().url

print "Go to this url enter the following from the response {0}\n".format(basic_authorisation_uri)

code = raw_input("Enter the code\n")

new_state = raw_input("Enter the State\n")

if not state == new_state:
   print "Invalid State"
   sys.exit()

r = requests.get(token_uri, params={'client_id':client_id, 'client_secret':client_secret, 'code':code, 'redirect_uri':redirect_uri})

print r.content

token = dict(urlparse.parse_qsl(r.content.split('#')[0]))['access_token']

print '\n' + token 



