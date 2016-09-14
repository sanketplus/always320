import mechanize
import BeautifulSoup

from downloader import wget_get
from parseyoutube import get_results

def main():
    # query
    # url = youtube_search(query)
    # link = get_link(url)
    # =>>>>>>>#SERVICE-SELECTION get_html_service-name(url)
    # =>>> get_link(html,look)
    # path = wget(link)
    # picard?
    query = raw_input("Song name:")
    print "parsing youtube..."

    results = get_results(query)
    choice = 0

    print "generating MP3 link..."

    b = mechanize.Browser()
    b.open("https://vubey.yt")
    b.select_form('wf-form-signup-form')
    b.form['videoURL'] = results[choice][1]
    fs = b.submit()
    d = fs.get_data()

    bs = BeautifulSoup.BeautifulSoup(d)
    links = bs.findAll("a")

    link = [l for l in links if "here" in l]
    url = link[0].get("href")

    print "link generated: " + url
    wget_get(url)


if __name__ == "__main__":
    main()
