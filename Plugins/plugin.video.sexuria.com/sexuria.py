﻿#########################################
if 64 - 64: i11iIiiIii
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , urllib , urllib2 , os , re , sys , base64
from resources . libs . common_addon import Addon
import requests
import resolveurl
from metahandler import metahandlers
from HTMLParser import HTMLParser
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = 'plugin.video.sexuria.com'
oi1000 = 'plugin.video.sexuria.com'
oo = Addon ( o0OO00 , sys . argv )
i1iII1IiiIiI1 = xbmcaddon . Addon ( id = o0OO00 )
iIiiiI1IiI1I1 = '[COLOR blue][B]Sexuria[/B][/COLOR]'
iIiiiI1IiI1I2 = '[COLOR blue][B]Sexuria[/B][/COLOR]'
o0OoOoOO00 = os . path . join ( os . path . join ( xbmc . translatePath ( 'special://home' ) , 'addons' ) , 'plugin.video.sexuria.com' )
I11i = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'fanart.jpg' ) )
O0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'fanart.jpg' ) )
Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'icon.png' ) )
I1ii11iIi11i = 'https://img3.picload.org/image/dlgcaigw/nextpage.png'
I1IiI = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + oi1000 , 'favs.xml' ) )
o0OOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + oi1000 , 'settings.xml' ) )
iIiiiI = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.sexuria.com/downloads/' ) )
Iii1ii1II11i = xbmcgui . DialogProgress ( )
iI111iI = xbmcgui . Dialog ( )
if 34 - 34: iii1I1I / O00oOoOoO0o0O . O0oo0OO0 + Oo0ooO0oo0oO . I1i1iI1i - II
def OoI1Ii11I1Ii1i ( ) :
 if 67 - 67: iiI1iIiI . ooo0Oo0 * i1 - Oooo0000 * i1IIi11111i / o000o0o00o0Oo
 if not os . path . exists ( os . path . dirname ( iIiiiI ) ) :
  try :
   os . makedirs ( os . path . dirname ( iIiiiI ) )
   with open ( o0OOO , "w" ) as ooIiII1I1i1i1ii :
    ooIiII1I1i1i1ii . write ( "<date>000</date>" )
  except OSError as IIIII :
   if IIIII . errno != errno . EEXIST :
    raise
 I1 ( )
 if 54 - 54: oO % IiiIIiiI11 / oooOOOOO * I1i1iI1i / IiiIIiiI11
def oOO ( url , mode , name , iconimage , fanart ) :
 if 34 - 34: i1 % OoooooooOO / i1IIi . o000o0o00o0Oo + O0
 with open ( I1IiI , "a" ) as I1Ii :
  I1Ii . write ( '<item>\n<title>' + name + '</title>\n<url>' + url + '</url>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  iI111iI . notification ( iIiiiI1IiI1I1 , '[COLOR blue]' + name + ' added to favourites[/COLOR]' , 'https://img1.picload.org/image/dloiowoa/sexuria.png' , 5000 )
  if 66 - 66: i1IIi11111i
def oo0Ooo0 ( ) :
 if 46 - 46: oooOOOOO % oooOOOOO - ooo0Oo0 * II % o000o0o00o0Oo
 OOooO0OOoo ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , 'https://img3.picload.org/image/dlgcaira/x.png' , I11i , '[COLOR red]EMERGENCY EXIT[/COLOR]' )
 OOooO0OOoo ( '[COLOR blue]' + "REMOVE ALL FAVOURITES" + '[/COLOR]' , 'url' , 893 , 'https://img3.picload.org/image/dlgcaigl/favs.png' , I11i )
 with open ( I1IiI , "a" ) as I1Ii :
  oOOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + oi1000 , 'favs.xml' ) )
  O0OoO000O0OO = open ( oOOoO0 ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iiI1IiI = re . compile ( '<item>(.+?)</item>' ) . findall ( O0OoO000O0OO )
  OOooO0OOoo ( '[COLOR blue]' + "Your Favourites" + '[/COLOR]' , 'url' , '2' , 'https://img3.picload.org/image/dlgcaigl/favs.png' , I11i )
  OOooO0OOoo ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , 'https://img3.picload.org/image/dlgcaigl/favs.png' , I11i )
  if len ( iiI1IiI ) < 1 :
   OOooO0OOoo ( '[COLOR blue]' + "NO FAVS ADDED YET" + '[/COLOR]' , 'url' , '2' , 'https://img3.picload.org/image/dlgcaigl/favs.png' , I11i )
  for IIooOoOoo0O in iiI1IiI :
   OooO0 = re . compile ( '<title>(.+?)</title>' ) . findall ( IIooOoOoo0O ) [ 0 ]
   II11iiii1Ii = re . compile ( '<url>(.+?)</url>' ) . findall ( IIooOoOoo0O ) [ 0 ]
   Oo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( IIooOoOoo0O ) [ 0 ]
   O0O = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( IIooOoOoo0O ) [ 0 ]
   OOooO0OOoo ( '[COLOR blue]' + OooO0 + '[/COLOR]' , II11iiii1Ii , 99 , Oo , O0O )
 OOooO0OOoo ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , 'https://img3.picload.org/image/dlgcaira/x.png' , I11i , '[COLOR red]EMERGENCY EXIT[/COLOR]' )
 if 70 - 70: ooo0Oo0 / iIii1I11I1II1 % oooOOOOO % i11iIiiIii . O00oOoOoO0o0O
