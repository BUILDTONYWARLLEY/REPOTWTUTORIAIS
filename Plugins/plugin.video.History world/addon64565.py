# -*- coding: UTF-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,sys
import urlresolver
from BeautifulSoup import BeautifulSoup
import plugintools

addon_base = 'History world'
addon_id = 'plugin.video.History world'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
fanart = addonfolder + '/fanart.jpg'
icones = addonfolder + '/icon.png'
arquivos_file = addonfolder + '/UPEEIIIIII.txt'
dialog=xbmcgui.Dialog()

############################################################################################
import xbmcaddon,xbmc,xbmcgui
import os 

addon_base			= 'History world'
addon_id			= 'plugin.video.History world'
selfAddon			=	xbmcaddon.Addon(id=addon_id)
addonfolder			=	selfAddon.getAddonInfo('path')	
pesquisar_addon		=	addonfolder + '/addon.xml'
itemsss				=	open(pesquisar_addon,'r').read()
REPO				=	xbmc.translatePath('special://home/addons/plugin.video.REPO-LOJINK')
dialog				=	xbmcgui.Dialog()
if 'PGFkZG9uIGlkPSJwbHVnaW4udmlkZW8uSGlzdG9yeSB3b3JsZCIgbmFtZT0iSGlzdG9yeSB3b3JsZCIgdmVyc2lvbj0iMy4wLjAiIHByb3ZpZGVyLW5hbWU9ImxvamluayI+'.decode('base64') in itemsss:
	pass
else:
	dialog.textviewer(addon_base,'                                                            [COLOR red]ADD-ON BLOQUEADO\n\n\nSE VOCÊ ESTÁ VENDO ESTA MENSAGEM É PORQUÊ ESSE ADD-ON FOI PLAGIADO ENTÃO PROCURE O ORIGINAL QUE ATENDE PELO NOME DE[/COLOR]:  [COLOR green][B]'+addon_base+'[/B][/COLOR]\n\n\n[COLOR red]OU PROCURE O REPOSITÓRIO DO ADD-ON[/COLOR]:  [COLOR green][B]REPO LOJINK[/B][/COLOR]')
	sys.exit(0)

if not os.path.exists(REPO):
	dialog.textviewer(addon_base,'                                                            [COLOR red]ADD-ON BLOQUEADO\n\n\nSE VOCÊ ESTÁ VENDO ESTA MENSAGEM É PORQUÊ VOCÊ  NÃO INSTALOU O REPOSITÓRIO DO ADD-ON  QUE ATENDE PELO NOME DE[/COLOR]:  [COLOR green][B]REPO-LOJINK[/B][/COLOR]')
	sys.exit(0)	
else:
	pass	
	
##############################################################################################	
	
def add_item(title="",url="",thumbnail="",folder=True):
	listitem=xbmcgui.ListItem(title,iconImage="DefaultVideo.png",thumbnailImage=thumbnail)
	if url.startswith("plugin://"): 
		itemurl=url
	contextMenuItems = []
	#contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
	listitem.addContextMenuItems(contextMenuItems, replaceItems=True)  
	listitem.setProperty('IsPlayable','true')
	listitem.setProperty('fanart_image', fanart)
	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=itemurl,listitem=listitem,isFolder=folder)
	
def CATEGORIES():
	linkss = abrir_url('https://raw.githubusercontent.com/brunolojino/listas/master/history%20world.txt')
	htmls = BeautifulSoup(linkss)
	links = htmls.findAll('item')
	for link in links:
		nome = link.title.text
		#type = link.utube.text
		img = link.thumbnail.text
		if link.utube.text.startswith('UC') and len(link.utube.text) > 12:
			utube = 'plugin://plugin.video.youtube/channel/' + link.utube.text + '/'
		elif not link.utube.text.startswith('UC') and not (link.utube.text.startswith('PL'))  :
			utube = 'plugin://plugin.video.youtube/user/' + link.utube.text + '/'
		add_item(nome.encode('utf8'),utube,img,folder= True)
		

def plugin_url(url):
	xbmc.executebuiltin('XBMC.RunPlugin(%s)'% url)
	
def abrir_url(url):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		return link
	except IOError:#     except urllib2.HTTPError, e:
		dialog.notification(addon_base,'Não foi possivel acessar o servidor.',icones)
		sys.exit(0)
	

def addDir(name,url,mode,iconimage,pasta=True,total=1,plot=''):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo( type="video", infoLabels={ "title": name, "plot": plot } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	return ok

############################################################################################################
#                                               GET PARAMS                                                 #
############################################################################################################
              
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

      
params=get_params()
url=None
name=None
mode=None
iconimage=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

try:        
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass


xbmc.log("URL: "+str(url))
xbmc.log("Name: "+str(name))



###############################################################################################################
#                                                   MODOS                                                     #
###############################################################################################################
#abrir_url('https://goo.gl/oKyPTl')


if mode==None or url==None or len(url)<1:
        CATEGORIES()

elif mode==2: plugin_url(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))