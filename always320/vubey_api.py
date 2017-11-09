try:
    # Python 2
    from BeautifulSoup import BeautifulSoup
except Exception as e:
    # Python 3
    from bs4 import BeautifulSoup

def get_mp3_url(yt_url):
    try:
        import mechanize
    except Exception as e:
        raise e
    b = mechanize.Browser()
    b.open("https://vubey.yt")
    b.select_form('wf-form-signup-form')
    b.form['videoURL'] = yt_url
    fs = b.submit()
    d = fs.get_data()

    bs = BeautifulSoup(d)
    links = bs.findAll("a")

    link = [l for l in links if "here" in l]
    url = link[0].get("href")
    return (url,url.split('/')[-1])

