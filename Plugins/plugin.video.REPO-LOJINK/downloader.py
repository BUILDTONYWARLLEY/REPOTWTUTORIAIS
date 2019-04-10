#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import xbmcgui
import urllib, time

addon_base='ADD-ONS REPOSITORY'
dialog = xbmcgui.Dialog()    

exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("ZCAxKDYuMTIpOgoJNCA9ICczLzUuMCAoZTsgYiAxNSkgMi85LjExIChjLCAxMCBhKSA4LzE0LjAuZi4xMyA3LzkuMTEn")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|aresdownload|AppleWebKit|Mozilla|version|5|urllib|Safari|Chrome|537|Gecko|Linux|KHTML|class|X11|1271|like|11|FancyURLopener|64|23|x86_64".split("|")))

class StopDownloading(Exception): 
    def __init__(self, value): 
        self.value = value 
    def __str__(self): 
        return repr(self.value)

def download(url, dest, null):

	global start_time
	global dp

	start_time=time.time()

	if url.find('ares1') == -1:

		if not 'dp' in globals():
			dp = xbmcgui.DialogProgress()
			dp.create("repo-lojink".title(),"iniciando download".title(),' ', ' ')
		dp.update(0)
		urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs))

		
	else:
	
		if not 'dp' in globals():
			dp = xbmcgui.DialogProgress()
			dp.create("repo-lojink".title(),"iniciando download".title(),' ', ' ')
		dp.update(0)
		aresdownload().retrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs))
		

		

 
def _pbhook(numblocks, blocksize, filesize):
        try:
            percent = min(numblocks * blocksize * 100 / filesize, 100) 
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0: 
                eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: 
                eta = 0 
            kbps_speed = kbps_speed / 1024 
            mbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '[COLOR lightskyblue]%.02f MB[/COLOR] of [B]%.02f MB[/B]' % (currently_downloaded, total)
            e = '[COLOR white][B]Speed: [/B][/COLOR][COLOR lightskyblue]%.02f Mb/s ' % mbps_speed  + '[/COLOR]'
            e += '[COLOR white][B]ETA: [/B][/COLOR][COLOR lightskyblue]%02d:%02d' % divmod(eta, 60)  + '[/COLOR]'
            dp.update(percent, mbs, e)
        except:
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled():
            dialog.ok("repo-lojink".title(), 'o download foi cancelado.'.title())
            dp.close()
            quit()
