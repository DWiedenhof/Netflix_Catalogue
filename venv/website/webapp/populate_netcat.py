import os
import requests
from lxml import html
import pandas as pd
import django

# requests + lxml
page = requests.get('https://www.netflix-nederland.nl/aanbod-netflix-nederland/')
tree = html.fromstring(page.content)

table = tree.xpath('//tr')

# find headers
col=[]
i=0
for t in table[0]:
    i+=1
    header = t.text_content()
    col.append((header, []))

# extract data and import into dataframe
for j in range(1, len(table)):
    row = table[j]

    if len(row) > 5:
        break
    i = 0

    for t in row.iterchildren():
        data = t.text_content()
        col[i][1].append(data)

        i+=1

Dict={header:column for (header,column) in col}
df = pd.DataFrame(Dict)

def add_title(name, genre, year, imdb, date_added):
        title = Movies.objects.get_or_create(name=name, genre=genre, year=year, imdb=imdb, date_added=date_added)
        return title

def populate():

    for row, i in enumerate(df['Titel']):
        add_title(name=df['Titel'][row],
        genre=df['Genre'][row],
        year=df['Jaar'][row],
        imdb=df['IMDb *'][row],
        date_added=df['Nieuw op:'][row])

if __name__ == '__main__':
    print ("Starting database population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')
    django.setup()
    from netcat.models import Movies
    populate()
