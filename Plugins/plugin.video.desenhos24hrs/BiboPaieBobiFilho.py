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




eng2sp = {1:"http://www.blogger.com/video-play.mp4?contentId=b5b6a72f596733b",
2:"http://www.blogger.com/video-play.mp4?contentId=532fbadb4e448fa0",
3:"http://www.blogger.com/video-play.mp4?contentId=949e27c822b4e075",
4:"http://www.blogger.com/video-play.mp4?contentId=a4a95e6ea3bfbe",
5:"http://www.blogger.com/video-play.mp4?contentId=d80a6175b0a6a397",
6:"http://www.blogger.com/video-play.mp4?contentId=f170ec1a98a17ef6",
7:"http://www.blogger.com/video-play.mp4?contentId=d1049ce29e2f184d",
8:"http://www.blogger.com/video-play.mp4?contentId=92674fef7d5153e9",
9:"http://www.blogger.com/video-play.mp4?contentId=304bb3905b7aecb8",
10:"http://www.blogger.com/video-play.mp4?contentId=14187a5dd3a0cac8",
11:"http://www.blogger.com/video-play.mp4?contentId=50d8d0a699747865",
12:"http://www.blogger.com/video-play.mp4?contentId=680af3245d30e8ec",
13:"http://www.blogger.com/video-play.mp4?contentId=cd46e81c0a60661a",
14:"http://www.blogger.com/video-play.mp4?contentId=ab69ee09445a2a4c",
15:"http://www.blogger.com/video-play.mp4?contentId=957026eb00fde523",
16:"http://www.blogger.com/video-play.mp4?contentId=71c4654ccdce082",
17:"http://www.blogger.com/video-play.mp4?contentId=b627546023f46889",
18:"http://www.blogger.com/video-play.mp4?contentId=7afc32399774ad60",
19:"http://www.blogger.com/video-play.mp4?contentId=a1c4c93bca8c2d0c",
20:"http://www.blogger.com/video-play.mp4?contentId=4f4847778c3597ca",
21:"http://www.blogger.com/video-play.mp4?contentId=467bd510db62539f",
22:"http://www.blogger.com/video-play.mp4?contentId=b938ecee72e661b3",
23:"http://www.blogger.com/video-play.mp4?contentId=3034e9ea9a432e91",
24:"http://www.blogger.com/video-play.mp4?contentId=4b2451ad023fa5e6",
25:"http://www.blogger.com/video-play.mp4?contentId=1d299bbc321ab30c",
26:"http://www.blogger.com/video-play.mp4?contentId=c55494a7e6acf782",
27:"http://www.blogger.com/video-play.mp4?contentId=9892a9b58c5d3786",
28:"http://www.blogger.com/video-play.mp4?contentId=900f7c6311432521",
29:"http://www.blogger.com/video-play.mp4?contentId=ce77c2a4d91d1008",
30:"http://www.blogger.com/video-play.mp4?contentId=59e78f1c3aa54bcf",
31:"http://www.blogger.com/video-play.mp4?contentId=54c1b1739fbd0dbf",
32:"http://www.blogger.com/video-play.mp4?contentId=c23624c09e814497",
33:"http://www.blogger.com/video-play.mp4?contentId=2581a560bcb7c6ee",
34:"http://www.blogger.com/video-play.mp4?contentId=d94e91748a1f297f",
35:"http://www.blogger.com/video-play.mp4?contentId=2b091937f504aab6",
36:"http://www.blogger.com/video-play.mp4?contentId=50829d8936335832",
37:"http://www.blogger.com/video-play.mp4?contentId=7685a6b1d10ad045",
38:"http://www.blogger.com/video-play.mp4?contentId=8f0a6aad1e094f57",
39:"http://www.blogger.com/video-play.mp4?contentId=a84a8180a29787a4",
40:"http://www.blogger.com/video-play.mp4?contentId=f5bb571ba9919c04",
41:"http://www.blogger.com/video-play.mp4?contentId=62b5836f57d68ed2",
42:"http://www.blogger.com/video-play.mp4?contentId=b366e00d7e42ed0a",
43:"http://www.blogger.com/video-play.mp4?contentId=b334019f309559ef",
44:"http://www.blogger.com/video-play.mp4?contentId=ad25412ab226e5d2",
45:"http://www.blogger.com/video-play.mp4?contentId=c78c3c8717c58308",         
}

def createserverbpebf():
        eps = randint(1,45)
        ieps = 35 - eps

        if eps == 45:
                eps = eps - 25

        if eps > 45:
                eps = eps - 45

        for j in range(eps,(eps+25)):
                
                file = open(""+m3u+"","a")
                eps = eng2sp[j]
                file.write(eps)
                file.write("\n")
                file.close

                
        xbmc.Player().play(""+m3u+"")

#import atualizar
#atualizar.Update(addonID)


