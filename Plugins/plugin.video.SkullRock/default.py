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

addonID = 'plugin.video.SkullRock'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
#icon = local.getAddonInfo('icon')
icon = local.getAddonInfo('icon')
icon2 = "https://cld.pt/dl/download/54d42e4a-493d-479b-9fdf-1a2300469345/Concert.png?download=true"
icon3 = "https://cld.pt/dl/download/cf701c86-ddf6-4649-821a-a8f5ed8cbda4/clips.png?download=true"
icon4 = "https://cld.pt/dl/download/163fdadd-ca13-4a96-8f50-48982d3c5016/ACUSTIC.jpg?download=true"
icon5 = "https://cld.pt/dl/download/3428239e-10b2-433b-ae06-c75615fbc803/AUDIOMIX.jpg?download=true"
icon6 = "https://cld.pt/dl/download/9e61d62d-141e-4d21-b561-b0d71b73602b/ACDC.png?download=true"
icon7 = "https://cld.pt/dl/download/fe40b006-9d9a-460d-b6f7-89263764917a/AERO.png?download=true"
icon8 = "https://cld.pt/dl/download/d6fa43ac-5d6f-4e27-ad4e-b7051b716f46/BLACK%20SABBATH.jpg?download=true"
icon9 = "https://cld.pt/dl/download/50d112ad-6fc4-4b9d-a201-094ebe128679/BONJOVI.jpg?download=true"
icon10 = "https://cld.pt/dl/download/5b431f82-781e-4c4b-af39-9f146da9aef3/COLDPLAY.jpg?download=true"
icon11 = "https://cld.pt/dl/download/1ef0dc90-9d8e-4f03-8fb1-420cf9a55a9b/CREEDENCE.jpg?download=true"
icon12 = "https://cld.pt/dl/download/6599395c-ad4e-4337-871d-f5c923fd4357/DEEP.jpg?download=true"
icon13 = "https://cld.pt/dl/download/33e635dc-c3d5-481a-ab4c-26d1bee77951/DIO.jpg?download=true"
icon14 = "https://cld.pt/dl/download/d3be5ecd-c450-4d33-868c-260ccd7757b3/EAGLES.jpg?download=true"
icon15 = "https://cld.pt/dl/download/31778852-9e1c-4563-b723-9567f407603d/FOOF.jpg?download=true"
icon16 = "https://cld.pt/dl/download/f3feb480-367c-4c77-84ee-f926b34adc75/GREEND.jpg?download=true"
icon17 = "https://cld.pt/dl/download/3809b1af-eb55-41c2-b15a-3e3338a2280f/GUNS.jpg?download=true"
icon18 = "https://cld.pt/dl/download/c5107fb7-f185-4faf-8faf-88d5287c8130/HENDRIX.jpg?download=true"
icon19 = "https://cld.pt/dl/download/7472facd-4bfd-4161-bde3-4c04789bad07/IRON.jpg?download=true"
icon20 = "https://cld.pt/dl/download/f6167659-17c0-4369-85f9-7a8b2948fc2a/KISS.jpg?download=true"
icon21 = "https://cld.pt/dl/download/a02944ad-c99e-4fe6-a268-8ec3cb36f498/LED%20ZEPPELIN.jpg?download=true"
icon22 = "https://cld.pt/dl/download/9c42a5b3-5e25-469e-8668-574fd7f7d987/METALLICA.jpg?download=true"
icon23 = "https://cld.pt/dl/download/2cf9047e-c66d-41b2-bba3-c7cf55852bfe/MOTORH.jpg?download=true"
icon24 = "https://cld.pt/dl/download/e044e6cc-f5e7-4d9f-a53b-a766a73d810e/nirvana.jpg?download=true"
icon25 = "https://cld.pt/dl/download/41fcb40c-50bb-43d0-baec-09e5a2e84b47/OZZY.jpg?download=true"
icon26 = "https://cld.pt/dl/download/0b33b393-d3f3-4330-896e-cebcf58be496/PEARLJAM.jpg?download=true"
icon27 = "https://cld.pt/dl/download/dcba44d6-6766-4d2d-8df8-d46d97596383/PINKFLOYD.jpg?download=true"
icon28 = "https://cld.pt/dl/download/eec54b79-40db-4ef3-a110-386e71c5d76c/QUEEN.jpg?download=true"
icon29 = "https://cld.pt/dl/download/370f717f-ab1f-4c7c-a9ea-91d4b402fed5/RED%20HOT.jpg?download=true"
icon30 = "https://cld.pt/dl/download/01fd2efb-4dfb-4a10-810b-13760365e440/ROLLING%20STONES.jpg?download=true"
icon31 = "https://cld.pt/dl/download/d8c19661-1fc1-4974-9b5d-b7c83345c14b/RUSH.jpg?download=true"
icon32 = "https://cld.pt/dl/download/8caef1d5-210d-41e5-ad80-734adcc7a5b8/SCORPIONS.jpg?download=true"
icon33 = "https://cld.pt/dl/download/f0d53f72-5b5e-42d0-94c3-734c50fe1b27/THE%20BEATLES.jpg?download=true"
icon34 = "https://cld.pt/dl/download/055ed98d-ccfa-4b30-aab5-11ca52c79132/U2.jpg?download=true"
icon35 = "https://cld.pt/dl/download/317beba1-2774-42f6-871e-8cd0c22f254d/ZZTOP.jpg?download=true"
addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=resfolder+"entrada.mp4"
YOUTUBE_CHANNEL_ID = "playlist/PLNtZ1Pn1y2b5DSYQVARmkwwPkmtEZCvHy"
YOUTUBE_CHANNEL_ID2 = "playlist/PLNtZ1Pn1y2b5MZt68GqV1eb-ybY4kjZ04"
YOUTUBE_CHANNEL_ID3 = "playlist/PLNtZ1Pn1y2b4XTOIv-IH5Z2vCkMt9sqe3"
YOUTUBE_CHANNEL_ID4 = "playlist/PLNtZ1Pn1y2b6eNFhjATZ14rmRYPIQDxHC"
YOUTUBE_CHANNEL_ID5 = "playlist/PLNtZ1Pn1y2b7W1lbOINE3TKqXFqp5-e0-"
YOUTUBE_CHANNEL_ID6 = "playlist/PLNtZ1Pn1y2b6xT99-dTjTDlxtdZNIw3In"
YOUTUBE_CHANNEL_ID7 = "playlist/PLNtZ1Pn1y2b5PfAb2K-cjoXE9dJXy6g7i"
YOUTUBE_CHANNEL_ID8 = "playlist/PLNtZ1Pn1y2b6pju3ecmQg7gdu-v3ZYJQI"
YOUTUBE_CHANNEL_ID9 = "playlist/PLNtZ1Pn1y2b5H3mjLhC53QhICU9OpPOW-"
YOUTUBE_CHANNEL_ID10 = "playlist/PLNtZ1Pn1y2b5da_mWoyEpqIP60DQhir6C"
YOUTUBE_CHANNEL_ID11 = "playlist/PLNtZ1Pn1y2b7qQOKglx3U7T1CVJy8yPfK"
YOUTUBE_CHANNEL_ID12 = "playlist/PLNtZ1Pn1y2b7MB0E8E9xx4E-A8wVv3Qxe"
YOUTUBE_CHANNEL_ID13 = "playlist/PLNtZ1Pn1y2b41Exa1nCS161tuN9LCZaNs"
YOUTUBE_CHANNEL_ID14 = "playlist/PLNtZ1Pn1y2b55dpYOfanlH3j4sqDyvCSX"
YOUTUBE_CHANNEL_ID15 = "playlist/PLNtZ1Pn1y2b4zk8nIzWdfNQ8z_rLBIqxl"
YOUTUBE_CHANNEL_ID16 = "playlist/PLNtZ1Pn1y2b6WqyjmdNkemI-NKZUuvwav"
YOUTUBE_CHANNEL_ID17 = "playlist/PLNtZ1Pn1y2b4iDcXzzlq-KRsODZ2bg6c7"
YOUTUBE_CHANNEL_ID18 = "playlist/PLNtZ1Pn1y2b4XLgoMlSpOEPWvNamy3Zee"
YOUTUBE_CHANNEL_ID19 = "playlist/PLNtZ1Pn1y2b7FY3RK2H7DnOlWnx46FRr4"
YOUTUBE_CHANNEL_ID20 = "playlist/PLNtZ1Pn1y2b5QZC7VnTjZZCOxq21zjsxT"
YOUTUBE_CHANNEL_ID21 = "playlist/PLNtZ1Pn1y2b5fj6nL8TTy-gby8WruGoLx"
YOUTUBE_CHANNEL_ID22 = "playlist/PLNtZ1Pn1y2b7mPno2klEuRBX6dJpV4Hoz"
YOUTUBE_CHANNEL_ID23 = "playlist/PLNtZ1Pn1y2b7Zal-WSfWOb_HsvcSmfmRZ"
YOUTUBE_CHANNEL_ID24 = "playlist/PLNtZ1Pn1y2b5s6c_lL684ieKEx2pz9qf-"
YOUTUBE_CHANNEL_ID25 = "playlist/PLNtZ1Pn1y2b50fsZGdPtlZo5hIeIL3ido"
YOUTUBE_CHANNEL_ID26 = "playlist/PLNtZ1Pn1y2b5ccHLpA2-mY9Iy7MJ7r8V8"
YOUTUBE_CHANNEL_ID27 = "playlist/PLNtZ1Pn1y2b71k6Fi4Efq0UnanYDchC0_"
YOUTUBE_CHANNEL_ID28 = "playlist/PLNtZ1Pn1y2b4kn9p2Nly-VGepApkOsfHg"
YOUTUBE_CHANNEL_ID29 = "playlist/PLNtZ1Pn1y2b4iIUMLRk7bx9xPwDHBPFur"
YOUTUBE_CHANNEL_ID30 = "playlist/PLNtZ1Pn1y2b7BqL9M2jJ1Jyl5yHfd7kXq"
YOUTUBE_CHANNEL_ID31 = "playlist/PLNtZ1Pn1y2b5uYYi8txipo0nDcBFPqtYA"
YOUTUBE_CHANNEL_ID32 = "playlist/PLNtZ1Pn1y2b7nFc8t5FAZ2hy0Sx-9K-EP"
YOUTUBE_CHANNEL_ID33 = "playlist/PLNtZ1Pn1y2b4KTTH_-hlTiZ2xNXbydFXy"
YOUTUBE_CHANNEL_ID34 = "playlist/PLNtZ1Pn1y2b4N1HY3g95h-sKPTCnFCCLc"
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
	plugintools.log("SkullRock.main_list "+repr(params))
	
	plugintools.log("SkullRock.run")
	
	#plugintools.direct_play(str(entryurl))

