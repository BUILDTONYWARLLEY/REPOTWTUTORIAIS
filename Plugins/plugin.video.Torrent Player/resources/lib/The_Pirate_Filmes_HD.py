# -*- coding: utf-8 -*-

import urllib, urllib2, sys, re, os, unicodedata,urlparse
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser
h = HTMLParser()		
##############################################################################################
plugin_handle = int(sys.argv[1])

mysettings = xbmcaddon.Addon(id = 'plugin.video.Torrent Player')
addon_name = 'MMFilmes'
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')
fanarts = xbmc.translatePath(os.path.join(home, 'fanart2.jpg'))
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
Proxima = xbmc.translatePath(os.path.join(home, 'Proxima.png'))
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
base = 'https://www.meuguia.tv/'
dialog = xbmcgui.Dialog()    
Fav = xbmc.translatePath(os.path.join(profile, 'Fav.json'))

#############################################################################################
def getUrl(url):
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
xbmc.log('%s'  % params)
url = params.get("url")
name = params.get("name")
mode = int(params.get("mode",'0'))
iconimage = params.get("iconimage")
description = params.get("description")
items = ['Home']
def Home():
	add_link('Lançamentos','http://www.thepiratefilmeshd.com/',2,icon, fanarts,'Lançamentos')
	add_link('Séries','http://www.thepiratefilmeshd.com/',2,icon, fanarts,'Séries')
	add_link('Categorias','http://www.thepiratefilmeshd.com/',3,icon, fanarts,'Categoria')
	add_link('Pesquisa','http://',4,icon, fanarts,'Categoria')

#mode 2	
def Listar_Filmes_E_Series(url):
	fa = getUrl(url)
	match = re.compile('<h2 class="post-box-title">\s*<a href="(.*?)">(.*?)</a>.*?<img.*?src="(.*?)" alt=').findall(fa.replace('\n',''))
	for a in match:
		try: name = a[1].split(' Torrent ')[0]
		except: name = a[1]
		url = a[0]
		img = a[2]
		add_link(name,url,100,img, fanarts,'d')
	soup = BeautifulSoup(fa)
	match = soup('div',{'class':'pagination'})
	for a in match:
		url_pagina = '%s' % a.findAll('span',{'id':'tie-next-page'})[0].a['href']
		pagina = '%s' % a.findAll('span',{'class':'pages'})[0].text
		add_link('[COLOR green]'+pagina.encode('utf-8')+'[/COLOR]',url_pagina,2,Proxima, fanarts,'d')
	
def Listar_Categorias(url):	
	fa = getUrl(url)
	soup = BeautifulSoup(fa)#<div class="main-menu">
	match = soup.find('div',{'class':'main-menu'}).findAll('a')
	for a in match:
		try:
			name = a.text.encode('utf-8')
			url = a.get('href')
			if not name in items:
				add_link(name,url,2,icon, fanarts,'categoria')	
		except: pass	
def Pesquisar():
	keyb = xbmc.Keyboard('', 'Buscar..')
	keyb.doModal()
	if (keyb.isConfirmed()):
		search = keyb.getText()
		parametro_pesquisa=urllib.quote(search)
		url = 'http://www.thepiratefilmeshd.com/?s='+parametro_pesquisa
		Listar_Filmes_E_Series(url)
	else:
		sys.exit()		