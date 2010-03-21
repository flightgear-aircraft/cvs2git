#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib


BASE_URL = 'http://github.com/api/v2/json/'
GITHUB_USER = 'flightgear-aircraft'





## Create Repos
payload = urllib.urlencode({'name': 'test1243', 'description': 'test', 'homepage': 'www', 'public': 1})
f = urllib.urlopen(BASE_URL + "repos/create/%s" % GITHUB_USER, payload)
print f

print "-------------------------"

## lists repositories
f = urllib.urlopen(BASE_URL + "repos/show/%s" % GITHUB_USER)
print f.read()

