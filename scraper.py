import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import os

# The website categories
category = [ 'wissenschaft', 'kultur', 'geschichte']

# Create a dictionary for articles
my_dict={}
# Number of pages that will be scraped for every categotry
MAX_PAGES =500
# Indexing the articles
article_num = 1

for cat in category:
    for page in tqdm(range(1,MAX_PAGES)): 
        url = "https://www.spiegel.de/{}/p{}".format(cat,page)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        articles = soup.select('article') # select all articles
        for a in articles:
            # Select the articles' titles from attribute 'aria-label'
            my_dict[article_num]={"title":a.get('aria-label')}
            
            # Select the articles' summary from class 'leading-loose'
            my_dict[article_num].update({"text":"".join([x.text.strip()
                                                            for x in a.select('.leading-loose')])
                                        })
            # Add the category
            my_dict[article_num].update({"category":cat})
            
            # index' Increment  
            article_num +=1


print(my_dict)




       
  
df = pd.DataFrame.from_dict(data=my_dict, orient='index')
    # Drop duplicate articles
df2 = df.drop_duplicates(subset='title', keep='first')
    # Save as csv as utf-16 due to spicial German charachters
df2.to_csv('DerSpiegel2.csv', index=False, encoding = 'utf-8')