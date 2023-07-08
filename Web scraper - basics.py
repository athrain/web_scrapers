from urllib.request import urlopen
from bs4 import BeautifulSoup

from urllib.error import HTTPError #to handle errors with HTML page
from urllib.error import URLError #to handle error when there is no connection to the server


#html = urlopen('http://www.pythonscraping.com/pages/page1.html')
#html = urlopen('https://nofluffjobs.com/pl/job/senior-azure-devops-engineer-xebia-remote')

html = urlopen('https://nofluffjobs.com/pl/Java?page=1')


bs = BeautifulSoup(html.read(), 'html.parser')

object = 'head'

#print(bs.h1) #prints only H1
print(bs)

# below - some line to see the errors while loading a page
# try:
#  html = urlopen('https://pythonscrapingthisurldoesnotexist.com')
# except HTTPError as e:
#  print(e)
# except URLError as e:
#  print('The server could not be found!')
# else:
#  print('It Worked!')