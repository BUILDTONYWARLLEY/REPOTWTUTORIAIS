# -*- coding: utf-8 -*-

import urllib, urllib2, sys, re, os, unicodedata,urlparse
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser
h = HTMLParser()		
##############################################################################################
plugin_handle = int(sys.argv[1])
addon_id = 'plugin.video.The Pirate Filmes'
mysettings = xbmcaddon.Addon(id = addon_id)
addon_name = 'The Pirate Filmes'
profile =xbmc.translatePath(mysettings.getAddonInfo('profile').decode('utf-8'))
home = mysettings.getAddonInfo('path')
fanarts = xbmc.translatePath(os.path.join(home, 'fanart2.jpg'))
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
dialog = xbmcgui.Dialog()    
Proxima = xbmc.translatePath(os.path.join(home, 'Proxima.png'))
Fav = os.path.join(profile, 'Fav')
#############################################################################################
from bs4 import BeautifulSoup as bs4

def Soups(url):
	link = abrir_url(url)
	return bs4(link)			
	
def log(log):
	xbmc.log('%s'% log, xbmc.LOGNOTICE)
		
def abrir_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link

def GetEncodeString(str):
	try:
		str = str.decode(chardet.detect(str)["encoding"]).encode("utf-8")
	except:
		try:
			str = str.encode("utf-8")
		except:
			pass
	return str

def add_dir(name, url, mode, iconimage, fanart,description):
	if 'Menus' in description:
		try: 
			name = GetEncodeString(name)
		except: pass
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	cmItems = []
	if mode==2:
		cmItems.append(('[COLOR springgreen]Ver Sinopse[/COLOR]', 'XBMC.RunPlugin(%s?url=%s&mode=5&name=%s&iconimage=%s)'%(sys.argv[0], url,name.decode('utf-8'),iconimage)))	
		cmItems.append(('[COLOR springgreen]Play Trailer[/COLOR]', 'XBMC.RunPlugin(%s?url=%s&mode=6&name=%s&iconimage=%s)'%(sys.argv[0], url,name.decode('utf-8'),iconimage)))	
	liz.addContextMenuItems(cmItems, replaceItems=False)
	liz.setProperty('fanart_image', fanart)	
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok

def add_link(name, url, mode, iconimage, fanart,description):
	u = sys.argv[0]+ "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage) + "&description=" + urllib.quote_plus(description)	
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'true')
	contextMenu = []

	liz.addContextMenuItems(contextMenu)
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)  		

def get_params():
	param = []
	paramstring = sys.argv[2]
	if len(paramstring)>= 2:
		params = sys.argv[2]
		cleanedparams = params.replace('?', '')
		if (params[len(params)-1] == '/'):
			params = params[0:len(params)-2]
		pairsofparams = cleanedparams.split('&')
		param = {}
		for i in range(len(pairsofparams)):
			splitparams = {}
			splitparams = pairsofparams[i].split('=')
			if (len(splitparams)) == 2:
				param[splitparams[0]] = splitparams[1]
	return param
	
params = get_params()
#log(params)
url = None
name = None
mode = None
iconimage = None
description  = None
try: url = urllib.unquote_plus(params["url"])
except: pass
try: name = urllib.unquote_plus(params["name"])
except: pass
try: mode = int(params["mode"])
except: pass

try: iconimage = urllib.unquote_plus(params["iconimage"])
except: pass  

try: description = urllib.unquote_plus(params["description"])
except: pass  

		
if os.path.exists(profile)==False:
    os.mkdir(profile)		

Repo = xbmc.translatePath('special://home/addons/plugin.video.REPO-LOJINK')
if os.path.exists(Repo)==False:
	dialog.textviewer(addon_name,'                                                            ADD-ON BLOQUEADO\n\n\nSE VOCÊ ESTÁ VENDO ESTÁ MENSAGEM É PORQUÊ VOCÊ  NÃO INSTALOU O REPOSITÓRIO DO ADD-ON.\nNOME DO REPOSITÓRIO OFICIAL:   [COLOR red]REPO-LOJINK[/COLOR]\nFAÇA DOWNLOAD PELO LINK:         [COLOR red]bit.ly/Repo_Lojink_2[/COLOR]'.decode('unicode_escape'))
	sys.exit()	
	
if mode==None:
	add_dir('Lançamentos', 'https://thepiratefilmesoficial.com/', 1, icon, fanart,'Menu')
	add_dir('Séries', 'https://thepiratefilmesoficial.com/category/series', 1, icon, fanart,'Menu')
	add_dir('Gêneros', 'https://thepiratefilmesoficial.com/', 3, icon, fanart,'Menu')
	add_dir('Pesquisar', '0-0', 4, icon, fanart,'Menu')
	
