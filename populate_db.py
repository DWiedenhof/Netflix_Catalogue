import requests
from lxml import html

# requests + lxml
page = requests.get('https://www.netflix-nederland.nl/aanbod-netflix-nederland/')
tree = html.fromstring(page.content)

table = tree.xpath('//tr')
[len(t) for t in table[:]]

# find headers
col=[]
i=0
for t in table[0]:
    i+=1
    header = t.text_content()
    print('%d:"%s"' %(i, header))
    col.append((header, []))

# extract data and import into dataframe
for j in range(1, len(table)):
    row = table[j]

    if len(row) > 5:
        break
    i = 0

    for t in row.iterchildren():
        data = t.text_content()
        # if i > 0:
        #     try:
        #         data = float(data)
        #     except:
        #         pass
        col[i][1].append(data)

        i+=1

[len(C) for (header, C) in col]

Dict={header:column for (header,column) in col}
df = pd.DataFrame(Dict)
df = df.rename(columns = {"Titel": "name",
                         "Genre": "genre",
                         "Jaar": "year",
                         "IMDb" : "imdb",
                         "Nieuw op:": "date_added"})