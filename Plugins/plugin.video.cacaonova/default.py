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

addonID = 'plugin.video.cacaonova'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=""

YOUTUBE_CHANNEL_ID1=  "channel/UCd_7pYLjCvv9Ms40_4ATVqw/playlists"
YOUTUBE_CHANNEL_ID2=  "channel/UCVrKQMmA2ew9LFzeIDaOFgw/playlists"
YOUTUBE_CHANNEL_ID3=  "channel/UCVrKQMmA2ew9LFzeIDaOFgw/live"
YOUTUBE_CHANNEL_ID4=  "channel/UCUD3lbUojOMbFBBSsUN1yYg/playlists"
YOUTUBE_CHANNEL_ID5=  "channel/UC6V9mqiVuzd-v3ozUfCtZFA/playlists"

icon2 = "https://yt3.ggpht.com/a-/AAuE7mAWyx20wWyZOPXo5bxtFZPvJRLKO_y7Tx4Z9A=s256-mo-c-c0xffffffff-rj-k-no"
icon3 = "https://yt3.ggpht.com/a-/AAuE7mBXaXrEuNN6dqnNqvMQ6c9AzC6vtgTTO4wmzw=s256-mo-c-c0xffffffff-rj-k-no"
icon4 = "https://yt3.ggpht.com/a-/AAuE7mCp5a0NsoLWOeB9p2OCP9iRX4bTP3kFk_z9XQ=s256-mo-c-c0xffffffff-rj-k-no"


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
	plugintools.log("cancaonova.main_list "+repr(params))
	
	plugintools.log("cancaonova.run")
	
	#plugintools.direct_play(str(entryurl))

	plugintools.add_item(
		title = "Canal Canção Nova",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/",
		thumbnail = icon2,
		folder = True )

	plugintools.add_item(
		title = "Tv Canção Nova",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID2+"/",
		thumbnail = icon3,
		folder = True )

	plugintools.add_item(
		title = "Canção Nova Oficial",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID5+"/",
		thumbnail = icon3,
		folder = True )

	plugintools.add_item(
		title = "Canção Nova Kids",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID4+"/",
		thumbnail = icon4,
		folder = True )

	

run()
