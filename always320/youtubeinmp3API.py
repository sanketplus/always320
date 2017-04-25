try:
    from urllib.request import urlopen
    from urllib.parse import unquote
except Exception as e:
    from urllib import urlopen
    from urllib import unquote

import json
from robobrowser import RoboBrowser

def get_mp3_url(yt_url):
    response = urlopen("http://www.youtubeinmp3.com/fetch/?format=JSON&video="+str(yt_url))
    data = response.read()
    j = json.loads(data)

    return (j['link'],j['title']+".mp3")


def dirty_get_mp3_url(yt_url):
    browser = RoboBrowser(history=True)
    browser.open("http://www.youtubeinmp3.com/")
    form = browser.get_form(id="form")
    form["video"].value = yt_url
    browser.submit_form(form)

    a = browser.get_link(id="download")
    browser.follow_link(a)
    return (browser.url,unquote(browser.url.split("t=")[-1])+".mp3")