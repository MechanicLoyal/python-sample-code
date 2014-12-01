#!/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(user='root', password='password', database='test', use_unicode=True)
cursor = conn.cursor()

cursor.execute('create table code(code varchar(24))')

cursor.execute
