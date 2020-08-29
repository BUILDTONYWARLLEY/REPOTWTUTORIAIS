import sys
import urllib
import urlparse
import xbmcgui
import xbmcplugin
import xbmcaddon
import shutil
from shutil import copyfile

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
addon = xbmcaddon.Addon()

xbmcplugin.setContent(addon_handle, 'videos')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

xxxmenu = xbmcaddon.Addon('plugin.video.xxxmenu')

addon_icon = 'special://home/addons/plugin.video.xxxmenu/icon.png'
recycle_icon = 'special://home/addons/plugin.video.xxxmenu/recycle.png'

pandamovies_icon = 'special://home/addons/plugin.video.xxxmenu/pandamovie.png'
mangoporn_icon = 'special://home/addons/plugin.video.xxxmenu/mangoporn.png'
streamingporn_icon = 'special://home/addons/plugin.video.xxxmenu/streamingporn.png'
sexkino_icon = 'special://home/addons/plugin.video.xxxmenu/sexkino.png'
pornkino_icon = 'special://home/addons/plugin.video.xxxmenu/pornkino.png'
sexuria_icon = 'special://home/addons/plugin.video.xxxmenu/sexuria.png'

mode = args.get('mode', None)

if mode is None:

    url = build_url({'mode': 'xxxmenu', 'foldername': '[COLOR blue][B]XXX MENU[/B][/COLOR]'})
    li = xbmcgui.ListItem('[COLOR blue][B]XXX MENU[/B][/COLOR]', iconImage=addon_icon)
    li.setInfo(type='video', infoLabels={'plot': '[COLOR blue][B]XXX MENU[/B][/COLOR]'})
    li.setArt({'fanart': xxxmenu.getAddonInfo('fanart')}) 
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=False)

    url = build_url({'mode': 'mangoporn', 'foldername': 'Mangoporn'})
    li = xbmcgui.ListItem('Mangoporn', iconImage=mangoporn_icon)
    li.setInfo(type='video', infoLabels={'plot': 'www.mangoporn.net'})
    li.setArt({'fanart': xxxmenu.getAddonInfo('fanart')}) 
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=False)

    url = build_url({'mode': 'pandamovies', 'foldername': 'Pandamovies'})
    li = xbmcgui.ListItem('Pandamovies', iconImage=pandamovies_icon)
    li.setInfo(type='video', infoLabels={'plot': 'www.pandamovies.pw'})
    li.setArt({'fanart': xxxmenu.getAddonInfo('fanart')}) 
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=False)

    url = build_url({'mode': 'pornkino', 'foldername': 'Pornkino'})
    li = xbmcgui.ListItem('Pornkino', iconImage=pornkino_icon)
    li.setInfo(type='video', infoLabels={'plot': 'www.pornkino.to'})
    li.setArt({'fanart': xxxmenu.getAddonInfo('fanart')}) 
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=False)

    url = build_url({'mode': 'sexkino', 'foldername': 'Sexkino'})
    li = xbmcgui.ListItem('Sexkino', iconImage=sexkino_icon)
    li.setInfo(type='video', infoLabels={'plot': 'www.sexkino.to'})
    li.setArt({'fanart': xxxmenu.getAddonInfo('fanart')}) 
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=False)


    url = build_url({'mode': 'sexuria', 'foldername': 'Sexuria'})
    li = xbmcgui.ListItem('Sexuria', iconImage=sexuria_icon)
    li.setInfo(type='video', infoLabels={'plot': 'www.sexuria.com'})
    li.setArt({'fanart': xxxmenu.getAddonInfo('fanart')}) 
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=False)

    url = build_url({'mode': 'streamingporn', 'foldername': 'Streamingporn'})
    li = xbmcgui.ListItem('Streamingporn', iconImage=streamingporn_icon)
    li.setInfo(type='video', infoLabels={'plot': 'www.streamingporn.xyz'})
    li.setArt({'fanart': xxxmenu.getAddonInfo('fanart')}) 
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=False)

    url = build_url({'mode': 'clean', 'foldername': 'Clear [COLOR blue][B]XXX MENU[/B][/COLOR] cache'})
    li = xbmcgui.ListItem('Clear [COLOR blue][B]XXX MENU[/B][/COLOR] cache', iconImage=recycle_icon)
    li.setInfo(type='video', infoLabels={'plot': 'Clear [COLOR blue][B]XXX MENU[/B][/COLOR] cache'})
    li.setArt({'fanart': xxxmenu.getAddonInfo('fanart')}) 
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=False)

    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'xxxmenu':
    xbmc.executebuiltin('Container.Refresh')

elif mode[0] == 'pandamovies':
    xbmc.executebuiltin('RunAddon(plugin.video.pandamovies.pw)')

elif mode[0] == 'mangoporn':
    xbmc.executebuiltin('RunAddon(plugin.video.mangoporn.net)')

elif mode[0] == 'streamingporn':
    xbmc.executebuiltin('RunAddon(plugin.video.streamingporn.xyz)')

elif mode[0] == 'sexkino':
    xbmc.executebuiltin('RunAddon(plugin.video.sexkino.to)')

elif mode[0] == 'pornkino':
    xbmc.executebuiltin('RunAddon(plugin.video.pornkino.to)')

elif mode[0] == 'sexuria':
    xbmc.executebuiltin('RunAddon(plugin.video.sexuria.com)')

elif mode[0] == 'clean':
    tmp_path = xbmc.translatePath("special://userdata/addon_data/plugin.video.xxxmenu/tmp/").decode("utf-8")
    try:
        shutil.rmtree(tmp_path, ignore_errors=True)
    except:
        pass
    xbmc.executebuiltin('Notification([COLOR blue][B]XXX MENU[/B][/COLOR], Cache successfully cleared., 5000, %s)' % (addon_icon))
    xbmc.executebuiltin('Container.Refresh')
