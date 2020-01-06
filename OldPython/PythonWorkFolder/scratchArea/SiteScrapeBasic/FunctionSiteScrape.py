# doesn't work with twitter because javascript is disabled

import bs4, requests

def fuckTwitter(url):
  res = requests.get(url)
  res.raise_for_status() # tells us if we dun goof'd

  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  elems = soup.select('p')
  return elems[0].text

price = fuckTwitter('https://twitter.com/search?l=&q=%23kf2Calc%20from%3ATor_kcWebDev&src=typd&lang=en')

print('output ' + price)