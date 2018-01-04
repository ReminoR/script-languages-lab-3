from bs4 import BeautifulSoup
import	requests

url = 'http://3dtoday.ru/'
site = requests.get(url).text

soup = BeautifulSoup(site, 'html.parser')

title = soup.select('#new .post_list .post_list_item_title span a')
autor = soup.select('#new .post_list .post_list_item_autor a')
date = soup.select('#new .post_list .post_list_item_date')
desc = soup.select('#new .post_list .post_list_item_text')

with open('info.html', 'a') as file:
	for i in range(len(title)):
		file.write('<div class="block">')
		file.write('<strong>Заголовок: </strong>' + title[i].get_text() + '<br>')
		file.write('<strong>Автор: </strong>' + autor[i].get_text() + '<br>')
		file.write('<strong>Дата: </strong>' + date[i].get_text() + '<br>')
		file.write('<strong>Описание: </strong>' + desc[i].get_text() + '<br>')
		file.write('</div><br>')
	file.close()