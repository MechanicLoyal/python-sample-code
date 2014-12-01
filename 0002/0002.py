#!/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
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

conn = mysql.connector.connect(user='root', password='password', database='test', use_unicode=True)
cursor = conn.cursor()

cursor.execute('create table code(id varchar(10) primary key, code varchar(24))')

for t in range(len(codelist)):
    cursor.execute('insert into code(id, code) values (%s, %s)', [t, codelist[t]])

conn.commit()

cursor.close()
conn.close()

