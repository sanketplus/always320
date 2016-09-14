import wget
import os


def wget_get(url):
    out_path = os.path.expanduser("~")+"/Music/always320/"

    if not os.path.exists(out_path):
        os.makedirs(out_path)

    file_name = out_path + url.split("/")[-1]

    downloaded = wget.download(url,file_name)

    print "\n Downloaded file: " + downloaded