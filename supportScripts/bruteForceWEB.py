import requests
from requests.auth import HTTPBasicAuth
from PIL import Image
from io import BytesIO
import hashlib
import time
from collections import Counter

# fourLetterWords.txt

with open('fourLetterWords.txt', 'r') as file:
	
	wordList = file.read()

wlist = wordList.split('\n')

# # 6 letter words with bef
# words = 'begulf, behalf, behoof, belfry, belief, bereft, baffed, baffle, baffed, baffle, barfed, beefed, befell, beflea, before, befret, beefed, belief, bereft, biface, biffed, biflex, biffed, bouffe, bouffe, briefs, buffed, buffer, buffet, buffed, buffer, buffet, feeble, feebly, ferbam, fabled, fabler, fables, feeble, feebly, feeble, fibers, fibbed, fibber, fibres, fibbed, fibber, fimble, flambe, fobbed, fobbed, foible, forbye, foreby, fubbed, fubbed, fumble, prefab, rebuff, rebuff, webfed, webfed'
# # 4 letter words with be
# words = 'bead, beak, beam, bean, bear, beat, beau, beck, beds, bedu, beef, been, beep, beer, bees, beet, begs, bell, bels, belt, bema, bend, bene, bens, bent, berg, berk, berm, best, beta, beth, bets, bevy, beys, babe, bade, bake, bale, bane, bare, base, bate, beef, been, beep, beer, bees, beet, bene, bier, bice, bide, bike, bile, bine, bise, bite, bize, bleb, bled, blet, blew, blae, blue, bode, bole, bone, bore, bred, bree, bren, brew, brae, bree, brie, bute, byes, byre, byte, ebbs, ebon, ebbs, abed, abet, abbe, able, abye, abbe, babe, bleb, cube, debs, debt, gibe, gybe, hebe, herb, hebe, ibex, jibe, jube, kerb, kibe, lobe, lube, mabe, nebs, nabe, obes, obey, oboe, pleb, rebs, robe, rube, sabe, tube, unbe, verb, vibe, webs, zebu'
# # 5 letter words with bef
# wlist5bef = ["befit","befog","beefs","beefy","beefs","beefy","brief","fable","fiber","fibre"]
# # 5 letter words with be
# words = 'beach, beads, beady, beaks, beaky, beams, beamy, beano, beans, beard, bears, beast, beats, beaus, beaut, beaux, bebop, becap, becks, bedel, bedew, bedim, beech, beefs, beefy, beeps, beers, beery, beets, befit, befog, began, begat, beget, begin, begot, begum, begun, beige, beigy, being, belay, belch, belga, belie, belle, bells, belly, below, belts, bemas, bemix, bench, bends, bendy, benes, benne, benni, benny, bento, bents, beret, bergs, berme, berms, berry, berth, beryl, beset, besom, besot, bests, betas, betel, beths, beton, betta, bevel, bevor, bewig, bezel, bezil, baaed, babel, babes, badge, bagel, baize, baked, baker, bakes, baled, baler, bales, baned, banes, bared, barer, bares, barbe, barde, barge, barre, barye, based, baser, bases, baste, bated, bates, bathe, bayed, beech, beefs, beefy, beeps, beers, beery, beets, bedel, bedew, beget, beige, belie, belle, benes, benne, beret, berme, beset, betel, bevel, bezel, bield, biers, bible, bicep, bices, bided, bider, bides, bidet, biked, biker, bikes, bikie, biles, bilge, bines, binge, biome, biped, birle, birse, bises, biter, bites, bizes, bleak, blear, bleat, blebs, bleed, bleep, blend, blent, bless, blest, blets, blade, blame, blare, blase, blate, blaze, bleed, bleep, blite, bloke, blued, bluer, blues, bluet, bluey, blume, blype, bocce, boche, boded, bodes, bogey, bogie, bogle, bohea, boite, bokeh, boles, bombe, boned, boner, bones, boney, bonne, bonze, booed, booze, bored, borer, bores, borne, botel, boule, bouse, bowed, bowel, bower, bowse, boxed, boxer, boxes, bread, break, bream, brede, breed, brees, brens, brent, breve, brews, braes, brace, brake, brave, braze, breed, brees, brede, breve, brief, brier, bries, bribe, bride, brine, broke, brome, brose, brume, brute, budge, bugle, bulge, buret, burke, burse, bused, buses, buteo, butle, butte, buyer, byres, bytes, ebbed, ebbet, ebola, ebons, ebony, ebook, ebbed, ebbet, elbow, embar, embay, embed, ember, embow, exurb, abeam, abele, abets, abase, abate, abbes, abbey, abele, abide, abled, abler, ables, abode, above, abuse, abyes, abbes, abbey, acerb, adobe, amber, amble, ameba, ardeb, bebop, babel, babes, barbe, bible, blebs, bombe, bribe, cebid, ceiba, celeb, caber, cable, celeb, coble, combe, cubeb, cubed, cuber, cubes, cubeb, cyber, debar, debit, debts, debug, debut, debye, demob, derby, daube, debye, dobie, dweeb, dweeb, ebbed, ebbet, ebbed, ebbet, embed, ember, fable, fiber, fibre, gable, gambe, gibed, giber, gibes, gleba, glebe, glebe, globe, grebe, grebe, gybed, gybes, hebes, herbs, herby, hebes, imbed, imbue, inbye, jebel, jambe, jebel, jibed, jiber, jibes, jubes, kebab, kebar, kebob, kebab, kebob, kerbs, kibei, kibes, kibbe, kibbe, leben, label, leben, libel, liber, lobed, lobes, lubed, lubes, mabes, maybe, nabes, noble, obeah, obeli, obese, obeys, obese, objet, oboes, obole, omber, ombre, orbed, plebe, plebs, plebe, probe, pubes, rebar, rebbe, rebec, rebel, rebid, rebop, rebus, rebut, rebuy, rebbe, redub, rehab, rebec, rebel, rebbe, rebbe, ribes, robed, robes, roble, rubes, ruble, sebum, sabed, saber, sabes, sable, sabre, sober, suber, taber, tabes, table, thebe, thebe, tribe, tubed, tuber, tubes, tubae, umbel, umber, upbye, verbs, vibes, webby, weber, webby, weber, xebec, xebec, yerba, zebec, zebra, zebus, zebec, zibet, zineb'

# wlist = words.split(', ')#.sort()
# wlist = list(set(wlist))
# wlist.sort()
# exit()



theurl= 'http://notpron.org/notpron/jerk2/nose/'
username = 'rensm'
password = 'Ahx6efav'
test = 'triceratops'

for i, w in enumerate(wlist):

	if i% 100 == 0:
		print('i = %s' %i)
		r=requests.head(theurl + test + '.php', auth=HTTPBasicAuth(username, password))
		if not '200' in str(r):
			print(r)
			print('THROTLED')
			exit()

	# r=requests.get(theurl + w + '.php', auth=HTTPBasicAuth(username, password))
	r=requests.head(theurl + w.lower() + '.php', auth=HTTPBasicAuth(username, password))
	if not '404' in str(r):
		print(r)
		print('word = %s: %s' %(w,r))
	# time.sleep(5)

exit()

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