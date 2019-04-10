# -*- coding: utf-8 -*-

import urllib, urllib2, sys, re, os, unicodedata,urlparse
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser
h = HTMLParser()		
##############################################################################################
plugin_handle = int(sys.argv[1])
addon_id = 'plugin.video.Torrent Player'
mysettings = xbmcaddon.Addon(id = addon_id)
addon_name = 'Torrent Player'
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')
fanarts = xbmc.translatePath(os.path.join(home, 'fanart2.jpg'))
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
dialog = xbmcgui.Dialog()    
#############################################################################################
def contar_acessos():
	try:
		req = urllib2.Request('https://goo.gl/sb9b22')
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
	except:
		pass

def clean_name(name):
	name = name.replace('#038;','').replace('amp;','').replace('&','').replace('WWW.BLUDV.COM','').replace(' [BluRay] ',' ').replace(' IMAX ',' ').replace(' [720p] ',' ').replace('- WWW.',' ').replace('TORRENTBRAZIL.ORG','').replace('-BLACKOUT','').replace('.Nacional','').replace('.AC3','').replace('.DVDRip','').replace(' Torrent ',' ').replace(' Download ',' ').replace('– WEB-DL ',' ').replace(' 720p e 1080p ',' ').replace(' BluRay ',' ').replace('– Dublado ',' ').replace('#8211;','').replace(' WEBRip ',' ').replace(' Dual Áudio',' ').replace('  / ',' ').replace(' / ',' ').replace('  Legendado',' ').replace(' Legendado',' ').replace(' – 5.1',' ').replace(' 1080p ',' ').replace(' WEB-DL ',' ').replace(' Dublado ',' ').replace(' 5.1 ',' ').replace(' REMASTERIZADO ',' ').replace(' HDTV ',' ').replace(' – ',' ').replace(' 720p ',' ').replace(' – ',' ').replace('#8217;','').replace(' Download',' ').replace(' | ',' ').replace(' HDRip ',' ').replace(' e ',' ').replace('.x264-GECKOS',' ').replace('.H264.AAC-RARBG',' ').replace('.PROPER',' ').replace('.WWW.COMANDOTORRENTS.COM',' ').replace('.DD5.1.x264-DUAL ',' ').replace('[COMANDOTORRENTS.COM] ',' ').replace('.ENG.X264-Feel.Free',' ').replace(' COMANDOTORRENTS.COM',' ').replace('.x264-REGARDS',' ').replace('.x264-FGT',' ').replace('.DD5.1.H264-FGT',' ').replace('.XviD-FGT',' ').replace('.HC.HDRip.X264-DUAL ',' ').replace(' COMANDOTORRRENTS.COM',' ').replace('.x264-DUAL ',' ').replace('.FULL','').replace('.x264-BiPOLAR',' ').replace('.BDRip ',' ').replace('.x264-VALUE',' ').replace(' x264-JellyBean',' ').replace('-WWW.COMANDOTORRENTS.COM',' ').replace('TS.x264.',' ').replace('.1920X1080.NonDRM_[FHD].mp4',' ').replace('.H264.AAC-CJCONTENTS.mp4',' ').replace(' x264 AC3 Line DUAL ',' ').replace('.XviD.MP3-RARBG',' ').replace('.x264-VETO',' ').replace('.x264.TiTAN',' ').replace('.X264-AMIABLE',' ').replace('.x264.DTS-DUAL ',' ').replace('.x264.HORiZON-ArtSubs',' ').replace('.HDRip.XviD-EVO',' ').replace('.x264-SVA','').replace('.REPACK',' ').replace('.XviD.MP3-FGT',' ').replace('.x264-DRONES',' ').replace('- MKvCage',' ').replace('.x264-Grym',' ').replace('.COMANDOTORRENTS.COM',' ').replace('-COMANDOTORRENTS.COM',' ').replace('.HDTV.x264','.HDTV').replace(' Baixar ',' ').replace(' |   ',' ').replace(' |  ',' ').replace(' |1080p  ',' ').replace(' Leg',' ').replace(' Dub ',' ').replace(' Blu-Ray ',' ').replace(' Dublado',' ').replace(' (2017) ',' ').replace(' #Desafio Mundial ',' ').replace('Audio-BLUDV.COM','')
	return name			
				
