import requests
from bs4 import BeautifulSoup
import re
import os
import pandas as pd

class GeneralHarvestor:

    def extract_from_web(self, link):
        r = requests.get(link)
        c = r.content
        soup = BeautifulSoup(c, features="xml")
        # for script in soup(["script", "style"]):
        #     script.extract()

        text = soup.get_text()
        titles = soup.find_all('title')
        
        name = soup.find_all('name')
        data_id = soup.find_all('id')
        location = soup.find_all('location')
        revision_id = soup.find_all('revision-id')

        lists = []
        for n, l in enumerate(name):
            li = [l.text, data_id[n].text, location[n].text, revision_id[n].text]
            lists.append(li)

        df = pd.DataFrame(lists, columns=["Name", "Id", "Location", "Revision_id"])

        df.to_csv('file1.csv')
        return df

p1 = GeneralHarvestor()
print(p1.extract_from_web("https://cmr.earthdata.nasa.gov/search/collections?page-size=20"))