# -*- coding: utf-8 -*-
import feedparser
import hashlib
import libtorrent as lt
import time

#Game of Thrones
feedRSS = "http://showrss.info/feeds/350.rss"
lastHash = None
savePath = '/home/matheus/Downloads/Teste'
sleeptime = 3600 

def main():
    global lastHash
  
    RSSitems = getfeeditens(feedRSS)
    lastHash = generatehash(RSSitems.entries[0].link, RSSitems.entries[0].title)
    checknew()


#Checa se existe um item diferente no feed
def checknew():
    global lastHash
    while True:
        try:
            feeds = getfeeditens(feedRSS)
            newHash = generatehash(feeds.entries[0].link, feeds.entries[0].title)

            if newHash == lastHash:
                #print newHash, lastHash
                time.sleep(sleeptime)
            else:
                downloadtorrent(feeds.entries[0].link)
                lastHash = newHash
        except:
            pass


def generatehash(link, title):
    return  hashlib.md5(link + title).hexdigest()

def getfeeditens(rss):
    return feedparser.parse(rss)

def downloadtorrent(link):
    try:
        params = {
            'save_path' : savePath,
            'storage_mode': lt.storage_mode_t(2),
            'paused': False,
            'auto_managed': True,
            'duplicate_is_error': True
        }

        #Inicia o Download
        ses = lt.session()
        ses.listen_on(6881, 6891)
        handle = lt.add_magnet_uri(ses, link, params)
        ses.start_dht()

        
        while (not handle.has_metadata()):
            time.sleep(1)
        
        while (handle.status().state != lt.torrent_status.seeding):
            s = handle.status()
            

            time.sleep(5)
            
    except:
        pass



main()