def abrir_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link

def add_link(name,url,mode,iconimage,fanart,description):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name,"Plot":description} )
		cmItems = []
		if mode==4:
			cmItems.append(('[COLOR gold]Próximos Programas[/COLOR]',  'XBMC.RunPlugin(%s?url=%s&mode=3&name=%s&iconimage=%s&description=%s)'%(sys.argv[0],urllib.quote_plus(url),urllib.quote_plus(name),urllib.quote_plus(iconimage),urllib.quote_plus(description))))
		liz.addContextMenuItems(cmItems, replaceItems=False)
		liz.setProperty('fanart_image', fanart)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		return ok
#############################################################################################	
params = dict(urlparse.parse_qsl(sys.argv[2].replace('/?','/&')))
xbmc.log('%s' % params)
url = params.get("url")
name = params.get("name")
mode = int(params.get("mode",'0'))
iconimage = params.get("iconimage")
description = params.get("?description")


libDir = os.path.join(home, 'resources', 'lib')
sys.path.insert(0, libDir)
import The_Pirate_Filmes_HD as Site1
import LAPUMiA_FiLMES as Site2
import filmesviatorrents as Site3
import Comando_Torrents as Site4
import So_Filmes_HD as Site5
import BLUDV as Site6
import Comando_4k_Filmes_Torrent as Site7

if mode==0:
	add_link('The Pirate Filmes HDs','',1,icon, fanarts,'Torrents')
	add_link('LAPUMiA FiLMES','',5,icon, fanarts,'Torrents')
	add_link('Filmes via Torrents','',9,icon, fanarts,'Torrents')
	add_link('Comando Torrents','',13,icon, fanarts,'Torrents')
	add_link('Só Filmes HD','',17,icon, fanarts,'Torrents')
	add_link('BLUDV','',21,icon, fanarts,'Torrents')
	add_link('Comando 4k Filmes Torrent','',25,icon, fanarts,'Torrents')
	
###############The_Pirate_Filmes_HD		
elif mode == 1:
	Site1.Home()
elif mode==2:
	Site1.Listar_Filmes_E_Series(url)
elif mode==3:
	Site1.Listar_Categorias(url)
elif mode==4:
	Site1.Pesquisar()

##############LAPUMiA FiLMES		
elif mode==5:
	Site2.Home()
elif mode==6:
	Site2.Listar_Filmes_E_Series(url)
elif mode==7:
	Site2.Listar_Categorias(url)
elif mode==8:
	Site2.Pesquisar()
#################Filmes via Torrents
elif mode==9:
	Site3.Home()
elif mode==10:
	Site3.Listar_Filmes_E_Series(url)
elif mode==11:
	Site3.Listar_Categorias(url)
elif mode==12:
	Site3.Pesquisar()
##################Comando Torrents
elif mode==13:
	Site4.Home()	
elif mode==14:
	Site4.Listar_Filmes_E_Series(url)
elif mode==15:
	Site4.Listar_Categorias(url)
elif mode==16:
	Site4.Pesquisar()
##################Só Filmes HD
elif mode==17:
	Site5.Home()
elif mode==18:
	Site5.Listar_Filmes_E_Series(url)
elif mode==19:
	Site5.Listar_Categorias(url)
elif mode==20:
	Site5.Pesquisar()
#################BLUDV	
elif mode==21:
	Site6.Home()
elif mode==22:
	Site6.Listar_Filmes_E_Series(url)
elif mode==23:
	Site6.Listar_Categorias(url)
elif mode==24:
	Site6.Pesquisar()
################Comando 4k Filmes Torrent	
elif mode==25:
	Site7.Home()
elif mode==26:
	Site7.Listar_Filmes_E_Series(url)