plugintools.add_item(
		title = "[B][COLOR red]CONCERT[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID+"/",
		thumbnail = icon2,
		folder = True )
		
plugintools.add_item(
		title = "[B][COLOR red]SELECTING CLIPS[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID2+"/",
		thumbnail = icon3,
		folder = True )

plugintools.add_item(
		title = "[B][COLOR red]ACUSTIC[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID3+"/",
		thumbnail = icon4,
		folder = True )		

plugintools.add_item(
		title = "[B][COLOR red]AUDIO MIX[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID4+"/",
		thumbnail = icon5,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]AC / DC[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID5+"/",
		thumbnail = icon6,
		folder = True )	
		
plugintools.add_item(
		title = "[B][COLOR red]AEROSMITH[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID6+"/",
		thumbnail = icon7,
		folder = True )	
plugintools.add_item(
		title = "[B][COLOR red]BLACK SABBATH[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID7+"/",
		thumbnail = icon8,
		folder = True )	
plugintools.add_item(
		title = "[B][COLOR red]BON JOVI[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID8+"/",
		thumbnail = icon9,
		folder = True )	
		
plugintools.add_item(
		title = "[B][COLOR red]COLDPLAY[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID9+"/",
		thumbnail = icon10,
		folder = True )	
		
