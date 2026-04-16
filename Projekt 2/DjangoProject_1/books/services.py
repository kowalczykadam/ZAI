import requests
from .models import Book

def fetch_books_from_api(query="python"):
    url = f"https://openlibrary.org/search.json?q={query}"
    response = requests.get(url)

    data = response.json()

    books = []
    for item in data["docs"][:10]:
        book, created = Book.objects.get_or_create(
            title=item.get("title"),
            defaults={
                "author": ", ".join(item.get("author_name", ["Unknown"])),
                "year": item.get("first_publish_year"),
                "external_id": item.get("key")
            }
        )
        books.append(book)

    return books