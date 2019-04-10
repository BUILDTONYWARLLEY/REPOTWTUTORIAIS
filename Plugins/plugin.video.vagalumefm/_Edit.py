import xbmcaddon
import base64
base = 'ohEZBFWNuB1L3Fmcv02bj5ibpJWZ0NXYw9yL6MHc0RHa'
tam = len(base)
basedem = base[::-1]
MainBase = base64.b64decode(basedem)
addon = xbmcaddon.Addon('plugin.video.vagalumefm')
