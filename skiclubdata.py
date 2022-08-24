import requests
from bs4 import BeautifulSoup
from csv import writer
import time



"""
with open('skiclubV0.99.csv', "w", encoding="utf8", newline="") as f:
    thewriter = writer(f)
    header = ["name" , "address"]
    thewriter.writerow(header) 

    soup = BeautifulSoup(page.text, "lxml")
    lists = soup.findAll("div", class_="accordion club")
    for list in lists:
        #id = soup.find_all("span", class_="span1 numClub")
        phone = soup.find_all("span", class_="span1 numClub").soup.find_all("div", {"class":"span6"})
        email = soup.find_all("dd") [2].
        for div in id:
            print(phone)
        
            #thewriter.writerow([span.text , email + "\n"])
"""

#this one works
url ="http://www.ffs.fr/federation/clubs/recherche-de-club?num_page=1"
page = requests.get(url)
if page.ok:
    soup = BeautifulSoup(page.text, "lxml")
    id = soup.find_all("span", {"class":"numClub"})
    email = soup.find("dl", {"class":"dl-horizontal essentiel"}).find_all_next("dd") [2].text
    for span in id:
        print(span.text + email)
        


"""
url ="http://www.ffs.fr/federation/clubs/recherche-de-club?num_page=1"
page = requests.get(url)

if page.ok:
    soup = BeautifulSoup(page.text, "lxml")
    id = soup.find_all("span", class_="span1 numClub")
    for span in id:
        print(id.text)
"""