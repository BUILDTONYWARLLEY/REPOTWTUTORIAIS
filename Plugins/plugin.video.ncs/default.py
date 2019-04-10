# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/ncs
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import os
import sys
import time
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.ncs'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=resfolder+"entrada.mp4"
#Meu canal apartir user/Joyce3329

YOUTUBE_CHANNEL_ID1 = "PLRBp0Fe2GpgnZOm5rCopMAOYhZCPoUyO5"
YOUTUBE_CHANNEL_ID2 = "PLRBp0Fe2GpglkzuspoGv-mu7B2ce9_0Fn"
YOUTUBE_CHANNEL_ID3 = "PLRBp0Fe2GpglDkRdEd_BhnSkHo8FgPmzs"
YOUTUBE_CHANNEL_ID4 = "PLRBp0Fe2GpgnXJ2owag81mqSFklL83-d5"
YOUTUBE_CHANNEL_ID5 = "PLRBp0Fe2Gpgm0WF6DEGmb7ab4qHAGlPzg"
YOUTUBE_CHANNEL_ID6 = "PLRBp0Fe2GpglTnOLbhyrHAVaWsCIEX53Y"
YOUTUBE_CHANNEL_ID7 = "PLRBp0Fe2Gpgm57nFVNM7qYZ9u64U9Q-Bf"
YOUTUBE_CHANNEL_ID8 = "PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK"
YOUTUBE_CHANNEL_ID9 = "PLRBp0Fe2GpgnzYdHtTCoBYPyIJG9_opMn"

icon1				= "http://i.ytimg.com/vi/tua4SVV-GSE/hqdefault.jpg"
icon2 				= "http://i.ytimg.com/vi/-xKKo7t72Tg/hqdefault.jpg"
icon3 				= "http://i.ytimg.com/vi/7wNb0pHyGuI/hqdefault.jpg"
icon4 				= "http://i.ytimg.com/vi/bKG2RFUmATs/hqdefault.jpg"
icon5 				= "http://i.ytimg.com/vi/dXYFK-jEr8Y/hqdefault.jpg"
icon6 				= "http://i.ytimg.com/vi/0E6KXgWuaHo/hqdefault.jpg"
icon7               = "http://i.ytimg.com/vi/7t8lRdpv5IQ/hqdefault.jpg"
icon8 				= "http://i.ytimg.com/vi/yPPuloAGvwA/hqdefault.jpg"
icon9 				= "http://i.ytimg.com/vi/UFEi2FOMXVs/hqdefault.jpg"
# Ponto de Entrada
def run():
	# Pega Parâmetros
	params = plugintools.get_params()
	
	if params.get("action") is None:
		xbmc.Player().play(entryurl)
		
		while xbmc.Player().isPlaying():
			time.sleep(1)

		main_list(params)
	else:
		action = params.get("action")
		exec action+"(params)"

	plugintools.close_item_list()

# Menu Principal
def main_list(params):
	plugintools.log("ncs.main_list "+repr(params))
	
	plugintools.log("ncs.run")
	
	#plugintools.direct_play(str(entryurl))

	plugintools.add_item(
		title = "NCS Electronic",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID1+"/",
		thumbnail = icon1,
		folder = True )
		
	plugintools.add_item(
		title = "NCS Indie Dance",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID2+"/",
		thumbnail = icon2,
		folder = True )
		
	plugintools.add_item(
		title = "NCS Tobu",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID3+"/",
		thumbnail = icon3,
		folder = True )
		
	plugintools.add_item(
		title = "NCS Hardstyle",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID4+"/",
		thumbnail = icon4,
		folder = True )
	
	plugintools.add_item(
		title = "NCS Trap",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID5+"/",
		thumbnail = icon5,
		folder = True )
		
	plugintools.add_item(
		title = "NCS Drumstep",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID6+"/",
		thumbnail = icon6,
		folder = True )
	
	plugintools.add_item(
		title = "NCS Melodic Dubstep",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID7+"/",
		thumbnail = icon7,
		folder = True )
		
	plugintools.add_item(
		title = "NCS House",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID8+"/",
		thumbnail = icon8,
		folder = True )
		
	plugintools.add_item(
		title = "NCS: Drum&Bass",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID9+"/",
		thumbnail = icon9,
		folder = True )
run()
