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




eng2sp = {1:"http://173.249.8.202/home/dpicapau/000%20Pica%20Pau%20-%20Ataca%20Novamente.avi",
2:"http://173.249.8.202/home/dpicapau/001%20Pica%20Pau%20-%20Biruta.avi",
3:"http://173.249.8.202/home/dpicapau/002%20Pica%20Pau%20-%20O%20Rachador.avi",
4:"http://173.249.8.202/home/dpicapau/003%20Pica%20Pau%20-%20PÃ¢nico%20na%20Cozinha.avi",
5:"http://173.249.8.202/home/dpicapau/004%20Pica%20Pau%20-%20O%20Matador%20De%20Hollywood.avi",
6:"http://173.249.8.202/home/dpicapau/005%20Pica%20Pau%20-%20Um%20As%20Demais.avi",
7:"http://173.249.8.202/home/dpicapau/006%20Pica%20Pau%20-%20A%20Loja%20Do%20Prego.avi",
8:"http://173.249.8.202/home/dpicapau/007%20Pica%20Pau%20-%20Baseball%20Maluco.avi",
9:"http://173.249.8.202/home/dpicapau/008%20Pica%20Pau%20-%20O%20Acrobata%20Maluco.avi",
10:"http://173.249.8.202/home/dpicapau/009%20Pica%20Pau%20-%20O%20Afanador%20De%20Gasolina.avi",
11:"http://173.249.8.202/home/dpicapau/010%20Pica%20Pau%20-%20O%20Barbeiro%20de%20Sevilha.avi",
12:"http://173.249.8.202/home/dpicapau/011%20Pica%20Pau%20-%20O%20Doido%20da%20Praia.avi",
13:"http://173.249.8.202/home/dpicapau/012%20Pica%20Pau%20-%20Ski%20Para%20Dois.avi",
14:"http://173.249.8.202/home/dpicapau/013%20Pica%20Pau%20-%20Uma%20Dama%20Muito%20Fina.avi",
15:"http://173.249.8.202/home/dpicapau/014%20Pica%20Pau%20-%20O%20Pica%20Pau%20Come%20Fora.avi",
16:"http://173.249.8.202/home/dpicapau/015%20Pica%20Pau%20-%20O%20Famoso%20Diplomata.avi",
17:"http://173.249.8.202/home/dpicapau/016%20Pica%20Pau%20-%20O%20Biruta%20A%20Solta.avi",
18:"http://173.249.8.202/home/dpicapau/017%20Pica%20Pau%20-%20Quem%20Cozinha%20Quem.avi",
19:"http://173.249.8.202/home/dpicapau/018%20Pica%20Pau%20-%20Hora%20Do%20Banho.avi",
20:"http://173.249.8.202/home/dpicapau/019%20Pica%20Pau%20-%20Carteira%20de%20Motorista.avi",
21:"http://173.249.8.202/home/dpicapau/020%20Pica%20Pau%20-%20Amigos%20Penosos.avi",
22:"http://173.249.8.202/home/dpicapau/021%20Pica%20Pau%20-%20Miniaturas%20Musicais.avi",
23:"http://173.249.8.202/home/dpicapau/022%20Pica%20Pau%20-%20Presuntos%20Defumados.avi",
24:"http://173.249.8.202/home/dpicapau/023%20Pica%20Pau%20-%20O%20Passarinho%20do%20RelÃ³gio.avi",
25:"http://173.249.8.202/home/dpicapau/024%20Pica%20Pau%20-%20Roubando%20Gasolina.avi",
26:"http://173.249.8.202/home/dpicapau/025%20Pica%20Pau%20-%20O%20Ovo%20da%20Galinha.avi",
27:"http://173.249.8.202/home/dpicapau/026%20Pica%20Pau%20-%20Mata%20Gigantes.avi",
28:"http://173.249.8.202/home/dpicapau/027%20Pica%20Pau%20-%20A%20Cartola.avi",
29:"http://173.249.8.202/home/dpicapau/028%20Pica%20Pau%20-%20O%20Fila%20BÃ³ia.avi",
30:"http://173.249.8.202/home/dpicapau/029%20Pica%20Pau%20-%20Hora%20do%20Bebe.avi",
31:"http://173.249.8.202/home/dpicapau/030%20Pica%20Pau%20-%20ApÃ³lice%20Cobertor.avi",
32:"http://173.249.8.202/home/dpicapau/031%20Pica%20Pau%20-%20O%20Xerife.avi",
33:"http://173.249.8.202/home/dpicapau/032%20Pica%20Pau%20-%20DelÃ­cia%20Gelada.avi",
34:"http://173.249.8.202/home/dpicapau/033%20Pica%20Pau%20-%20O%20Mensageiro.avi",
35:"http://173.249.8.202/home/dpicapau/034%20Pica%20Pau%20-%20Durma%20Bem.avi",
36:"http://173.249.8.202/home/dpicapau/035%20Pica%20Pau%20-%20Cricket%20Maluco.avi",
37:"http://173.249.8.202/home/dpicapau/036%20Pica%20Pau%20-%20CampeÃ£o%20do%20Estilingue.avi",
38:"http://173.249.8.202/home/dpicapau/037%20Pica%20Pau%20-%20Os%20Trabalhadores%20Da%20Floresta.avi",
39:"http://173.249.8.202/home/dpicapau/038%20Pica%20Pau%20-%20A%20Polka%20do%20Pica%20Pau.avi",
40:"http://173.249.8.202/home/dpicapau/039%20Pica%20Pau%20-%20Uma%20Aventura%20no%20Supermercado.avi",
41:"http://173.249.8.202/home/dpicapau/040%20Pica%20Pau%20-%20Nascido%20Para%20Picar.avi",
42:"http://173.249.8.202/home/dpicapau/041%20Pica%20Pau%20-%20O%20Grande%20Logro.avi",
43:"http://173.249.8.202/home/dpicapau/042%20Pica%20Pau%20-%20CampeÃ£o%20de%20Golf.avi",
44:"http://173.249.8.202/home/dpicapau/043%20Pica%20Pau%20-%20O%20Cabeleireiro.avi",
45:"http://173.249.8.202/home/dpicapau/044%20Pica%20Pau%20-%20O%20Grande%20Quem%20Faz%20Isso.avi",
46:"http://173.249.8.202/home/dpicapau/045%20Pica%20Pau%20-%20Formigas%20de%20Marte.avi",
47:"http://173.249.8.202/home/dpicapau/046%20Pica%20Pau%20-%20O%20Varre%20Varre.avi",
48:"http://173.249.8.202/home/dpicapau/047%20Pica%20Pau%20-%20O%20Pirata.avi",
49:"http://173.249.8.202/home/dpicapau/048%20Pica%20Pau%20-%20OperaÃ§Ã£o%20Cerragem.avi",
50:"http://173.249.8.202/home/dpicapau/049%20Pica%20Pau%20-%20O%20Vale%20Tudo.avi",
51:"http://173.249.8.202/home/dpicapau/050%20Pica%20Pau%20-%20Os%20Mensageiros.avi",
52:"http://173.249.8.202/home/dpicapau/051%20Pica%20Pau%20-%20O%20Hipnotizador%20Caipira.avi",
53:"http://173.249.8.202/home/dpicapau/052%20Pica%20Pau%20-%20Meio%20Dia%20Quente.avi",
54:"http://173.249.8.202/home/dpicapau/053%20Pica%20Pau%20-%20Briga%20Em%20Marrocos.avi",
55:"http://173.249.8.202/home/dpicapau/054%20Pica%20Pau%20-%20A%20Alameda%20Para%20Bali.avi",
56:"http://173.249.8.202/home/dpicapau/055%20Pica%20Pau%20-%20O%20EspiÃ£o%20Espiado.avi",
57:"http://173.249.8.202/home/dpicapau/056%20Pica%20Pau%20-%20O%20Vendedor%20De%20CarrÃµes.avi",
58:"http://173.249.8.202/home/dpicapau/057%20Pica%20Pau%20-%20O%20Trio%20Amoroso.avi",
59:"http://173.249.8.202/home/dpicapau/058%20Pica%20Pau%20-%20Pesadelo%20Dourado.avi",
60:"http://173.249.8.202/home/dpicapau/059%20Pica%20Pau%20-%20Concerto%20Na%20Marra.avi",
61:"http://173.249.8.202/home/dpicapau/060%20Pica%20Pau%20-%20Os%20Desabrigados.avi",
62:"http://173.249.8.202/home/dpicapau/061%20Pica%20Pau%20-%20A%20Vassoura%20da%20Bruxa.avi",
63:"http://173.249.8.202/home/dpicapau/062%20Pica%20Pau%20-%20Farejador%20vs%20Pica%20Pau.avi",
64:"http://173.249.8.202/home/dpicapau/063%20Pica%20Pau%20-%20Pica%20Pau%20Ama%20Seca.avi",
65:"http://173.249.8.202/home/dpicapau/064%20Pica%20Pau%20-%20LadrÃ£o%20Que%20Rouba%20LadrÃ£o.avi",
66:"http://173.249.8.202/home/dpicapau/065%20Pica%20Pau%20-%20Um%20Tesouro%20DifÃ­cil.avi",
67:"http://173.249.8.202/home/dpicapau/066%20Pica%20Pau%20-%20MÃ©dico%20de%20Ãrvore.avi",
68:"http://173.249.8.202/home/dpicapau/067%20Pica%20Pau%20-%20Depois%20da%20Bola.avi",
69:"http://173.249.8.202/home/dpicapau/068%20Pica%20Pau%20-%20Os%20Perdidinhos.avi",
70:"http://173.249.8.202/home/dpicapau/069%20Pica%20Pau%20-%20Chefe%20Charlie%20Cavalo.avi",
71:"http://173.249.8.202/home/dpicapau/070%20Pica%20Pau%20-%20Um%20Pica%20Pau%20de%20Marte.avi",
72:"http://173.249.8.202/home/dpicapau/071%20Pica%20Pau%20-%20Festival%20de%20Cuckoos.avi",
73:"http://173.249.8.202/home/dpicapau/072%20Pica%20Pau%20-%20Vamos%20Ã€s%20Cataratas.avi",
74:"http://173.249.8.202/home/dpicapau/073%20Pica%20Pau%20-%20Artes%20e%20Flores.avi",
75:"http://173.249.8.202/home/dpicapau/074%20Pica%20Pau%20-%20Davy%20Escovinha%20enfrenta%20Pica%20Pau.avi",
76:"http://173.249.8.202/home/dpicapau/075%20Pica%20Pau%20-%20Chapeuzinho%20Diferente.avi",
77:"http://173.249.8.202/home/dpicapau/076%20Pica%20Pau%20-%20O%20Bandido%20do%20Trem.avi",
78:"http://173.249.8.202/home/dpicapau/077%20Pica%20Pau%20-%20O%20Vendedor%20InsuportÃ¡vel.avi",
79:"http://173.249.8.202/home/dpicapau/078%20Pica%20Pau%20-%20Pica%20Pau%20Internacional.avi",
80:"http://173.249.8.202/home/dpicapau/079%20Pica%20Pau%20-%20CaÃ§a%20Ao%20Pica%20Pau.avi",
81:"http://173.249.8.202/home/dpicapau/080%20Pica%20Pau%20-%20Viagem%20Ã%20%20Marte.avi",
82:"http://173.249.8.202/home/dpicapau/081%20Pica%20Pau%20-%20Dopey%20Dick.avi",
83:"http://173.249.8.202/home/dpicapau/082%20Pica%20Pau%20-%20Papai%20Urso.avi",
84:"http://173.249.8.202/home/dpicapau/083%20Pica%20Pau%20-%20Um%20Seguro%20Furado.avi",
85:"http://173.249.8.202/home/dpicapau/084%20Pica%20Pau%20-%20Ornitolomania.avi",
86:"http://173.249.8.202/home/dpicapau/085%20Pica%20Pau%20-%20Selins%20Vazios.avi",
87:"http://173.249.8.202/home/dpicapau/086%20Pica%20Pau%20-%20Seu%20Melhor%20Duende.avi",
88:"http://173.249.8.202/home/dpicapau/087%20Pica%20Pau%20-%20Investimento%20NÃ£o%20TÃ£o%20Seguro.avi",
89:"http://173.249.8.202/home/dpicapau/088%20Pica%20Pau%20-%20Era%20Uma%20Vez%20Um%20Parque.avi",
90:"http://173.249.8.202/home/dpicapau/089%20Pica%20Pau%20-%20Um%20Bobo%20e%20Tanto.avi",
91:"http://173.249.8.202/home/dpicapau/090%20Pica%20Pau%20-%20Luta%20do%20Gatoso.avi",
92:"http://173.249.8.202/home/dpicapau/091%20Pica%20Pau%20-%20Ã‰%20Madeira%20Pra%20Burro.avi",
93:"http://173.249.8.202/home/dpicapau/092%20Pica%20Pau%20-%20Pica%20Pau%20Delegado.avi",
94:"http://173.249.8.202/home/dpicapau/093%20Pica%20Pau%20-%20Pica%20Pau%20na%20Lua.avi",
95:"http://173.249.8.202/home/dpicapau/094%20Pica%20Pau%20-%20Um%20Jogador%20de%20Sorte.avi",
96:"http://173.249.8.202/home/dpicapau/095%20Pica%20Pau%20-%20Brincadeira%20no%20PÃ¢ntano.avi",
97:"http://173.249.8.202/home/dpicapau/096%20Pica%20Pau%20-%20AlianÃ§a%20Miri.avi",
98:"http://173.249.8.202/home/dpicapau/097%20Pica%20Pau%20-%20Surrupiador%20de%20Um%20BilhÃ£o.avi",
99:"http://173.249.8.202/home/dpicapau/098%20Pica%20Pau%20-%20Pica%20Pau%20Pistoleiro.avi",
100:"http://173.249.8.202/home/dpicapau/099%20Pica%20Pau%20-%20O%20Charme%20Vence.avi",
101:"http://173.249.8.202/home/dpicapau/100%20Pica%20Pau%20-%20Propaganda%20Super.avi",
102:"http://173.249.8.202/home/dpicapau/101%20Pica%20Pau%20-%20Como%20Rechear%20Um%20Pica%20Pau.avi",
103:"http://173.249.8.202/home/dpicapau/102%20Pica%20Pau%20-%20Morcegos%20no%20CampanÃ¡rio.avi",
104:"http://173.249.8.202/home/dpicapau/103%20Pica%20Pau%20-%20O%20Ãšltimo%20Martin.avi",
105:"http://173.249.8.202/home/dpicapau/104%20Pica%20Pau%20-%20Hospitalidade%20GÃ©rmida.avi",
106:"http://173.249.8.202/home/dpicapau/105%20Pica%20Pau%20-%20CaÃ§a%20ao%20FaraÃ³.avi",
107:"http://173.249.8.202/home/dpicapau/106%20Pica%20Pau%20-%20Pirata%20do%20Barulho.avi",
108:"http://173.249.8.202/home/dpicapau/107%20Pica%20Pau%20-%20O%20PÃ¡ssaro%20Que%20Veio%20Pra%20Jantar.avi",
109:"http://173.249.8.202/home/dpicapau/108%20Pica%20Pau%20-%20O%20Jantar%20de%20Gaby.avi",
110:"http://173.249.8.202/home/dpicapau/109%20Pica%20Pau%20-%20O%20Gato%20a%20Jato.avi",
111:"http://173.249.8.202/home/dpicapau/110%20Pica%20Pau%20-%20NÃ£o%20Puxe%20As%20Minhas%20Penas.avi",
112:"http://173.249.8.202/home/dpicapau/111%20Pica%20Pau%20-%20Os%20Azares%20do%20Motorista.avi",
113:"http://173.249.8.202/home/dpicapau/112%20Pica%20Pau%20-%20O%20Fantasma%20da%20Ã“pera.avi",
114:"http://173.249.8.202/home/dpicapau/113%20Pica%20Pau%20-%20O%20Mestre%20Cuca.avi",
115:"http://173.249.8.202/home/dpicapau/114%20Pica%20Pau%20-%20Vamos%20Nanar%20JacarÃ©.avi",
116:"http://173.249.8.202/home/dpicapau/115%20Pica%20Pau%20-%20O%20Doce%20Lar%20Quase%20DestruÃ­do.avi",
117:"http://173.249.8.202/home/dpicapau/116%20Pica%20Pau%20-%20Vivendo%20Num%20Buraco.avi",
118:"http://173.249.8.202/home/dpicapau/117%20Pica%20Pau%20-%20Foguete%20Fajuto.avi",
119:"http://173.249.8.202/home/dpicapau/118%20Pica%20Pau%20-%20O%20Cuidador%20Descuidado.avi",
120:"http://173.249.8.202/home/dpicapau/119%20Pica%20Pau%20-%20MÃ¡gica%20TrÃ¡gica.avi",
121:"http://173.249.8.202/home/dpicapau/120%20Pica%20Pau%20-%20O%20Rei%20do%20Voo-Doo.avi",
122:"http://173.249.8.202/home/dpicapau/121%20Pica%20Pau%20-%20Os%20Azares%20De%20Um%20Corvo.avi",
123:"http://173.249.8.202/home/dpicapau/122%20Pica%20Pau%20-%20Chapeuzinho%20Vermelho%20de%20Araque.avi",
124:"http://173.249.8.202/home/dpicapau/123%20Pica%20Pau%20-%20O%20Guloso%20ZÃ©%20JacarÃ©.avi",
125:"http://173.249.8.202/home/dpicapau/124%20Pica%20Pau%20-%20Pica%20Pau%20Robin%20Hoody.avi",
126:"http://173.249.8.202/home/dpicapau/125%20Pica%20Pau%20-%20Viagem%20Ao%20Hawaii.avi",
127:"http://173.249.8.202/home/dpicapau/126%20Pica%20Pau%20-%20O%20FotÃ³grafo%20Chato.avi",
128:"http://173.249.8.202/home/dpicapau/127%20Pica%20Pau%20-%20O%20Pica%20Pato.avi",
129:"http://173.249.8.202/home/dpicapau/128%20Pica%20Pau%20-%20O%20Inquilino%20Malandro.avi",
130:"http://173.249.8.202/home/dpicapau/129%20Pica%20Pau%20-%20O%20Garimpeiro%20Garimpado.avi",
131:"http://173.249.8.202/home/dpicapau/130%20Pica%20Pau%20-%20Chachado%20Pra%20Dois.avi",
132:"http://173.249.8.202/home/dpicapau/131%20Pica%20Pau%20-%20FricÃ§Ã£o%20CientÃ­fica.avi",
133:"http://173.249.8.202/home/dpicapau/132%20Pica%20Pau%20-%20Chamando%20Dr.%20Pica%20Pau.avi",
134:"http://173.249.8.202/home/dpicapau/133%20Pica%20Pau%20-%20Esperto%20Contra%20Sabido.avi",
135:"http://173.249.8.202/home/dpicapau/134%20Pica%20Pau%20-%20O%20Calejado%20da%20Sala.avi",
136:"http://173.249.8.202/home/dpicapau/135%20Pica%20Pau%20-%20O%20Pica%20Pau%20na%20Barbearia.avi",
137:"http://173.249.8.202/home/dpicapau/136%20Pica%20Pau%20-%20Os%20Parentes.avi",
138:"http://173.249.8.202/home/dpicapau/137%20Pica%20Pau%20-%20Que%20Lindinho%20O%20Cachorrinho.avi",
139:"http://173.249.8.202/home/dpicapau/138%20Pica%20Pau%20-%20Auto%20Estrada%20Fracassada.avi",
140:"http://173.249.8.202/home/dpicapau/139%20Pica%20Pau%20-%20Em%20Roma%20FaÃ§a%20Como%20Os%20Pica%20Paus.avi",
141:"http://173.249.8.202/home/dpicapau/140%20Pica%20Pau%20-%20Os%20TrÃªs%20Pica-Paus.avi",
142:"http://173.249.8.202/home/dpicapau/141%20Pica%20Pau%20-%20Procura-se%20Um%20Pica%20Pau.avi",
143:"http://173.249.8.202/home/dpicapau/142%20Pica%20Pau%20-%20A%20Observadora%20de%20PÃ¡ssaros.avi",
144:"http://173.249.8.202/home/dpicapau/143%20Pica%20Pau%20-%20Esse%20Dia%20Ã‰%20Da%20CaÃ§a.avi",
145:"http://173.249.8.202/home/dpicapau/144%20Pica%20Pau%20-%20Jane%20Calamidade.avi",
146:"http://173.249.8.202/home/dpicapau/145%20Pica%20Pau%20-%20Um%20Amigo%20Leal.avi",
147:"http://173.249.8.202/home/dpicapau/146%20Pica%20Pau%20-%20O%20Pica%20Pau%20e%20o%20Professor.avi",
148:"http://173.249.8.202/home/dpicapau/147%20Pica%20Pau%20-%20QualÃ©%20a%20Sua,%20ChapÃ©u.avi",
149:"http://173.249.8.202/home/dpicapau/148%20Pica%20Pau%20-%20O%20SolidÃ¡rio.avi",
150:"http://173.249.8.202/home/dpicapau/149%20Pica%20Pau%20-%20Pica%20Pau%20e%20o%20PÃ©%20de%20FeijÃ£o.avi",
151:"http://173.249.8.202/home/dpicapau/150%20Pica%20Pau%20-%20HistÃ³ria%20Boa%20Pra%20Cachorro.avi",
152:"http://173.249.8.202/home/dpicapau/151%20Pica%20Pau%20-%20Encantos%20e%20Desencantos.avi",
153:"http://173.249.8.202/home/dpicapau/152%20Pica%20Pau%20-%20Pica%20Pau,%20Um%20Biruta%20no%20EspaÃ§o.avi",
154:"http://173.249.8.202/home/dpicapau/153%20Pica%20Pau%20-%20Nunca%20Gema%20As%20Claras.avi",
155:"http://173.249.8.202/home/dpicapau/154%20Pica%20Pau%20-%20Pica%20Pau%20Einstein.avi",
156:"http://173.249.8.202/home/dpicapau/155%20Pica%20Pau%20-%20Xerife%20Meio%20Frouxo.avi",
157:"http://173.249.8.202/home/dpicapau/156%20Pica%20Pau%20-%20O%20Paladino%20do%20Oeste.avi",
158:"http://173.249.8.202/home/dpicapau/157%20Pica%20Pau%20-%20Biruta%20NÃ¡utico.avi",
159:"http://173.249.8.202/home/dpicapau/158%20Pica%20Pau%20-%20Esse%20Cachorro%20Ã©%20Quente.avi",
160:"http://173.249.8.202/home/dpicapau/159%20-%20Pica%20Pau%20-%20Problema_Cavalar.avi",
161:"http://173.249.8.202/home/dpicapau/160%20Pica%20Pau%20-%20Pica%20Pau,%20O%20Agente%20Secreto.avi",
162:"http://173.249.8.202/home/dpicapau/161%20Pica%20Pau%20-%20Sorte%20Grande.avi",
163:"http://173.249.8.202/home/dpicapau/162%20Pica%20Pau%20-%20Reflorestamento%20Ã€%20ForÃ§a.avi",
164:"http://173.249.8.202/home/dpicapau/163%20Pica%20Pau%20-%20O%20Rei%20do%20Faroeste.avi",
165:"http://173.249.8.202/home/dpicapau/164%20Pica%20Pau%20-%20Pica%20Pau%20Adotivo.avi",
166:"http://173.249.8.202/home/dpicapau/165%20Pica%20Pau%20-%20Briga%20Pra%20NinguÃ©m%20Botar%20Defeito.avi",
167:"http://173.249.8.202/home/dpicapau/166%20Pica%20Pau%20-%20Alado%20em%20BaguidÃ¡.avi",
168:"http://173.249.8.202/home/dpicapau/167%20Pica%20Pau%20-%20Cidade%20de%20Um%20Cavalo%20SÃ³.avi",
169:"http://173.249.8.202/home/dpicapau/168%20Pica%20Pau%20-%20Pescaria%20Agitada.avi",
170:"http://173.249.8.202/home/dpicapau/169%20Pica%20Pau%20-%20NÃ£o%20Tem%20Mosquito.avi",
171:"http://173.249.8.202/home/dpicapau/170%20Pica%20Pau%20-%20Cumprimentem%20a%20Coroa.avi",
172:"http://173.249.8.202/home/dpicapau/171%20Pica%20Pau%20-%20TraiÃ§Ã£o%20no%20Deserto.avi",
173:"http://173.249.8.202/home/dpicapau/172%20Pica%20Pau%20-%20O%20Marujo%20IntrÃ©pido.avi",
174:"http://173.249.8.202/home/dpicapau/173%20Pica%20Pau%20-%20Super%20Vendedor%20PrÃ©-HistÃ³rico.avi",
175:"http://173.249.8.202/home/dpicapau/174%20Pica%20Pau%20-%20Upa%20Upa%20PangarÃ©.avi",
176:"http://173.249.8.202/home/dpicapau/175%20Pica%20Pau%20-%20Foca%20A%20Solta.avi",
177:"http://173.249.8.202/home/dpicapau/176%20Pica%20Pau%20-%20O%20Pistoleiro%20Sem%20SoluÃ§Ã£o.avi",
178:"http://173.249.8.202/home/dpicapau/177%20Pica%20Pau%20-%20Pica%20Pau%20Tropical.avi",
179:"http://173.249.8.202/home/dpicapau/178%20Pica%20Pau%20-%20ConstruÃ§aÃµ%20Demolida.avi",
180:"http://173.249.8.202/home/dpicapau/179%20Pica%20Pau%20-%20A%20Grande%20Aventura%20de%20Bonga.avi",
181:"http://173.249.8.202/home/dpicapau/180%20Pica%20Pau%20-%20Encrencas%20a%20Bordo.avi",
182:"http://173.249.8.202/home/dpicapau/181%20Pica%20Pau%20-%20A%20Fonte%20da%20Juventude.avi",
183:"http://173.249.8.202/home/dpicapau/182%20Pica%20Pau%20-%20Hora%20de%20Dormir.avi",
184:"http://173.249.8.202/home/dpicapau/183%20Pica%20Pau%20-%20O%20Recruta%20Relutante.avi",
185:"http://173.249.8.202/home/dpicapau/184%20Pica%20Pau%20-%20Como%20Capturar%20um%20Pica%20Pau.avi",
186:"http://173.249.8.202/home/dpicapau/185%20Pica%20Pau%20-%20O%20Toque%20MÃ¡gico%20Do%20Pica%20Pau.avi",
187:"http://173.249.8.202/home/dpicapau/186%20Pica%20Pau%20-%20O%20Gato%20da%20Cidade.avi",
188:"http://173.249.8.202/home/dpicapau/187%20Pica%20Pau%20-%20SÃ³%20Uma%20Soneca.avi",
189:"http://173.249.8.202/home/dpicapau/188%20Pica%20Pau%20-%20O%20Raptado.avi",
190:"http://173.249.8.202/home/dpicapau/189%20Pica%20Pau%20-%20HistÃ³ria%20Pra%20Ãndio.avi",
191:"http://173.249.8.202/home/dpicapau/190%20Pica%20Pau%20-%20Nem%20Tudo%20que%20Reluz%20Ã©%20Ouro.avi",
192:"http://173.249.8.202/home/dpicapau/191%20Pica%20Pau%20-%20Nunca%20Aposte%20Num%20Poste%20Furado.avi",
193:"http://173.249.8.202/home/dpicapau/192%20Pica%20Pau%20-%20Chili%20com%20Carne.avi",
194:"http://173.249.8.202/home/dpicapau/193%20Pica%20Pau%20-%20um%20CÃ£o%20Falante.avi",
195:"http://173.249.8.202/home/dpicapau/194%20Pica%20Pau%20-%20Por%20Um%20Amor%20Ã€%20Pizza.avi",
196:"http://173.249.8.202/home/dpicapau/195%20Pica%20Pau%20-%20GÃªnio%20Engenhoso.avi",
197:"http://173.249.8.202/home/dpicapau/196%20Pica%20Pau%20-%20Adeus%20Ã%20s%20Aulas.avi",
}

def createserverpicapau():
        eps = randint(1,197)
        ieps = 35 - eps

        if eps == 161:
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


