import requests
from requests.auth import HTTPBasicAuth
allstring = 'IMAGINABLE IMAGINABLY IMAGININGS IMAGINISTS IMBALANCED IMBALANCES IMBECILELY IMBECILITY IMBIBITION IMBITTERED IMBOLDENED IMBORDERED IMBOSOMING IMBOWERING IMBRANGLED IMBRANGLES IMBRICATED IMBRICATES IMBROCCATA IMBROGLIOS IMBROWNING IMBRUEMENT IMBUEMENTS IMIDAZOLES IMINAZOLES IMINOUREAS IMIPRAMINE IMITANCIES IMITATIONS IMMACULACY IMMACULATE IMMANACLED IMMANACLES IMMANATION IMMANENCES IMMANENTAL IMMANENTLY IMMANITIES IMMANTLING IMMATERIAL IMMATURELY IMMATURITY IMMEASURED IMMEMORIAL IMMERGENCE IMMERITOUS IMMERSIBLE IMMERSIONS IMMIGRANTS IMMIGRATED IMMIGRATES IMMIGRATOR IMMINENCES IMMINENTLY IMMINGLING IMMINUTION IMMISCIBLE IMMISCIBLY IMMISERISE IMMISERIZE IMMISSIONS IMMITTANCE IMMIXTURES IMMOBILISE IMMOBILISM IMMOBILITY IMMOBILIZE IMMODERACY IMMODERATE IMMODESTLY IMMOLATING IMMOLATION IMMOLATORS IMMORALISM IMMORALIST IMMORALITY IMMORTALLY IMMORTELLE IMMOTILITY IMMOVABLES IMMOVEABLE IMMOVEABLY IMMUNISERS IMMUNISING IMMUNITIES IMMUNIZERS IMMUNIZING IMMUNOBLOT IMMUNOGENS IMMUNOLOGY IMMUREMENT IMPACTIONS IMPACTITES IMPAINTING IMPAIRABLE IMPAIRINGS IMPAIRMENT IMPALEMENT IMPALPABLE IMPALPABLY IMPALUDISM IMPANATION IMPANELING IMPANELLED IMPARADISE IMPARITIES IMPARLANCE IMPARTABLE IMPARTIBLE IMPARTIBLY IMPARTMENT IMPASSABLE IMPASSABLY IMPASSIBLE IMPASSIBLY IMPASSIONS IMPATIENCE IMPEACHERS IMPEACHING IMPEARLING IMPECCABLE IMPECCABLY IMPECCANCY IMPEDANCES IMPEDIMENT IMPEDINGLY IMPEDITIVE IMPELLENTS IMPENDENCE IMPENDENCY IMPENITENT IMPERATIVE IMPERATORS IMPERFECTS IMPERIALLY IMPERILING IMPERILLED IMPERSONAL IMPERVIOUS IMPETRATED IMPETRATES IMPETRATOR IMPICTURED IMPISHNESS IMPLACABLE IMPLACABLY IMPLANTERS IMPLANTING IMPLEACHED IMPLEACHES IMPLEADERS IMPLEADING IMPLEDGING IMPLEMENTS IMPLETIONS IMPLEXIONS IMPLEXUOUS IMPLICATED IMPLICATES IMPLICITLY IMPLODENTS IMPLORATOR IMPLOSIONS IMPLOSIVES IMPLUNGING IMPOCKETED IMPOLDERED IMPOLICIES IMPOLITELY IMPOLITEST IMPORTABLE IMPORTANCE IMPORTANCY IMPORTINGS IMPORTUNED IMPORTUNER IMPORTUNES IMPOSINGLY IMPOSITION IMPOSSIBLE IMPOSSIBLY IMPOSTHUME IMPOSTROUS IMPOSTUMED IMPOSTUMES IMPOSTURES IMPOTENCES IMPOTENTLY IMPOUNDAGE IMPOUNDERS IMPOUNDING IMPOVERISH IMPOWERING IMPRECATED IMPRECATES IMPREGNANT IMPREGNATE IMPREGNING IMPRESARIO IMPRESSERS IMPRESSING IMPRESSION IMPRESSIVE IMPRESSURE IMPRIMATUR IMPRINTERS IMPRINTING IMPRISONED IMPRISONER IMPROBABLE IMPROBABLY IMPROMPTUS IMPROPERLY IMPROVABLE IMPROVABLY IMPROVISED IMPROVISER IMPROVISES IMPROVISOR IMPRUDENCE IMPSONITES IMPUDENCES IMPUDENTLY IMPUDICITY IMPUGNABLE IMPUGNMENT IMPUISSANT IMPULSIONS IMPUNDULUS IMPUNITIES IMPURENESS IMPURITIES IMPURPLING IMPUTATION IMPUTATIVE'
words = allstring.split(' ')

