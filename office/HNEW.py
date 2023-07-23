# coding:UTF-8

import os

text = input()

if text.startswith('H'):
    path = (r'G:\hu')
elif text.startswith('KM'):
    path = (r'\\192.168.251.9\pe\制造本部工艺资料管理\外贸工艺资料\KM类')
elif text.startswith('GN'):
    path = (r'\\192.168.251.9\pe\制造本部工艺资料管理\内销工艺资料\GN--（功能）')
elif text.startswith('KG'):
    path = (r'\\192.168.251.9\pe\制造本部工艺资料管理\内销工艺资料\KG--（内销功能）')
elif text.startswith('DK'):
    path = (r'\\192.168.251.9\pe\制造本部工艺资料管理\内销工艺资料\DK--类（电商）')
else:
    print("无法识别")
    exit()

if text.startswith('H'):
    filename = text[1:]
else:
    filename = text

full_path = os.path.join(path, filename)
os.startfile(full_path)

