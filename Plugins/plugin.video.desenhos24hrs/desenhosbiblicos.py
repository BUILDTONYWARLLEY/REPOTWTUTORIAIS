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




eng2sp = {1:"http://www.blogger.com/video-play.mp4?contentId=bf954809c32732f2",
2:"http://www.blogger.com/video-play.mp4?contentId=57384e14f834e2d8",
3:"http://www.blogger.com/video-play.mp4?contentId=6f91faf0c831ae43",
4:"http://www.blogger.com/video-play.mp4?contentId=2b1b961fec89f5b1",
5:"http://www.blogger.com/video-play.mp4?contentId=2d23660441dc9b6a",
6:"http://www.blogger.com/video-play.mp4?contentId=449d78b1607fa4d2",
7:"http://www.blogger.com/video-play.mp4?contentId=10508016d672d62d",
8:"http://www.blogger.com/video-play.mp4?contentId=ebd4b17d144d2474",
9:"http://www.blogger.com/video-play.mp4?contentId=53d50cd36d5cd823",
10:"http://www.blogger.com/video-play.mp4?contentId=5c632fa4795ae537",
11:"http://www.blogger.com/video-play.mp4?contentId=fbe18f2ba9c7b218",
12:"http://www.blogger.com/video-play.mp4?contentId=e35365fcec0a0d88",
13:"http://www.blogger.com/video-play.mp4?contentId=e9cc538bf3e2b70a",
14:"http://www.blogger.com/video-play.mp4?contentId=1a86a2111a4f532d",
15:"http://www.blogger.com/video-play.mp4?contentId=2e1be2ad59949a2a",
16:"http://www.blogger.com/video-play.mp4?contentId=7d0bd2e010c8cdb4",
17:"http://www.blogger.com/video-play.mp4?contentId=b3acba950d76f5a2",
18:"http://www.blogger.com/video-play.mp4?contentId=df1b729858cbd080",
19:"http://www.blogger.com/video-play.mp4?contentId=8ff486bb3a88493c",
20:"http://www.blogger.com/video-play.mp4?contentId=5c5065ddac51ee6a",
21:"http://www.blogger.com/video-play.mp4?contentId=ed40e955710da5eb",
22:"http://www.blogger.com/video-play.mp4?contentId=e3252e1fe644f9ce",
23:"http://www.blogger.com/video-play.mp4?contentId=a7884b1f2378782f",
24:"http://www.blogger.com/video-play.mp4?contentId=9353ade907db5a73",
25:"http://www.blogger.com/video-play.mp4?contentId=2eb0e7b03b0c9495",
26:"http://www.blogger.com/video-play.mp4?contentId=58dc1e51a6dcbf86",
27:"http://www.blogger.com/video-play.mp4?contentId=59859da27be906ee",
28:"http://www.blogger.com/video-play.mp4?contentId=ebc85cbfd8e4629",
29:"http://www.blogger.com/video-play.mp4?contentId=53b2695f77a16b02",
30:"http://www.blogger.com/video-play.mp4?contentId=2fc8ee8044c37672",
31:"http://www.blogger.com/video-play.mp4?contentId=1023f3d704f77e17",
32:"http://www.blogger.com/video-play.mp4?contentId=4f60aa5b63270541",
33:"http://www.blogger.com/video-play.mp4?contentId=5cdc224e44f200d7",
34:"http://www.blogger.com/video-play.mp4?contentId=e0ce77579df19280",
35:"http://www.blogger.com/video-play.mp4?contentId=591e792bca086d02",
36:"http://www.blogger.com/video-play.mp4?contentId=bb35ed527069f910",
37:"http://www.blogger.com/video-play.mp4?contentId=4f0b27a5a3cb574b",
38:"http://www.blogger.com/video-play.mp4?contentId=9f152f65f2f63f18",
39:"http://www.blogger.com/video-play.mp4?contentId=bf954809c32732f2",         
}

def createserverdesenhobiblicos():
        eps = randint(1,38)
        ieps = 35 - eps

        if eps == 38:
                eps = eps - 25

        if eps > 39:
                eps = eps - 38

        for j in range(eps,(eps+25)):
                
                file = open(""+m3u+"","a")
                eps = eng2sp[j]
                file.write(eps)
                file.write("\n")
                file.close

                
        xbmc.Player().play(""+m3u+"")

#import atualizar
#atualizar.Update(addonID)