elif mode==4:	
	keyb = xbmc.Keyboard('', 'Pesquisar...')
	keyb.doModal()
	if (keyb.isConfirmed()):
		search = keyb.getText()
		parametro_pesquisa=urllib.quote(search)
		urls = 'https://thepiratefilmesoficial.com/?s=%s' % parametro_pesquisa 
		link = abrir_url(urls)
		soup  = bs4(link)
		try:
			pagina = re.compile('<.a><.li><li><a href="(.*?)"><i class="uk-icon-angle-double-right"><.i><.a><.li><.ul><.div>').findall(link)[0].split('href="')[-1]
			add_dir('[COLOR springgreen]Próxima Página[/COLOR]',pagina,1,Proxima, fanarts,'Menus')
		except: pass
		rew = soup.findAll('div',{'class':"uk-container uk-container-center uk-margin-large-top uk-margin-large-bottom"})
		x = 0
		for a in rew:
			filmes  = a('div',{'class':"uk-overlay uk-overlay-hover"})
			idioma = a('span',{'class':"rating"})
			for b in filmes:
				name  =  '%s  -  %s' % (b.a['title'].encode('utf-8'),re.compile('\s*(.*)\s*').findall(idioma[x].text.encode('utf-8'))[0])
				img   =  b.img['src']
				url   =  b.a['href']
				x = x+1
				add_dir(name, url, 2, img, fanart,'')		

elif mode==3:
	link = abrir_url(url)
	soup  = bs4(link)
	rew = soup('ul',{'role':"menu",'class':"uk-nav-sub"})
	for a in rew:
		for b in a.findAll('a'):
			name  =  b.text.encode('utf-8')
			url = b['href']
			if '/category/' in url:
				add_dir(name, url, 1, icon, fanart,'dd')

elif mode==1:#Listar filme s e séries
	link = abrir_url(url)
	soup  = bs4(link)
	try:
		pagina = re.compile('<.a><.li><li><a href="(.*?)"><i class="uk-icon-angle-double-right"><.i><.a><.li><.ul><.div>').findall(link)[0].split('href="')[-1]
		add_dir('[COLOR springgreen]Próxima Página[/COLOR]',pagina,1,Proxima, fanarts,'Menus')
	except: pass
	rew = soup.findAll('div',{'class':"uk-container uk-container-center uk-margin-large-top uk-margin-large-bottom"})
	x = 0
	for a in rew:
		filmes  = a('div',{'class':"uk-overlay uk-overlay-hover"})
		idioma = a('span',{'class':"rating"})
		for b in filmes:
			name  =  '%s  -  %s' % (b.a['title'].encode('utf-8'),re.compile('\s*(.*)\s*').findall(idioma[x].text.encode('utf-8'))[0])
			img   =  b.img['src']
			url   =  b.a['href']
			x = x+1
			add_dir(name, url, 2, img, fanart,'')		

elif mode==2:#def player ou buscar os links
	link = abrir_url(url)
	soup  = bs4(link)
	try:
		Trailers = soup('div',{'class':"uk-cover uk-margin-top",'style':"height: 400px;"})
		Trailer = Trailers[0].iframe['src']
		add_dir('Play Trailer', Trailer, 100, iconimage, fanart,'')
	except: pass
	try:
		rew = soup.find('div',{'class':"uk-accordion",'data-uk-accordion':"{showfirst: false}"})
		for a in rew.findAll(re.compile('(a|h3)')):
			name =  a.text.encode('utf-8')
			url = a.get('href','')
			add_dir(name, url, 100, iconimage, fanart,'')
	except:
		rew = soup.find('div',{'id':"modal",'class':"uk-modal"})
		for a in rew('center'):
			try: name = a.img.get('alt','')
			except: name = ''
			try: url  =  a.a['href']
			except: url = ''
			name = name
			url = url
			if not name=='':
				add_dir(name, url, 100, iconimage, fanart,'')

elif mode==5:
	soup  = Soups(url)
	rew = soup('ul',{'id':"media-tabs",'class':"uk-switcher"})
	ad = '[COLOR springgreen]%s[/COLOR]' % name
	ad += '%s\n' % rew[0]('ul',{'class':"uk-subnav uk-subnav-line"})[0].text.encode('utf-8')
	ad += '[COLOR springgreen]Descrição[/COLOR]: %s\n' % rew[0]('p',{'class':"uk-text-muted uk-h4"})[0].text.encode('utf-8')
	ad += '%s\n' % rew[0]('dl',{'class':"uk-description-list-horizontal uk-margin-top"})[0].text.encode('utf-8').replace(':\n',':').split('Tags')[0]
	ad = ad.replace('Título Original','[COLOR springgreen]Título Original[/COLOR]').replace('Gênero','[COLOR springgreen]Gênero[/COLOR]').replace('Idioma','[COLOR springgreen]Idioma[/COLOR]')
	ad = ad.replace('IMDb','[COLOR springgreen]IMDb[/COLOR]').replace('Tempo','[COLOR springgreen]Tempo[/COLOR]').replace('Ano','[COLOR springgreen]Ano[/COLOR]').replace('Audio','[COLOR springgreen]Audio[/COLOR]').replace('Video','[COLOR springgreen]Video[/COLOR]').replace('Formato','[COLOR springgreen]Formato[/COLOR]')
	dialog.textviewer(addon_name,ad)

elif mode==6:
	import urlresolver
	link = abrir_url(url)
	soup  = bs4(link)
	Trailers = soup('div',{'class':"uk-cover uk-margin-top",'style':"height: 400px;"})
	Trailer = Trailers[0].iframe['src']
	playd = urlresolver.resolve(Trailer)
	listItem = xbmcgui.ListItem(name, thumbnailImage=iconimage)
	xbmc.Player().play(item=playd, listitem=listItem)			
	sys.exit()	
elif mode==100:
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