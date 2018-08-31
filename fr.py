<<<<<<< HEAD
import time
import winsound
import requests
import bs4

alredy = []
url = 'https://freelansim.ru/tasks'
headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0' }

while True:
    try:
        r = requests.get(url, headers = headers).text
    except:
        r = ""
        
    b = bs4.BeautifulSoup(r,'lxml')
    title_task = b.find("li", class_="content-list__item")
    if alredy.count(title_task.article.div.header.div.a.text) == 0: # уже существует?
        alredy.append(title_task.article.div.header.div.a.text)
        print("Заголовок: {}\nЦена: {}\nСсылка: {}".format(title_task.article.div.header.div.a.text,title_task.article.aside('span')[1].text,"https://freelansim.ru"+(title_task.article.div.header.div.a.get("href")))+'\r',end='\n\n')
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
    time.sleep(20) # задержка
=======
import time
import winsound
import requests
import bs4

alredy = []
url = 'https://freelansim.ru/tasks'
headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0' }

while True:
    try:
        r = requests.get(url, headers = headers).text
    except:
        r = ""
        
    b = bs4.BeautifulSoup(r,'lxml')
    title_task = b.find("li", class_="content-list__item")
    if alredy.count(title_task.article.div.header.div.a.text) == 0: # уже существует?
        alredy.append(title_task.article.div.header.div.a.text)
        print("Заголовок: {}\nЦена: {}\nСсылка: {}".format(title_task.article.div.header.div.a.text,title_task.article.aside('span')[1].text,"https://freelansim.ru"+(title_task.article.div.header.div.a.get("href")))+'\r',end='\n\n')
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
    time.sleep(20) # задержка
>>>>>>> affb003fa30c39681e0751f73eb6e402d407a751
