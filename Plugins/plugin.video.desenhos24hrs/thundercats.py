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




eng2sp = {1:"http://www.blogger.com/video-play.mp4?contentId=b7816fc9e0a93a21",
2:"http://www.blogger.com/video-play.mp4?contentId=43f9337524dee3f5",
3:"http://www.blogger.com/video-play.mp4?contentId=c18a96e78b4341d8",
4:"http://www.blogger.com/video-play.mp4?contentId=612acf5144dc903a",
5:"http://www.blogger.com/video-play.mp4?contentId=75589f33884dfb59",
6:"http://www.blogger.com/video-play.mp4?contentId=21a31b6d07916b48",
7:"http://www.blogger.com/video-play.mp4?contentId=4ab501108635f95b",
8:"http://www.blogger.com/video-play.mp4?contentId=346292636b997e73",
9:"http://www.blogger.com/video-play.mp4?contentId=983cb5bca8a94d3b",
10:"http://www.blogger.com/video-play.mp4?contentId=d32174e0fd963dae",
11:"http://www.blogger.com/video-play.mp4?contentId=45be517be621bba4",
12:"http://www.blogger.com/video-play.mp4?contentId=90866dee22b0dcf4",
13:"http://www.blogger.com/video-play.mp4?contentId=315b934dad5058b7",
14:"http://www.blogger.com/video-play.mp4?contentId=b0dc967d175bed4f",
15:"http://www.blogger.com/video-play.mp4?contentId=2a3da650c9de5edc",
16:"http://www.blogger.com/video-play.mp4?contentId=7031cde84247d602",
17:"http://www.blogger.com/video-play.mp4?contentId=662892837720dcfe",
18:"http://www.blogger.com/video-play.mp4?contentId=685e925fa91acf2e",
19:"http://www.blogger.com/video-play.mp4?contentId=6643285ae420d97b",
20:"http://www.blogger.com/video-play.mp4?contentId=b30471b040a63d0d",
21:"http://www.blogger.com/video-play.mp4?contentId=ff31a6ce5498ee2a",
22:"http://www.blogger.com/video-play.mp4?contentId=cf136efc6f9fd696",
23:"http://www.blogger.com/video-play.mp4?contentId=b8c925b5f8fad192",
24:"http://www.blogger.com/video-play.mp4?contentId=3f93d0c07214e30",
25:"http://www.blogger.com/video-play.mp4?contentId=744e83b05a2386b2",
26:"http://www.blogger.com/video-play.mp4?contentId=1b0c54f86d65d4d0",
27:"http://www.blogger.com/video-play.mp4?contentId=3b8c697b4e6fc71e",
28:"http://www.blogger.com/video-play.mp4?contentId=c0ce841e19a229a7",
29:"http://www.blogger.com/video-play.mp4?contentId=f5de924494c1dd53",
30:"http://www.blogger.com/video-play.mp4?contentId=921c4e1427abacc8",
31:"http://www.blogger.com/video-play.mp4?contentId=3ee6ef04cd46a980",
32:"http://www.blogger.com/video-play.mp4?contentId=20a6782b9cf3d1d0",
33:"http://www.blogger.com/video-play.mp4?contentId=f9984b6f15af2fa5",
34:"http://www.blogger.com/video-play.mp4?contentId=6b1d63ad3553b051",
35:"http://www.blogger.com/video-play.mp4?contentId=21b0043b4c95e2cf",
36:"http://www.blogger.com/video-play.mp4?contentId=3ea989c428a4b6ca",
37:"http://www.blogger.com/video-play.mp4?contentId=47f61a22e5509af7",
38:"http://www.blogger.com/video-play.mp4?contentId=af71f5ced22ef82f",
39:"http://www.blogger.com/video-play.mp4?contentId=a53fd861f7a3c061",
40:"http://www.blogger.com/video-play.mp4?contentId=44d41931fe8466f6",
41:"http://www.blogger.com/video-play.mp4?contentId=438ef899bc44b0c9",
42:"http://www.blogger.com/video-play.mp4?contentId=1dade5093cb60e13",
43:"http://www.blogger.com/video-play.mp4?contentId=4f8bcf7e37c834b7",
44:"http://www.blogger.com/video-play.mp4?contentId=f3b369965a5c657",
45:"http://www.blogger.com/video-play.mp4?contentId=77e2734443b5f234",
46:"http://www.blogger.com/video-play.mp4?contentId=91e5a30831b7f333",
47:"http://www.blogger.com/video-play.mp4?contentId=80fce1f69c09ca3f",
48:"http://www.blogger.com/video-play.mp4?contentId=2449b35a6061d212",
49:"http://www.blogger.com/video-play.mp4?contentId=c3e258676cfde054",
50:"http://www.blogger.com/video-play.mp4?contentId=c0b6a6b8231c33d5",
51:"http://www.blogger.com/video-play.mp4?contentId=45c6b82000510f58",
52:"http://www.blogger.com/video-play.mp4?contentId=6c0a2d90778c3eaa",
53:"http://www.blogger.com/video-play.mp4?contentId=f6342a04438eb9c7",
54:"http://www.blogger.com/video-play.mp4?contentId=e29e9edda90b76f5",
55:"http://www.blogger.com/video-play.mp4?contentId=f510bcf4813c5616",
56:"http://www.blogger.com/video-play.mp4?contentId=976a3e859653e892",
57:"http://www.blogger.com/video-play.mp4?contentId=c9eb8b05c2ab3c62",
58:"http://www.blogger.com/video-play.mp4?contentId=d5441ceb65a77f8a",
59:"http://www.blogger.com/video-play.mp4?contentId=4854e7750683cee6",
60:"http://www.blogger.com/video-play.mp4?contentId=7264806754dced78",
61:"http://www.blogger.com/video-play.mp4?contentId=50bccef1133f8a6a",
62:"http://www.blogger.com/video-play.mp4?contentId=cdcc1f9573de3de1",
63:"http://www.blogger.com/video-play.mp4?contentId=e01b4dee32793724",
64:"http://www.blogger.com/video-play.mp4?contentId=aa51b090a98ffcf3",
65:"http://www.blogger.com/video-play.mp4?contentId=ce9e81dbe19541d0",
66:"http://www.blogger.com/video-play.mp4?contentId=d9699a74a1c9627f",
67:"http://www.blogger.com/video-play.mp4?contentId=43f1460a4a5c5c23",
68:"http://www.blogger.com/video-play.mp4?contentId=35e46e8e0c15eded",
69:"http://www.blogger.com/video-play.mp4?contentId=3bff41457c94c849",
70:"http://www.blogger.com/video-play.mp4?contentId=67679a875751ae14",
71:"http://www.blogger.com/video-play.mp4?contentId=e6630016ec1bf5a7",
72:"http://www.blogger.com/video-play.mp4?contentId=e7421e53961d1fc1",
73:"http://www.blogger.com/video-play.mp4?contentId=134f8952e3c787be",
74:"http://www.blogger.com/video-play.mp4?contentId=ffc62f94f0a9b72b",
75:"http://www.blogger.com/video-play.mp4?contentId=743407b53d8c7b88",
76:"http://www.blogger.com/video-play.mp4?contentId=439f4b2821ed5fea",
77:"http://www.blogger.com/video-play.mp4?contentId=7428b152db81868d",
78:"http://www.blogger.com/video-play.mp4?contentId=198d52162e29560a",
79:"http://www.blogger.com/video-play.mp4?contentId=88a77c2511f11bf",
80:"http://www.blogger.com/video-play.mp4?contentId=3c8e3a7d53bb1458",
81:"http://www.blogger.com/video-play.mp4?contentId=105894d72546c668",
82:"http://www.blogger.com/video-play.mp4?contentId=e18cecade421ffea",
83:"http://www.blogger.com/video-play.mp4?contentId=3fcd3c983de727a4",
84:"http://www.blogger.com/video-play.mp4?contentId=adec30800516e86f",
85:"http://www.blogger.com/video-play.mp4?contentId=35406d0cfea40727",
86:"http://www.blogger.com/video-play.mp4?contentId=9845d9b08ccc0774",
87:"http://www.blogger.com/video-play.mp4?contentId=f9e039bc19913956",
88:"http://www.blogger.com/video-play.mp4?contentId=81ab3e3cbedd8063",
89:"http://www.blogger.com/video-play.mp4?contentId=3388b014af9f7a5f",
90:"http://www.blogger.com/video-play.mp4?contentId=9e57dae5cb32a523",
91:"http://www.blogger.com/video-play.mp4?contentId=c84eca194514e78f",
92:"http://www.blogger.com/video-play.mp4?contentId=427064daaba4e9fe",
93:"http://www.blogger.com/video-play.mp4?contentId=b750b504e3478cf9",
94:"http://www.blogger.com/video-play.mp4?contentId=6127ad59405ac5f8",
95:"http://www.blogger.com/video-play.mp4?contentId=35ffe3ac805a245e",
96:"http://www.blogger.com/video-play.mp4?contentId=1616a536c4bb3205",
97:"http://www.blogger.com/video-play.mp4?contentId=a6352292555cd6db",
98:"http://www.blogger.com/video-play.mp4?contentId=a18cfa2594725aaf",
99:"http://www.blogger.com/video-play.mp4?contentId=d9fa053a3f6b5f8",
100:"http://www.blogger.com/video-play.mp4?contentId=99ef87da31947a1c",
101:"http://www.blogger.com/video-play.mp4?contentId=539b60457debbda2",
102:"http://www.blogger.com/video-play.mp4?contentId=d0ce5b1e027b9cbd",
103:"http://www.blogger.com/video-play.mp4?contentId=609115bdd32654a3",
104:"http://www.blogger.com/video-play.mp4?contentId=923198d8355bcfef",
105:"http://www.blogger.com/video-play.mp4?contentId=96e74602e321d604",
106:"http://www.blogger.com/video-play.mp4?contentId=6438c5d0bc94f62b",
107:"http://www.blogger.com/video-play.mp4?contentId=473ca6ccdeeefda6",
108:"http://www.blogger.com/video-play.mp4?contentId=6438c5d0bc94f62b",
109:"http://www.blogger.com/video-play.mp4?contentId=bc9e4b02a22da9ff",
110:"http://www.blogger.com/video-play.mp4?contentId=d79722bfe66e35ea",
111:"http://www.blogger.com/video-play.mp4?contentId=b278110ee448eb29",
112:"http://www.blogger.com/video-play.mp4?contentId=c23580f52538b1fd",
113:"http://www.blogger.com/video-play.mp4?contentId=8a3ff5125965e422",
114:"http://www.blogger.com/video-play.mp4?contentId=cae8d666c28e010d",
115:"http://www.blogger.com/video-play.mp4?contentId=fa25fd66519786b1",
116:"http://www.blogger.com/video-play.mp4?contentId=34bc0e794b215e",
117:"http://www.blogger.com/video-play.mp4?contentId=fa7b2fb88954302f",
118:"http://www.blogger.com/video-play.mp4?contentId=f7fafb8f7ddf2663",
119:"http://www.blogger.com/video-play.mp4?contentId=a5deeb722518b330",
120:"http://www.blogger.com/video-play.mp4?contentId=d24542d58d4a0f6f",
121:"http://www.blogger.com/video-play.mp4?contentId=69d709a9cfdccdcd",
122:"http://www.blogger.com/video-play.mp4?contentId=ec3b37842e342d06",
123:"http://www.blogger.com/video-play.mp4?contentId=8cad09c41d178ffb",
124:"http://www.blogger.com/video-play.mp4?contentId=c58501bfdfa05d96",
125:"http://www.blogger.com/video-play.mp4?contentId=8f20ec8294808724",
126:"http://www.blogger.com/video-play.mp4?contentId=2290ee9576110f3f",
127:"http://www.blogger.com/video-play.mp4?contentId=537a4bfde6e4c4dc",
128:"http://www.blogger.com/video-play.mp4?contentId=c346350df3fe5ccc",
129:"http://www.blogger.com/video-play.mp4?contentId=c492b0651dc5d928",
130:"http://www.blogger.com/video-play.mp4?contentId=e19dd8dd27b9c5bb",
}

def createserverthunder():
        eps = randint(1,130)
        ieps = 35 - eps

        if eps == 35:
                eps = eps - 10

        if eps > 129:
                eps = eps - 129

        for j in range(eps,(eps+35)):
                
                file = open(""+m3u+"","a")
                eps = eng2sp[j]
                file.write(eps)
                file.write("\n")
                file.close

                
        xbmc.Player().play(""+m3u+"")

#import atualizar
#atualizar.Update(addonID)


