#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from qcloud_image import Client
from qcloud_image import CIUrl, CIFile, CIBuffer, CIUrls, CIFiles, CIBuffers

appid = '#########'
secret_id = '##############'
secret_key = '#####################'
bucket = 'faceslib'

client = Client(appid, secret_id, secret_key, bucket)
client.use_http()
client.set_timeout(30)

result = client.face_identify('group1', CIFile('./10xxl2.jpeg'))
value_no=80
value_yes=96
person=client.face_getinfo(result['data']['candidates'][0]['person_id'])
person_name = person['data']['person_name']
confidence=result['data']['candidates'][0]['confidence']
print(confidence)
if confidence<value_no:
    print("不存在该顾客")
if value_no<=confidence<value_yes:
    print("该顾客可能是：")

    print(person_name)
if confidence>=value_yes:
    print('该顾客是：')
    print(person_name)

# print(client.face_getinfo('person_5'))

# print (client.face_newperson('person_10', ['group1',], CIFile('./10xxl1.jpeg')))
# print (client.face_setinfo('person_10', 'Xiongxinli'))
# print (client.face_getpersonids('group1'))
