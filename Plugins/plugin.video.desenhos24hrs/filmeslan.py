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




eng2sp = {1:"https://goo.gl/jcR4n7",
2:"https://goo.gl/4cC5We",
3:"https://goo.gl/tPHZ2e",
4:"https://goo.gl/TjoKhn",
5:"https://goo.gl/yYzKqU",
6:"https://goo.gl/G4Nyj8",
7:"https://goo.gl/Gczvk3",
8:"https://goo.gl/68ipkm",
9:"https://goo.gl/xBHgXm",
10:"https://goo.gl/2X7hdk",
11:"https://goo.gl/aCx4yN",
12:"https://goo.gl/DgusQV",
13:"https://goo.gl/SFbSMT",
14:"https://goo.gl/QprhLn",
15:"https://goo.gl/sTrst8",
16:"https://goo.gl/PNjqPF",
17:"https://goo.gl/gBaaNi",
18:"https://goo.gl/it8rHh",
19:"https://goo.gl/nKDjgG",
20:"https://goo.gl/3Uu324",
21:"https://goo.gl/VJEjgE",
22:"https://goo.gl/cZVWhA",
23:"https://goo.gl/xYz1j7",
24:"https://goo.gl/L4tKcq",
25:"https://goo.gl/zg56xs"
}

def createserverfilmes():
        eps = randint(1,25)
        
        

        if eps == 25:
                eps = eps - 25

        if eps > 24:
                eps = eps - 25

        for j in range(eps,(eps+5)):
                
                file = open(""+m3u+"","a")
                eps = eng2sp[j]
                file.write(eps)
                file.write("\n")
                file.close

                
        xbmc.Player().play(""+m3u+"")

#import atualizar
#atualizar.Update(addonID)


