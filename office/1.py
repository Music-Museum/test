# coding:UTF-8

import os

text = input()

if text.startswith('H'):
    path = (r'G:\hu')
elif text.startswith('DY'):
    path = (r'\\192.168.251.9\功能产品事业部研发部\项目管理模块\OA打样单\2022~2023年立项及开发资料')
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

if text.startswith('H') :
    filename = text[1:]
elif text.startswith('DY') :
    filename = text[2:]
    
else:
    filename = text

full_path = os.path.join(path, filename)
os.startfile(full_path)

