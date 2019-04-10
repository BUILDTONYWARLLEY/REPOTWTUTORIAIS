

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools

from addon.common.addon import Addon

addonID = 'plugin.video.CountryBox'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
icon2   = "https://yt3.ggpht.com/-Ay0mPIoFk3c/AAAAAAAAAAI/AAAAAAAAAAA/8j4J0h4LBEo/s500-mo-c-c0xffffffff-rj-k-no/photo.jpg"
icon3   = "https://yt3.ggpht.com/-QRUGV7yb6U0/AAAAAAAAAAI/AAAAAAAAAAA/8stINId_VI0/s500-mo-c-c0xffffffff-rj-k-no/photo.jpg"
icon4   = "https://yt3.ggpht.com/-079Xv2JYHq4/AAAAAAAAAAI/AAAAAAAAAAA/szq8Sh1LyNE/s500-mo-c-c0xffffffff-rj-k-no/photo.jpg"
icon5   = "https://yt3.ggpht.com/-3azPi-Sx1P4/AAAAAAAAAAI/AAAAAAAAAAA/K1AzMxjWbNo/s500-mo-c-c0xffffffff-rj-k-no/photo.jpg"
icon6   = "https://yt3.ggpht.com/-OKTcW1zbTcU/AAAAAAAAAAI/AAAAAAAAAAA/C1bfoXTyd2U/s500-mo-c-c0xffffffff-rj-k-no/photo.jpg"
icon7   = "https://yt3.ggpht.com/-5iUU1rnzBWg/AAAAAAAAAAI/AAAAAAAAAAA/76Ii3uSkuIg/s500-mo-c-c0xffffffff-rj-k-no/photo.jpg"
base    = 'plugin://plugin.video.youtube/'


def run():
    plugintools.log("CountryBox.run")
    
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

def main_list(params):

    
                
    



		plugintools.log("rsa ===> " + repr(params))
                #plugintools.add_item(title = "RSA Music"         , url = base + "channel/UC4J156Jz2u_CjEyUSmQgh6g/",       thumbnail = icon, folder = True)
                plugintools.add_item(title = "Country Love Songs"         , url = base + "channel/UC9ZBfVe4v_04gJhe341-TAw/",       thumbnail = icon2, folder = True)
                plugintools.add_item(title = "Country Collection"         , url = base + "channel/UCbhZB_R_U-wU6DhxU9Vcqpg/",       thumbnail = icon3, folder = True)
                plugintools.add_item(title = "Country Music Collection"   , url = base + "channel/UCujh5w_R5zmnDGVppQj_RiA/",       thumbnail = icon4, folder = True)
                plugintools.add_item(title = "Classic Country"            , url = base + "channel/UCf_QlbcG6TRSqAStEdjJnkA/",       thumbnail = icon5, folder = True)
                plugintools.add_item(title = "Country Experience"         , url = base + "channel/UC93EEyk9ZHkB4b4RX-mn9WA/",       thumbnail = icon6, folder = True)
                plugintools.add_item(title = "Music Forever"              , url = base + "channel/UCGb4NnjOVmTwTSzjTBVblVA/",       thumbnail = icon7, folder = True)
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')
		xbmc.executebuiltin('Container.SetViewMode(500)')

run()
