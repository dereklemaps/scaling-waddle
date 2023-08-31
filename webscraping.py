# WEBSCRAPING - GRAB TEXT FROM HTML TAG
import requests
import bs4
res = requests.get('https://example.com/')
soup = bs4.BeautifulSoup(res.text, 'lxml')
h1_tag = soup.select('h1') # grab h1 tag
print(h1_tag[0].getText()) # print out text from tag

# WEBSCRAPING - CHEAP BOOKS < 12
url = 'https://books.toscrape.com/catalogue/page-{}.html'
cheaper_books = {}
for i in range(1,51):
    res = requests.get(url.format(i))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')
    for book in books:
        if float(book.select('.price_color')[0].getText()[2:]) < 12.00:
            cheaper_books[(book.select('a')[1]['title'])] = float(book.select('.price_color')[0].getText()[2:])
print(cheaper_books)

# WEBSCRAPING - FILTER FOR LARGE COUNTRY AREA
res = requests.get('https://www.scrapethissite.com/pages/simple')
soup = bs4.BeautifulSoup(res.text, 'lxml')
areas = soup.select('.col-md-4.country')
large_country_area = {}
for country in areas:
    country_name = country.select('h3')[0].get_text().strip()
    country_area = float(country.select('.country-area')[0].getText())
    if country_area > 1000000:
        large_country_area[country_name] = country_area
print(large_country_area)

# WEBSCRAPING - FILTER FOR SMALL COUNTRY POPULATION
res = requests.get('https://www.scrapethissite.com/pages/simple/')
soup = bs4.BeautifulSoup(res.text, 'lxml')
all_countries = soup.select('.col-md-4.country')
low_pop_countries = {}
for country in all_countries:
    country_pop = int(country.select('.country-population')[0].getText())
    country_name = country.select('h3')[0].getText().strip()
    if country_pop < 50000:
        low_pop_countries[country_name] = country_pop
print(low_pop_countries)

# WEBSCRAPING - ALL WINNING NHL RECORDS
winning_teams = []
for i in range(1,25):
    base_url = f'https://www.scrapethissite.com/pages/forms/?page_num={i}'
    res = requests.get(base_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    teams = soup.select('.team')
    for team in teams:
        if team.select('.pct.text-success'):
            win_percent = float(team.select('.pct.text-success')[0].getText())
            year = int(team.select('.year')[0].getText())
            team_name = team.select('.name')[0].getText().strip()
            winning_teams.append([year, team_name, win_percent])
print(winning_teams)

# WEBSCRAPING - BEST NHL RECORD BY YEAR
best_teams = {}
current_high = 0.0
for i in range(1,25):
    base_url = f'https://www.scrapethissite.com/pages/forms/?page_num={i}'
    res = requests.get(base_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    teams = soup.select('.team')
    for team in teams:
        if team.select('.pct.text-success'):
            win_percent = float(team.select('.pct.text-success')[0].getText())
            year = int(team.select('.year')[0].getText())
            team_name = team.select('.name')[0].getText().strip()
            if year in best_teams.keys():
                if win_percent > current_high:
                    best_teams[year] = [win_percent, team_name]
                    current_high = win_percent
                elif win_percent == current_high:
                    best_teams[year].extend([team_name])
            else:
                current_high = 0.0
                if win_percent > current_high:
                    best_teams[year] = [win_percent, team_name]
                    current_high = win_percent
print(best_teams)