import urllib
from BeautifulSoup import BeautifulSoup


def get_results(query):
    url = "https://www.youtube.com/results?search_query=" + urllib.quote(query)
    res = urllib.urlopen(url)
    html = res.read()
    soup = BeautifulSoup(html)

    videos = soup.findAll(attrs={'class': 'yt-lockup-content'})
    list = []

    for v in videos:
        try:
            a_song = v.findAll('a')[0]
            title = a_song.get('title')
            link = "https://youtube.com" + a_song.get('href')
            uploader = v.findAll('a')[1].getText()
            views = v.findAll(attrs={'class': 'yt-lockup-meta-info'}).pop().findAll('li')[1].getText()

            list.append((title, link, uploader, views))
        except:
            continue

    return list
