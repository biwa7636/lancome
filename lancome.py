from bs4 import BeautifulSoup
myurl = 'http://www.lancome-usa.com/skincare-cleanse/skincare-cleanse,default,sc.html'

# 1. urllib2
import urllib2
r = urllib2.urlopen(myurl)
soup = BeautifulSoup(r)
print 'MOUSSE RADIANCE' in soup.text.encode('utf-8').upper()
print '$32.00' in soup.text.encode('utf-8')

print '------------------------------------------------------'

# 2. requests
import requests
r = requests.get(myurl)
soup = BeautifulSoup(r.text)
print 'MOUSSE RADIANCE' in soup.text.encode('utf-8').upper()
print '$32.00' in soup.text.encode('utf-8')

#
#
#products = soup.find_all('div', {'class':re.compile('product-tile')})
#
#print len(products)
#for product in products:
#    try:
#        name = product.find('div', {'class':'product-name'}).text.encode('utf-8').strip()
#        description = product.find('div', {'class':'productdescription'}).text.encode('utf-8').strip()
#        pricing = product.find('span', {'class':'product-sales-price'}).text.encode('utf-8').strip()
#        rating = product.find('div', {'class':'productTile-rating'}).find('img')['src'].split('/')[-1].strip()
#        print '|'.join([name, pricing, rating, description])
#    except:
#        pass