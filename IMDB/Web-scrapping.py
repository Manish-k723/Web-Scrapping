from bs4 import BeautifulSoup
import requests , openpyxl

excel = openpyxl.Workbook()


sheet = excel.active
sheet.title = 'IMDB top rated movies'
sheet.append(['Rank','Movie name','year of Release','IMDB Rating'])

try:
    source = requests.get('https://www.imdb.com/chart/top')
    source.raise_for_status() #This method tell us whether the url which we are using is valid or not. 
    
    soup = BeautifulSoup(source.text,'html.parser')
    
    movies = soup.find('tbody', class_ = 'lister-list').find_all('tr')
    
    for movie in movies:
        rank = movie.find('td', class_ = 'titleColumn').get_text(strip = True).split('.')[0]
        name = movie.find('td', class_ = 'titleColumn').a.text
        year = movie.find('td', class_ = 'titleColumn').span.text[1:-1]
        rating = movie.find('td', class_ = 'imdbRating').strong.text
        sheet.append([rank,name,year,rating])
    
    
except Exception as e:
    print(e)
#This is a good practice to use try and except module because it helps us in advance to validate our URL.
excel.save('IMDB Rating.xlsx')
