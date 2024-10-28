import requests
from bs4 import BeautifulSoup


def get_books(url):
    # Отправка HTTP-запроса к веб-странице
    response = requests.get(url)

    # Проверка успешности запроса
    if response.status_code != 200:
        print(f"Не удалось загрузить страницу, статус-код: {response.status_code}")
        return []
    else:
        print("All right!")
    # Парсинг HTML-кода страницы
    soup = BeautifulSoup(response.text, 'html.parser')
    file = open("books.txt", "w")
    #file.write(response.text)
    file.close()
    # Поиск всех элементов, содержащих информацию о книгах
    books = []
    for book_item in soup.find_all('div', class_='book-item'):
        title_tag = book_item.find('div', class_='book-title')
        if title_tag:
            title = title_tag.get_text(strip=True)
            books.append(title)

    return books


# URL страницы с книгами
url = "https://dmkpress.com/catalog/computer/programming/"
books = get_books(url)

# Вывод списка книг
for book in books:
    print(book)