def O0o0Oo ( ) :
 if 78 - 78: iIii1I11I1II1 - i1IIi11111i * Oo0ooO0oo0oO + II + o000o0o00o0Oo + o000o0o00o0Oo
 with open ( I1IiI , "w" ) as I1Ii :
  I1Ii . write ( '' )
  iI111iI . notification ( iIiiiI1IiI1I2 , '[COLOR blue]Favourites has been wiped[/COLOR]' , 'https://img1.picload.org/image/dloiowoa/sexuria.png' , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 11 - 11: o000o0o00o0Oo - Oo0ooO0oo0oO % oooOOOOO % o000o0o00o0Oo / I1i1iI1i - Oo0ooO0oo0oO
def o0o0oOOOo0oo ( ) :
 if 80 - 80: Oooo0000 * i11iIiiIii / IiiIIiiI11
 I11II1i ( "[COLOR white][B]M[COLOR blue]enu[/B][/COLOR]" , 'null' , 5 , 'https://img3.picload.org/image/dlgcaigi/home.png' , I11i , 'Back to [B][COLOR orange]RUB[/COLOR][COLOR blue] THE [/COLOR][COLOR orange]DUCK[/COLOR][/B] Menu' )
 I11II1i ( "[COLOR white][B]S[COLOR blue]earch[/B][/COLOR]" , 'null' , 2 , 'https://img3.picload.org/image/dloigrli/search.png' , I11i , '[COLOR blue]Search XXX[/COLOR]' )
 I11II1i ( "[COLOR white][B]M[COLOR blue]ovies[/B][/COLOR]" , 'null' , 1 , Oo , I11i , '[COLOR blue]XXX Movies[/COLOR]' )
 I11II1i ( "[COLOR white][B]S[COLOR blue]cenes[/B][/COLOR]" , 'null' , 6 , Oo , I11i , '[COLOR blue]XXX Scenes[/COLOR]' )
 I11II1i ( "[COLOR white][B]C[COLOR blue]lips HD[/B][/COLOR]" , 'null' , 7 , Oo , I11i , '[COLOR blue]XXX Clips in HD[/COLOR]' )
 I11II1i ( "[COLOR white][B]Y[COLOR blue]our Favourites[/B][/COLOR]" , 'null' , 890 , 'https://img3.picload.org/image/dlgcaigl/favs.png' , I11i , '[COLOR blue]Save Your Favourite Videos[/COLOR]' )
 OoI1Ii11I1Ii1i ( )
 IIIIIooooooO0oo ( )
 if 49 - 49: II * iIii1I11I1II1 / i1IIi / i11iIiiIii / II
def I1i1I1II ( url ) :
 if 45 - 45: IiiIIiiI11 . I1i1iI1i
 OOooO0OOoo ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , 'https://img3.picload.org/image/dlgcaira/x.png' , I11i , '[COLOR red]EMERGENCY EXIT[/COLOR]' )
 oOii1i1I1i = 972
 if 'null' in url :
  url = 'http://www.sexuria.com/Streams_DVD.Rips___hoster__Page_1.html'
 o00oOO0 = oOoo ( url )
 iiI1IiI = re . compile ( '<li class=\'span2 marginbottom0\'>(.*?)</li>' ) . findall ( o00oOO0 )
 for iIii11I in iiI1IiI :
  OooO0 = re . compile ( '<h6 class="text-center formsearch">(.*?)</h6>' ) . findall ( iIii11I ) [ 0 ]
  OooO0 = OooO0[:-8]
  OooO0 = OooO0.replace("..", "...")
  OOO0OOO00oo = re . compile ( 'href=\'(.*?)\'' ) . findall ( iIii11I ) [ 0 ]
  OOO0OOO00oo = 'http://www.sexuria.com/' + OOO0OOO00oo
  Oo = re . compile ( '<img src=\'(.*?)\'' ) . findall ( iIii11I ) [ 0 ] . strip ( )
  Iii111II = re . compile ( '<h6 class="text-center formsearch">(.*?)</h6>' ) . findall ( iIii11I ) [ 0 ]
  Iii111II = Iii111II[:-8]
  Iii111II = Iii111II.replace("..", "...")
  OooO0 = iiii11I ( OooO0 )
  Iii111II = iiii11I ( Iii111II )
  I11II1i ( "[COLOR blue]" + OooO0 + "[/COLOR]" , OOO0OOO00oo , 98 , Oo , I11i , Iii111II )
 try :
  Ooo0OO0oOO = url.replace("http://www.sexuria.com/Streams_DVD.Rips___hoster__Page_", "")
  Ooo0OO0oOO = Ooo0OO0oOO.replace(".html", "")
  Ooo0OO0oOO = int ( Ooo0OO0oOO )
  ii11i1 = Ooo0OO0oOO + 1
  IIIii1II1II = 'http://www.sexuria.com/Streams_DVD.Rips___hoster__Page_' + str ( ii11i1 ) + '.html'
  if ii11i1 < oOii1i1I1i :
   I11II1i ( "[COLOR yellow]Next Page ---->[/COLOR]" , IIIii1II1II , 1 , I1ii11iIi11i , I11i , 'Next Page' )
 except :
  pass
 OOooO0OOoo ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , 'https://img3.picload.org/image/dlgcaira/x.png' , I11i , '[COLOR red]EMERGENCY EXIT[/COLOR]' )
 IIIIIooooooO0oo ( )
