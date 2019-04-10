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




eng2sp = {1:"http://www.blogger.com/video-play.mp4?contentId=64797ed2cb609777",
2:"http://www.blogger.com/video-play.mp4?contentId=9c702aab5c4c6b82",
3:"http://www.blogger.com/video-play.mp4?contentId=84dfd172c5d51678",
4:"http://www.blogger.com/video-play.mp4?contentId=cb4503bf71f2ef31",
5:"http://www.blogger.com/video-play.mp4?contentId=ef1c4d6bf234406e",
6:"http://www.blogger.com/video-play.mp4?contentId=78f566d5727887f2",
7:"http://www.blogger.com/video-play.mp4?contentId=dba3850adead2746",
8:"http://www.blogger.com/video-play.mp4?contentId=60d65f4fc81cdfe6",
9:"http://www.blogger.com/video-play.mp4?contentId=d0fa13ddc7da8948",
10:"http://www.blogger.com/video-play.mp4?contentId=150f49b458be37e3",
11:"http://www.blogger.com/video-play.mp4?contentId=5b480ca80d4cb49e",
12:"http://www.blogger.com/video-play.mp4?contentId=9fa9d4aaf45ff59b",
13:"http://www.blogger.com/video-play.mp4?contentId=d2fb31a62e69c39",
14:"http://www.blogger.com/video-play.mp4?contentId=c627d02489920487",
15:"http://www.blogger.com/video-play.mp4?contentId=fc238525751a8cbb",
16:"http://www.blogger.com/video-play.mp4?contentId=700b4d7618faeead",
17:"http://www.blogger.com/video-play.mp4?contentId=acb031a4023c7f63",
18:"http://www.blogger.com/video-play.mp4?contentId=fbe66d3068b6d203",
19:"http://www.blogger.com/video-play.mp4?contentId=c3ebd5250947c1fa",
20:"http://www.blogger.com/video-play.mp4?contentId=fb3de87a22ea4279",
21:"http://www.blogger.com/video-play.mp4?contentId=5aeba3324bfc180e",
22:"http://www.blogger.com/video-play.mp4?contentId=48203f8d99c5a835",
23:"http://www.blogger.com/video-play.mp4?contentId=34a6cefd35d5ac87",
24:"http://www.blogger.com/video-play.mp4?contentId=b3f6b2b8755ed566",
25:"http://www.blogger.com/video-play.mp4?contentId=8c78699dccdf720b",
26:"http://www.blogger.com/video-play.mp4?contentId=1e60c9d1172ab708",
27:"http://www.blogger.com/video-play.mp4?contentId=dfe0805aa04ed044",
28:"http://www.blogger.com/video-play.mp4?contentId=87e2a2a114694ac1",
29:"http://www.blogger.com/video-play.mp4?contentId=f5debf37a12f39bc",
30:"http://www.blogger.com/video-play.mp4?contentId=73d2cb7ccfeb3807",
31:"http://www.blogger.com/video-play.mp4?contentId=e5755f27cbc42ca0",
32:"http://www.blogger.com/video-play.mp4?contentId=ab852fccdb11e5f2",
33:"http://www.blogger.com/video-play.mp4?contentId=ef0e9a9d0bc116bd",
34:"http://www.blogger.com/video-play.mp4?contentId=c6a93158c556af88",
35:"http://www.blogger.com/video-play.mp4?contentId=6cbaa46248155db0",
36:"http://www.blogger.com/video-play.mp4?contentId=2202dc05c6c14497",
37:"http://www.blogger.com/video-play.mp4?contentId=dc231d0681a28aad",
38:"http://www.blogger.com/video-play.mp4?contentId=fd54eab665c3e39c",
39:"http://www.blogger.com/video-play.mp4?contentId=ccdad92c08243c9a",
40:"http://www.blogger.com/video-play.mp4?contentId=caf8a7ef9dfec4b7",
41:"http://www.blogger.com/video-play.mp4?contentId=646c75205340f1b4",
42:"http://www.blogger.com/video-play.mp4?contentId=91ab42020496b926",
43:"http://www.blogger.com/video-play.mp4?contentId=8e04d8be5182581",
44:"http://www.blogger.com/video-play.mp4?contentId=d77e524fa68e4338",
45:"http://www.blogger.com/video-play.mp4?contentId=14bdd0b0d5e7e707",
46:"http://www.blogger.com/video-play.mp4?contentId=c4173ba119ccb98e",
47:"http://www.blogger.com/video-play.mp4?contentId=ae6325470aa9f72e",
48:"http://www.blogger.com/video-play.mp4?contentId=f94b4a4245a43bfe",
49:"http://www.blogger.com/video-play.mp4?contentId=b3993730673831b7",
50:"http://www.blogger.com/video-play.mp4?contentId=9e60ee765455dac2",
51:"http://www.blogger.com/video-play.mp4?contentId=b0c7f419e4cdee1",
52:"http://www.blogger.com/video-play.mp4?contentId=1368045f58aebd16",
53:"http://www.blogger.com/video-play.mp4?contentId=4ec85f965fdb8ed5",
54:"http://www.blogger.com/video-play.mp4?contentId=516568c2293b5be9",
55:"http://www.blogger.com/video-play.mp4?contentId=e9ef13140e5274bf",
56:"http://www.blogger.com/video-play.mp4?contentId=4047c0107be3ee0b",
57:"http://www.blogger.com/video-play.mp4?contentId=fa0f91722b71106e",
58:"http://www.blogger.com/video-play.mp4?contentId=557562ad4dd938dc",
59:"http://www.blogger.com/video-play.mp4?contentId=9bbe2e19dae2e563",
60:"http://www.blogger.com/video-play.mp4?contentId=e825e2b13975b810",
61:"http://www.blogger.com/video-play.mp4?contentId=ccf9502e7a179ace",
62:"http://www.blogger.com/video-play.mp4?contentId=99e0bdbc6d60fa37",
63:"http://www.blogger.com/video-play.mp4?contentId=abc2f318a8716fe5",
64:"http://www.blogger.com/video-play.mp4?contentId=7761c79feeaee155",
65:"http://www.blogger.com/video-play.mp4?contentId=24f8355b78224326",
66:"http://www.blogger.com/video-play.mp4?contentId=12a9065a30681afc",
67:"http://www.blogger.com/video-play.mp4?contentId=aa5862e9c386172d",
68:"http://www.blogger.com/video-play.mp4?contentId=a7daed1ccd2565ce",
69:"http://www.blogger.com/video-play.mp4?contentId=9d97fa38fdb8d9cd",
70:"http://www.blogger.com/video-play.mp4?contentId=2d10c11259252fcd",
71:"http://www.blogger.com/video-play.mp4?contentId=8000294cd4b65e9f",
72:"http://www.blogger.com/video-play.mp4?contentId=43eefa484ad047c2",
73:"http://www.blogger.com/video-play.mp4?contentId=e321c2f64ba1147c",
74:"http://www.blogger.com/video-play.mp4?contentId=9dc3725053e19c4d",
75:"http://www.blogger.com/video-play.mp4?contentId=a235a37b3e3da871",
76:"http://www.blogger.com/video-play.mp4?contentId=82475b664fa03025",
77:"http://www.blogger.com/video-play.mp4?contentId=405217ae7f5b0ce2",
78:"http://www.blogger.com/video-play.mp4?contentId=c510a1ab6e747212",
79:"http://www.blogger.com/video-play.mp4?contentId=adc606f47d168087",
80:"http://www.blogger.com/video-play.mp4?contentId=395fca3ec726a730",
81:"http://www.blogger.com/video-play.mp4?contentId=96aa4f4c9e461897",
82:"http://www.blogger.com/video-play.mp4?contentId=96aa4f4c9e461897",           
}

def createserverfmbob():
        eps = randint(1,81)
        ieps = 35 - eps

        if eps == 81:
                eps = eps - 25

        if eps > 82:
                eps = eps - 81

        for j in range(eps,(eps+25)):
                
                file = open(""+m3u+"","a")
                eps = eng2sp[j]
                file.write(eps)
                file.write("\n")
                file.close

                
        xbmc.Player().play(""+m3u+"")

#import atualizar
#atualizar.Update(addonID)


