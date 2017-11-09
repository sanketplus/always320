#!python
from time import sleep
import os
import threading
from sys import argv

import re

import vubey_api as vubey_api

from downloader import wget_get
from parseyoutube import get_results



def select_link(results):
    """Shows resut set and returns selected result
    Args:
        results: YouTube search result set
    Return:
        result: Selected YouTube result
    """
    for i in range(len(results)):
        result = results[i]
        print("%d)\nTitle:%s\nUploader:%s\nViews:%s\nYT Link:%s\n"%(i+1,result['title'].encode('utf8'),result['uploader'].encode('utf8'),result['views'].encode('utf8'),result['link'].encode('utf8')))
        
        #Show only 5 reults
        if (i!= 0 and i%4 ==0) or (i==len(results)-1):
            print("")
            try:
                choice = raw_input("Select Song (x for more results):")
            except Exception as e:
                choice = input("Select Song (x for more results):")
            if choice == 'x':
                continue
            try:
                return results[int(choice)-1]
            except Exception as e:
                print("Invalid Input")
                return select_link(results)
                pass
    return select_link(results)



def do_main(cmd_line=False,query=""):
    """ Main function
    Args:
        cmd_line(default = False): For command line without UI
        query (default = ""): Search term

    """
    if not cmd_line:
        try:
            query = raw_input("Song name:")
        except Exception as e:
            query = input("Song name:")
    else:
        print("Searching for: %s"%(query))

    print("parsing youtube...")

    results = get_results(query)
    if cmd_line:
        result = results[0]
    else:
        result = select_link(results)
    
    print("Downloading: %s\n%s"%(result['title'].encode('utf8'),result['link'].encode('utf8')))
    yt_url = result['link']

    print("generating MP3 link...")
    try:
        file_name = re.sub("[^a-zA-Z0-9.-]", "_",str(result['title']))+".mp3"
    except Exception as e:
        file_name = re.sub("[^a-zA-Z0-9.-]", "_",str(result['title'].encode('utf8'))+".mp3")
    
    try:
        mp3_url,title = vubey_api.get_mp3_url(yt_url)
        if mp3_url!=None and title!=None:
            print("link generated: " + mp3_url.encode('utf8'))
            wget_get(mp3_url,True,file_name)
    except Exception as e:
        print("Vubey not supported... No fallback available")
        raise e
        

def main():
    if len(argv)>1:
        cmd_line = True
        if len(argv) == 3 and argv[1]=="-f".lower():
            #File Fetch
            #Threaded
            threads = []
            fp = open(argv[2],'r')
            for i in fp.readlines():
                threads.append(threading.Thread(target=do_main,args=(True,i,)))
            for i in range(len(threads)):
                while threading.active_count()>5:
                    sleep(1)
                threads[i].start()
            fp.close()
        else:
            if argv[1] == "-h".lower() or argv[1]== "--help".lower():
                print("Usage: get320.py [-f file_name] [Song Name]")
                exit()
            do_main(True,argv[1])
    else:
        do_main()


if __name__ == "__main__":
    main()