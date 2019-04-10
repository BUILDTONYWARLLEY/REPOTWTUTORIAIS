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




eng2sp = {1:"http://173.249.8.202/home/CFG/cfgo.01.avi",
2:"http://173.249.8.202/home/CFG/cfgo.02.avi",
3:"http://173.249.8.202/home/CFG/cfgo.03.avi",
4:"http://173.249.8.202/home/CFG/cfgo.04.avi",
5:"http://173.249.8.202/home/CFG/cfgo.05.avi",
6:"http://173.249.8.202/home/CFG/cfgo.06.avi",
7:"http://173.249.8.202/home/CFG/cfgo.07.avi",
8:"http://173.249.8.202/home/CFG/cfgo.08.avi",
9:"http://173.249.8.202/home/CFG/cfgo.09.avi",
10:"http://173.249.8.202/home/CFG/cfgo.10.avi",
11:"http://173.249.8.202/home/CFG/cfgo.11.avi",
12:"http://173.249.8.202/home/CFG/cfgo.12.avi",
13:"http://173.249.8.202/home/CFG/cfgo.13.avi",
}

def createservercfg():
        eps = 1

        for j in range(eps,(eps+13)):
                
                file = open(""+m3u+"","a")
                eps = eng2sp[j]
                file.write(eps)
                file.write("\n")
                file.close

                
        xbmc.Player().play(""+m3u+"")

#import atualizar
#atualizar.Update(addonID)


