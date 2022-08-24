# githubSKICLUB
webscraping a skiclub website

url ="http://www.ffs.fr/federation/clubs/recherche-de-club?num_page=1"
page = requests.get(url)
if page.ok:
    soup = BeautifulSoup(page.text, "lxml")
    id = soup.find_all("span", {"class":"numClub"})
    email = soup.find("dl", {"class":"dl-horizontal essentiel"}).find_all_next("dd") [2].text
    for span in id:
        print(span.text + email)
