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

addonID = 'plugin.video.historychannel'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=resfolder+"entrada.mp4"

YOUTUBE_CHANNEL_ID1 = "playlist/PLOrPJ_6Lt3wBgzR87cF35RHsxqDsbaV46"
YOUTUBE_CHANNEL_ID2 = "playlist/PLOrPJ_6Lt3wChQc3wy5D3QitsG6VaN9uG"
YOUTUBE_CHANNEL_ID3 = "playlist/PLOrPJ_6Lt3wA_JAOoumuOBGpyXvjpgv7-"
YOUTUBE_CHANNEL_ID4 = "playlist/PLOrPJ_6Lt3wAvWtC40HrCKcf2oWdFMQRC"
YOUTUBE_CHANNEL_ID5 = "playlist/PLOrPJ_6Lt3wAojCbQIYjZFtJjzW9tcoDO"
YOUTUBE_CHANNEL_ID6 = "playlist/PLOrPJ_6Lt3wALtldFKlq2qnGfzuHkOeI2"
YOUTUBE_CHANNEL_ID7 = "playlist/PLOrPJ_6Lt3wD1xpcCSNUGIkNvOvataxg9"
YOUTUBE_CHANNEL_ID8 = "playlist/PLOrPJ_6Lt3wAyFx9BoREMx8c7CIXzxLyh"
YOUTUBE_CHANNEL_ID9 = "playlist/PLOrPJ_6Lt3wCQph3bQNPxOTnf57bOsQZm"
YOUTUBE_CHANNEL_ID10 = "playlist/PLOrPJ_6Lt3wAN-mxpbYrPZfBTmyA-PxNg"
YOUTUBE_CHANNEL_ID11 = "playlist/PLOrPJ_6Lt3wDKmIE5WD7cBn98HVS-nvcv"
YOUTUBE_CHANNEL_ID12 = "playlist/PLOrPJ_6Lt3wASNs0RBZc0CMMYJI7vbDvs"
YOUTUBE_CHANNEL_ID13 = "playlist/PLOrPJ_6Lt3wDYjIwLg78FyjjaQmYcmFba"
YOUTUBE_CHANNEL_ID14 = "playlist/PLOrPJ_6Lt3wCZbyE0Sqv8rWPdiX5VAX-S"
YOUTUBE_CHANNEL_ID15 = "playlist/PLOrPJ_6Lt3wDGC-28Hi_0SPYsupyUp8ZM"
YOUTUBE_CHANNEL_ID16 = "playlist/PLOrPJ_6Lt3wD6cttrt9AVdXCfE2b758D-"
YOUTUBE_CHANNEL_ID17 = "playlist/PLOrPJ_6Lt3wAyrvM0GzqxMhmdAKZyLqo2"
YOUTUBE_CHANNEL_ID18 = "playlist/PLOrPJ_6Lt3wBzzInXuRDl9-byNl6M61Wq"
YOUTUBE_CHANNEL_ID19 = "playlist/PLOrPJ_6Lt3wD6he1jYPMzFb1WjlzMaWvQ"
YOUTUBE_CHANNEL_ID20 = "playlist/PLOrPJ_6Lt3wDtBpkJGutuK_P0lVd_p8DO"
YOUTUBE_CHANNEL_ID21 = "playlist/PLOrPJ_6Lt3wB4UnkUTAUmlV1RqKaItVVn"
YOUTUBE_CHANNEL_ID22 = "playlist/PLOrPJ_6Lt3wDvCF7Sal7fgqM5A6zQBpIg"
YOUTUBE_CHANNEL_ID23 = "playlist/PLOrPJ_6Lt3wCIUSVUzoTTYTXcMo6WzOwX"
YOUTUBE_CHANNEL_ID24 = "playlist/PLOrPJ_6Lt3wB3b_446ZfbE7_U0089Jz2a"
YOUTUBE_CHANNEL_ID25 = "playlist/PLOrPJ_6Lt3wC7j7RmFubjZCN-H7kAPo8w"
YOUTUBE_CHANNEL_ID26 = "playlist/PLOrPJ_6Lt3wByUPeNkMhZ3c_DrnlPfWY6"
YOUTUBE_CHANNEL_ID27 = "playlist/PLOrPJ_6Lt3wCz0pk9yDt66YxMvNp3YAOQ"
YOUTUBE_CHANNEL_ID28 = "playlist/PLOrPJ_6Lt3wA_39LEUbJ_nCXrwxKOnwJu"
YOUTUBE_CHANNEL_ID29 = "playlist/PLOrPJ_6Lt3wBTDyPZPbzTGp7VaVz1hbRq"
YOUTUBE_CHANNEL_ID30 = "playlist/PLOrPJ_6Lt3wAM8ipXrUiNvusky7l7a08T"
YOUTUBE_CHANNEL_ID31 = "playlist/PLOrPJ_6Lt3wCKIxuT9TA6rkAeb6OUOLYl"
YOUTUBE_CHANNEL_ID32 = "playlist/PLOrPJ_6Lt3wA9Sa87bLTbf3nc1T7aomjO"
YOUTUBE_CHANNEL_ID33 = "playlist/PLOrPJ_6Lt3wDcd0iVPEIn0uK2xftl-XHt"
YOUTUBE_CHANNEL_ID34 = "playlist/PLOrPJ_6Lt3wCNc4cwNOQT0TNK3MahqprX"
YOUTUBE_CHANNEL_ID35 = "playlist/PLOrPJ_6Lt3wCEq1wDil5bSfJooU4sVWyi"
YOUTUBE_CHANNEL_ID36 = "playlist/PLOrPJ_6Lt3wDU-nAeIH75jsaT1byoDgoE"
YOUTUBE_CHANNEL_ID37 = "playlist/PLOrPJ_6Lt3wB0lGJGeWIlI6wbDe1Q3xUC"
YOUTUBE_CHANNEL_ID38 = "playlist/PLOrPJ_6Lt3wCX7tzZbqxTxf8do4utFWig"
YOUTUBE_CHANNEL_ID39 = "playlist/PLOrPJ_6Lt3wD0H9LvXpWsTr8TmVqnwiew"
YOUTUBE_CHANNEL_ID40 = "playlist/PLOrPJ_6Lt3wDKmnER5c45-c9z5GU_91wr"
YOUTUBE_CHANNEL_ID41 = "playlist/PLOrPJ_6Lt3wBqvsKZxs5foqEGKuzIS4-l"
YOUTUBE_CHANNEL_ID42 = "playlist/PLOrPJ_6Lt3wDvMJE01Wd6opFoZFHh1CMp"
YOUTUBE_CHANNEL_ID43 = "playlist/PLOrPJ_6Lt3wCR9zqUkViBtn_G8xbkFwoV"
YOUTUBE_CHANNEL_ID44 = "playlist/PLOrPJ_6Lt3wC4WhPI817oI_jSvmOFoU9q"
YOUTUBE_CHANNEL_ID45 = "playlist/PLOrPJ_6Lt3wC4WhPI817oI_jSvmOFoU9q"
YOUTUBE_CHANNEL_ID46 = "playlist/PLOrPJ_6Lt3wAd-7ZsTjOD18puaoEoJRvg"
YOUTUBE_CHANNEL_ID47 = "playlist/PLOrPJ_6Lt3wAbBUS9iFQWRFGHvrqZMCwH"
YOUTUBE_CHANNEL_ID48 = "playlist/PLOrPJ_6Lt3wDuBGO3J6ZyvKD-SbJYf7eM"
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
	plugintools.log("KondZilla.main_list "+repr(params))
	
	plugintools.log("KondZilla.run")
	
	#plugintools.direct_play(str(entryurl))

	plugintools.add_item(
		title = "Caçadores de Ovinis",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/",
		thumbnail = icon,
		folder = True )

	plugintools.add_item(
		title = "Historias do Mundo",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID2+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Super Humanos",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID3+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Forças Especiais",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID4+"/",
		thumbnail = icon,
		folder = True )

	plugintools.add_item(
		title = "Caçador de Tumbas",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID5+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Maravilhas Modernas",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID6+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Misterios da Biblia",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID7+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Vida Privada dos Poderosos",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID8+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Construido um Imperio",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID9+"/",
		thumbnail = icon,
		folder = True )

	plugintools.add_item(
		title = "Efeito Nostradamus 1",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID10+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Efeito Nostradamus 2",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID11+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Arquivos Extraterrestres",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID12+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "O Infiltrado",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID13+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Tribo Germanicas",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID14+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Bárbaros",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID15+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Mundo Perdidos",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID16+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "2 guerra Filmes Perdidos",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID17+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Em Busca do Tesouro Sagrado",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID18+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Sou César",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID19+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Guia Politicamente Incorreto",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID20+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "O Universo",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID21+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Planeta Egito",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID22+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Templarios",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID23+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Batalha Decisivas",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID24+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Investigação",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID25+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Gestapo",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID26+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Combates Aereos",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID27+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Decifrando o Passado",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID28+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Inventos da Antiguidade",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID29+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "A Ciência de Tudo",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID30+"/",
		thumbnail = icon,
		folder = True )

	plugintools.add_item(
		title = "Caçadores de Monstros",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID31+"/",
		thumbnail = icon,
		folder = True )

	plugintools.add_item(
		title = "Como Nasceu nosso planeta",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID32+"/",
		thumbnail = icon,
		folder = True )

	plugintools.add_item(
		title = "Alienígenas do Passado",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID33+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "O Socio",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID34+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Confronto dos deuses",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID35+"/",
		thumbnail = icon,
		folder = True )
		
        plugintools.add_item(
		title = "Unidos pela história",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID36+"/",
		thumbnail = icon,
		folder = True )
        
        plugintools.add_item(
		title = "Terceiro Reich",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID37+"/",
		thumbnail = icon,
		folder = True )
        
        plugintools.add_item(
		title = "Decifrando Codigos",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID38+"/",
		thumbnail = icon,
		folder = True )
        
        plugintools.add_item(
		title = "Grandes batalhas da antiguidade",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID39+"/",
		thumbnail = icon,
		folder = True )
		
        plugintools.add_item(
		title = "Icones do mau comportamento",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID40+"/",
		thumbnail = icon,
		folder = True )
        
        plugintools.add_item(
		title = "Como o sexo mudou o mundo",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID41+"/",
		thumbnail = icon,
		folder = True )

        plugintools.add_item(
		title = "Mistérios e mitos",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID42+"/",
		thumbnail = icon,
		folder = True )
		
        plugintools.add_item(
		title = "Batalhas a.c.",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID43+"/",
		thumbnail = icon,
		folder = True )
		
        plugintools.add_item(
		title = "Humanidade: a história de todos nós",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID44+"/",
		thumbnail = icon,
		folder = True )
        
        plugintools.add_item(
		title = "Corpo marcado",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID45+"/",
		thumbnail = icon,
		folder = True )

        plugintools.add_item(
		title = "Evolução",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID46+"/",
		thumbnail = icon,
		folder = True )
		
        plugintools.add_item(
		title = "Gigantes do brasil",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID47+"/",
		thumbnail = icon,
		folder = True )
		
        plugintools.add_item(
		title = "A bíblia proibida",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID48+"/",
		thumbnail = icon,
		folder = True )

run()
