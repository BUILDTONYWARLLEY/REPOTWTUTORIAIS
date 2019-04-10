# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/gsfvideos
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

addonID = 'plugin.video.musicbrazuka'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
#icon = local.getAddonInfo('icon')
icon = local.getAddonInfo('icon')
icon2 = "https://cld.pt/dl/download/ec393cac-fc13-444f-b74d-5c946d616fb4/ROCKSHOWS.jpg?download=true"
icon3 = "https://cld.pt/dl/download/7dc89445-f3a6-47a2-ada9-e2a1487037ce/REGGAESHOWS.jpg?download=true"
icon4 = "https://cld.pt/dl/download/5c94fa07-d5e9-4f09-8208-195155600c5a/POPSHOWS.jpg?download=true"
icon5 = "https://cld.pt/dl/download/d755742d-03ef-4912-87c2-63a2abf4831f/MPBSHOWS.jpg?download=true"
icon6 = "https://cld.pt/dl/download/12c69723-084a-49dc-8435-a1b7ac70d55c/ROCKCLIPES.jpg?download=true"
icon7 = "https://cld.pt/dl/download/427b27cd-03e3-42a1-8a28-12c6c97cca91/REGGAECLIPES.jpg?download=true"
icon8 = "https://cld.pt/dl/download/30a041dc-c942-4d67-8a35-e1456c0d227d/POPCLIPES.jpg?download=true"
icon9 = "https://cld.pt/dl/download/65d25019-5745-4b99-aa18-e7caf9a75df1/MPBCLIPES.jpg?download=true"
icon10 = "https://cld.pt/dl/download/60a0c574-1ee9-486b-8be4-d86ad8550ff9/SAMBASHOWS.jpg?download=true"
icon11 = "https://cld.pt/dl/download/f7b83221-dcbc-4616-972c-e69515962531/PAGODESHOWS.jpg?download=true"
icon12 = "https://cld.pt/dl/download/c58aaa94-2e4b-43a4-98a7-168286c183ec/SAMBACLIPES.jpg?download=true"
icon13 = "https://cld.pt/dl/download/588aa96c-4657-4123-b202-2e65605e822f/PAGODECLIPES.jpg?download=true"
icon14 = "https://cld.pt/dl/download/2f13aef2-89a1-42b5-bb84-8a54551eeec6/AXESHOWS.jpg?download=true"
icon15 = "https://cld.pt/dl/download/b1e7d9a2-1a2e-4cba-947e-7be24f16b738/AXECLIPES.jpg?download=true"
addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=resfolder+"entrada.mp4"
YOUTUBE_CHANNEL_ID = "playlist/PLNtZ1Pn1y2b5vj5YXmTERxBySUBgmBMe6"
YOUTUBE_CHANNEL_ID2 = "playlist/PLNtZ1Pn1y2b4jZanoQrvNpt3Fk0zfuWsD"
YOUTUBE_CHANNEL_ID3 = "playlist/PLNtZ1Pn1y2b7eLcsSRG9vmigxB3H7WYD5"
YOUTUBE_CHANNEL_ID4 = "playlist/PLNtZ1Pn1y2b4UhF8bEYpsjpN6EDqbjenU"
YOUTUBE_CHANNEL_ID5 = "playlist/PLNtZ1Pn1y2b6kznAfiEDzi7spHhtgS0B0"
YOUTUBE_CHANNEL_ID6 = "playlist/PLNtZ1Pn1y2b5AY2QZJrNf77_gsz95vCTE"
YOUTUBE_CHANNEL_ID7 = "playlist/PLNtZ1Pn1y2b59gJLFyKYnx2rR6DjL2mpA"
YOUTUBE_CHANNEL_ID8 = "playlist/PLNtZ1Pn1y2b6lZXDp9JGu9UUZi8Ay106d"
YOUTUBE_CHANNEL_ID9 = "playlist/PLNtZ1Pn1y2b41Mp2LQTddWZLFJbBtSLfA"
YOUTUBE_CHANNEL_ID10 = "playlist/PLNtZ1Pn1y2b4bCoBz0Q99Y0u4308v7jP7"
YOUTUBE_CHANNEL_ID11 = "playlist/PLNtZ1Pn1y2b78ykVsGGsUPf69mDscyOcb"
YOUTUBE_CHANNEL_ID12 = "playlist/PLNtZ1Pn1y2b5skTe6wGuJrgBTx1qAwSll"
YOUTUBE_CHANNEL_ID13 = "playlist/PLNtZ1Pn1y2b5f2zKOiwx0HKAEWM0_623h"
YOUTUBE_CHANNEL_ID14 = "playlist/PLNtZ1Pn1y2b5TDWVTRIR5PToZSKqORmMJ"


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
	plugintools.log("musicbrazuka.main_list "+repr(params))
	
	plugintools.log("musicbrazuka.run")
	
	#plugintools.direct_play(str(entryurl))

