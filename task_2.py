import requests
from bs4 import BeautifulSoup

data = {}


def main():
    url = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F%3A%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
    get_names(url)
    sorted_data = dict(sorted(data.items(), key=lambda x: x[0]))

    for i, k in sorted_data.items():
        print(f'{i}: {k}')


def get_names(url):
    while True:
        req = requests.get(url).text
        soup = BeautifulSoup(req, 'lxml')
        names = soup.find('div', class_='mw-category-columns').find_all('a')
        for name in names:
            first_char = name.text[0]
            if first_char in data.keys():
                data[first_char] += 1
            else:
                data[first_char] = 1
        if soup.find('div', id='mw-pages').find_all('a')[-1].string == 'Следующая страница':
            url = 'https://ru.wikipedia.org' + soup.find('div', id='mw-pages').find_all('a')[-1].get('href')
        else:
            break


if __name__ == '__main__':
    main()