def i1I1iI ( url ) :
 if 30 - 30: iii1I1I - i1 - i11iIiiIii % I1i1iI1i - iii1I1I * i1IIi11111i
 OOooO0OOoo ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , 'https://img3.picload.org/image/dlgcaira/x.png' , I11i , '[COLOR red]EMERGENCY EXIT[/COLOR]' )
 oOii1i1I1i = 313
 if 'null' in url :
  kb = xbmc.Keyboard ('default', 'heading', False)
  kb.setDefault('')
  kb.setHeading('Search')
  kb.setHiddenInput(False)
  kb.doModal()
  if (kb.isConfirmed()):
   try:
    search = kb.getText(kb)
    search = search.replace ( ' ' , '-' )
    search = search.decode('utf-8')
   except:
    pass
  url = 'http://www.sexuria.com/Downloads__'+search+'__hoster__Page_1.html'
 o00oOO0 = oOoo ( url )
 iiI1IiI = re . compile ( '<li class=\'span2 marginbottom0\'>(.*?)</li>' ) . findall ( o00oOO0 )
 for iIii11I in iiI1IiI :
  OooO0 = re . compile ( '<h6 class="text-center formsearch">(.*?)</h6>' ) . findall ( iIii11I ) [ 0 ]
  OooO0 = OooO0[:-8]
  OooO0 = OooO0.replace("..", "...")
  OOO0OOO00oo = re . compile ( 'href=\'(.*?)\'' ) . findall ( iIii11I ) [ 0 ]
  OOO0OOO00oo = 'http://www.sexuria.com/' + OOO0OOO00oo
  Oo = re . compile ( '<img src=\'(.*?)\'' ) . findall ( iIii11I ) [ 0 ] . strip ( )
  try :
   Iii111II = re . compile ( '<h6 class="text-center formsearch">(.*?)</h6>' ) . findall ( iIii11I ) [ 0 ]
   Iii111II = Iii111II[:-8]
   Iii111II = Iii111II.replace("..", "...")
  except :
   Iii111II = '[COLOR blue]No Description Available For This Movie[/COLOR]'
  OooO0 = iiii11I ( OooO0 )
  Iii111II = iiii11I ( Iii111II )
  I11II1i ( "[COLOR blue]" + OooO0 + "[/COLOR]" , OOO0OOO00oo , 98 , Oo , I11i , Iii111II )
 try :
  url = url.replace(".html", "")
  Ooo0OO0oOO = url . split ( 'Page_' ) [ - 1 ]
  IOoo0OO0oOO = url.rsplit('//')[-1].split('Page_')[0]
  Ooo0OO0oOO = int ( Ooo0OO0oOO )
  ii11i1 = Ooo0OO0oOO + 1
  IIIii1II1II = 'http://'+IOoo0OO0oOO+'Page_' + str ( ii11i1 ) + '.html'
  if ii11i1 < oOii1i1I1i :
   I11II1i ( "[COLOR yellow]Next Page ---->[/COLOR]" , IIIii1II1II , 2 , I1ii11iIi11i , I11i , 'Next Page' )
 except :
  pass
 OOooO0OOoo ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , 'https://img3.picload.org/image/dlgcaira/x.png' , I11i , '[COLOR red]EMERGENCY EXIT[/COLOR]' )
 IIIIIooooooO0oo ( )
