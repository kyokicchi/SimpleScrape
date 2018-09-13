
# coding: utf-8

# In[34]:



def SimpleSpider(orders,recipe,output):
    import requests
    import lxml.html
    f = open(orders, 'r')
    dump= f.read()
    f.close()
    l_url = dump.split('\n')
    l_out = []
    for url in l_url:
        if url != '':
            response = requests.get(url)
            html = lxml.html.fromstring(response.content)
            l_res = []
            l_res = html.xpath(recipe)
            l_out.extend(l_res)

    csv_out = "\n".join(l_out)
    f = open(output, 'w')
    f.write(csv_out)
    f.close()


# In[27]:



orders = 'target.txt'
recipe = '//a[contains(@href, "entry") and (starts-with(@href,"http://") or starts-with(@href,"https://"))]/@href'
output = 'results.csv'

#SimpleSpider(orders,recipe,output)


# In[36]:



orders = 'minilist.txt'
recipe = '//*[@class ="entry-content"]/p/descendant::text()'
output = 'mini.csv'

SimpleSpider(orders,recipe,output)


# In[30]:


import pandas as pd
df = pd.read_csv('results.csv', header=None)
df = df.drop_duplicates()
df = df[df[0].str.contains('//www.sakunori')]
df.describe()
df.to_csv('results.csv', header=False, index=False)

