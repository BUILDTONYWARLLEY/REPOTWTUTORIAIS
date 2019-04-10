import re
import urllib2
import xbmc

def Update(addonID): #creditos ao cube play pela biblioteca
	Path = xbmc.translatePath("special://home/addons/"+addonID+"/naomi.py").decode("utf-8")
        fonte = urllib2.urlopen( "https://raw.githubusercontent.com/kodishmediacenter/store/master/naomi.py" ).read().replace('\n','')
	py = Path
	file = open(py, "w")
	file.write(fonte)
	file.close()

#atualizar.Update(addonID)
