from mechanize import Browser
from bs4 import BeautifulSoup as BS
import json
 
br = Browser()
 
# Browser options
# Ignore robots.txt. Do not do this without thought and consideration.
br.set_handle_robots(False)
 
# Don't add Referer (sic) header
br.set_handle_referer(False)
 
# Don't handle Refresh redirections
br.set_handle_refresh(False)
 
#Setting the user agent as firefox
br.addheaders = [('User-agent', 'Firefox')]
 



for i in range(25):
    url = "https://www.amazon.com/s/ref=sr_pg_"+str(i)+"?rh=i%3Aaps%2Ck%3Aipad&page=2&keywords=smartphone&ie=UTF8&qid=1468456508&spIA=B003KGBD16,B01DM1N0NC"
    #print(url)
    br.open(url)
    # br.open('http://www.amazon.in/')
    # br.select_form(name="site-search")
    # br['field-keywords'] = "Ipad"
    #br.submit()
    
    #Getting the response in beautifulsoup
    soup = BS(br.response().read(), "html5lib")
        
    items = []


    for li in soup.find_all('li', class_="s-result-item"):
        items.append({})
        items[-1]['h2'] = li.find_all('h2')
        items[-1]['h2'] = items[-1]['h2'][0].string
        items[-1]['price'] = li.find_all('span',{"class":"a-color-price"})
        items[-1]['price'] = items[-1]['price'][0].string
        items[-1]['imgs'] = li.img['srcset']
        items[-1]['imgs'] = items[-1]['imgs'].split(',')

    f = open('products.json', 'a')
    f.write(json.dumps(items,sort_keys=True,indent=4, separators=(',', ': ')))
    f.close();
    print(i)

