# -*- coding: cp1252 -*-
import starvsforcasmal
import tomejerry
import picapau
import xman
import jackiechan
import popaye
import cavalofogo
import xbmcgui
import desenhosbiblicos
import fantasticomundobob
import capitaocavernaeaspanteras
import BiboPaieBobiFilho
import thundercats
import filmeslan



dialog = xbmcgui.Dialog()
link3 = dialog.select('Bem Vindo 24 Horas Vip', ['Desenhos','Filmes 24 Horas [Em Breve]'])

if link3 == 0:
	dialog = xbmcgui.Dialog()
	link = dialog.select('Bem Vindo 24 Horas Vip', ['Star Vs Forças do Mal', 'Tom e Jerry','Pica Pau','X-Man','As Aventuras de Jackie Chan','Popaye','Cavalo de Fogo','Desenhos Biblicos','Fantastico Mundo Bob','Capitao Caverna e as Panteras','Bibo Pai e Bobi Filho','Thundercats'])

if link3 == 1:
	dialog = xbmcgui.Dialog()
	link2 = dialog.select('Bem Vindo 24 Horas Vip', ['Filmes 24 Horas Lancamentos'])
	link = 12 + link2

if link == 0:
    starvsforcasmal.createserverstar()

if link == 1:
    tomejerry.createservertom()

if link == 2:
    picapau.createserverpicapau()

if link == 3:
    xman.createserverxm()

if link == 4:
    jackiechan.createserverjj()
    
if link == 5:
    popaye.createserverpy()

if link == 6:
    cavalofogo.createservercfg()

if link == 7:
    desenhosbiblicos.createserverdesenhobiblicos()
	
if link == 8: 
	fantasticomundobob.createserverfmbob()
	
if link == 9:
	capitaocavernaeaspanteras.createservercapcavpan()
	
if link == 10:	
	BiboPaieBobiFilho.createserverbpebf()
	
if link == 11:
	thundercats.createserverthunder()
	
if link == 12: 
	filmeslan.createserverfilmes()

           
