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




eng2sp = {1:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.01.Tom&Jerry.CP.PradO.avi",
2:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.02.Tom&Jerry.CP.PradO.avi",
3:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.03.Tom&Jerry.CP.PradO.avi",
4:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.04.Tom&Jerry.CP.PradO.avi",
5:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.05.Tom&Jerry.CP.PradO.avi",
6:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.06.Tom&Jerry.CP.PradO.avi",
7:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.07.Tom&Jerry.CP.PradO.avi",
8:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.08.Tom&Jerry.CP.PradO.avi",
9:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.09.Tom&Jerry.CP.PradO.avi",
10:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.10.Tom&Jerry.CP.PradO.avi",
11:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.11.Tom&Jerry.CP.PradO.avi",
12:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.12.Tom&Jerry.CP.PradO.avi",
13:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.13.Tom&Jerry.CP.PradO.avi",
14:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.14.Tom&Jerry.CP.PradO.avi",
15:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.15.Tom&Jerry.CP.PradO.avi",
16:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.16.Tom&Jerry.CP.PradO.avi",
17:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.17.Tom&Jerry.CP.PradO.avi",
18:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.18.Tom&Jerry.CP.PradO.avi",
19:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.19.Tom&Jerry.CP.PradO.avi",
20:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.20.Tom&Jerry.CP.PradO.avi",
21:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.21.Tom&Jerry.CP.PradO.avi",
22:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.22.Tom&Jerry.CP.PradO.avi",
23:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.23.Tom&Jerry.CP.PradO.avi",
24:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.24.Tom&Jerry.CP.PradO.avi",
25:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.25.Tom&Jerry.CP.PradO.avi",
26:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.26.Tom&Jerry.CP.PradO.avi",
27:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.27.Tom&Jerry.CP.PradO.avi",
28:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.28.Tom&Jerry.CP.PradO.avi",
29:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.29.Tom&Jerry.CP.PradO.avi",
30:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.30.Tom&Jerry.CP.PradO.avi",
31:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.31.Tom&Jerry.CP.PradO.avi",
32:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.32.Tom&Jerry.CP.PradO.avi",
33:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.33.Tom&Jerry.CP.PradO.avi",
34:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.34.Tom&Jerry.CP.PradO.avi",
35:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.35.Tom&Jerry.CP.PradO.avi",
36:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.36.Tom&Jerry.CP.PradO.avi",
37:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.37.Tom&Jerry.CP.PradO.avi",
38:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.38.Tom&Jerry.CP.PradO.avi",
39:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.39.Tom&Jerry.CP.PradO.avi",
40:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.40.Tom&Jerry.CP.PradO.avi",
41:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.41.Tom&Jerry.CP.PradO.avi",
42:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.42.Tom&Jerry.CP.PradO.avi",
43:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.43.Tom&Jerry.CP.PradO.avi",
44:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.44.Tom&Jerry.CP.PradO.avi",
45:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.45.Tom&Jerry.CP.PradO.avi",
46:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.46.Tom&Jerry.CP.PradO.avi",
47:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.47.Tom&Jerry.CP.PradO.avi",
48:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.48.Tom&Jerry.CP.PradO.avi",
49:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.49.Tom&Jerry.CP.PradO.avi",
50:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.50.Tom&Jerry.CP.PradO.avi",
51:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.51.Tom&Jerry.CP.PradO.avi",
52:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.52.Tom&Jerry.CP.PradO.avi",
53:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.53.Tom&Jerry.CP.PradO.avi",
54:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.54.Tom&Jerry.CP.PradO.avi",
55:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.55.Tom&Jerry.CP.PradO.avi",
56:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.56.Tom&Jerry.CP.PradO.avi",
57:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.57.Tom&Jerry.CP.PradO.avi",
58:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.58.Tom&Jerry.CP.PradO.avi",
59:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.59.Tom&Jerry.CP.PradO.avi",
60:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.60.Tom&Jerry.CP.PradO.avi",
61:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.61.Tom&Jerry.CP.PradO.avi",
62:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.62.Tom&Jerry.CP.PradO.avi",
63:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.63.Tom&Jerry.CP.PradO.avi",
64:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.64.Tom&Jerry.CP.PradO.avi",
65:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.65.Tom&Jerry.CP.PradO.avi",
66:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.66.Tom&Jerry.CP.PradO.avi",
67:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.67.Tom&Jerry.CP.PradO.avi",
68:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.68.Tom&Jerry.CP.PradO.avi",
69:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.69.Tom&Jerry.CP.PradO.avi",
70:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.70.Tom&Jerry.CP.PradO.avi",
71:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.71.Tom&Jerry.CP.PradO.avi",
72:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.72.Tom&Jerry.CP.PradO.avi",
73:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.73.Tom&Jerry.CP.PradO.avi",
74:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.74.Tom&Jerry.CP.PradO.avi",
75:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.75.Tom&Jerry.CP.PradO.avi",
76:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.76.Tom&Jerry.CP.PradO.avi",
77:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.77.Tom&Jerry.CP.PradO.avi",
78:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.78.Tom&Jerry.CP.PradO.avi",
79:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.79.Tom&Jerry.CP.PradO.avi",
80:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.80.Tom&Jerry.CP.PradO.avi",
81:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.81.Tom&Jerry.CP.PradO.avi",
82:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.82.Tom&Jerry.CP.PradO.avi",
83:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.83.Tom&Jerry.CP.PradO.avi",
84:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.84.Tom&Jerry.CP.PradO.avi",
85:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.85.Tom&Jerry.CP.PradO.avi",
86:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.86.Tom&Jerry.CP.PradO.avi",
87:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.87.Tom&Jerry.CP.PradO.avi",
88:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.88.Tom&Jerry.CP.PradO.avi",
89:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.89.Tom&Jerry.CP.PradO.avi",
90:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.90.Tom&Jerry.CP.PradO.avi",
91:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.91.Tom&Jerry.CP.PradO.avi",
92:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.92.Tom&Jerry.CP.PradO.avi",
93:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.93.Tom&Jerry.CP.PradO.avi",
94:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.94.Tom&Jerry.CP.PradO.avi",
95:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.95.Tom&Jerry.CP.PradO.avi",
96:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.96.Tom&Jerry.CP.PradO.avi",
97:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.97.Tom&Jerry.CP.PradO.avi",
98:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.98.Tom&Jerry.CP.PradO.avi",
99:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.99.Tom&Jerry.CP.PradO.avi",
100:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.100.Tom&Jerry.CP.PradO.avi",
101:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.101.Tom&Jerry.CP.PradO.avi",
102:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.102.Tom&Jerry.CP.PradO.avi",
103:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.103.Tom&Jerry.CP.PradO.avi",
104:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.104.Tom&Jerry.CP.PradO.avi",
105:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.105.Tom&Jerry.CP.PradO.avi",
106:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.106.Tom&Jerry.CP.PradO.avi",
107:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.108.Tom&Jerry.CP.PradO.avi",
108:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.109.Tom&Jerry.CP.PradO.avi",
109:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.110.Tom&Jerry.CP.PradO.avi",
110:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.111.Tom&Jerry.CP.PradO.avi",
111:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.112.Tom&Jerry.CP.PradO.avi",
112:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.113.Tom&Jerry.CP.PradO.avi",
113:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.114.Tom&Jerry.CP.PradO.avi",
114:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.115.Tom&Jerry.CP.PradO.avi",
115:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.116.Tom&Jerry.CP.PradO.avi",
116:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.117.Tom&Jerry.CP.PradO.avi",
117:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.118.Tom&Jerry.CP.PradO.avi",
118:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.119.Tom&Jerry.CP.PradO.avi",
119:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.120.Tom&Jerry.CP.PradO.avi",
120:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.121.Tom&Jerry.CP.PradO.avi",
121:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.122.Tom&Jerry.CP.PradO.avi",
122:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.123.Tom&Jerry.CP.PradO.avi",
123:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.124.Tom&Jerry.CP.PradO.avi",
124:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.125.Tom&Jerry.CP.PradO.avi",
125:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.126.Tom&Jerry.CP.PradO.avi",
126:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.127.Tom&Jerry.CP.PradO.avi",
127:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.128.Tom&Jerry.CP.PradO.avi",
128:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.129.Tom&Jerry.CP.PradO.avi",
129:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.130.Tom&Jerry.CP.PradO.avi",
130:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.131.Tom&Jerry.CP.PradO.avi",
131:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.132.Tom&Jerry.CP.PradO.avi",
132:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.133.Tom&Jerry.CP.PradO.avi",
133:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.134.Tom&Jerry.CP.PradO.avi",
134:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.135.Tom&Jerry.CP.PradO.avi",
135:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.136.Tom&Jerry.CP.PradO.avi",
136:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.137.Tom&Jerry.CP.PradO.avi",
137:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.138.Tom&Jerry.CP.PradO.avi",
138:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.139.Tom&Jerry.CP.PradO.avi",
139:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.140.Tom&Jerry.CP.PradO.avi",
140:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.141.Tom&Jerry.CP.PradO.avi",
141:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.142.Tom&Jerry.CP.PradO.avi",
142:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.143.Tom&Jerry.CP.PradO.avi",
143:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.144.Tom&Jerry.CP.PradO.avi",
144:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.145.Tom&Jerry.CP.PradO.avi",
145:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.146.Tom&Jerry.CP.PradO.avi",
146:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.147.Tom&Jerry.CP.PradO.avi",
147:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.148.Tom&Jerry.CP.PradO.avi",
148:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.149.Tom&Jerry.CP.PradO.avi",
149:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.150.Tom&Jerry.CP.PradO.avi",
150:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.151.Tom&Jerry.CP.PradO.avi",
151:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.152.Tom&Jerry.CP.PradO.avi",
152:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.153.Tom&Jerry.CP.PradO.avi",
153:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.154.Tom&Jerry.CP.PradO.avi",
154:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.155.Tom&Jerry.CP.PradO.avi",
155:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.156.Tom&Jerry.CP.PradO.avi",
156:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.157.Tom&Jerry.CP.PradO.avi",
157:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.158.Tom&Jerry.CP.PradO.avi",
158:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.159.Tom&Jerry.CP.PradO.avi",
159:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.160.Tom&Jerry.CP.PradO.avi",
160:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.161.Tom&Jerry.CP.PradO.avi",
161:"http://173.249.8.202/home/Tom&Jerry.DVDRip.1940-2005.CF.PradO/Epis%C3%B3dios/Ep.162.Tom&Jerry.CP.PradO.avi",}

def createservertom():
        eps = randint(1,161)
        ieps = 35 - eps

        if eps == 161:
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


