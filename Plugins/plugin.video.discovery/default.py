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
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.discovery'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
#entryurl=resfolder+"entrada.mp4"
entryurl=""
YOUTUBE_CHANNEL_ID1=  "user/discoverybrasil"
YOUTUBE_CHANNEL_ID2=  "user/discoverymulherhh"
YOUTUBE_CHANNEL_ID3=  "channel/UCb7mSDa6UVj6ZEbvpd8_iyg"
YOUTUBE_CHANNEL_ID4=  "user/DCnosferahcorp"

icon1 = "https://yt3.ggpht.com/a-/AAuE7mBXxSGTn11TtO8iBCzLWxo5eCoSMeFa59Dq4Q=s256-mo-c-c0xffffffff-rj-k-no"
icon2 = "https://yt3.ggpht.com/a-/AAuE7mBGn7t0WJqAVmyw95w7SOJsRbT0lcq1LwFTgw=s256-mo-c-c0xffffffff-rj-k-no"
icon3 = "https://yt3.ggpht.com/a-/AAuE7mDX-RF_d1vhBxb_8mlUiQ9gqpGvYPmZ7dEvQA=s256-mo-c-c0xffffffff-rj-k-no"
icon4 = "https://yt3.ggpht.com/a-/AAuE7mCYc0-il8hhJXhY6tPZ2VLGcyfCZu6w6LFF3Q=s256-mo-c-c0xffffffff-rj-k-no"


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
	plugintools.log("discoverysnacks.main_list "+repr(params))
	
	plugintools.log("discoverysnacks.run")
	
	#plugintools.direct_play(str(entryurl))

	plugintools.add_item(
		title = "Discovery Brasil",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/",
		thumbnail = icon1,
		folder = True )


	plugintools.add_item(
		title = "Discovery Home & Health Brasil",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID2+"/",
		thumbnail = icon2,
		folder = True )

	plugintools.add_item(
		title = "Discovery Kids Brasil",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID3+"/",
		thumbnail = icon3,
		folder = True )

	plugintools.add_item(
		title = "Discovery Documentarios [Fan]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID4+"/",
		thumbnail = icon4,
		folder = True )

run()
