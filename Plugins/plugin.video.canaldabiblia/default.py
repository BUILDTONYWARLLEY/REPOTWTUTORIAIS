# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/OMundo2osBrasileiros
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools

from addon.common.addon import Addon

addonID = 'plugin.video.canaldabiblia'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'


def run():
    plugintools.log("caillou.run")
    
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

def main_list(params):

    
                icon1 = "https://i.ytimg.com/vi/zg0mwOrt_9M/maxresdefault.jpg"
                icon2 = "https://i.ytimg.com/vi/lfLQuI5a42g/maxresdefault.jpg"
                icon3 = "https://i.ytimg.com/vi/YImAWKrCGNM/maxresdefault.jpg"
                icon4 = "https://i.ytimg.com/vi/wbkJTMdvAWE/maxresdefault.jpg"
                icon5 = "https://i.ytimg.com/vi/dAImBovTiug/maxresdefault.jpg"
                icon6 = "https://i.ytimg.com/vi/T91rQrUfxHw/maxresdefault.jpg"
                icon7 = "https://i.ytimg.com/vi/Z8MAj-2j7Pc/maxresdefault.jpg"
                icon8 = "https://i.ytimg.com/vi/E1BjAqc_rbA/maxresdefault.jpg"
                icon9 = "https://i.ytimg.com/vi/-Y2f0Q1w2H8/maxresdefault.jpg"
                icon10 = "https://i.ytimg.com/vi/xQTQN9Abgk8/maxresdefault.jpg"
                icon11 = "https://i.ytimg.com/vi/BaMDoO1nNOY/maxresdefault.jpg"
                icon12 = "https://i.ytimg.com/vi/-cIGLBspftY/maxresdefault.jpg"
                icon13 = "https://i.ytimg.com/vi/XVN27IyrnQo/maxresdefault.jpg"
                icon14 = "https://i.ytimg.com/vi/DHzK5R0jl_o/maxresdefault.jpg"

                icon15 = "https://i.ytimg.com/vi/0HdrPFtiJNc/maxresdefault.jpg"
                icon16 = "https://i.ytimg.com/vi/4aaEW4q1pig/maxresdefault.jpg"
                icon17 = "https://i.ytimg.com/vi/tgyfer6yfZA/maxresdefault.jpg"
                icon18 = "https://i.ytimg.com/vi/CD2MQ07xhIc/maxresdefault.jpg"
                icon19 = "https://i.ytimg.com/vi/HS7EMIMVqFI/maxresdefault.jpg"
                icon20 = "https://i.ytimg.com/vi/4YPg3rlskvw/maxresdefault.jpg"
                icon21 = "https://i.ytimg.com/vi/7cLyj78Z9fI/maxresdefault.jpg"
                icon22 = "https://i.ytimg.com/vi/GbPlfHyHtVQ/maxresdefault.jpg"
                icon22 = "https://i.ytimg.com/vi/QMYVBxAfe_4/maxresdefault.jpg"
                icon23 = "https://i.ytimg.com/vi/0QIGmgcjIew/maxresdefault.jpg"
                icon24 = "https://i.ytimg.com/vi/BXFT3AOaW8U/maxresdefault.jpg"
                icon25 = "https://i.ytimg.com/vi/cnkeTzGxneE/maxresdefault.jpg"
                icon26 = "https://i.ytimg.com/vi/krUThhTohdQ/maxresdefault.jpg"
                icon27 = "https://i.ytimg.com/vi/AIKlfioJx6Y/maxresdefault.jpg"
                iconx1 = "https://i.ytimg.com/vi/GbPlfHyHtVQ/maxresdefault.jpg"
               

                



                

                


		plugintools.log("canaldabiblia ===> " + repr(params))
                plugintools.add_item(title = "Genesis"         , url = base + "playlist/PLQM1wN-kTLE6LVZQFnJt8H3FXGxftWPV4",       thumbnail = icon1, folder = True)
                plugintools.add_item(title = "Exodus"         , url = base + "playlist/PLQM1wN-kTLE4ySj1BbWbwA14JAjm1UpWS",       thumbnail = icon2, folder = True)
                plugintools.add_item(title = "Levitico"         , url = base + "playlist/PLQM1wN-kTLE7TN8daRS4gPGZEnslN5n1T/",       thumbnail = icon3, folder = True)
                plugintools.add_item(title = "Numeros"         , url = base + "playlist/PLQM1wN-kTLE77NeerOaDsS_N5VmfZkoDF/",       thumbnail = icon4, folder = True)
                plugintools.add_item(title = "Deuteronomio"         , url = base + "playlist/PLQM1wN-kTLE7FVZEA1TN87SQ-27oSFbb8/",       thumbnail = icon5, folder = True)
                plugintools.add_item(title = "Josue"         , url = base + "playlist/PLQM1wN-kTLE55kCcTFd2m8x0mEkFW2vMm/",       thumbnail = icon6, folder = True)
                plugintools.add_item(title = "Juizes"         , url = base + "playlist/PLQM1wN-kTLE6t-lRxic3t7p86zz5HC8sO/",       thumbnail = icon7, folder = True)
                plugintools.add_item(title = "Rute"         , url = base + "playlist/PLQM1wN-kTLE7Sz2eL5d3l0YO2FB0CPQFi/",       thumbnail = icon8, folder = True)
                plugintools.add_item(title = "I Samuel"         , url = base + "playlist/PLQM1wN-kTLE5fn_S-pAX7SHxy2OE9EyIb/",       thumbnail = icon9, folder = True)
                plugintools.add_item(title = "II Samuel"         , url = base + "playlist/PLQM1wN-kTLE6PRS_UqZYqKDI3qzNrrdOU/",       thumbnail = icon10, folder = True)

                plugintools.add_item(title = "I Reis"         , url = base + "playlist/PLQM1wN-kTLE6FjSAjyOiylm1am0HeIRZo/",       thumbnail = icon11, folder = True)
                plugintools.add_item(title = "II Reis"         , url = base + "playlist/PLQM1wN-kTLE4mRov22XiioQ91ZSmSThVF/",       thumbnail = icon12, folder = True)
                plugintools.add_item(title = "I Cronicas"         , url = base + "playlist/PLQM1wN-kTLE6V_FT0YSRHpOabPWS8O52f/",       thumbnail = icon13, folder = True)
                plugintools.add_item(title = "II Cronicas"         , url = base + "playlist/PLQM1wN-kTLE7WB6A0mkFFyQR8HOwbz0Ia/",       thumbnail = icon14, folder = True)
                plugintools.add_item(title = "Esdras" ,       url = base + "playlist/PLQM1wN-kTLE4Ys8DD6PYXc-m4uqQjfIM8/",       thumbnail = icon15, folder = True)
                plugintools.add_item(title = "Neemias" ,       url = base + "playlist/PLQM1wN-kTLE785L3ewU7jBk804ODqQTss/",       thumbnail = icon16, folder = True)
                plugintools.add_item(title = "Ester " ,       url = base + "playlist/PLQM1wN-kTLE6SEfBYMg0vywW2nMV3OQ13/",       thumbnail = icon17, folder = True)
                plugintools.add_item(title = "Jó " ,       url = base + "playlist/PLQM1wN-kTLE6NQFPSiNsoVHpb6pmKuQwg/",       thumbnail = icon18, folder = True)
                plugintools.add_item(title = "Salmos" ,       url = base + "playlist/PLQM1wN-kTLE4TcJ8KjxalITeg5dfaU-HM/",       thumbnail = icon19, folder = True)
                plugintools.add_item(title = "Proverbios" ,       url = base + "playlist/PLQM1wN-kTLE7HY1lJZc46yrZNxoxMOR6S/",       thumbnail = icon20, folder = True)
                plugintools.add_item(title = "Eclesiates" ,       url = base + "playlist/PLQM1wN-kTLE5nqAXFCaXuNWF1EwqPQHoZ/",       thumbnail = icon21, folder = True)
                plugintools.add_item(title = "Canticos dos Canticos" ,       url = base + "playlist/PLQM1wN-kTLE5m1z34aWlYMYsV-3CAacRO/",       thumbnail = iconx1, folder = True)
		plugintools.add_item(title = "Isaias" ,       url = base + "playlist/PLQM1wN-kTLE6PDWO1V8rHtv9Ig3EgcBSb/",       thumbnail = icon22, folder = True)
                plugintools.add_item(title = "Jeremias" ,       url = base + "playlist/PLQM1wN-kTLE4GTVQ_Gx4wNLoZ2fcyW9ig/",       thumbnail = icon23, folder = True)
                plugintools.add_item(title = "Lamentações" ,       url = base + "playlist/PLQM1wN-kTLE6qFtUt9eQVPqB2WdsBkLjM/",       thumbnail = icon24, folder = True)
                plugintools.add_item(title = "Ezequiel" ,       url = base + "playlist/PLQM1wN-kTLE5vNkFPy5nTyFgOhh3zrOWV/",       thumbnail = icon25, folder = True)
                plugintools.add_item(title = "Daniel" ,       url = base + "playlist/PLQM1wN-kTLE5OHpOZ5MHNV9geiqE6aHq/",       thumbnail = icon26, folder = True)
                plugintools.add_item(title = "Oseias" ,       url = base + "playlist/PLQM1wN-kTLE75cWwxc_6gfL50VprIf_o2/",       thumbnail = icon27, folder = True)
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')
		xbmc.executebuiltin('Container.SetViewMode(500)')

run()
