import bs4  # http://beautiful-soup-4.readthedocs.io/en/latest/#making-the-soup
import requests  # http://docs.python-requests.org/en/master/user/quickstart/
res = requests.get('https://twitter.com/search?l=&q=%23kf2Calc%20from%3ATor_kcWebDev&src=typd&lang=en')

res.raise_for_status() # tells us if we dun goof'd

soup = bs4.BeautifulSoup(res.text, 'html.parser')

elems = soup.select('p.tweet-text')
