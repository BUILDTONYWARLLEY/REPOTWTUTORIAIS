"""

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 """

import urllib,urllib2,re,xbmcplugin,xbmcgui,os,sys,datetime
from resources.lib.common_variables import *
from resources.lib.directory import *
from resources.lib.youtubewrapper import *
from resources.lib.watched import * 

fanart = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.master', 'fanart.jpg'))
art = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.master/resources/img', ''))

def CATEGORIES():
        addDir('[COLOR orchid][B]GREATEST SLOW ROCK SONGS[/B][/COLOR]','PLq0ajtdli5G8idRnNPS_ei1eBimVu8tcn',1,art + 'http://legionworldtv.com/freeworld/images/rock.jpg')
        addDir('[COLOR blue][B]80S SOFT ROCK LOVE SONGS[/B][/COLOR]','PLq0ajtdli5G8idRnNPS_ei1eBimVu8tcn&index=1',1,art + 'http://legionworldtv.com/freeworld/images/rock.jpg')
        addDir('[COLOR yellow][B]ROCK SONGS HITS ALL TIME[/B][/COLOR]','PLp56AzR7YZeulJwWZc4yur7ooDg_UtKhD',1,art + '')
        addDir('[COLOR lime][B]CLASSIC SONGS 80S 90S[/B][/COLOR]','PLLlgdvO0Nffb3KR4mVLu7j3shB2ViZLGP',1,art + '')
        addDir('[COLOR orange][B]MOST BEAUTIFUL LOVE SONGS[/B][/COLOR]','PLAN2ijY9WzlwYR6_WtieIZtqZ94Wke5o9',1,art + '')
        addDir('[COLOR dodgerblue][B]BEST SONGS EVER[/B][/COLOR]','PLjZf72-EsullE1D-3zZj1Q1AVQS-zBzj5',1,art + '')
        addDir('[COLOR red][B]GREATEST HITS OF THE 80[/B][/COLOR]','PLEffX5-5DhPtWTyU3r8nm-ha6DySzKzoW&index=2',1,art + '')
        addDir('[COLOR darkmagenta][B]GREATEST HITS OF THE 70s 80s[/B][/COLOR]','PL8ICnoVYi7pc7AftMD5aY98hSkv3K0BEB',1,art + '')
        addDir('[COLOR cyan][B]BEST MOTOWN SONGS OF ALL TIME[/B][/COLOR]','PLwXYgB2CtnVM4M_yqVtxYpnJB3I95HU-l',1,art + '')
        addDir('[COLOR darkgoldenrod][B]BEST OLDIES LOVE SONGS OF ALL TIME[/B][/COLOR]','PLwXYgB2CtnVOLnv_SCr4V6YMKYwj92fhk',1,art + '')
        addDir('[COLOR orangered][B]GREATEST SOUL SONGS[/B][/COLOR]','PL00ZqAjyF5PW5uT90RAcS4UrEijLucslj',1,art + '')
        addDir('[COLOR salmon][B]GREATEST 70S 80S ROCK SONGS[/B][/COLOR]','PLYUQMTiCwszIPKuHfAaA7pcaM0Y6ljT6g',1,art + '')
        addDir('[COLOR chartreuse][B]BEST ROMANTIC ENGLISH LOVE SONGS[/B][/COLOR]','PLFjbVJl7eR36JfQl-_KbWf32e9aUwrJhO',1,art + '')
        addDir('[COLOR darkturquoise][B]CLASSIC OF THE 1986[/B][/COLOR]','PLtmCPKUMm2qafI6JvTqhIXwOK-LdtwXDv',1,art + '')
        addDir('[COLOR fuchsia][B]BALLADS 70 80 90 MIX[/B][/COLOR]','PLcKqw5e0etEDWf-kpMeDUE-4ZliLUha9J',1,art + '')
        addDir('[COLOR goldenrod][B]SLOW ROCK MEDLEY SONGS[/B][/COLOR]','PLa-b2dUvu_lB15vHu4qROJBKzPzVTbml2',1,art + '')
        addDir('[COLOR lawngreen][B]CLASSIC COLLECTION[/B][/COLOR]','PLmE-U8SJLN0TXSlUFjbq0c03jdig1920P',1,art + '')
        addDir('[COLOR limegreen][B]ROMANTIC SONGS EVER[/B][/COLOR]','PLjZf72-EsullE1D-3zZj1Q1AVQS-zBzj5',1,art + '')
        addDir('[COLOR maroon][B]DISCO 70S 80S 90S[/B][/COLOR]','PLGKE0rBZEgcN1z4AdApz9TSK7jkvO3SOh',1,art + '')	
        addDir('[COLOR blue]PlayLists[/COLOR]','url',10,art + 'PlayLists.png')
        logo = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.master','logo.png'))
        xbmcgui.Dialog().notification('Addon Master is brought to you','by Freeworld',logo,5000,False)
        

