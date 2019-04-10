# -*- coding: utf-8 -*-
#------------------------------------------------------------
# 
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import os
import sys
import time
#import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon
from random import randint
import base64
import naomi

addonID = 'plugin.video.desenhos24hrs'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'

tunel = "UmVmZXJlcj1odHRwOi8vd3d3LnJlZGVjYW5haXMuY29tLmJyLw=="
ftunel = base64.b64decode(tunel)

addon_data_dir = os.path.join(xbmc.translatePath("special://userdata/addon_data" ).decode("utf-8"), addonID)

if not os.path.exists(addon_data_dir):
	os.makedirs(addon_data_dir)

m3u =  os.path.join(addon_data_dir, "files.m3u")

file = open(""+m3u+"","w")
file.close




eng2sp = {1:"http://www.blogger.com/video-play.mp4?contentId=c0fecce30b67fa25",
2:"http://www.blogger.com/video-play.mp4?contentId=b89b8072c0b28868",
3:"http://www.blogger.com/video-play.mp4?contentId=c7e0317a2770d9a1",
4:"http://www.blogger.com/video-play.mp4?contentId=d0e997bbfe4c0ed7",
5:"http://www.blogger.com/video-play.mp4?contentId=afc0dbcdcbdc3f5b",
6:"http://www.blogger.com/video-play.mp4?contentId=e6839c9c7f092845",
7:"http://www.blogger.com/video-play.mp4?contentId=7440082b7d171416",
8:"http://www.blogger.com/video-play.mp4?contentId=b83cec95341ac4fa",
9:"http://www.blogger.com/video-play.mp4?contentId=8233e5c98149c921",
10:"http://www.blogger.com/video-play.mp4?contentId=65816cf155e1871e",
11:"http://www.blogger.com/video-play.mp4?contentId=cc86e000ee91b56a",
12:"http://www.blogger.com/video-play.mp4?contentId=2d86859ce7a079c7",
13:"http://www.blogger.com/video-play.mp4?contentId=ba13f0c52651e2db",
14:"http://www.blogger.com/video-play.mp4?contentId=470eac2833be3574",
15:"http://www.blogger.com/video-play.mp4?contentId=82e149a9dff3437",
16:"http://www.blogger.com/video-play.mp4?contentId=3b9005f8c487d4fb",
17:"http://www.blogger.com/video-play.mp4?contentId=b449dc6f501aee20",
18:"http://www.blogger.com/video-play.mp4?contentId=7d0295984a4bb74b",
19:"http://www.blogger.com/video-play.mp4?contentId=88ca58ae1373154e",
20:"http://www.blogger.com/video-play.mp4?contentId=6e36684a7b1d8429",
21:"http://www.blogger.com/video-play.mp4?contentId=a135ca925c90a5d3",
22:"http://www.blogger.com/video-play.mp4?contentId=75971f67c8535eea",
23:"http://www.blogger.com/video-play.mp4?contentId=49723fd7effdabda",
24:"http://www.blogger.com/video-play.mp4?contentId=e76ca6d15320964d",
25:"http://www.blogger.com/video-play.mp4?contentId=84faf579a1c5c050",
26:"http://www.blogger.com/video-play.mp4?contentId=abc1a6dfa4676b17",
27:"http://www.blogger.com/video-play.mp4?contentId=497f2b60d2bae1f2",
28:"http://www.blogger.com/video-play.mp4?contentId=90454846c0dff7b8",
29:"http://www.blogger.com/video-play.mp4?contentId=2efad71560651016",
30:"http://www.blogger.com/video-play.mp4?contentId=8a53c441da6206f5",
31:"http://www.blogger.com/video-play.mp4?contentId=ebe94a6a87e99239",
32:"http://www.blogger.com/video-play.mp4?contentId=27826ab9a3cf0942",
33:"http://www.blogger.com/video-play.mp4?contentId=684cc3093765b64f",
34:"http://www.blogger.com/video-play.mp4?contentId=9d1a33920924776f",
35:"http://www.blogger.com/video-play.mp4?contentId=454ef69ce73c9d78",
36:"http://www.blogger.com/video-play.mp4?contentId=a0465aa4f1fc5d07",
37:"http://www.blogger.com/video-play.mp4?contentId=55fd6cba4019121b",
38:"http://www.blogger.com/video-play.mp4?contentId=5498b9a788cb3c7c",
39:"http://www.blogger.com/video-play.mp4?contentId=df9a8957cdb316f",
40:"http://www.blogger.com/video-play.mp4?contentId=68bfc7ee7576ac6a",
41:"http://www.blogger.com/video-play.mp4?contentId=c6b8ddae8125b270",
42:"http://www.blogger.com/video-play.mp4?contentId=dc49bd642d5b6554",
43:"http://www.blogger.com/video-play.mp4?contentId=ec8b480d633fe0a7",
44:"http://www.blogger.com/video-play.mp4?contentId=5c7a68a901755a22",
45:"http://www.blogger.com/video-play.mp4?contentId=3b14f13b75df1f71",
46:"http://www.blogger.com/video-play.mp4?contentId=aab2f2b8b7f143d",
47:"http://www.blogger.com/video-play.mp4?contentId=4b4dadc40cdafb96",
48:"http://www.blogger.com/video-play.mp4?contentId=30def42dc77c4d90",
49:"http://www.blogger.com/video-play.mp4?contentId=9ec9950d373b214b",
50:"http://www.blogger.com/video-play.mp4?contentId=f80332c41f699ebc",
51:"http://www.blogger.com/video-play.mp4?contentId=840b6eac78b25708",
52:"http://www.blogger.com/video-play.mp4?contentId=a37129b5550a2cf7",
53:"http://www.blogger.com/video-play.mp4?contentId=90baab490bb4a10a",
54:"http://www.blogger.com/video-play.mp4?contentId=6ed596e9aac93bce",
55:"http://www.blogger.com/video-play.mp4?contentId=37c20833f28571c4",
56:"http://www.blogger.com/video-play.mp4?contentId=17de9c8d98e02466",
57:"http://www.blogger.com/video-play.mp4?contentId=9e48125568605fa4",
58:"http://www.blogger.com/video-play.mp4?contentId=3d000b893cf764c9",
59:"http://www.blogger.com/video-play.mp4?contentId=e959b36a1febf6aa",
60:"http://www.blogger.com/video-play.mp4?contentId=3bd38e8cdab69aed",
61:"http://www.blogger.com/video-play.mp4?contentId=4cffcce8e199511a",
62:"http://www.blogger.com/video-play.mp4?contentId=ec0235217460fc5f",
63:"http://www.blogger.com/video-play.mp4?contentId=8c9644f74d1588d4",
64:"http://www.blogger.com/video-play.mp4?contentId=b6cf2127225ca852",
65:"http://www.blogger.com/video-play.mp4?contentId=cfd5f7c4427660f3",
66:"http://www.blogger.com/video-play.mp4?contentId=c902e7ae8eea2f9f",
67:"http://www.blogger.com/video-play.mp4?contentId=6e49623f4f0dc1e0",
68:"http://www.blogger.com/video-play.mp4?contentId=e41bce9f783e2963",
69:"http://www.blogger.com/video-play.mp4?contentId=239fdf00980c2e9f",
70:"http://www.blogger.com/video-play.mp4?contentId=b9890a1cf599f831",
71:"http://www.blogger.com/video-play.mp4?contentId=17c0cfbbec584fb6",
72:"http://www.blogger.com/video-play.mp4?contentId=46b9d873f0017066",
73:"http://www.blogger.com/video-play.mp4?contentId=5ec529961ff26abd",
74:"http://www.blogger.com/video-play.mp4?contentId=368233705f37a359",
75:"http://www.blogger.com/video-play.mp4?contentId=398cd6f345a6636f",
76:"http://www.blogger.com/video-play.mp4?contentId=60523ef1fa5c4f7b",
77:"http://www.blogger.com/video-play.mp4?contentId=b9d6a9ff72d08eb1",
78:"http://www.blogger.com/video-play.mp4?contentId=bab4db1e9df52e26",
79:"http://www.blogger.com/video-play.mp4?contentId=df2b623fdf11d5b3",
80:"http://www.blogger.com/video-play.mp4?contentId=28d68eef8c7f1490",
81:"http://www.blogger.com/video-play.mp4?contentId=414d0259cfc47c49",
82:"http://www.blogger.com/video-play.mp4?contentId=4c446809fdfe16c9",
83:"http://www.blogger.com/video-play.mp4?contentId=833546574d1a018a",
84:"http://www.blogger.com/video-play.mp4?contentId=1f9b32c427d763ce",
85:"http://www.blogger.com/video-play.mp4?contentId=abd08613be768388",
86:"http://www.blogger.com/video-play.mp4?contentId=7cd0aa272eaee387",
87:"http://www.blogger.com/video-play.mp4?contentId=8494770836d75017",
88:"http://www.blogger.com/video-play.mp4?contentId=137b75d1db915033",
89:"http://www.blogger.com/video-play.mp4?contentId=18f161abeeb74e77",
90:"http://www.blogger.com/video-play.mp4?contentId=18feaaecad395312",
91:"http://www.blogger.com/video-play.mp4?contentId=84dcdf1763c20025",
92:"http://www.blogger.com/video-play.mp4?contentId=42a38bd4b3b35148",
93:"http://www.blogger.com/video-play.mp4?contentId=5efede1498967ecb",
94:"http://www.blogger.com/video-play.mp4?contentId=e0f9172bcc8e14d5",
95:"http://www.blogger.com/video-play.mp4?contentId=40135dfe58db95cc",}

def createserverjj():
        eps = randint(1,95)
        ieps = 35 - eps

        if eps == 95:
                eps = eps - 25

        for j in range(eps,(eps+25)):
                
                file = open(""+m3u+"","a")
                eps = eng2sp[j]
                file.write(eps)
                file.write("\n")
                file.close

                
        xbmc.Player().play(""+m3u+"")

#import atualizar
#atualizar.Update(addonID)


