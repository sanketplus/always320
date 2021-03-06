try:
    from urllib.request import urlopen
    from urllib.parse import quote
except Exception as e:
    from urllib import urlopen
    from urllib import quote

try:
    from BeautifulSoup import BeautifulSoup
except Exception as e:
    from bs4 import BeautifulSoup



def get_results(query):
    """ Get YouTube search results
    Args:
        query: search term
    Returns:
        results: A list of dictionaries in format of {'title':<title>,'link':<yt_link>,
                                                    'uploader':<uploader>,'views':<views>}
    """
    url = "https://www.youtube.com/results?search_query=" + quote(query)
    res = urlopen(url)
    html = res.read()
    soup = BeautifulSoup(html)

    videos = soup.findAll(attrs={'class': 'yt-lockup-content'})
    results = []

    for v in videos:
        try:
            a_song = v.findAll('a')[0]
            title = a_song.get('title')
            link = "https://youtube.com" + a_song.get('href')
            uploader = v.findAll('a')[1].getText()
            views = v.findAll(attrs={'class': 'yt-lockup-meta-info'}).pop().findAll('li')[1].getText()

            results.append({'title':title,'link': link,'uploader': uploader,'views': views})
        except:
            continue

    return results
