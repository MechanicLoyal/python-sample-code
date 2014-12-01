#!/bin/env python
# -*- coding: utf-8 -*-

import random

def getcode(i):
    code = ""
    for t in range(i):
        code = code + chr(random.randint(65, 90))
    return code

codelist = []
for t in range(200):
    newcode=getcode(24)
    if newcode not in codelist:
        codelist.append(getcode(24))

for code in codelist:
    print code