def Ii1iIiii1 ( url ) :
 if 91 - 91: Oo0ooO0oo0oO . iiI1iIiI + Oo0ooO0oo0oO - o000o0o00o0Oo / OoooooooOO
 OOooO0OOoo ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , 'https://img3.picload.org/image/dlgcaira/x.png' , I11i , '[COLOR red]EMERGENCY EXIT[/COLOR]' )
 oOii1i1I1i = 972
 if 'null' in url :
  url = 'http://www.sexuria.com/Streams_Scenes___hoster__Page_1.html'
 o00oOO0 = oOoo ( url )
 iiI1IiI = re . compile ( '<li class=\'span2 marginbottom0\'>(.*?)</li>' ) . findall ( o00oOO0 )
 for iIii11I in iiI1IiI :
  OooO0 = re . compile ( '<h6 class="text-center formsearch">(.*?)</h6>' ) . findall ( iIii11I ) [ 0 ]
  OooO0 = OooO0[:-8]
  OooO0 = OooO0.replace("..", "...")
  OOO0OOO00oo = re . compile ( 'href=\'(.*?)\'' ) . findall ( iIii11I ) [ 0 ]
  OOO0OOO00oo = 'http://www.sexuria.com/' + OOO0OOO00oo
  Oo = re . compile ( '<img src=\'(.*?)\'' ) . findall ( iIii11I ) [ 0 ] . strip ( )
  try :
   Iii111II = re . compile ( '<h6 class="text-center formsearch">(.*?)</h6>' ) . findall ( iIii11I ) [ 0 ]
   Iii111II = Iii111II[:-8]
   Iii111II = Iii111II.replace("..", "...")
  except :
   Iii111II = '[COLOR blue]No Description Available For This Movie[/COLOR]'
  OooO0 = iiii11I ( OooO0 )
  Iii111II = iiii11I ( Iii111II )
  I11II1i ( "[COLOR blue]" + OooO0 + "[/COLOR]" , OOO0OOO00oo , 98 , Oo , I11i , Iii111II )
 try :
  Ooo0OO0oOO = url.replace("http://www.sexuria.com/Streams_Scenes___hoster__Page_", "")
  Ooo0OO0oOO = Ooo0OO0oOO.replace(".html", "")
  Ooo0OO0oOO = int ( Ooo0OO0oOO )
  ii11i1 = Ooo0OO0oOO + 1
  IIIii1II1II = 'http://www.sexuria.com/Streams_Scenes___hoster__Page_' + str ( ii11i1 ) + '.html'
  if ii11i1 < oOii1i1I1i :
   I11II1i ( "[COLOR yellow]Next Page ---->[/COLOR]" , IIIii1II1II , 6 , I1ii11iIi11i , I11i , 'Next Page' )
 except :
  pass
 OOooO0OOoo ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , 'https://img3.picload.org/image/dlgcaira/x.png' , I11i , '[COLOR red]EMERGENCY EXIT[/COLOR]' )
 IIIIIooooooO0oo ( )
def iII1 ( url ) :
 if 30 - 30: iii1I1I - i1 - i11iIiiIii % I1i1iI1i - iii1I1I * i1IIi11111i
 OOooO0OOoo ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , 'https://img3.picload.org/image/dlgcaira/x.png' , I11i , '[COLOR red]EMERGENCY EXIT[/COLOR]' )
 oOii1i1I1i = 313
 if 'null' in url :
  url = 'http://www.sexuria.com/Streams_HD-Clips___hoster__Page_1.html'
 o00oOO0 = oOoo ( url )
 iiI1IiI = re . compile ( '<li class=\'span2 marginbottom0\'>(.*?)</li>' ) . findall ( o00oOO0 )
 for iIii11I in iiI1IiI :
  OooO0 = re . compile ( '<h6 class="text-center formsearch">(.*?)</h6>' ) . findall ( iIii11I ) [ 0 ]
  OooO0 = OooO0[:-8]
  OooO0 = OooO0.replace("..", "...")
  OOO0OOO00oo = re . compile ( 'href=\'(.*?)\'' ) . findall ( iIii11I ) [ 0 ]
  OOO0OOO00oo = 'http://www.sexuria.com/' + OOO0OOO00oo
  Oo = re . compile ( '<img src=\'(.*?)\'' ) . findall ( iIii11I ) [ 0 ] . strip ( )
  try :
   Iii111II = re . compile ( '<h6 class="text-center formsearch">(.*?)</h6>' ) . findall ( iIii11I ) [ 0 ]
   Iii111II = Iii111II[:-8]
   Iii111II = Iii111II.replace("..", "...")
  except :
   Iii111II = '[COLOR blue]No Description Available For This Movie[/COLOR]'
  OooO0 = iiii11I ( OooO0 )
  Iii111II = iiii11I ( Iii111II )
  I11II1i ( "[COLOR blue]" + OooO0 + "[/COLOR]" , OOO0OOO00oo , 98 , Oo , I11i , Iii111II )
 try :
  Ooo0OO0oOO = url.replace("http://www.sexuria.com/Streams_HD-Clips___hoster__Page_", "")
  Ooo0OO0oOO = Ooo0OO0oOO.replace(".html", "")
  Ooo0OO0oOO = int ( Ooo0OO0oOO )
  ii11i1 = Ooo0OO0oOO + 1
  IIIii1II1II = 'http://www.sexuria.com/Streams_HD-Clips___hoster__Page_' + str ( ii11i1 ) + '.html'
  if ii11i1 < oOii1i1I1i :
   I11II1i ( "[COLOR yellow]Next Page ---->[/COLOR]" , IIIii1II1II , 7 , I1ii11iIi11i , I11i , 'Next Page' )
 except :
  pass
 OOooO0OOoo ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , 'https://img3.picload.org/image/dlgcaira/x.png' , I11i , '[COLOR red]EMERGENCY EXIT[/COLOR]' )
 IIIIIooooooO0oo ( )
