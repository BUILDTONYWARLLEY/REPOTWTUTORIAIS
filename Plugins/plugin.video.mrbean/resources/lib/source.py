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

import sys, os, re
import urllib, urllib2
import json, random, base64
import xbmcgui, xbmc, xbmcvfs
import Addon

class Source:

    def __init__(self):
        self.dlg = xbmcgui.Dialog()
        self.mBASE = base64.b64decode('aHR0cHM6Ly9taGFuY29jNy5zb3VyY2Vjb2RlLmFnL3l0cG93ZXJlZA==')

    def build_main(self):
        content = self._get_json('/get_playlists' + base64.b64decode('LnBocA==') , {'id': base64.b64decode('VUNrQUdySENMRm1sSzNIMmtkNmlzaXBn')})
	playlists = []
	results = content['results']
	for i in results:
	    playlists.append({
                'channel': i['title'],
                'title': i['title'],
                'playlist_id': i['playlist_id'],
                'img': i['img']
	        })
	return playlists  

    def get_streams(self, playlist_id):
	content = self._get_json('/get_streams' + base64.b64decode('LnBocA=='), {'id': playlist_id})
	streams = []
	results = content['results']
	for i in results:
            streams.append({
                'channel': i['title'],
	        'title': i['title'],
	        'videoId': i['id'],
                'img': i['img']
	    })
	        
	return streams 
            
    def _build_url(self, path, queries={}):
        if queries:
            query = Addon.build_query(queries)
            return '%s/%s?%s' % (self.mBASE, path, query)
        else:
            return '%s/%s' % (self.mBASE, path)

    def _build_json(self, path, queries={}):
        if queries:
            query = urllib.urlencode(queries)
            return '%s/%s?%s' % (self.mBASE, path, query)
        else:
            return '%s/%s' % (self.mBASE, path)

    def _fetch(self, url, form_data=False):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        if form_data:
            req = urllib2.Request(url, form_data)
        else:
            req = url
        try:
            response = opener.open(req)
            return response
        except urllib2.URLError, e:
            return False

    def _get_json(self, path, queries={}):
        content = False
        url = self._build_json(path, queries)
        response = self._fetch(url)
        if response:
            content = json.loads(response.read())
        else:
            content = False
        return content

    def _get_html(self, path, queries={}):
        html = False
        url = self._build_url(path, queries)
   
        response = self._fetch(url)
        if response:
            html = response.read()
        else:
            html = False
        return html
