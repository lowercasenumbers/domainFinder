import requests
import json

def getThreatCrowd(domain):
	url = 'https://www.threatcrowd.org/searchApi/v2/domain/report/?domain=' + str(domain)
	r = requests.get(url)
	domains = []	


	# Need to Decode Json
	results = json.loads(r.content)
	domains = results['subdomains']	
		
	return domains
