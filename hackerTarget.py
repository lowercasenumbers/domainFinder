import requests
def getHackerTarget(domain):
	url = 'https://api.hackertarget.com/hostsearch/?q=' + str(domain)
	r = requests.get(url)
	domains = []	

	for line in r.iter_lines(decode_unicode=True):
		domain = line.split(',')
		domains.append(domain[0])
	
	print(*domains, sep="\n")
	return domains



