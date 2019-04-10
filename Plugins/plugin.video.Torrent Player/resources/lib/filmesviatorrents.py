# -*- coding: utf-8 -*-

import urllib, urllib2, sys, re, os, unicodedata,urlparse
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup as bs4

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
	add_link('Lançamentos','http://www.filmesviatorrents.info/',10,icon, fanarts,'Lançamentos')
	add_link('Séries','http://www.filmesviatorrents.info/series-torrent',10,icon, fanarts,'Lançamentos')
	add_link('Categorias','http://www.filmesviatorrents.info/',11,icon, fanarts,'Lançamentos')
	add_link('Pesquisa','http://www.lapumiafilmes.com/',12,icon, fanarts,'Lançamentos')

def Pesquisar():
	keyb = xbmc.Keyboard('', 'Buscar..')
	keyb.doModal()
	if (keyb.isConfirmed()):
		search = keyb.getText()
		parametro_pesquisa=urllib.quote(search)
		url = 'http://www.filmesviatorrents.info/?s=%s&x=0&y=0' % parametro_pesquisa
		Listar_Filmes_E_Series(url)
	else:
		sys.exit()			
	
def Listar_Categorias(url):
	link = getUrl(url)
	soup = bs4(link)#<h2 style="text-align: center;">
	match = soup.find('div',{'style':'overflow: auto; height: 1240px; margin: 0px 0px 0px 6px;'})
	for a in match(re.compile('(i|li)')):
		name =  a.text.encode('utf-8')
		try:
			url = a.a['href']
		except: 
			name = '[COLOR red]'+name+'[/COLOR]'
			url = ''
		if not 'Tutoriais' in name:
			add_link(name,url,10,icon, fanarts,'Lançamentos')
		
def Listar_Filmes_E_Series(url):
	fa = getUrl(url)
	match = re.compile('<div class="center-widget"><h2 class="post-title"><a href="(.*?)".*?">(.*?)<.a>.*?<div class="post-content">.*?<img.*?src=.(.*?). width').findall(fa.replace('\n',''))
	temp = len(match)
	for a in match:
		try: name = a[1].split(' Torrent ')[0].replace('&','').replace('#8211;',"-").replace('#038;',"&")
		except: name = a[1]
		url = a[0]
		img = a[2]
		add_link(name,url,100,img, fanarts,'d')
	if temp==0:
		match = re.compile('''<div class="center-widget">\s*<h2 class="post-title">\s*<a href="(.*?)".*?>(.*?)<.a>.*?<div class="post-content">.*?<img.*?src=[",'](.*?)[",'] width''').findall(fa.replace('\n',''))
		for a in match:
			try: name = a[1].split(' Torrent ')[0].replace('&','').replace('#8211;',"-").replace('#038;',"&")
			except: name = a[1]
			url = a[0]
			try:img = a[2].split('"')[0]
			except: img = a[2]
			add_link(name,url,100,img, fanarts,'d')
	soup = BeautifulSoup(fa)
	match = soup('div',{'class':'wp-pagenavi'})
	for a in match:
		url_pagina = '%s' % a.findAll('a',{'class':'nextpostslink'})[0]['href']
		pagina = '%s' % a.findAll('span',{'class':'pages'})[0].text
		add_link('[COLOR green]'+pagina.encode('utf-8')+'[/COLOR]',url_pagina,10,Proxima, fanarts,'d')
		
