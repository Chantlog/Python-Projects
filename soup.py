import bs4, requests

res = requests.get('https://nostarch.com')
res.raise_for_status()

noStarchSoup = bs4.BeautifulSoup(res.text,'html.parser')

elems = noStarchSoup.select('#block-uc-cart-cart > table > tbody > tr > td.cart-block-summary-items')
print(len(elems))
print(elems[0].getText())