def oOOOoO0O00o0 ( url ) :
 if 30 - 30: II . i1IIi11111i - OoooooooOO
 if 'null' in url :
  xbmc.executebuiltin('RunAddon(plugin.video.rubtheduck)')
def oO00O0O0O ( title ) :
 if 31 - 31: Oooo0000 - iii1I1I . Oooo0000
 title = title . lower ( )
 if 'openload' in title :
  title = title . title ( )
  title = title + '[COLOR yellow] (Requires Pairing)[/COLOR]'
  return title
 if 'flashx' in title :
  title = title . title ( )
  title = title + '[COLOR yellow] (Requires Pairing)[/COLOR]'
  return title
 if 'thevideo' in title :
  title = title . title ( )
  title = title + '[COLOR yellow] (Requires Pairing)[/COLOR]'
  return title
 if 'vidup' in title :
  title = title . title ( )
  title = title + '[COLOR yellow] (Requires Pairing)[/COLOR]'
  return title
 if 'upvid' in title :
  title = 'not supported'
  return title
 else :
  title = title . title ( )
  return title
  if 18 - 18: II
def O0o0O00Oo0o0 ( name , url , iconimage , description ) :
 if 87 - 87: oooOOOOO * O0oo0OO0 % i11iIiiIii % I1i1iI1i - i1
 OOooO0OOoo ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , 'https://img3.picload.org/image/dlgcaira/x.png' , I11i , '[COLOR red]EMERGENCY EXIT[/COLOR]' )
 o00oOO0 = oOoo ( url )
 iiI1IiI = re . compile ( 'class="btn btn-large btn-info"(.*?)<div class="modal-footer">' ) . findall ( o00oOO0 )
 for iIii11I in iiI1IiI :
  try :
   OooO0 = re . compile ( 'data-toggle="modal">(.*?)</a>' ) . findall ( iIii11I ) [ 0 ]
   OooO0 = iiii11I ( OooO0 )
   OooO0 = oO00O0O0O ( OooO0 )
   OOO0OOO00oo = re . compile ( 'disabled\'" href="(.*?)"' ) . findall ( iIii11I ) [ 0 ]
   if 'share-online' in OOO0OOO00oo:
    OooO0 = 'not supported'
   elif 'ul.to' in OOO0OOO00oo:
    OooO0 = 'not supported'
   elif 'uploaded.net' in OOO0OOO00oo:
    OooO0 = 'not supported'
   elif 'uploaded.to' in OOO0OOO00oo:
    OooO0 = 'not supported'
   else:
    pass
   if not 'not supported' in OooO0 :
    OOooO0OOoo ( "[COLOR blue]" + name + " :[/COLOR][COLOR white]: " + OooO0 + "[/COLOR]" , OOO0OOO00oo , 99 , iconimage , I11i , description )
  except : pass
 OOooO0OOoo ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , 'https://img3.picload.org/image/dlgcaira/x.png' , I11i , '[COLOR red]EMERGENCY EXIT[/COLOR]' )
 IIIIIooooooO0oo ( )
def oOoo ( url ) :
 try :
  O0ooo0O0oo0 = urllib2 . Request ( url )
  O0ooo0O0oo0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  oo0oOo = urllib2 . urlopen ( O0ooo0O0oo0 , timeout = 5 )
  o00oOO0 = oo0oOo . read ( )
  oo0oOo . close ( )
  o00oOO0 = o00oOO0 . replace ( '\n' , '' ) . replace ( '\r' , '' )
  return o00oOO0
 except : quit ( )
 if 89 - 89: I1i1iI1i
 if 68 - 68: Oo0ooO0oo0oO * OoooooooOO % O0 + Oo0ooO0oo0oO + oooOOOOO
