# -*- coding: utf-8 -*-
#------------------------------------------------------------
# 
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import os
import sys
import time
#import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon
from random import randint
import base64
import naomi

addonID = 'plugin.video.desenhos24hrs'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'

tunel = "UmVmZXJlcj1odHRwOi8vd3d3LnJlZGVjYW5haXMuY29tLmJyLw=="
ftunel = base64.b64decode(tunel)

addon_data_dir = os.path.join(xbmc.translatePath("special://userdata/addon_data" ).decode("utf-8"), addonID)

if not os.path.exists(addon_data_dir):
	os.makedirs(addon_data_dir)

m3u =  os.path.join(addon_data_dir, "files.m3u")

file = open(""+m3u+"","w")
file.close




eng2sp = {1:"http://173.249.8.202/home/X-Men%20%5bVolume%2001%5d/X-MEN%20-%2001%20-%20A%20Noite%20Das%20Sentinelas%20Parte%201.avi",
2:"http://173.249.8.202/home/X-Men%20%5bVolume%2001%5d/X-MEN%20-%2002%20-%20A%20Noite%20Das%20Sentinelas%20Parte%202.avi",
3:"http://173.249.8.202/home/X-Men%20%5bVolume%2001%5d/X-MEN%20-%2003%20-%20Surge%20Magneto.avi",
4:"http://173.249.8.202/home/X-Men%20%5bVolume%2001%5d/X-MEN%20-%2004%20-%20Encontros%20Mortais.avi",
5:"http://173.249.8.202/home/X-Men%20%5bVolume%2001%5d/X-MEN%20-%2005%20-%20Paix%c3%a3o%20Secreta.avi",
6:"http://173.249.8.202/home/X-Men%20%5bVolume%2001%5d/X-MEN%20-%2006%20-%20Vingan%c3%a7a%20Gelada.avi",
7:"http://173.249.8.202/home/X-Men%20%5bVolume%2001%5d/X-MEN%20-%2007%20-%20Ilha%20de%20Escravos.avi",
8:"http://173.249.8.202/home/X-Men%20%5bVolume%2001%5d/X-MEN%20-%2008%20-%20O%20Indestrutivel%20Juggernaut.avi",
9:"http://173.249.8.202/home/X-Men%20%5bVolume%2001%5d/X-MEN%20-%2009%20-%20A%20Cura.avi",
10:"http://173.249.8.202/home/X-Men%20%5bVolume%2001%5d/X-MEN%20-%2010%20-%20Vem%20o%20Apocalipse.avi",
11:"http://173.249.8.202/home/X-Men%20%5bVolume%2001%5d/X-MEN%20-%2011%20-%20Dias%20de%20Passado%20e%20Futuro%20Parte%201.avi",
12:"http://173.249.8.202/home/X-Men%20%5bVolume%2001%5d/X-MEN%20-%2012%20-%20Dias%20de%20Passado%20e%20Futuro%20Parte%202.avi",
13:"http://173.249.8.202/home/X-Men%20%5bVolume%2001%5d/X-MEN%20-%2013%20-%20A%20Decis%c3%a3o%20Final.avi",
14:"http://173.249.8.202/home/X-Men%20%5bVolume%2002%5d/X-MEN%20-%2014%20-%20At%c3%a9%20que%20a%20Morte%20nos%20Separe%20Parte%201.avi",
15:"http://173.249.8.202/home/X-Men%20%5bVolume%2002%5d/X-MEN%20-%2015%20-%20At%c3%a9%20que%20a%20Morte%20nos%20Separe%20Parte%202.avi",
16:"http://173.249.8.202/home/X-Men%20%5bVolume%2002%5d/X-MEN%20-%2016%20-%20O%20que%20for%20Preciso.avi",
17:"http://173.249.8.202/home/X-Men%20%5bVolume%2002%5d/X-MEN%20-%2017%20-%20Crepusculo%20Vermelho.avi",
18:"http://173.249.8.202/home/X-Men%20%5bVolume%2002%5d/X-MEN%20-%2018%20-%20O%20Homem%20de%20A%c3%a7o.avi",
19:"http://173.249.8.202/home/X-Men%20%5bVolume%2002%5d/X-MEN%20-%2019%20-%20Eternamente%20Sua.avi",
20:"http://173.249.8.202/home/X-Men%20%5bVolume%2002%5d/X-MEN%20-%2020%20-%20Fugitivos%20do%20Tempo%20Parte%201.avi",
21:"http://173.249.8.202/home/X-Men%20%5bVolume%2002%5d/X-MEN%20-%2021%20-%20Fugitivos%20do%20Tempo%20Parte%202.avi",
22:"http://173.249.8.202/home/X-Men%20%5bVolume%2002%5d/X-MEN%20-%2022%20-%20Uma%20Hist%c3%b3ria%20da%20Vampira.avi",
23:"http://173.249.8.202/home/X-Men%20%5bVolume%2002%5d/X-MEN%20-%2023%20-%20A%20Bela%20e%20a%20Fera.avi",
24:"http://173.249.8.202/home/X-Men%20%5bVolume%2002%5d/X-MEN%20-%2024%20-%20Mojovis%c3%a3o.avi",
25:"http://173.249.8.202/home/X-Men%20%5bVolume%2002%5d/X-MEN%20-%2025%20-%20Reuni%c3%a3o%20Parte%201.avi",
26:"http://173.249.8.202/home/X-Men%20%5bVolume%2002%5d/X-MEN%20-%2026%20-%20Reuni%c3%a3o%20Parte%202.avi",
27:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-MEN%20-%2027%20-%20Retorno%20ao%20Passado%20Parte%201.avi",
28:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-MEN%20-%2028%20-%20Retorno%20ao%20Passado%20Parte%202.avi",
29:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-MEN%20-%2029%20-%20A%20Saga%20de%20Fenix%20Parte%201.avi",
30:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-MEN%20-%2030%20-%20A%20Saga%20de%20Fenix%20Parte%202.avi",
31:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-MEN%20-%2031%20-%20A%20Saga%20de%20Fenix%20Parte%203.avi",
32:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-MEN%20-%2032%20-%20A%20Saga%20de%20Fenix%20Parte%204.avi",
33:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-MEN%20-%2033%20-%20A%20Saga%20de%20Fenix%20Parte%205.avi",
34:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-MEN%20-%2034%20-%20Obesess%c3%a3o.avi",
35:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-MEN%20-%2036%20-%20Terra%20Selvagem,%20Cora%c3%a7%c3%a3o%20Selvagem%20Parte%201.avi",
36:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-MEN%20-%2037%20-%20Terra%20Selvagem,%20Cora%c3%a7%c3%a3o%20Selvagem%20Parte%202.avi",
37:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-MEN%20-%2038%20-%20A%20Saga%20da%20Fenix%20Negra%20Parte%201.avi",
38:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-Men%20-%2035%20-%20Conforto%20Gelado.avi",
39:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-Men%20-%2039%20-%20A%20Saga%20da%20Fenix%20Negra%20Parte%202.avi",
40:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-Men%20-%2040%20-%20A%20Saga%20da%20Fenix%20Negra%20Parte%203.avi",
41:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-Men%20-%2041%20-%20A%20Saga%20da%20Fenix%20Negra%20Parte%204.avi",
42:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-Men%20-%2042%20-%20Orf%c3%a3o%20Nunca%20Mais.avi",
43:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-Men%20-%2043%20-%20O%20Retorno%20De%20Juggernaut.avi",
44:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-Men%20-%2044%20-%20Noturno.avi",
45:"http://173.249.8.202/home/X-Men%20%5bVolume%2003%5d/X-Men%20-%2045%20-%20Arma%20X%20Mentiras%20E%20Videotape.avi",
46:"http://173.249.8.202/home/X-Men%20%5bVolume%2004%5d/X-Men%20-%2046%20-%20Proteus%201.avi",
47:"http://173.249.8.202/home/X-Men%20%5bVolume%2004%5d/X-Men%20-%2047%20-%20Proteus%202.avi",
48:"http://173.249.8.202/home/X-Men%20%5bVolume%2004%5d/X-Men%20-%2048%20-%20O%20Santuario%20Parte%201.avi",
49:"http://173.249.8.202/home/X-Men%20%5bVolume%2004%5d/X-Men%20-%2049%20-%20O%20Santuario%20Parte%202.avi",
50:"http://173.249.8.202/home/X-Men%20%5bVolume%2004%5d/X-Men%20-%2050%20-%20Acima%20Do%20Bem%20E%20Do%20Mal%20Parte%201.avi",
51:"http://173.249.8.202/home/X-Men%20%5bVolume%2004%5d/X-Men%20-%2051%20-%20Acima%20Do%20Bem%20E%20Do%20Mal%20Parte%202.avi",
52:"http://173.249.8.202/home/X-Men%20%5bVolume%2004%5d/X-Men%20-%2052%20-%20Acima%20Do%20Bem%20E%20Do%20Mal%20Parte%203.avi",
53:"http://173.249.8.202/home/X-Men%20%5bVolume%2004%5d/X-Men%20-%2053%20-%20Acima%20Do%20Bem%20E%20Do%20Mal%20Parte%204.avi",
54:"http://173.249.8.202/home/X-Men%20%5bVolume%2004%5d/X-Men%20-%2054%20-%20O%20Valor%20De%20Um%20Homem%20Parte%201.avi",
55:"http://173.249.8.202/home/X-Men%20%5bVolume%2004%5d/X-Men%20-%2055%20-%20O%20Valor%20De%20Um%20Homem%20Parte%202.avi",
56:"http://173.249.8.202/home/X-Men%20%5bVolume%2004%5d/X-Men%20-%2056%20-%20Coragem.avi",
57:"http://173.249.8.202/home/X-Men%20%5bVolume%2004%5d/X-Men%20-%2057%20-%20Passando%20o%20Natal%20Com%20os%20Morlocks.avi",
58:"http://173.249.8.202/home/X-Men%20%5bVolume%2004%5d/X-Men%20-%2058%20-%20A%20Lotus%20e%20o%20A%c3%a7o.avi",
59:"http://173.249.8.202/home/X-Men%20%5bVolume%2004%5d/X-Men%20-%2059%20-%20Amor%20em%20V%c3%a3o.avi",
60:"http://173.249.8.202/home/X-Men%20%5bVolume%2004%5d/X-Men%20-%2060%20-%20Secrets%20no%20Long%20Buried.avi",
61:"http://173.249.8.202/home/X-Men%20%5bVolume%2004%5d/X-Men%20-%2061%20-%20Xavier%20Relembra.avi",
62:"http://173.249.8.202/home/X-Men%20%5bVolume%2004%5d/X-Men%20-%2062%20-%20La%c3%a7os%20De%20Familia.avi",
63:"http://173.249.8.202/home/X-Men%20%5bVolume%2005%5d/X-Men%20-%2063%20-%20A%20Falange%20Parte%201.avi",
64:"http://173.249.8.202/home/X-Men%20%5bVolume%2005%5d/X-Men%20-%2064%20-%20A%20Falange%20Parte%202.avi",
65:"http://173.249.8.202/home/X-Men%20%5bVolume%2005%5d/X-Men%20-%2065%20-%20Trato%20Com%20O%20Diabo.avi",
66:"http://173.249.8.202/home/X-Men%20%5bVolume%2005%5d/X-Men%20-%2066%20-%20Nenhum%20Mutante%20E%20Uma%20Ilha.avi",
67:"http://173.249.8.202/home/X-Men%20%5bVolume%2005%5d/X-Men%20-%2067%20-%20Longshot.avi",
68:"http://173.249.8.202/home/X-Men%20%5bVolume%2005%5d/X-Men%20-%2068%20-%20Exame%20De%20Sangue.avi",
69:"http://173.249.8.202/home/X-Men%20%5bVolume%2005%5d/X-Men%20-%2069%20-%20O%20Temporal%20Parte%201.avi",
70:"http://173.249.8.202/home/X-Men%20%5bVolume%2005%5d/X-Men%20-%2070%20-%20O%20Temporal%20Parte%202.avi",
71:"http://173.249.8.202/home/X-Men%20%5bVolume%2005%5d/X-Men%20-%2071%20-%20O%20Conto%20De%20Fadas%20De%20Jubileu.avi",
72:"http://173.249.8.202/home/X-Men%20%5bVolume%2005%5d/X-Men%20-%2072%20-%20O%20Quinto%20Cavaleiro.avi",
73:"http://173.249.8.202/home/X-Men%20%5bVolume%2005%5d/X-Men%20-%2073%20-%20Velhos%20Soldados.avi",
74:"http://173.249.8.202/home/X-Men%20%5bVolume%2005%5d/X-Men%20-%2074%20-%20A%20Descencia.avi",
75:"http://173.249.8.202/home/X-Men%20%5bVolume%2005%5d/X-Men%20-%2075%20-%20Encontros%20Secretos.avi",
76:"http://173.249.8.202/home/X-Men%20%5bVolume%2005%5d/X-Men%20-%2076%20-%20O%20Dia%20Da%20Formatura.avi",
}

def createserverxm():
        eps = randint(1,76)
        ieps = 35 - eps

        if eps == 76:
                eps = eps - 25

        for j in range(eps,(eps+25)):
                
                file = open(""+m3u+"","a")
                eps = eng2sp[j]
                file.write(eps)
                file.write("\n")
                file.close

                
        xbmc.Player().play(""+m3u+"")

#import atualizar
#atualizar.Update(addonID)


