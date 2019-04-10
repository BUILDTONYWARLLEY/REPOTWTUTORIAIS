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




eng2sp = {1:"Popeye%20-%20EP001%20-%20Os%20Misseis%20by%20TVFlashback.avi",
2:"Popeye%20-%20EP002%20-%20Churrasco%20Para%20Dois%20by%20TVFlashback.avi",
3:"Popeye%20-%20EP003%20-%20Concurso%20de%20Beb&#00234;s%20by%20TVFlashback.avi",
4:"Popeye%20-%20EP004%20-%20Os%20Musculosos%20by%20TVFlashback.avi",
5:"Popeye%20-%20EP005%20-%20Popeye%20no%20Oeste%20by%20TVFlashback.avi",
6:"Popeye%20-%20EP006%20-%20A%20Grande%20Corrida%20by%20TVFlashback.avi",
7:"Popeye%20-%20EP007%20-%20O%20Monstro%20Louco%20by%20TVFlashback.avi",
8:"Popeye%20-%20EP008%20-%20As%20do%20Espa&#00231;o%20by%20TVFlashback.avi",
9:"Popeye%20-%20EP009%20-%20Homem%20das%20Cavernas%20by%20TVFlashback.avi",
10:"Popeye%20-%20EP010%20-%20A%20Tourada%20by%20TVFlashback.avi",
11:"Popeye%20-%20EP011%20-%20O%20Abomin&#00225;vel%20Homem%20das%20Neves%20by%20TVFlashback.avi",
12:"Popeye%20-%20EP012%20-%20Colega%20de%20Pancadaria%20by%20TVFlashback.avi",
13:"Popeye%20-%20EP013%20-%20Os%20Esquiadores%20by%20TVFlashback.avi",
14:"Popeye%20-%20EP014%20-%20Voa%20Voa%20Passarinho%20by%20TVFlashback.avi",
15:"Popeye%20-%20EP015%20-%20O%20Pirata%20Pirado%20by%20TVFlashback.avi",
16:"Popeye%20-%20EP017%20-%20Confus&#00227;o%20do%20Velho%20Oeste%20by%20TVFlashback.avi",
17:"Popeye%20-%20EP018%20-%20Cara%20P&#00225;lida%20de%20Duas%20Caras%20by%20TVFlashback.avi",
18:"Popeye%20-%20EP019%20-%20Confus&#00227;o%20Infantil%20by%20TVFlashback.avi",
19:"Popeye%20-%20EP020%20-%20A%20Bola%20De%20Cristal%20by%20TVFlashback.avi",
20:"Popeye%20-%20EP021%20-%20O%20Atleta%20by%20TVFlashback.avi",
21:"Popeye%20-%20EP022%20-%20Can&#00231;&#00227;o%20de%20Ninar%20Interrompida%20by%20TVFlashback.avi",
22:"Popeye%20-%20EP023%20-%20Loucura%20do%20Espa&#00231;o%20by%20TVFlashback.avi",
23:"Popeye%20-%20EP024%20-%20Perigo%20no%20Mar%20by%20TVFlashback.avi",
24:"Popeye%20-%20EP025%20-%20Dupla%20Vis&#00227;o%20by%20TVFlashback.avi",
25:"Popeye%20-%20EP026%20-%20O%20Grande%20Roubo%20by%20TVFlashback.avi",
26:"Popeye%20-%20EP027%20-%20A%20Cidade%20Perdida%20by%20TVFlashback.avi",
27:"Popeye%20-%20EP028%20-%20A%20Sopa%20Do%20Gugu%20by%20TVFlashback.avi",
28:"Popeye%20-%20EP029%20-%20Astronauta%20Biruta%20by%20TVFlashback.avi",
29:"Popeye%20-%20EP030%20-%20N&#00227;o%20H&#00225;%20Lugar%20Como%20o%20Lar%20by%20TVFlashback.avi",
30:"Popeye%20-%20EP031%20-%20A%20Lo&#00231;&#00227;o%20Poderosa%20by%20TVFlashback.avi",
31:"Popeye%20-%20EP032%20-%20Vamos%20Com%20Calma%20by%20TVFlashback.avi",
32:"Popeye%20-%20EP033%20-%20Querer%20&#00233;%20Poder%20by%20TVFlashback.avi",
33:"Popeye%20-%20EP034%20-%20A%20Escultura%20by%20TVFlashback.avi",
34:"Popeye%20-%20EP035%20-%20As%20Pulgas%20Adestradas%20by%20TVFlashback.avi",
35:"Popeye%20-%20EP036%20-%20A%20Dor%20de%20Cabe&#00231;a%20do%20Popeye%20by%20TVFlashback.avi",
36:"Popeye%20-%20EP037%20-%20Popeye%20do%20Egito%20by%20TVFlashback.avi",
37:"Popeye%20-%20EP038%20-%20O%20&#00218;ltimo%20Recurso%20by%20TVFlashback.avi",
38:"Popeye%20-%20EP039%20-%20O%20Grande%20Espirro%20by%20TVFlashback.avi",
39:"Popeye%20-%20EP040%20-%20O%20Xerife%20by%20TVFlashback.avi",
40:"Popeye%20-%20EP041%20-%20Beb&#00234;%20Trabalhoso%20by%20TVFlashback.avi",
41:"Popeye%20-%20EP042%20-%20E%20O%20Vento%20Levou%20Pra%20Longe%20by%20TVFlashback.avi",
42:"Popeye%20-%20EP043%20-%20Insultando%20o%20Sult&#00227;o%20by%20TVFlashback.avi",
43:"Popeye%20-%20EP044%20-%20O%20Apanhador%20de%20Cachorros%20by%20TVFlashback.avi",
44:"Popeye%20-%20EP045%20-%20Voz%20do%20Al&#00233;m%20by%20TVFlashback.avi",
45:"Popeye%20-%20EP046%20-%20Astro%20de%20Cinema%20by%20TVFlashback.avi",
46:"Popeye%20-%20EP047%20-%20Os%20Castores%20Teimosos%20by%20TVFlashback.avi",
47:"Popeye%20-%20EP048%20-%20O%20Grande%20Jogo%20by%20TVFlashback.avi",
48:"Popeye%20-%20EP050%20-%20Os%20Mergulhadores%20by%20TVFlashback.avi",
49:"Popeye%20-%20EP051%20-%20O%20Posto%20de%20Gasolina%20by%20TVFlashback.avi",
50:"Popeye%20-%20EP052%20-%20A%20Lanchonete%20by%20TVFlashback.avi",
51:"Popeye%20-%20EP053%20-%20Academia%20de%20Corre&#00231;&#00227;o%20Fisica%20by%20TVFlashback.avi",
52:"Popeye%20-%20EP054%20-%20O%20Observador%20de%20Passaros%20by%20TVFlashback.avi",
53:"Popeye%20-%20EP055%20-%20Recuo%20do%20Tempo%20by%20TVFlashback.avi",
54:"Popeye%20-%20EP056%20-%20A%20Loja%20de%20Animais%20do%20Popeye%20by%20TVFlashback.avi",
55:"Popeye%20-%20EP057%20-%20Ballet%20de%20Espinafre%20by%20TVFlashback.avi",
56:"Popeye%20-%20EP058%20-%20Os%20Impostos%20da%20Bruxa%20by%20TVFlashback.avi",
57:"Popeye%20-%20EP059%20-%20Escassez%20de%20Espinafre%20by%20TVFlashback.avi",
58:"Popeye%20-%20EP060%20-%20Popeye%20e%20o%20Drag&#00227;o%20by%20TVFlashback.avi",
59:"Popeye%20-%20EP061%20-%20Popeye,%20O%20Bombeiro%20by%20TVFlashback.avi",
60:"Popeye%20-%20EP062%20-%20A%20Pizzaria%20do%20Popeye%20by%20TVFlashback.avi",
61:"Popeye%20-%20EP063%20-%20A%20Brava%20Familia%20by%20TVFlashback.avi",
62:"Popeye%20-%20EP064%20-%20O%20Faroleiro%20by%20TVFlashback.avi",
63:"Popeye%20-%20EP065%20-%20Popeye%20e%20o%20Fantasma%20by%20TVFlashback.avi",
64:"Popeye%20-%20EP066%20-%20O%20Picnic%20do%20Popeye%20by%20TVFlashback.avi",
65:"Popeye%20-%20EP067%20-%20Fora%20Deste%20Mundo%20by%20TVFlashback.avi",
66:"Popeye%20-%20EP068%20-%20Madame%20Salami%20by%20TVFlashback.avi",
67:"Popeye%20-%20EP069%20-%20Popeye%20Lenhador%20by%20TVFlashback.avi",
68:"Popeye%20-%20EP070%20-%20Trabalhando%20nas%20Alturas%20by%20TVFlashback.avi",
69:"Popeye%20-%20EP071%20-%20Popeye,%20O%20Detetive%20by%20TVFlashback.avi",
70:"Popeye%20-%20EP072%20-%20Olivia%20Chapeuzinho%20Palito%20by%20TVFlashback.avi",
71:"Popeye%20-%20EP073%20-%20Olhar%20Hipn&#00243;tico%20by%20TVFlashback.avi",
72:"Popeye%20-%20EP074%20-%20O%20Cavalo%20de%20Troia%20by%20TVFlashback.avi",
73:"Popeye%20-%20EP075%20-%20Alice,%20O%20Monstro%20by%20TVFlashback.avi",
74:"Popeye%20-%20EP076%20-%20A%20Batalha%20Musical%20by%20TVFlashback.avi",
75:"Popeye%20-%20EP077%20-%20Rumo%20Ao%20Oeste%20by%20TVFlashback.avi",
76:"Popeye%20-%20EP078%20-%20A%20Piscina%20do%20Popeye%20by%20TVFlashback.avi",
77:"Popeye%20-%20EP079%20-%20Jeep%20Jeep%20by%20TVFlashback.avi",
78:"Popeye%20-%20EP080%20-%20A%20Pe&#00231;a%20do%20Museu%20by%20TVFlashback.avi",
79:"Popeye%20-%20EP081%20-%20O%20Jogo%20de%20Golf%20by%20TVFlashback.avi",
80:"Popeye%20-%20EP082%20-%20O%20Restaurante%20do%20Dudu%20by%20TVFlashback.avi",
81:"Popeye%20-%20EP083%20-%20O%20Meteorologista%20by%20TVFlashback.avi",
82:"Popeye%20-%20EP084%20-%20O%20Chapeu%20M&#00225;gico%20by%20TVFlashback.avi",
83:"Popeye%20-%20EP085%20-%20O%20Bandido%20do%20Oeste%20by%20TVFlashback.avi",
84:"Popeye%20-%20EP086%20-%20O%20Ca&#00231;ador%20de%20Baleia%20by%20TVFlashback.avi",
85:"Popeye%20-%20EP087%20-%20Popeye%20e%20o%20P&#00233;%20de%20Espinafre%20by%20TVFlashback.avi",
86:"Popeye%20-%20EP088%20-%20Torneio%20de%20Paraquedismo%20by%20TVFlashback.avi",
87:"Popeye%20-%20EP089%20-%20Tigre%20Burger%20by%20TVFlashback.avi",
88:"Popeye%20-%20EP090%20-%20O%20Pistoleiro%20by%20TVFlashback.avi",
89:"Popeye%20-%20EP091%20-%20Olivia%20de%20Neve%20e%20os%20Sete%20Gugus%20by%20TVFlashback.avi",
90:"Popeye%20-%20EP092%20-%20O%20Farol%20do%20Cabo%20by%20TVFlashback.avi",
91:"Popeye%20-%20EP093%20-%20Nas%20Ru&#00237;nas%20Astecas%20by%20TVFlashback.avi",
92:"Popeye%20-%20EP094%20-%20Sapatinhos%20Verdes%20by%20TVFlashback.avi",
93:"Popeye%20-%20EP095%20-%20O%20Velocino%20de%20Ouro%20by%20TVFlashback.avi",
94:"Popeye%20-%20EP096%20-%20Poupe%20Essa%20Arvore%20by%20TVFlashback.avi",
95:"Popeye%20-%20EP097%20-%20O%20Alegre%20Gladiador%20by%20TVFlashback.avi",
96:"Popeye%20-%20EP098%20-%20O%20Grande%20Mec&#00226;nico%20by%20TVFlashback.avi",
97:"Popeye%20-%20EP099%20-%20O%20Barco%20a%20Vapor%20by%20TVFlashback.avi",
98:"Popeye%20-%20EP100%20-%20Gugu%20Vai%20Cortar%20Os%20Cabelos%20by%20TVFlashback.avi",
99:"Popeye%20-%20EP101%20-%20O%20Carro%20Velho%20do%20Popeye%20by%20TVFlashback.avi",
100:"Popeye%20-%20EP102%20-%20Madame%20Butter%20Palito%20by%20TVFlashback.avi",
101:"Popeye%20-%20EP103%20-%20Popeye%20e%20o%20Drag&#00227;o%20Polido%20by%20TVFlashback.avi",
102:"Popeye%20-%20EP104%20-%20O%20Patinho%20Feio%20by%20TVFlashback.avi",
103:"Popeye%20-%20EP105%20-%20O%20Ch&#00225;%20do%20Popeye%20by%20TVFlashback.avi",
104:"Popeye%20-%20EP106%20-%20O%20Vagabundo%20Que%20Ficou%20Ganancioso%20by%20TVFlashback.avi",
105:"Popeye%20-%20EP107%20-%20O%20Salvavidas%20by%20TVFlashback.avi",
106:"Popeye%20-%20EP108%20-%20Popeye%20na%20Floresta%20by%20TVFlashback.avi",
107:"Popeye%20-%20EP109%20-%20E%20a%20Bola%20Levou%20by%20TVFlashback.avi",
108:"Popeye%20-%20EP110%20-%20Popeye%20e%20o%20Amigo%20Brutus%20by%20TVFlashback.avi",
109:"Popeye%20-%20EP111%20-%20Lavadora%20de%20Carros%20by%20TVFlashback.avi",
110:"Popeye%20-%20EP112%20-%20Aventura%20no%20Deserto%20by%20TVFlashback.avi",
111:"Popeye%20-%20EP113%20-%20Encanador%20by%20TVFlashback.avi",
112:"Popeye%20-%20EP114%20-%20O%20Ladr&#00227;o%20de%20Arenquem%20by%20TVFlashback.avi",
113:"Popeye%20-%20EP115%20-%20Popeye,%20O%20Invisivel%20by%20TVFlashback.avi",
114:"Popeye%20-%20EP116%20-%20O%20Ovo%20Quadrado%20by%20TVFlashback.avi",
115:"Popeye%20-%20EP117%20-%20A%20Lenda%20da%20Ilha%20Monstruosa%20by%20TVFlashback.avi",
116:"Popeye%20-%20EP118%20-%20A%20F&#00225;bula%20do%20Jeep%20by%20TVFlashback.avi",
117:"Popeye%20-%20EP119%20-%20O%20Supermercado%20by%20TVFlashback.avi",
118:"Popeye%20-%20EP120%20-%20Empregado%20de%20Escritorio%20by%20TVFlashback.avi",
119:"Popeye%20-%20EP121%20-%20O%20Toque%20Especial%20by%20TVFlashback.avi",
120:"Popeye%20-%20EP122%20-%20Gugu%20Atrav&#00233;s%20do%20Espelho%20by%20TVFlashback.avi",
121:"Popeye%20-%20EP123%20-%20O%20Cavaleiro%20Negro%20by%20TVFlashback.avi",
122:"Popeye%20-%20EP124%20-%20Ca&#00231;ada%20na%20Selva%20by%20TVFlashback.avi",
123:"Popeye%20-%20EP125%20-%20A%20Grande%20Ca&#00231;a%20Ao%20Drag&#00227;o%20by%20TVFlashback.avi",
124:"Popeye%20-%20EP126%20-%20Rip%20Van%20Popeye%20by%20TVFlashback.avi",
125:"Popeye%20-%20EP127%20-%20Aventura%20No%20Mississipi%20by%20TVFlashback.avi",
126:"Popeye%20-%20EP128%20-%20A%20Grande%20Corrida%20by%20TVFlashback.avi",
127:"Popeye%20-%20EP129%20-%20Olivia,%20A%20Modelo%20by%20TVFlashback.avi",
128:"Popeye%20-%20EP130%20-%20Amnesia%20by%20TVFlashback.avi",
129:"Popeye%20-%20EP131%20-%20O%20Papel%20de%20Parede%20by%20TVFlashback.avi",
130:"Popeye%20-%20EP132%20-%20Popeye,%20O%20Treinador%20by%20TVFlashback.avi",
131:"Popeye%20-%20EP133%20-%20Popeye%20Revere%20by%20TVFlashback.avi",
132:"Popeye%20-%20EP134%20-%20Popeye%20no%20Hawaii%20by%20TVFlashback.avi",
133:"Popeye%20-%20EP135%20-%20Para%20Sempre%20Ambergris%20by%20TVFlashback.avi",
134:"Popeye%20-%20EP136%20-%20Popeye%20De%20Leon%20by%20TVFlashback.avi",
135:"Popeye%20-%20EP137%20-%20Popeye,%20O%20Pescador%20by%20TVFlashback.avi",
136:"Popeye%20-%20EP138%20-%20A%20Corrida%20com%20Barreiras%20by%20TVFlashback.avi",
137:"Popeye%20-%20EP139%20-%20A%20Guerra%20Nada%20Civil%20by%20TVFlashback.avi",
138:"Popeye%20-%20EP140%20-%20O%20Transportador%20de%20Piano%20by%20TVFlashback.avi",
139:"Popeye%20-%20EP141%20-%20O%20Jantar%20by%20TVFlashback.avi",
140:"Popeye%20-%20EP142%20-%20A%20Volta%20ao%20Mundo%20de%20Oitenta%20Maneiras%20by%20TVFlashback.avi",
141:"Popeye%20-%20EP143%20-%20Oficina%20de%20Consertos%20by%20TVFlashback.avi",
142:"Popeye%20-%20EP144%20-%20O%20Boy%20do%20Hotel%20by%20TVFlashback.avi",
143:"Popeye%20-%20EP145%20-%20O%20Fantasma%20by%20TVFlashback.avi",
144:"Popeye%20-%20EP146%20-%20Boliche%20e%20Espinafre%20by%20TVFlashback.avi",
145:"Popeye%20-%20EP147%20-%20O%20Jeep%20Sapeca%20by%20TVFlashback.avi",
146:"Popeye%20-%20EP148%20-%20O%20Entendido%20Em%20Espinafre%20by%20TVFlashback.avi",
147:"Popeye%20-%20EP149%20-%20Um%20Caso%20de%20Cuca%20by%20TVFlashback.avi",
148:"Popeye%20-%20EP150%20-%20Pobre%20Rico%20Pobre%20by%20TVFlashback.avi",
149:"Popeye%20-%20EP151%20-%20O%20Pai%20do%20Gugu%20by%20TVFlashback.avi",
150:"Popeye%20-%20EP152%20-%20Popeye%20Contra%20o%20Gigante%20by%20TVFlashback.avi",
151:"Popeye%20-%20EP153%20-%20O%20Vale%20dos%20Monstros%20by%20TVFlashback.avi",
152:"Popeye%20-%20EP154%20-%20A%20Busca%20do%20Vov&#00244;%20Popeye%20by%20TVFlashback.avi",
153:"Popeye%20-%20EP157%20-%20S&#00243;%20D&#00243;i%20Quando%20Eles%20Riem%20by%20TVFlashback.avi",
154:"Popeye%20-%20EP158%20-%20Dudu,%20O%20Folgado%20by%20TVFlashback.avi",
155:"Popeye%20-%20EP159%20-%20Magias%20e%20Truques%20by%20TVFlashback.avi",
156:"Popeye%20-%20EP160%20-%20A%20Liquida&#00231;&#00227;o%20by%20TVFlashback.avi",
157:"Popeye%20-%20EP161%20-%20A%20Viagem%20do%20Popeye%20by%20TVFlashback.avi",
158:"Popeye%20-%20EP162%20-%20Cachorro%20Pega%20Popeye%20by%20TVFlashback.avi",
159:"Popeye%20-%20EP163%20-%20O%20Que%20H&#00225;%20de%20Novo%20by%20TVFlashback.avi",
160:"Popeye%20-%20EP164%20-%20&#00201;%20Natal%20by%20TVFlashback.avi",
161:"Popeye%20-%20EP165%20-%20Tudo%20Bem%20Quando%20Termina%20Bem%20by%20TVFlashback.avi",
162:"Popeye%20-%20EP166%20-%20Problema%20no%20Motor%20by%20TVFlashback.avi",
163:"Popeye%20-%20EP167%20-%20O%20Parque%20de%20Divers&#00245;es%20by%20TVFlashback.avi",
164:"Popeye%20-%20EP168%20-%20O%20Duelo%20Fatal%20by%20TVFlashback.avi",
165:"Popeye%20-%20EP169%20-%20O%20Roubo%20da%20Esmeralda%20by%20TVFlashback.avi",
166:"Popeye%20-%20EP170%20-%20A%20Disputa%20das%20Feras%20by%20TVFlashback.avi",
167:"Popeye%20-%20EP171%20-%20O%20Parador%20de%20Chuva%20by%20TVFlashback.avi",
168:"Popeye%20-%20EP172%20-%20Confus&#00227;o%20no%20Mississipi%20by%20TVFlashback.avi",
169:"Popeye%20-%20EP174%20-%20A%20Serpente%20do%20Mar%20by%20TVFlashback.avi",
170:"Popeye%20-%20EP175%20-%20A%20L&#00226;mpada%20de%20Aladim%20by%20TVFlashback.avi",
171:"Popeye%20-%20EP176%20-%20O%20Leprechaun%20by%20TVFlashback.avi",
172:"Popeye%20-%20EP177%20-%20Parque%20de%20Divers&#00245;es%20by%20TVFlashback.avi",
173:"Popeye%20-%20EP178%20-%20Pescaria%20de%20Hamburguer%20by%20TVFlashback.avi",
174:"Popeye%20-%20EP179%20-%20Melodia%20Misteriosa%20by%20TVFlashback.avi",
175:"Popeye%20-%20EP180%20-%20Gato%20Assustado%20by%20TVFlashback.avi",
176:"Popeye%20-%20EP181%20-%20Aventura%20No%20Gelo%20by%20TVFlashback.avi",
177:"Popeye%20-%20EP182%20-%20A%20Cura%20by%20TVFlashback.avi",
178:"Popeye%20-%20EP183%20-%20Guilherme%20Popeye%20Tell%20by%20TVFlashback.avi",
179:"Popeye%20-%20EP184%20-%20O%20Apito%20Desaparecido%20by%20TVFlashback.avi",
180:"Popeye%20-%20EP185%20-%20O%20Autografo%20by%20TVFlashback.avi",
181:"Popeye%20-%20EP186%20-%20Uma%20Perola%20Para%20Olivia%20by%20TVFlashback.avi",
182:"Popeye%20-%20EP187%20-%20A%20Minha%20Linda%20Olivia%20by%20TVFlashback.avi",
183:"Popeye%20-%20EP188%20-%20O%20Tunel%20do%20Amor%20by%20TVFlashback.avi",
184:"Popeye%20-%20EP189%20-%20Coisas%20Estranhas%20Est&#00227;o%20Acontecendo%20by%20TVFlashback.avi",
185:"Popeye%20-%20EP190%20-%20O%20Vendedor%20de%20Remedios%20by%20TVFlashback.avi",
186:"Popeye%20-%20EP191%20-%20Em%20Busca%20do%20Mapa%20by%20TVFlashback.avi",
187:"Popeye%20-%20EP192%20-%20Confus&#00245;es%20no%20Zoo%20by%20TVFlashback.avi",
188:"Popeye%20-%20EP193%20-%20O%20Rob&#00244;%20Popeye%20by%20TVFlashback.avi",
189:"Popeye%20-%20EP194%20-%20A%20Vingan&#00231;a%20do%20P&#00225;ssaro%20M&#00225;gico%20by%20TVFlashback.avi",
190:"Popeye%20-%20EP195%20-%20O%20Bisbilhoteiro%20by%20TVFlashback.avi",
191:"Popeye%20-%20EP196%20-%20O%20Anel%20M&#00225;gico%20by%20TVFlashback.avi",
192:"Popeye%20-%20EP197%20-%20Popeye%20Polegar%20by%20TVFlashback.avi",
193:"Popeye%20-%20EP198%20-%20Sumindo,%20Sumindo,%20Sumiu%20by%20TVFlashback.avi",
194:"Popeye%20-%20EP199%20-%20O%20Bilion&#00225;rio%20by%20TVFlashback.avi",
195:"Popeye%20-%20EP200%20-%20Os%20Detetives%20Disfar&#00231;ados%20by%20TVFlashback.avi",
196:"Popeye%20-%20EP201%20-%20O%20Escultor%20by%20TVFlashback.avi",
197:"Popeye%20-%20EP202%20-%20Quem%20&#00233;%20Quem%20by%20TVFlashback.avi",
198:"Popeye%20-%20EP203%20-%20Interludio%20Intelectua%20by%20TVFlashback.avi",
199:"Popeye%20-%20EP204%20-%20O%20Carro%20Esporte%20by%20TVFlashback.avi",
200:"Popeye%20-%20EP205%20-%20Viajando%20Tempo%20a%20Fora%20by%20TVFlashback.avi",
201:"Popeye%20-%20EP206%20-%20C&#00227;o%20Falante%20by%20TVFlashback.avi",
202:"Popeye%20-%20EP207%20-%20O%20Disco%20Voador%20by%20TVFlashback.avi",
203:"Popeye%20-%20EP208%20-%20A%20Dieta%20da%20Olivia%20by%20TVFlashback.avi",
204:"Popeye%20-%20EP209%20-%20A%20Marca%20do%20Zero%20by%20TVFlashback.avi",
205:"Popeye%20-%20EP210%20-%20Roger%20by%20TVFlashback.avi",
206:"Popeye%20-%20EP211%20-%20Os%20Primeiros%20Dentes%20do%20Gugu%20by%20TVFlashback.avi",
207:"Popeye%20-%20EP212%20-%20O%20Incidente%20com%20a%20Cidade%20dos%20Misseis%20by%20TVFlashback.avi",
208:"Popeye%20-%20EP213%20-%20Popeye%20e%20o%20Gigante%20by%20TVFlashback.avi",
209:"Popeye%20-%20EP214%20-%20Na%20Briga%20dos%20Caipiras%20by%20TVFlashback.avi",
210:"Popeye%20-%20EP215%20-%20Comprando%20Encrenca%20by%20TVFlashback.avi",
211:"Popeye%20-%20EP216%20-%20O%20Mordomo%20by%20TVFlashback.avi",
212:"Popeye%20-%20EP217%20-%20Kiddie%20Kapers%20by%20TVFlashback.avi",
213:"Popeye%20-%20EP218%20-%20Os%20Problemas%20do%20Popeye%20by%20TVFlashback.avi",
214:"Popeye%20-%20EP219%20-%20Popeye%20Colombo%20by%20TVFlashback.avi",
215:"Popeye%20-%20EP220%20-%20O%20Carregamento%20de%20Hamburguers%20by%20TVFlashback.avi",}

def createserverpy():
        eps = randint(1,173)
        ieps = 35 - eps

        if eps == 173:
                eps = eps - 25

        for j in range(eps,(eps+45)):
                
                file = open(""+m3u+"","a")
                eps = eng2sp[j]
                file.write("http://173.249.8.202/home/Popeye%2075th%20Anniversary/"+eps)
                file.write("\n")
                file.close

                
        xbmc.Player().play(""+m3u+"")

#import atualizar
#atualizar.Update(addonID)


