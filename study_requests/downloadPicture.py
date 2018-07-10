#-*- coding: utf-8 -*
__author__ = 'geebos'

import requests

src = 'http://qrcode-1254412656.cosgz.myqcloud.com/sfdgfdyhtbcnhgjgm.mp4'

r = requests.get(src)

with open('movie.mp4', 'wb') as f:
    f.write(r.content)

print('下载完成')

src = 'http://qrcode-1254412656.cosgz.myqcloud.com/sfdgfdyhtbcnhgjgm.mp4'