plugintools.add_item(
		title = "[B][COLOR yellow]ROCK [COLOR green]SHOWS COMPLETOS[/COLOR][/B]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID+"/",
		thumbnail = icon2,
		folder = True )
		
plugintools.add_item(
		title = "[B][COLOR yellow]REGGAE [COLOR green]SHOWS COMPLETOS[/COLOR][/B]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID2+"/",
		thumbnail = icon3,
		folder = True )

plugintools.add_item(
		title = "[B][COLOR yellow]POP [COLOR green]SHOWS COMPLETOS[/COLOR][/B] ",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID3+"/",
		thumbnail = icon4,
		folder = True )		

plugintools.add_item(
		title = "[B][COLOR yellow]MPB [COLOR green]SHOWS COMPLETOS[/COLOR][/B]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID4+"/",
		thumbnail = icon5,
		folder = True )		

plugintools.add_item(
		title = "[B][COLOR yellow]SAMBA [COLOR green]SHOWS COMPLETOS[/COLOR][/B]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID9+"/",
		thumbnail = icon10,
		folder = True )			

plugintools.add_item(
		title = "[B][COLOR yellow]PAGODE [COLOR green]SHOWS COMPLETOS[/COLOR][/B]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID10+"/",
		thumbnail = icon11,
		folder = True )		

plugintools.add_item(
		title = "[B][COLOR yellow]AXE [COLOR green]SHOWS COMPLETOS[/COLOR][/B]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID13+"/",
		thumbnail = icon14,
		folder = True )	
		
		
plugintools.add_item(
		title = "[B][COLOR yellow]ROCK [COLOR green]CLIPES[/COLOR][/B]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID5+"/",
		thumbnail = icon6,
		folder = True )		
		
plugintools.add_item(
		title = "[B][COLOR yellow]REGGAE [COLOR green]CLIPES[/COLOR][/B]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID6+"/",
		thumbnail = icon7,
		folder = True )	
		
plugintools.add_item(
		title = "[B][COLOR yellow]POP [COLOR green]CLIPES[/COLOR][/B]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID7+"/",
		thumbnail = icon8,
		folder = True )			
		
plugintools.add_item(
		title = "[B][COLOR yellow]MPB [COLOR green]CLIPES[/COLOR][/B]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID8+"/",
		thumbnail = icon9,
		folder = True )			
			
plugintools.add_item(
		title = "[B][COLOR yellow]SAMBA [COLOR green]CLIPES[/COLOR][/B]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID11+"/",
		thumbnail = icon12,
		folder = True )			

plugintools.add_item(
		title = "[B][COLOR yellow]PAGODE [COLOR green]CLIPES[/COLOR][/B]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID12+"/",
		thumbnail = icon13,
		folder = True )	

plugintools.add_item(
		title = "[B][COLOR yellow]AXE [COLOR green]CLIPES[/COLOR][/B]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID14+"/",
		thumbnail = icon15,
		folder = True )			
run()