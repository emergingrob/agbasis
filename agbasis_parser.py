from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
	
	try:
		with closing(get(url, stream=True)) as resp:
			if is_good_response(resp):
				return resp.content
			else:
				return None

	except RequestsExcception as e:
		log_error('Error during request to {0} : {1}'.format(url, str(e)))
		return None

def is_good_response(resp):
	content_type = resp.headers['Content-Type'].lower()
	return (resp.status_code == 200
			and content_type is not None
			and content_type.find('html') > -1)

def log_error(e):
	print(e)

iowa_html = simple_get('https://www.iowaagriculture.gov/agMarketing/dailyGrainPrices.asp')
html = BeautifulSoup(iowa_html, 'html.parser')

for span in html.find_all('Yellow Corn'):
		print (span)