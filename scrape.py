from urllib.request import urlopen
from bs4 import BeautifulSoup

teams = [line.rstrip('\n') for line in open('teams.txt')]
for team in teams:

	response = urlopen('http://www.spotrac.com/nba/'+team+'/cap')
	content = response.read()
	soup = BeautifulSoup((content), 'html.parser')
	tabla = soup.find('tbody')
	data = []
	for link in tabla.find_all('tr'):
		player = []
		for aaa in link.find_all('td'):
		
			if(aaa.a):
				player.append(aaa.a.getText())
				continue
			player.append(aaa.getText())
		data.append(player)
	f = open(('teams/'+team+'.txt'), 'w') 
	for player in data:
		string = ''
		for cell in player:
			string = string + cell + '\t'
		f.write(string+'\n')

