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




eng2sp = {1:"http://www.blogger.com/video-play.mp4?contentId=63a830f0b70164b6",
2:"http://www.blogger.com/video-play.mp4?contentId=d81ae465368edf22",
3:"http://www.blogger.com/video-play.mp4?contentId=a396a320bde549d3",
4:"http://www.blogger.com/video-play.mp4?contentId=740ae1924c423a56",
5:"http://www.blogger.com/video-play.mp4?contentId=199183ff26ad255a",
6:"http://www.blogger.com/video-play.mp4?contentId=1181556022bb7609",
7:"http://www.blogger.com/video-play.mp4?contentId=ed1b202ad84db6e",
8:"http://www.blogger.com/video-play.mp4?contentId=94580317816326a0",
9:"http://www.blogger.com/video-play.mp4?contentId=58d943d3bcd0a7f1",
10:"http://www.blogger.com/video-play.mp4?contentId=db49ac50b64ab592",
11:"http://www.blogger.com/video-play.mp4?contentId=a7c139a4610f3f05",
12:"http://www.blogger.com/video-play.mp4?contentId=57f599b2371f2f09",
13:"http://www.blogger.com/video-play.mp4?contentId=a41dafe35fb82e38",
14:"http://www.blogger.com/video-play.mp4?contentId=ff4fd04db5b1bc7c",
15:"http://www.blogger.com/video-play.mp4?contentId=8cd7b31228f95a40",
16:"http://www.blogger.com/video-play.mp4?contentId=8bc2b329d4e26d11",
17:"http://www.blogger.com/video-play.mp4?contentId=fd8026f8df08ecaf",
18:"http://www.blogger.com/video-play.mp4?contentId=b045012a7c8c285f",
19:"http://www.blogger.com/video-play.mp4?contentId=dc2f679dcf926846",
20:"http://www.blogger.com/video-play.mp4?contentId=3bd329579a9b5fa4",         
}

def createservercapcavpan():
        eps = randint(1,20)
        ieps = 35 - eps

        if eps == 20:
                eps = eps - 15

        if eps > 20:
                eps = eps - 20

        for j in range(eps,(eps+10)):
                
                file = open(""+m3u+"","a")
                eps = eng2sp[j]
                file.write(eps)
                file.write("\n")
                file.close

                
        xbmc.Player().play(""+m3u+"")

#import atualizar
#atualizar.Update(addonID)


