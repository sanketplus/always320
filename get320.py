import mechanize
import BeautifulSoup


def main():
    # query
    # url = youtube_search(query)
    # link = get_link(url)
    # =>>>>>>>#SERVICE-SELECTION get_html_service-name(url)
    # =>>> get_link(html,look)
    # path = wget(link)
    # picard?

    b = mechanize.Browser()
    b.select_form('wf-form-signup-form')
    b.form['videoURL'] = raw_input("URL:")
    fs = b.submit()
    d = fs.get_data()

    bs = BeautifulSoup.BeautifulSoup(d)
    links = bs.findAll("a")

    link = [l for l in links if "here" in l]
    url = link[0].get("href")

    print url

if __name__ == "__main__":
    main()
