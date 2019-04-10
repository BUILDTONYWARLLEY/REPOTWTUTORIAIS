# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/OMundo2osBrasileiros
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools

from addon.common.addon import Addon

addonID = 'plugin.video.turmadamonica'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'


def run():
    plugintools.log("turmadamonica.run")
    
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

def main_list(params):
		plugintools.log("turmadamonica ===> " + repr(params))

		
                plugintools.add_item(title = "Turma da Mônica Todos os episódios"             , url = base + "playlist/PLWduEF1R_tVZYNTH8ajFOEDkDT_hfIQL9/",       thumbnail = icon, folder = True)
                plugintools.add_item(title = "Turma da Mônica Toy Todos os episódios"             , url = base + "playlist/PLWduEF1R_tVYCikTS9pSWwd3UtfmotVvr/",       thumbnail = icon, folder = True)
                #plugintools.add_item(title = "turmadamonica 3º Temp"             , url = base + "playlist/PLNu1vy5jyfy9YUHDSSZwlHhCe0oXvLWPw/",       thumbnail = icon, folder = True)
                #plugintools.add_item(title = "turmadamonica 4º Temp"             , url = base + "playlist/PLNu1vy5jyfy_RAr9Z8BMMjH--GE_7sKdS/",       thumbnail = icon, folder = True)
                #plugintools.add_item(title = "turmadamonica Especiais"            ,url = base + "playlist/PLgGs0j7UlMwiL1ltRijidE_sKgKnCFYRg/",       thumbnail = icon, folder = True)

		
		
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')
		xbmc.executebuiltin('Container.SetViewMode(500)')
		
run()
