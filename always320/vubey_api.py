import mechanize
import BeautifulSoup

def get_mp3_url(yt_url):
    b = mechanize.Browser()
    b.open("https://vubey.yt")
    b.select_form('wf-form-signup-form')
    b.form['videoURL'] = yt_url
    fs = b.submit()
    d = fs.get_data()

    bs = BeautifulSoup.BeautifulSoup(d)
    links = bs.findAll("a")

    link = [l for l in links if "here" in l]
    url = link[0].get("href")
    return url
