#!/usr/bin/env python3.11
import requests
import json
import re
import yaml

def get_total():
    params = {"deprecated": "false",
                "page": 1,
                "page_size":"1"}
    ret = requests.get('https://galaxy.ansible.com/api/internal/ui/search/',params=params).json()
    return ret.get('collection').get('count')


def get_coll():
    coll = []
    sess = requests.session()
    for x in range(1,(get_total()//100)+2):
        params = {"deprecated": "false",
                  "page": str(x),
                  "page_size":"100"}
        ret = sess.get('https://galaxy.ansible.com/api/internal/ui/search/',params=params).json()
        coll.extend(ret.get('collection',[]).get('results',[]))
        with open('.last.json','w') as w:
            w.write(json.dumps(coll))
    return coll



#r = json.loads(open('.last.json').read())
a = []
for x in get_coll():
    namespace = x.get('namespace').get('name')
    name = x.get('name')
    a.append(f"{namespace}.{name}")
print(yaml.dump({'collections':sorted(a)}).replace('\n-','\n  -'))