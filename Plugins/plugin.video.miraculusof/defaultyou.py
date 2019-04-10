
import os
import sys
import time
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.playlistLoader'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)

addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=resfolder+"entrada.mp4"
userDataFolder = xbmc.translatePath("special://home/addons/plugin.video.youplayer/data")

keyo = xbmc.Keyboard('', '1-playlist e canal e user 2- video avulso 3- Salvar em Regex: ')
keyo.doModal()
opcao = keyo.getText()

def m3u_gen(url,icone,bloco):
	keyplay = xbmc.Keyboard('', 'Digite Nome da Playlist:')
	keyplay.doModal()
	playlistn = keyplay.getText()
	arquivo = open(""+userDataFolder+"/"+playlistn+".m3u", 'a')
	arquivo.write("\n")
	arquivo.write("#EXTINF:-1 tvg-logo=\""+icone+"\","+bloco+"")
	arquivo.write("\n")
	arquivo.write(""+url+"")
	arquivo.close()
	
def save_favorite(url,icone,bloco):
	
	arquivo = open(""+userDataFolder+"/favorites.txt", 'a')
	
	keyopcaof = xbmc.Keyboard('', 'Deseja lacrar favorito 1 -S 2 -N:')
	keyopcaof.doModal()
	opcaof = keyopcaof.getText()
	
	if opcaof == "1":
		arquivo.write("<favourites>")
		arquivo.write("\n")
		arquivo.write(" <favourite name="+bloco+" thumb="+icone+">ActivateWindow(10025,&quot;plugin://plugin.video.youtube/"+url+"/&quot;,return)</favourite>")
		arquivo.write("\n")
		arquivo.write("</favourites>")
	
	else:
		arquivo.write("\n")
		arquivo.write(" <favourite name="+bloco+" thumb="+icone+">ActivateWindow(10025,&quot;plugin://plugin.video.youtube/"+url+"/&quot;,return)</favourite>")
	
	arquivo.close()
	
	
def save_favorite_xml(url,icone,bloco):
	
	keyopcaof = xbmc.Keyboard('', 'Deseja inserir uma fanart 1 -S 2 -N:')
	keyopcaof.doModal()
	opcaof = keyopcaof.getText()
	
	keyopcaoi = xbmc.Keyboard('', 'Primeiro Cadastro 1 -S 2 -N:')
	keyopcaoi.doModal()
	opcaoi = keyopcaoi.getText()
	
	
	arquivo = open(""+userDataFolder+"/favorites_regex.txt", 'a')
	
	if opcaoi == "1":
		arquivo.write("\n")
		arquivo.write("<layouttype>thumbnail</layouttype>")
		arquivo.write("\n")
		arquivo.write("<item>")
		arquivo.write("\n")
		arquivo.write("<title>"+bloco+"</title>")
		arquivo.write("\n")
		arquivo.write("<utube>"+url+"</utube>")
		arquivo.write("\n")
		arquivo.write("<thumbnail>"+icone+"</thumbnail>")
		arquivo.write("\n")
		arquivo.write("\n")
		
		
		if opcaof == "1":
			keyopcaof = xbmc.Keyboard('', 'Digite o Link da Fanart:')
			keyopcaof.doModal()
			fanart = keyopcaof.getText()
			arquivo.write("<fanart>"+fanart+"</fanart>")
			arquivo.write("\n")
			arquivo.write("</item>")
		
		else: 
			arquivo.write("<fanart>""</fanart>")
			arquivo.write("\n")
			arquivo.write("</item>")
	
	else:
		arquivo.write("\n")
		arquivo.write("<item>")
		arquivo.write("\n")
		arquivo.write("<title>"+bloco+"</title>")
		arquivo.write("\n")
		arquivo.write("<utube>"+url+"</utube>")
		arquivo.write("\n")
		arquivo.write("<thumbnail>"+icone+"</thumbnail>")
		arquivo.write("\n")
		arquivo.write("\n")
		arquivo.write("</item>")
		
		if opcaof == "1":
			keyopcaof = xbmc.Keyboard('', 'Digite o Link da Fanart:')
			keyopcaof.doModal()
			fanart = keyopcaof.getText()
			arquivo.write("<fanart>"+fanart+"</fanart>")
		
		else: 
			arquivo.write("<fanart>""</fanart>")
	
	
			

	
	arquivo.close()
	
if opcao == '1':
	keyb = xbmc.Keyboard('', 'Digite canal com /channel/id ou /playlist/id ou user/id')
	keyb.doModal()
	url = keyb.getText()

	keyf = xbmc.Keyboard('', 'Cole uma Imagem ou icone: ')
	keyf.doModal()
	icone = keyf.getText()

	keyc = xbmc.Keyboard('', 'Digite titulo para bloco: ')
	keyc.doModal()
	bloco = keyc.getText()
	
	keyop = xbmc.Keyboard('', 'Deseja Salvar Macro 1 para S 2 para N: ')
	keyop.doModal()
	save = keyop.getText()
	
	if save == "1":
		save_favorite(url,icone,bloco)

if opcao == '2':
	keyb = xbmc.Keyboard('', 'Digite o link do video')
	keyb.doModal()
	url = keyb.getText()

	keyf = xbmc.Keyboard('', 'Cole uma Imagem ou icone: ')
	keyf.doModal()
	icone = keyf.getText()

	keyc = xbmc.Keyboard('', 'Digite titulo do video: ')
	keyc.doModal()
	bloco = keyc.getText()
	m3u_gen(url,icone,bloco)


	
if opcao == '3':
	keyb = xbmc.Keyboard('', 'Digite canal,playlist ou user: ')
	keyb.doModal()
	url = keyb.getText()

	keyf = xbmc.Keyboard('', 'Cole uma Imagem ou icone: ')
	keyf.doModal()
	icone = keyf.getText()

	keyc = xbmc.Keyboard('', 'Digite titulo para bloco: ')
	keyc.doModal()
	bloco = keyc.getText()
	
	keyop = xbmc.Keyboard('', 'Deseja Salvar Macro 1 para S 2 para N: ')
	keyop.doModal()
	save = keyop.getText()
	
	if save == "1":
		save_favorite_xml(url,icone,bloco)
	
	
	
	
	
icon = icone
YOUTUBE_CHANNEL_ID = url
# Ponto de Entrada
def run():

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
	plugintools.log("youplayer.main_list "+repr(params))
	
	plugintools.log("youplayer.run")
	
	#plugintools.direct_play(str(entryurl))



plugintools.add_item(
		title = ""+bloco+"",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID+"/",
		thumbnail = icon,
		folder = True )
		
run()