elif mode==27:
	Site7.Listar_Categorias(url)
####################ADD-ON CONFIG
elif mode==100:# r'[s,S]\d+[e,E]\d+'r'magnet:\?[^\'"\s<>\[\]]+'
	link = abrir_url(url)
	for a in re.compile(r'(http://www.masterads.info[^\'"\s<>\[\]]+|magnet:\?[^\'"\s<>\[\]]+)').findall(link):
		nome = a
		if 'campanha.php?id' in nome:
			nome = nome.split('campanha.php?id')[1][::-1].decode('base64')
		try:name = clean_name(urlparse.parse_qsl(nome)[1][1])
		except: name = urlparse.parse_qsl(nome)[1][1]
		try: name = name.split('Acesse o')[0]
		except: name = name
		url = nome		
		add_link(name,url,999,iconimage, fanarts,'Player link')
elif mode==999:
	if 'magnet:?xt' in url or '.torrent' in url:	#'xt=urn:btih:([^&/]+) plugin://plugin.video.elementum/play?uri=%s
		Players_Torrent = ['Quasar','Pulsar','Yatp','Torrenter','XbmcTorrent','Torrentin','Elementum','Ace Stream(APK)','BitX Torrent Video Player(APK)']
		if mysettings.getSetting('player_torrent') == Players_Torrent[0]:#"Quasar":
			url = 'plugin://plugin.video.quasar/play?uri={0}'.format(urllib.quote_plus(url))
		elif mysettings.getSetting('player_torrent') == Players_Torrent[1]:# "Pulsar":
			url = 'plugin://plugin.video.pulsar/play?uri={0}'.format(urllib.quote_plus(url))
		elif mysettings.getSetting('player_torrent') == Players_Torrent[2]:#"Yatp":
			url = 'plugin://plugin.video.yatp/?action=play&torrent={0}'.format(urllib.quote_plus(url))
		elif mysettings.getSetting('player_torrent') ==  Players_Torrent[3]:##"Torrenter":
			url = 'plugin://plugin.video.torrenter/?action=playSTRM&url={0}'.format(urllib.quote_plus(url))
		elif mysettings.getSetting('player_torrent') ==  Players_Torrent[4]:# "XbmcTorrent":
			url = 'plugin://plugin.video.xbmctorrent/play/{0}'.format(urllib.quote_plus(url))
		elif mysettings.getSetting('player_torrent') ==  Players_Torrent[5]:#"Torrentin":
			url = 'plugin://plugin.video.torrentin/?uri={0}'.format(urllib.quote_plus(url))
		elif mysettings.getSetting('player_torrent') ==   Players_Torrent[6]:#"Elementum":
			url = 'plugin://plugin.video.elementum/play?uri={0}'.format(urllib.quote_plus(url))
		elif mysettings.getSetting('player_torrent') ==   Players_Torrent[7]:##"Ace Stream (apk)":
			if xbmc.getCondVisibility('system.platform.android'):
				xbmc.executebuiltin('XBMC.StartAndroidActivity("org.acestream.media","android.intent.action.VIEW","","'+url+'")')
			else:
				dialog.ok(addon_base,  "FUNCIONA APENAS EM SISTEMAS ANDROID !!".decode('unicode_escape'),'')
				sys.exit(0)	
		elif mysettings.getSetting('player_torrent') ==   Players_Torrent[8]:##"BitX Torrent Video Player":
			if xbmc.getCondVisibility('system.platform.android'):
				xbmc.executebuiltin('XBMC.StartAndroidActivity("tv.bitx.media","android.intent.action.VIEW","","'+url+'")')
			else:
				dialog.ok(addon_base,  "FUNCIONA APENAS EM SISTEMAS ANDROID !!".decode('unicode_escape'),'')
				sys.exit(0)	
				
	listItem = xbmcgui.ListItem(name, thumbnailImage=iconimage)
	xbmc.Player().play(item=url, listitem=listItem)			
	sys.exit()	
		
		
		
xbmcplugin.endOfDirectory(plugin_handle)