plugintools.add_item(
		title = "[B][COLOR red]CREEDENCE[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID10+"/",
		thumbnail = icon11,
		folder = True )
plugintools.add_item(
		title = "[B][COLOR red]DEEP PURPLE[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID11+"/",
		thumbnail = icon12,
		folder = True )
plugintools.add_item(
		title = "[B][COLOR red]DIO[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID12+"/",
		thumbnail = icon13,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]EAGLES[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID13+"/",
		thumbnail = icon14,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]FOO FIGHTERS[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID14+"/",
		thumbnail = icon15,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]GREEN DAY[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID15+"/",
		thumbnail = icon16,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]GUNS N' ROSES[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID16+"/",
		thumbnail = icon17,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]IRON MADEN[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID17+"/",
		thumbnail = icon19,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]JIMI HENDRIX[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID18+"/",
		thumbnail = icon18,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]KISS[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID19+"/",
		thumbnail = icon20,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]LED ZEPPELLIN[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID20+"/",
		thumbnail = icon21,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]METALLICA[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID21+"/",
		thumbnail = icon22,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]MOTORHEAD[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID22+"/",
		thumbnail = icon23,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]NIRVANA[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID23+"/",
		thumbnail = icon24,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]OZZY OSBOURNE[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID24+"/",
		thumbnail = icon25,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]PEARL JAM[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID25+"/",
		thumbnail = icon26,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]PINK FLOYD[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID26+"/",
		thumbnail = icon27,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]QUEEN[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID27+"/",
		thumbnail = icon28,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]RED HOT CHILLI PEPPERS[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID28+"/",
		thumbnail = icon29,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]ROLLING STONES[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID29+"/",
		thumbnail = icon30,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]RUSH[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID30+"/",
		thumbnail = icon31,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]SCORPIONS[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID31+"/",
		thumbnail = icon32,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]THE BEATLES[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID32+"/",
		thumbnail = icon33,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]U2[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID33+"/",
		thumbnail = icon34,
		folder = True )		
plugintools.add_item(
		title = "[B][COLOR red]ZZTOP[/B][/COLOR]",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID34+"/",
		thumbnail = icon35,
		folder = True )				
run()