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

addonID = 'plugin.video.copadonordeste'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=""


YOUTUBE_CHANNEL_ID2=  "channel/UCP-vp1zdHOa9k2hN_nMT9TA/playlists"
YOUTUBE_CHANNEL_ID3=  "channel/UCP-vp1zdHOa9k2hN_nMT9TA/live"


icon2 = "https://yt3.ggpht.com/a-/AAuE7mC8JQIfEAY2vnlKXtBpHh6k4r6PvpylpTxiyw=s256-mo-c-c0xffffffff-rj-k-no"




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
	plugintools.log("copadonordeste.main_list "+repr(params))
	
	plugintools.log("copadonordeste.run")
	
	#plugintools.direct_play(str(entryurl))

	plugintools.add_item(
		title = "Canal Copa do Nordeste",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID2+"/",
		thumbnail = icon2,
		folder = True )

	plugintools.add_item(
		title = "Ao Vivo [Dia de Jogo]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID3+"/",
		thumbnail = icon2,
		folder = True )



	

run()
