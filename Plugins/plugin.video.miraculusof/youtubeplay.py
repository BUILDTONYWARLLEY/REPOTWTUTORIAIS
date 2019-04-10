import default

def youtubeplay(name, url, iconimage):
    tam = len(url)
    print(tam)

    
    if tam == 43:
        
        base ="plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="
        baseurl = ""+base+"" ""+url[32:tam]+""
        default.PlayUrl(name,baseurl, iconimage)
       
        print(baseurl)

    if tam == 72:
        base1 ="plugin://plugin.video.youtube/playlist/"
        baseurl = ""+base1+"" ""+url[38:tam]+""
        default.PlayUrl(name,baseurl, iconimage)
       
       
        print(baseurl)

youtubeplay("https://www.youtube.com/playlist?list=PLSUn1UQk9K4ixaZXbZZN5UKlv3JP53juF") 
