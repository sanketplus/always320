import wget
try:
    from urllib.request import urlopen
except:
    from urllib import urlopen



def wget_get(url,use_url_lib=False,file_name=""):
    """ Download file using wget
    For backwards compatibility
    Args:
        url: URL to download
    Returns:
        file_name:name of downloaded file
    """
    if file_name == "":
        file_name = url.split("/")[-1]
    if use_url_lib:
        urllib_download(url,file_name)
    else:
        downloaded = wget.download(url,file_name)
        print("\n Downloaded file: " + downloaded)
    return file_name



def urllib_download(url,file_name=""):
    """Download file using urllib2, good for threading
    Args:
        url: URL to download
    Returns:
        file_name:name of downloaded file
    """
    print("Downlading: %s"%(url.encode('utf8').decode('ascii')))
    mp3file = urlopen(url)
    if file_name == "":
        file_name = url.split("/")[-1]
    with open(file_name,'wb') as output:
        print("Saving: %s"%(file_name.encode('utf8').decode('ascii')))
        output.write(mp3file.read())
    return file_name