def PlayLists():
        addDir('[COLOR limegreen][B]THE BEST ARTIST ALL TIMES[/B][/COLOR]','PLmE-U8SJLN0TXSlUFjbq0c03jdig1920P',1,art + 'master.png')
        addDir('[COLOR limegreen][B]CLASSIC SONGS ALL TIMES[/B][/COLOR]','PL3485902CC4FB6C67',1,art + 'master.png')		
        addDir('[COLOR limegreen][B]PHILL COLLINS[/B][/COLOR]','PL78645F08099E55F9',1,art + 'master.png')
        addDir('[COLOR limegreen][B]BRIAN ADAMS[/B][/COLOR]','PL54D3F57300A406FA',1,art + 'master.png')
        addDir('[COLOR limegreen][B]BON JOVI[/B][/COLOR]','PL574FBF341B72DAD5',1,art + 'master.png')
        addDir('[COLOR limegreen][B]GUNS AND ROSES[/B][/COLOR]','PLE6EB681577F21B3C',1,art + 'master.png')
        addDir('[COLOR limegreen][B]LED ZEPPELIN[/B][/COLOR]','PLjH4YJfu1WfE2bciiQZ7Ci0TiIDzYE3HJ',1,art + 'master.png')
        addDir('[COLOR limegreen][B]QUIET RIOT[/B][/COLOR]','PLPTh1c6pC1BxPCNypTxkzSpbWcOgpstC6',1,art + 'master.png')
        addDir('[COLOR limegreen][B]SCORPIONS[/B][/COLOR]','PL8AB0F5120809FF19',1,art + 'master.png')
        addDir('[COLOR limegreen][B]QUEENS[/B][/COLOR]','PLqDzNilwDj_dm_BOGxoCRmvA6CheRwAiw',1,art + 'master.png')
        addDir('[COLOR limegreen][B]TWISTED SISTER[/B][/COLOR]','PL29662FBF0FC8F98D',1,art + 'master.png')
        addDir('[COLOR limegreen][B]DEEP PURPLE[/B][/COLOR]','PL8384361C552AE037',1,art + 'master.png')
        addDir('[COLOR limegreen][B]AC DC[/B][/COLOR]','PLQlc99hV-nkGWDaG-gJxwOfqp8jxyHaaQ',1,art + 'master.png')
        addDir('[COLOR limegreen][B]KISS[/B][/COLOR]','PL71A9E09DEF0CE017',1,art + 'master.png')
        addDir('[COLOR limegreen][B]EUROPE[/B][/COLOR]','PLDD6E90D62FC64610',1,art + 'master.png')
        addDir('[COLOR limegreen][B]BARON ROJO[/B][/COLOR]','PL79E4245F0137AA18',1,art + 'master.png')
        addDir('[COLOR limegreen][B]BONNIE TYLER[/B][/COLOR]','PLvz78UNxtDruCicAvERgXFk2XVgiBn_4y',1,art + 'master.png')
        addDir('[COLOR limegreen][B]TOTO[/B][/COLOR]','PLyNIUJIA6jp58gmBKIUQ5zh4UWRxQtXKe',1,art + 'master.png')
        addDir('[COLOR limegreen][B]FOREIGNER[/B][/COLOR]','PL72D7EDFFBD267A94',1,art + 'master.png')
        addDir('[COLOR limegreen][B]KANSAS[/B][/COLOR]','PLCCAB3C8590D69DC1',1,art + 'master.png')
        addDir('[COLOR limegreen][B]BEE GEES[/B][/COLOR]','PLE572452B578F4B90',1,art + 'master.png')
        addDir('[COLOR limegreen][B]ROLLING STONE[/B][/COLOR]','PLP02sRgldWRb9LjuQgJ4AfxCd4cxygDrA',1,art + 'master.png')
        addDir('[COLOR limegreen][B]BEATLES[/B][/COLOR]','PLmo4pBukfRoN8SB5RKvfiY9CTl9pI_IFc',1,art + 'master.png')
        addDir('[COLOR limegreen][B]THE DOORS[/B][/COLOR]','PL7DlGI0vwP4S6tlQ-kMqrl6VCaN053_BN',1,art + 'master.png')
        addDir('[COLOR limegreen][B]JIMI HENDRIX[/B][/COLOR]','PLMKA5kzkfqk2GEImRCIqGqWmQvKYygUhG',1,art + 'master.png')
        addDir('[COLOR limegreen][B]VAN HALEN[/B][/COLOR]','PLoIh3u70c_PKEjlagdBAK3cEe_wXKSee2',1,art + 'master.png')		
        addDir('[COLOR limegreen][B]THE EAGLE[/B][/COLOR]','PLwNBAifp_VilC7ch4uI0SQgxkRch4qzPh',1,art + 'master.png')
        addDir('[COLOR limegreen][B]THE POLICE[/B][/COLOR]','PL36494E8634856791',1,art + 'master.png')
        addDir('[COLOR limegreen][B]U2[/B][/COLOR]','PL57CDBF4FB33C5BC1',1,art + 'master.png')
        addDir('[COLOR limegreen][B]NIRVANA[/B][/COLOR]','PLF1D793B61571DD4A',1,art + 'master.png')
        addDir('[COLOR limegreen][B]METALLICA[/B][/COLOR]','PL926CCB27995D3E94',1,art + 'master.png')
        addDir('[COLOR limegreen][B]THE WHO[/B][/COLOR]','PLB2359E68D19BA3C0',1,art + 'master.png')
        addDir('[COLOR limegreen][B]PINK FLOYD[/B][/COLOR]','PL8CQIFqDrjYUVdJbkHe4--PkWZYBB3NoW',1,art + 'master.png')
        addDir('[COLOR limegreen][B]AEROSMITH[/B][/COLOR]','PL9E80D3CB56F329AF',1,art + 'master.png')
        addDir('[COLOR limegreen][B]ALICE COOPER[/B][/COLOR]','PLzMhF_Kgqw3iZBdZ4sX-kdVaWPCEo3q9B',1,art + 'master.png')
        addDir('[COLOR limegreen][B]MEAT LOAF[/B][/COLOR]','PLslHapSMmen25gJiJ1h4ljKgGctdoRMbM',1,art + 'master.png')
        addDir('[COLOR limegreen][B]OZZY OSBOURNE[/B][/COLOR]','PLjsINEkV8yYEvi_6VtsI8BSqFXM1QtQwM',1,art + 'master.png')		

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
page = None
token = None

try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except:
	try: 
		mode=params["mode"]
	except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: token=urllib.unquote_plus(params["token"])
except: pass
try: page=int(params["page"])
except: page = 1

print ("Mode: "+str(mode))
print ("URL: "+str(url))
print ("Name: "+str(name))
print ("iconimage: "+str(iconimage))
print ("Page: "+str(page))
print ("Token: "+str(token))

		
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def create_directory(dir_path, dir_name=None):
    if dir_name:
        dir_path = os.path.join(dir_path, dir_name)
    dir_path = dir_path.strip()
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        return_youtubevideos(name,url,token,page)

elif mode==5: 
        play_youtube_video(url)

elif mode==6:
        mark_as_watched(url)

elif mode==7:
        removed_watched(url)

elif mode==8:
        add_to_bookmarks(url)

elif mode==9:
        remove_from_bookmarks(url)
		
elif mode==10:
        print ""+url
        PlayLists()
	

xbmcplugin.endOfDirectory(int(sys.argv[1]))