first = [1]
second = [0, 8, 4, 5]
third = [5, 3]
fourth = [7] # dirk gave the 7 away
fifth = [8, 2]
sixth = [2, 4, 5]
words = []
for i in first:
	for j in second:
		for k in third:
			for l in fourth:
				for m in fifth:
					for n in sixth:
						word = str(i) + str(j) + str(k) + str(l) + str(m) + str(n) 
						words.append(word)


base_url = 'http://notpron.org/notpron/bummel/'
username = 'jingle'
password = 'bells'
word = 'immediately'
theurl = '%s%s.htm' %(base_url, word.lower())
r=requests.get(theurl, auth=HTTPBasicAuth(username, password))
print(r)

for word in words:
	# print(word.lower())
	theurl = '%s%s.htm' %(base_url, word.lower())
	print(theurl)

	r=requests.get(theurl, auth=HTTPBasicAuth(username, password))
	print(r)

exit()

import requests
from requests.auth import HTTPBasicAuth
from PIL import Image
from io import BytesIO
import hashlib

from collections import Counter

# words = ['a', 'b', 'c', 'a']

# Counter(words).keys() # equals to list(set(words))
# Counter(words).values()

startTime = 1098928800 - 3600

theurl= 'http://www.deathball.net/notpron/love/pic.php?time=1098932400'
username = 'batman'
password = 'turkey'
tmp = []
for i in range(504):
	startTime += 3600

	theurl = 'http://www.deathball.net/notpron/love/pic.php?time=%s' %startTime

	r=requests.get(theurl, auth=HTTPBasicAuth(username, password))
	img = Image.open(BytesIO(r.content))

	curhash = str(hashlib.md5(r.content))
	print('%s_%s' %(curhash,startTime))
	tmp.append(curhash)
	if '0x00000208EFC91D00' in tmp[-1]:
		print(startTime)
		img.save("C:\\Users\\rensm\\Desktop\\imuniuqe%d.jpg" %startTime)

	if '0x00000208EFDC9D50' in tmp[-1]:
		print(startTime)
		img.save("C:\\Users\\rensm\\Desktop\\imuniuqe%d.jpg" %startTime)

# print(Counter(tmp).keys()) # equals to list(set(words))

# print(Counter(tmp).values())

print(Counter(tmp))


	# img.save("C:\\Users\\rensm\\Desktop\\lvl61%s.jpg" %startTime)
# print(r.content)
exit()

import re
import requests
from bs4 import BeautifulSoup
import os
import urllib.request
import requests
from requests.auth import HTTPBasicAuth
# import urllib

# import urllib2

site = 'http://www.deathball.net/notpron/love/main.php'
# picString = 
startTime = 1098928800 - 3600

# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
username = 'batman'
password = 'turkey'

# If we knew the realm, we could use it instead of None.
top_level_url = site
password_mgr.add_password(site, top_level_url, username, password)

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)

# use the opener to fetch a URL
# opener.open('http://www.deathball.net/notpron/love/pic.php?time=1098932400')

# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)


for i in range(503):

	startTime += 3600

	url = 'http://www.deathball.net/notpron/love/pic.php?time=%s' %startTime
	urllib.request.urlretrieve(url, "%s.jpg" %startTime, auth=HTTPBasicAuth(username, password))	
	# with open(url, 'wb') as f:
	# 	response = requests.get(url)
	# 	f.write(response.content)

exit()
urllib.urlretrieve(url, os.path.basename(url))

'http://www.deathball.net/notpron/love/pic.php?time=1098932400'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('pic.php?')

urls = [img['src'] for img in img_tags]

print(urls)
for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the site variable atm. 
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)