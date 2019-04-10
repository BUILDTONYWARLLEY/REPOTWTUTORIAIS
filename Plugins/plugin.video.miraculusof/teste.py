def gdrive(url):
        tam = len(url)
        utam = tam - 28
        gdrive = "plugin://plugin.video.gdrive?mode=streamURL&amp;url=https://docs.google.com/file/d/"+url[utam:tam]+""
        print (tam)
        print(gdrive)




gdrive("https://drive.google.com/open?id=0B13p6muB3isiNnZWdXk3eEhUVEE")