def I11II1i ( name , url , mode , iconimage , fanart , description = '' ) :
 if 4 - 4: oooOOOOO + O0 * i1
 if not "http" in iconimage :
  iconimage = Oo
 if not "http" in fanart :
  fanart = I11i
 description = description . encode ( encoding = 'UTF-8' , errors = 'strict' )
 OOoo0O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo0ooOo0o = True
 Ii1i1 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage , )
 Ii1i1 . setProperty ( "fanart_Image" , fanart )
 Ii1i1 . setProperty ( "icon_Image" , iconimage )
 Ii1i1 . setInfo ( 'video' , { 'Plot' : description } )
 Oo0ooOo0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoo0O , listitem = Ii1i1 , isFolder = True )
 iiIii = xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
 return Oo0ooOo0o
 if 79 - 79: OoooooooOO / O0
 if 75 - 75: I1i1iI1i % II % II . IiiIIiiI11
def OOooO0OOoo ( name , url , mode , iconimage , fanart , description = '' ) :
 if 5 - 5: II * oooOOOOO + I1i1iI1i . i1 + I1i1iI1i
 if not "http" in iconimage :
  iconimage = Oo
 if not "http" in fanart :
  fanart = I11i
 OOoo0O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 Oo0ooOo0o = True
 Ii1i1 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 Ii1i1 . setProperty ( "fanart_Image" , fanart )
 Ii1i1 . setProperty ( "icon_Image" , iconimage )
 Ii1i1 . setInfo ( 'video' , { 'Plot' : description } )
 I1IiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 Ii1i1 . addContextMenuItems ( [ ( '[COLOR blue]Add To XXX Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I1IiI + ')' ) ] )
 if 91 - 91: O0
 iiIii = xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
 Oo0ooOo0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoo0O , listitem = Ii1i1 , isFolder = False )
 return Oo0ooOo0o
 if 61 - 61: iii1I1I
 if 64 - 64: oooOOOOO / I1i1iI1i - O0 - Oooo0000
def O0oOoOOOoOO ( txt ) :
 if 38 - 38: IiiIIiiI11
 txt = txt . replace ( "&quot;" , "\"" )
 txt = txt . replace ( "&amp;" , "&" )
 txt = txt . replace ( u"\u2018" , "'" ) . replace ( u"\u2019" , "'" )
 txt = txt . strip ( )
 return txt
 if 7 - 7: O0 . o000o0o00o0Oo % iiI1iIiI - O00oOoOoO0o0O - iIii1I11I1II1
def I111IIIiIii ( string ) :
 oO0000OOo00 = ( c for c in string if 0 < ord ( c ) < 127 )
 if 27 - 27: O00oOoOoO0o0O % O00oOoOoO0o0O
 return '' . join ( oO0000OOo00 )
 if 1 - 1: Oo0ooO0oo0oO - ooo0Oo0 . Oooo0000 . Oo0ooO0oo0oO / O0oo0OO0 + Oooo0000
def Ooo ( heading , text ) :
 if 62 - 62: i1 / Oo0ooO0oo0oO + i1IIi11111i / Oo0ooO0oo0oO . iii1I1I
 text = text + "\n\nNews Updates Every 5 Seconds"
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 ooOOoooooo = xbmcgui . Window ( id )
 II1I = 50
 while ( II1I > 0 ) :
  try :
   xbmc . sleep ( 10 )
   II1I -= 1
   ooOOoooooo . getControl ( 1 ) . setLabel ( heading )
   ooOOoooooo . getControl ( 5 ) . setText ( text )
   quit ( )
   return
  except : pass
  if 84 - 84: oO . i11iIiiIii . oO * iiI1iIiI - Oooo0000
def ii ( name , url , iconimage ) :
 if 81 - 81: IiiIIiiI11 % o000o0o00o0Oo . iiI1iIiI / II
 iI111iI . notification ( iIiiiI1IiI1I1 , '[COLOR blue]Attempting To Resolve Link Now[/COLOR]' , Oo , 5000 )
 if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
  try:
   iiiIiI = resolveurl . HostedMediaFile ( url ) . resolve ( )
   Ii1i1 = xbmcgui . ListItem ( name , iconImage = Oo , thumbnailImage = Oo )
   Ii1i1 . setPath ( iiiIiI )
   xbmc . Player ( ) . play ( iiiIiI , Ii1i1 , False )
   quit ( )
  except:
   pass
 else :
  iiiIiI = url
  Ii1i1 = xbmcgui . ListItem ( name , iconImage = Oo , thumbnailImage = Oo )
  Ii1i1 . setPath ( iiiIiI )
  xbmc . Player ( ) . play ( iiiIiI , Ii1i1 , False )
  quit ( )
  if 91 - 91: o000o0o00o0Oo % i1IIi % iIii1I11I1II1
def I1 ( ) :
 if 20 - 20: i1 % i1IIi11111i / i1IIi11111i + i1IIi11111i
 if 45 - 45: ooo0Oo0 - oO - OoooooooOO - Oo0ooO0oo0oO . iii1I1I / O0
 oo0o00O = open ( o0OOO ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  o00O0OoO = "937AE1"
  if o00O0OoO == 'EXPIRED' :
   i1I = ''
   OoOO = xbmc . Keyboard ( i1I , '' )
   OoOO . doModal ( )
   if OoOO . isConfirmed ( ) :
    i1I = OoOO . getText ( )
    if len ( i1I ) > 1 :
     ooOOO0 = i1I . title ( )
     with open ( o0OOO , "w" ) as ooIiII1I1i1i1ii :
      ooIiII1I1i1i1ii . write ( "<pin>" + ooOOO0 + "</pin>" )
     I1 ( )
    else : quit ( )
   else :
    quit ( )
  if not 'EXPIRED' in o00O0OoO :
   o0o = "937AE1"
   O0OOoO00OO0o = 'https://mangoporn.net'
   o00oOO0 = oOoo ( O0OOoO00OO0o )
   if len ( o00oOO0 ) < 1 or 'Pin Expired' in o00oOO0 :
    with open ( o0OOO , "w" ) as ooIiII1I1i1i1ii :
     ooIiII1I1i1i1ii . write ( '<pin>EXPIRED</pin>' )
    I1 ( )
   else :
    global baseurl
    baseurl = o00oOO0
 except IndexError :
  with open ( o0OOO , "w" ) as ooIiII1I1i1i1ii :
   ooIiII1I1i1i1ii . write ( "<pin>EXPIRED</pin>\n" )
  I1 ( )
  if 38 - 38: i1 % Oooo0000 % II % Oo0ooO0oo0oO - O0oo0OO0
def i1Ii ( ) :
 if 14 - 14: o000o0o00o0Oo
 xbmc . executebuiltin ( "XBMC.Container.Update(path,replace)" )
 xbmc . executebuiltin ( "XBMC.ActivateWindow(Home)" )
 if 11 - 11: oO * O00oOoOoO0o0O . iIii1I11I1II1 % OoooooooOO + o000o0o00o0Oo
def IIIIIooooooO0oo ( ) :
 if 78 - 78: Oo0ooO0oo0oO . i1 + Oo0ooO0oo0oO / Oooo0000 / Oo0ooO0oo0oO
 oO0O00OoOO0 = xbmc . getInfoLabel ( "System.BuildVersion" )
 OoO = float ( oO0O00OoOO0 [ : 4 ] )
 if OoO >= 11.0 and OoO <= 11.9 :
  O00 = 'Eden'
 elif OoO >= 12.0 and OoO <= 12.9 :
  O00 = 'Frodo'
 elif OoO >= 13.0 and OoO <= 13.9 :
  O00 = 'Gotham'
 elif OoO >= 14.0 and OoO <= 14.9 :
  O00 = 'Helix'
 elif OoO >= 15.0 and OoO <= 15.9 :
  O00 = 'Isengard'
 elif OoO >= 16.0 and OoO <= 16.9 :
  O00 = 'Jarvis'
 elif OoO >= 17.0 and OoO <= 17.9 :
  O00 = 'Krypton'
 else : O00 = "Decline"
 if 29 - 29: IiiIIiiI11 / Oo0ooO0oo0oO . i1IIi * O00oOoOoO0o0O + i11iIiiIii
 if O00 == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif O00 == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 if 6 - 6: oooOOOOO / i11iIiiIii + o000o0o00o0Oo * ooo0Oo0
def iiii11I ( text ) :
 if 80 - 80: iii1I1I
 text = str ( text )
 text = text . replace ( '\\r' , '' )
 text = text . replace ( '\\n' , '' )
 text = text . replace ( '\\t' , '' )
 text = text . replace ( '\\' , '' )
 text = text . replace ( '<br />' , '\n' )
 text = text . replace ( '<hr />' , '' )
 text = text . replace ( '&#039;' , "'" )
 text = text . replace ( '&#39;' , "'" )
 text = text . replace ( '&quot;' , '"' )
 text = text . replace ( '&rsquo;' , "'" )
 text = text . replace ( '&amp;' , "&" )
 text = text . replace ( '&#8211;' , "&" )
 text = text . replace ( '&#8217;' , "'" )
 text = text . replace ( '&#038;' , "&" )
 text = text . replace ( '&#8211;' , "-" )
 text = text . replace ( '&#8216;' , "'" )
 text = text . replace ( '&#8230;' , "..." )
 text = text . replace ( '&#8220;' , "'" )
 text = text . replace ( '&#8221;' , "'" )
 text = text . replace ( '&#8212;' , "_" )
 text = text . lstrip ( ' ' )
 text = text . lstrip ( '	' )
 text = I111IIIiIii ( text )
 return text
 if 83 - 83: Oooo0000 . i11iIiiIii + iii1I1I . II * Oooo0000
 if 53 - 53: iii1I1I
def i1Ii1Ii ( ) :
 if 52 - 52: Oo0ooO0oo0oO . ooo0Oo0
 ii1iII1II = [ ]
 Iii1I1I11iiI1 = sys . argv [ 2 ]
 if len ( Iii1I1I11iiI1 ) >= 2 :
  I1I1i1I = sys . argv [ 2 ]
  ii1I = I1I1i1I . replace ( '?' , '' )
  if ( I1I1i1I [ len ( I1I1i1I ) - 1 ] == '/' ) :
   I1I1i1I = I1I1i1I [ 0 : len ( I1I1i1I ) - 2 ]
  O0oO0 = ii1I . split ( '&' )
  ii1iII1II = { }
  for oO0 in range ( len ( O0oO0 ) ) :
   O0OO0O = { }
   O0OO0O = O0oO0 [ oO0 ] . split ( '=' )
   if ( len ( O0OO0O ) ) == 2 :
    ii1iII1II [ O0OO0O [ 0 ] ] = O0OO0O [ 1 ]
 return ii1iII1II
 if 81 - 81: ooo0Oo0 . II % O0 / O00oOoOoO0o0O - ooo0Oo0
I1I1i1I = i1Ii1Ii ( ) ; II11iiii1Ii = None ; Ii1I1i = None ; OO = None ; I1iI1ii1II = None ; iIii1 = None ; O0O0OOOOoo = None
try : I1iI1ii1II = urllib . unquote_plus ( I1I1i1I [ "site" ] )
except : pass
try : II11iiii1Ii = urllib . unquote_plus ( I1I1i1I [ "url" ] )
except : pass
try : Ii1I1i = urllib . unquote_plus ( I1I1i1I [ "name" ] )
except : pass
try : OO = int ( I1I1i1I [ "mode" ] )
except : pass
try : iIii1 = urllib . unquote_plus ( I1I1i1I [ "iconimage" ] )
except : pass
try : O0O = urllib . unquote_plus ( I1I1i1I [ "fanart" ] )
except : pass
try : O0O0OOOOoo = urllib . unquote_plus ( I1I1i1I [ "description" ] )
except : pass
if 74 - 74: iiI1iIiI + iii1I1I / Oo0ooO0oo0oO
if OO == None or II11iiii1Ii == None or len ( II11iiii1Ii ) < 1 : o0o0oOOOo0oo ( )
if 100 - 100: I1i1iI1i * iIii1I11I1II1
elif OO == 1 : I1i1I1II ( II11iiii1Ii )
elif OO == 2 : i1I1iI ( II11iiii1Ii )
elif OO == 3 : Oo0O0O0ooO0O ( II11iiii1Ii )
elif OO == 4 : O0OOO0OOoO0O ( II11iiii1Ii )
elif OO == 5 : oOOOoO0O00o0 ( II11iiii1Ii )
elif OO == 6 : Ii1iIiii1 ( II11iiii1Ii )
elif OO == 7 : iII1 ( II11iiii1Ii )
if 86 - 86: Oo0ooO0oo0oO * i1 . o000o0o00o0Oo
if 32 - 32: II . oO * Oooo0000
if 93 - 93: II % i1IIi . i1IIi11111i . i11iIiiIii
if 56 - 56: iiI1iIiI % O0 - O00oOoOoO0o0O
elif OO == 98 : O0o0O00Oo0o0 ( Ii1I1i , II11iiii1Ii , iIii1 , O0O0OOOOoo )
elif OO == 99 : ii ( Ii1I1i , II11iiii1Ii , iIii1 )
elif OO == 889 : oOO ( II11iiii1Ii , OO , Ii1I1i , iIii1 , O0O )
elif OO == 890 : oo0Ooo0 ( )
elif OO == 891 : REMFAVS ( Ii1I1i , II11iiii1Ii , iIii1 )
elif OO == 892 : OPEN_SETTINGS ( )
elif OO == 893 : O0o0Oo ( )
elif OO == 911 : i1Ii ( )
if 100 - 100: i1IIi11111i - O0 % ooo0Oo0 * i1 + O00oOoOoO0o0O
if 88 - 88: OoooooooOO - Oo0ooO0oo0oO * O0 * OoooooooOO . OoooooooOO
if OO == None or II11iiii1Ii == None or len ( II11iiii1Ii ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True )
if 33 - 33: IiiIIiiI11 + o000o0o00o0Oo * ooo0Oo0 / iIii1I11I1II1 - O00oOoOoO0o0O
if 54 - 54: IiiIIiiI11 / i1 . ooo0Oo0 % o000o0o00o0Oo
if 57 - 57: i11iIiiIii . iiI1iIiI - i1IIi11111i - ooo0Oo0 + I1i1iI1i
if 63 - 63: I1i1iI1i * o000o0o00o0Oo
if 69 - 69: O0 . Oo0ooO0oo0oO
if 49 - 49: O00oOoOoO0o0O - Oooo0000
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3