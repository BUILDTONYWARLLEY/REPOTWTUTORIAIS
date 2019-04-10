# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/OMundo2osBrasileiros
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools

from addon.common.addon import Addon

addonID = 'plugin.video.pegadinhasdosilviosantos'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

icon1 = 'http://www.trash80s.com.br/wp-content/uploads/2011/07/gg.jpg'
icon2 = 'http://v003o.popscreen.com/cXhrdnQxOXpGU0Ux_o_a-maldio-de-chucky---susto-no-ponto-de-nibus---cmera-.jpg'
icon3 = 'http://www.sbt.com.br/static/centraldeblogs/posts/images/932.jpg'
icon4 = 'http://3.bp.blogspot.com/-bqkX6fzY5dg/ULj9e_0t61I/AAAAAAAADKY/qRS41CHSQiA/s1600/meninafantasma9876.jpg'
def run():
    plugintools.log("pegadinhasdosilviosantos.run")
    
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

def main_list(params):
		plugintools.log("pegadinhasdosilviosantos ===> " + repr(params))

		plugintools.add_item(title = "Cameras Escondidas Com Ivo Holanda"       , url = base + "playlist/PLNSPiWvuc501UM6YHvrtCUspiG_gFIMet/"            , thumbnail = icon1, folder = True)
		plugintools.add_item(title = "Cameras Escondidas"     , url = base + "playlist/PLNSPiWvuc501UxVRe_qQxGFlkgJXHtlSy/", thumbnail = icon2, folder = True)
		plugintools.add_item(title = "Os Velhinhos Se Divertem"                    , url = base + "playlist/PLNSPiWvuc500oHe9Vp4cJ2P0t9RKGlxdD/" , thumbnail = icon3, folder = True)
		plugintools.add_item(title = "Cameras Escondidas no Elevador"                    , url = base + "playlist/PLNSPiWvuc5037Z6hQVD8W2MFMHFvCy0S0/" , thumbnail = icon4, folder = True)
       
		
		
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')
		xbmc.executebuiltin('Container.SetViewMode(500)')
		
run()
