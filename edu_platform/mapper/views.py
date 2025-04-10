from .models import Book
def index():
    books = Book.objects.all()
    for book in books:
        print(
            f'(id:{book.id}, name:{book.name}, price:{book.price}, price:{book.create_time}, price:{book.update_time})')
    return "Hello World"
