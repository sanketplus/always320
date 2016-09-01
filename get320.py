import mechanize, BeautifulSoup

b=mechanize.Browser()
b.open("https://vubey.yt")
b.select_form('wf-form-signup-form')
b.form['videoURL']=raw_input("URL:")
fs=b.submit()
d=fs.get_data()

bs=BeautifulSoup.BeautifulSoup(d)
links = bs.findAll("a")

link = [l for l in links if "here" in l]
url = link[0].get("href")

print url 
