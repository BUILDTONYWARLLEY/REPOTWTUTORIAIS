'''
    Mr. Bean Add-on

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
'''

from resources.lib import Addon, source
import sys, os, urllib, urllib2
import json, base64
import xbmc, xbmcgui, xbmcplugin, xbmcaddon

import liveresolver

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
addonid = addon.getAddonInfo('id')
plugin_path = xbmcaddon.Addon(id=addonid).getAddonInfo('path')

Addon.plugin_url = sys.argv[0]
Addon.plugin_handle = int(sys.argv[1])
Addon.plugin_queries = Addon.parse_query(sys.argv[2][1:])

dlg = xbmcgui.Dialog()

Addon.log('plugin url: ' + Addon.plugin_url)
Addon.log('plugin queries: ' + str(Addon.plugin_queries))
Addon.log('plugin handle: ' + str(Addon.plugin_handle)) 

addon_logo = xbmc.translatePath(os.path.join(plugin_path,'tvaddons_logo.png'))

mode = Addon.plugin_queries['mode']

if mode == 'main':
    try:
        playlists = source.Source().build_main()
        if playlists:
            for c in sorted(playlists):
                Addon.add_directory({'mode': c['title']}, c['title'], img = c['img'])
        if len(Addon.get_setting('notify')) > 0:
            Addon.set_setting('notify', str(int(Addon.get_setting('notify')) + 1))  
        else:
            Addon.set_setting('notify', "1")        
        if int(Addon.get_setting('notify')) == 1:
            xbmcgui.Dialog().notification(addonname + ' is provided by:','www.tvaddons.co',addon_logo,5000,False)
        elif int(Addon.get_setting('notify')) == 9:
            Addon.set_setting('notify', "0")
    except:
        dlg.ok(Addon.get_string(5000), Addon.get_string(8000))
        exit()

def show_streams(title, playlist_id):
    if mode == title:
        streams = source.Source().get_streams(playlist_id)
        if streams:
            for c in streams:
                title = c['title']
                channel = c['title']
                videoId = c['videoId']
                img = c['img']
                rURL = Addon.plugin_url + "?channel=" + channel + "&videoId=" + videoId + "&mode=play"
                Addon.add_video_item(rURL, {'title': title}, img=img)

    elif mode == 'play':
        videoId = Addon.plugin_queries['videoId']
        stream_status = source.Source()._get_json('/check' + base64.b64decode('LnBocA=='), {'id': videoId})['status']
        if stream_status == 'true':
            stream = "https://www.youtube.com/watch?v=" + videoId
            stream_url = liveresolver.resolve(stream)
            item = xbmcgui.ListItem(path=stream_url)
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
        else:
            dlg.ok(Addon.get_string(5000), Addon.get_string(7000))
            exit()

if mode != 'main':
    playlists = source.Source().build_main()
    if playlists:
        for c in playlists:
            show_streams(c['title'], c['playlist_id'])

Addon.end_of_directory()
