#!python
import threading
from sys import argv

from always320.vubey_api import get_mp3_url
from always320.downloader import wget_get
from always320.parseyoutube import get_results



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
            choice = raw_input("Select Song (x for more results):")
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
        query = raw_input("Song name:")
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
    mp3_url = get_mp3_url(yt_url)
    print("link generated: " + mp3_url.encode('utf8'))
    file_name = wget_get(mp3_url,True)


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
                    pass
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