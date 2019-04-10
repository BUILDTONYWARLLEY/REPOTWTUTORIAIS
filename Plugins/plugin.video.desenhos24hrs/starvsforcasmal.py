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




eng2sp = {1:"http://173.249.8.202/home/STAR.VS.AS.FORCAS.DO.MAL.2015.T01.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP01.UP-LiPEH.mp4",
2:"http://173.249.8.202/home/STAR.VS.AS.FORCAS.DO.MAL.2015.T01.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP02.UP-LiPEH.mp4",
3:"http://173.249.8.202/home/STAR.VS.AS.FORCAS.DO.MAL.2015.T01.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP03.UP-LiPEH.mp4",
4:"http://173.249.8.202/home/STAR.VS.AS.FORCAS.DO.MAL.2015.T01.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP04.UP-LiPEH.mp4",
5:"http://173.249.8.202/home/STAR.VS.AS.FORCAS.DO.MAL.2015.T01.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP05.UP-LiPEH.mp4",
6:"http://173.249.8.202/home/STAR.VS.AS.FORCAS.DO.MAL.2015.T01.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP06.UP-LiPEH.mp4",
7:"http://173.249.8.202/home/STAR.VS.AS.FORCAS.DO.MAL.2015.T01.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP07.UP-LiPEH.mp4",
8:"http://173.249.8.202/home/STAR.VS.AS.FORCAS.DO.MAL.2015.T01.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP08.UP-LiPEH.mp4",
9:"http://173.249.8.202/home/STAR.VS.AS.FORCAS.DO.MAL.2015.T01.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP09.UP-LiPEH.mp4",
10:"http://173.249.8.202/home/STAR.VS.AS.FORCAS.DO.MAL.2015.T01.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP10.UP-LiPEH.mp4",
11:"http://173.249.8.202/home/STAR.VS.AS.FORCAS.DO.MAL.2015.T01.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP11.UP-LiPEH.mp4",
12:"http://173.249.8.202/home/STAR.VS.AS.FORCAS.DO.MAL.2015.T01.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP12.UP-LiPEH.mp4",
13:"http://173.249.8.202/home/STAR.VS.AS.FORCAS.DO.MAL.2015.T01.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP13.UP-LiPEH.mp4",
14:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP01-LiPEH.mp4",
15:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP02-LiPEH.mp4",
16:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP03-LiPEH.mp4",
17:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP04-LiPEH.mp4",
18:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP05-LiPEH.mp4",
19:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP06-LiPEH.mp4",
20:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP07-LiPEH.mp4",
21:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP08-LiPEH.mp4",
22:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP09-LiPEH.mp4",
23:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP10-LiPEH.mp4",
24:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP11-LiPEH.mp4",
25:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP12-LiPEH.mp4",
26:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP13-LiPEH.mp4",
27:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP14-LiPEH.mp4",
28:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP15-LiPEH.mp4",
29:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP16-LiPEH.mp4",
30:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP17-LiPEH.mp4",
31:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP18-LiPEH.mp4",
32:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP19-LiPEH.mp4",
33:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP20-LiPEH.mp4",
34:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP21-LiPEH.mp4",
35:"http://173.249.8.202/home/STARS.VS.AS.FORCAS.DO.MAL.2016.T02.COMPLETA.HDTV.X264.DUB.UP-LiPEH/EP22-LiPEH.mp4",

}

def createserverstar():
        eps = randint(1,35)
        ieps = 35 - eps

        if eps == 35:
                eps = eps - 10

        for j in range(eps,(eps+10)):
                
                file = open(""+m3u+"","a")
                eps = eng2sp[j]
                file.write(eps)
                file.write("\n")
                file.close

                
        xbmc.Player().play(""+m3u+"")

#import atualizar
#atualizar.Update(addonID)


