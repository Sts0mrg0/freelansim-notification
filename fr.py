import time
import winsound
import requests
import bs4

already = ""
url = 'https://freelansim.ru/tasks'
headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0' }

while True:
    try:
        r = requests.get(url, headers = headers).text
    except:
        r = ""
        
    b = bs4.BeautifulSoup(r,'lxml')
    title_ = b.find("li", class_="content-list__item")
    title_task = title_.article.div.header.div.a.text
    if  title_task != already: # уже существует?
        already = title_task
        print("Заголовок: {}\nЦена: {}\nСсылка: {}".format(title_task,title_.article.aside('span')[1].text,"https://freelansim.ru"+(title_.article.div.header.div.a.get("href")))+'\r',end='\n\n')
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
    time.sleep(20) # задержка
